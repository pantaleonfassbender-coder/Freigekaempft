"""Tafeln: Seitenbilder der Quellen (tools/build-seiten.py), Bilder von Wikimedia Commons (nur mit Gemeinfreiheits- oder
CC0-Vorlage auf der Dateiseite) und eigene Grafiken (tools/viz-*.py). Schreibt assets/plates/<id>.jpg (max. 1600 px), <id>_t.jpg und data/plates.json.
Lauf aus dem Repository:  python tools/build-plates.py [ids…]
"""
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "Freigekaempft/0.1 (educational; pantaleonfassbender@gmail.com)"}
OK = re.compile(r"\{\{\s*(PD-|Licensed-PD|cc-zero|CC0)", re.I)

LEDE = "Karten, Seiten der Quellen und die Grafiken des Apparats. Zeitungsseiten erscheinen nur als Ausschnitte ohne Zeitungskopf und ohne Hoheitszeichen. Jede Tafel nennt ihr Original."
LEDE_EN = "Maps, pages of the sources and the apparatus's own graphics. Newspaper pages appear only as excerpts without masthead and without national emblems. Every plate names its original."
CREDIT = "Seitenbilder aus gemeinfreien Digitalisaten (Internet Archive, dLib.si, booksite.ru), jeweils mit ihrem Original genannt; eigene Grafiken CC BY 4.0, Flüsse aus Natural Earth (gemeinfrei)."
CREDIT_EN = "Page images from public-domain scans (Internet Archive, dLib.si, booksite.ru), each named with its original; the apparatus's own graphics CC BY 4.0, rivers from Natural Earth (public domain)."

# Seitenbilder (Bild von tools/build-seiten.py): Quelle und Fundort
SEITE = {
    "ziemke42": ("Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), Map 42; Internet Archive, gemeinfrei",
                 "https://archive.org/details/StalingradToBerlinTheGermanDefeatInTheEast-nsia"),
    "mzokw20": ("Marburger Zeitung Nr. 110, 20.4.1945, S. 2 (Ausschnitt); dLib.si, Narodna in univerzitetna knjižnica",
                "https://www.dlib.si/details/URN:NBN:SI:DOC-F2DJDGGD"),
    "sib19": ("Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 177 (Ausschnitt); booksite.ru",
              "https://www.booksite.ru/fulltext/inform8/index.htm"),
}

# id, Seite, Quelle ("commons:Datei", "viz:Datei" oder "seite:id"), Titel, Titel EN, Bildunterschrift, EN, Verweis
PLATES = [
    ("vizlage", "hist", "viz:vizlage", "Drei Lagebilder, 19. und 20. April 1945", "Three pictures of the situation, 19 and 20 April 1945",
     "Grafik des Apparats: was Moskau am 19. und 20. April als genommen meldete, wohin das OKW am 19. April die „schmalen Angriffskeile“ reichen ließ, und wo Schörner den Angriff am 10. April erwartet hatte. Orte nach heutigen Koordinaten.",
     "The apparatus's graphic: what Moscow reported as taken on 19 and 20 April, how far the OKW let the 'narrow wedges of attack' reach on 19 April, and where Schörner had expected the attack on 10 April. Places by today's coordinates.",
     "#/text/lage/moskau/10"),
    ("ziemke42", "hist", "seite:ziemke42", "Ziemke, Karte 42: Berlin, 16. April – 7. Mai 1945", "Ziemke, Map 42: Berlin, 16 April – 7 May 1945",
     "Die Karte der amerikanischen Armeegeschichte, 1968. Zwischen Görlitz und Spremberg stehen die 2. Polnische Armee („Second (Polish)“) und die 52. Armee („Fifty-second“), nordwestlich Bautzen der Kasten der 4. Panzerarmee („Fourth Pz“); die deutsche Front vom 16. April gestrichelt, die vom 25. April schraffiert.",
     "The map of the American army history, 1968. Between Görlitz and Spremberg stand the Polish Second Army ('Second (Polish)') and the 52nd Army ('Fifty-second'), north-west of Bautzen the box of the Fourth Panzer Army ('Fourth Pz'); the German front of 16 April dashed, that of 25 April hatched.",
     "#/text/lage/falsch/1"),
    ("mzokw20", "dt", "seite:mzokw20", "Der Wehrmachtbericht vom 19. April in der Zeitung", "The Wehrmacht report of 19 April in the newspaper",
     "Marburger Zeitung, 20. April 1945, Seite 2: „Dem Sowjet-Massensturm standgehalten“, darunter der Bericht mit den „schmalen Angriffskeilen“ bis östlich Bautzen. Ausschnitt ohne Zeitungskopf.",
     "Marburger Zeitung, 20 April 1945, page 2: 'Withstood the Soviet mass onslaught', below it the report with the 'narrow wedges of attack' reaching east of Bautzen. Excerpt without masthead.",
     "#/text/lage/okw/8"),
    ("sib19", "sow", "seite:sib19", "Die sowjetische Meldung für den 19. April", "The Soviet report for 19 April",
     "Сообщения Советского Информбюро, Band 8, Seite 177: die „Оперативная сводка за 19 апреля“ mit der „силовая разведка“ der ersten drei Tage und der 2. Polnischen Armee bei Rothenburg.",
     "Soobshcheniya Sovetskogo Informbyuro, vol. 8, p. 177: the 'Operational summary for 19 April' with the 'reconnaissance in force' of the first three days and the Polish Second Army at Rothenburg.",
     "#/text/lage/moskau/9"),
]


def api(params):
    q = urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q, headers=UA)
    for wait in (0, 20, 60, 120):
        time.sleep(wait)
        try:
            return json.load(urllib.request.urlopen(req))
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("rate-limited")


def commons(fname):
    d = api({"action": "query", "titles": "File:" + fname, "prop": "imageinfo|revisions", "rvprop": "content",
             "rvslots": "main", "iiprop": "url", "iiurlwidth": "1600"})
    pg = next(iter(d["query"]["pages"].values()))
    if not OK.search(pg["revisions"][0]["slots"]["main"]["*"]):
        raise SystemExit(f"keine Gemeinfreiheits-/CC0-Vorlage: {fname}")
    ii = pg["imageinfo"][0]
    for wait in (0, 20, 60):
        time.sleep(wait)
        try:
            return urllib.request.urlopen(urllib.request.Request(ii.get("thumburl") or ii["url"], headers=UA)).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("rate-limited")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[1:])
    meta = []
    for pid, side, src, t, t_en, c, c_en, cite in PLATES:
        kind, _, name = src.partition(":")
        if kind == "commons":
            url, source = "https://commons.wikimedia.org/wiki/File:" + urllib.parse.quote(name.replace(" ", "_")), f"Wikimedia Commons, {name}"
        elif kind == "seite":
            source, url = SEITE[name]
        else:
            url, source = "", "Grafik des Apparats, CC BY 4.0"
        if kind == "commons" and (not only or pid in only):
            im = Image.open(io.BytesIO(commons(name))).convert("RGB")
            big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / f"{pid}.jpg", quality=86)
            th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / f"{pid}_t.jpg", quality=82)
            print("ok", pid, big.size)
            time.sleep(6)
        meta.append({"id": pid, "side": side, "titel": t, "titel_en": t_en, "caption": c, "caption_en": c_en,
                     "source": source, "url": url, "cite": cite})
    (ROOT / "data" / "plates.json").write_text(json.dumps({"lede": LEDE, "lede_en": LEDE_EN, "credit": CREDIT,
                                                           "credit_en": CREDIT_EN, "plates": meta}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
