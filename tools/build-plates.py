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
    "mzlauban": ("Marburger Zeitung Nr. 68, 9.3.1945, S. 1 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-WWSMFHVA"),
    "mzgoebbels": ("Marburger Zeitung Nr. 71, 12.3.1945, S. 1 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-E7P1B7LR"),
    "sib9mai": ("Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 209 (Ausschnitt); booksite.ru", "https://www.booksite.ru/fulltext/inform8/index.htm"),
    "mzkamenz": ("Marburger Zeitung Nr. 115, 25.4.1945, S. 1 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-YQUEVGVE"),
    "mzkamenz2": ("Marburger Zeitung Nr. 121, 1.5.1945, S. 2 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-WTLJFS5P"),
    "sib25": ("Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 186 (Ausschnitt); booksite.ru", "https://www.booksite.ru/fulltext/inform8/index.htm"),
    "sib21": ("Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 180 (Ausschnitt); booksite.ru", "https://www.booksite.ru/fulltext/inform8/index.htm"),
    "mzbautzen": ("Marburger Zeitung Nr. 117, 27.4.1945, S. 1 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-YYEMNBC2"),
    "mzjungen": ("Marburger Zeitung Nr. 124, 4.5.1945, S. 1 (Ausschnitt); dLib.si", "https://www.dlib.si/details/URN:NBN:SI:DOC-J0J8RBGY"),
    "ziemke483": ("Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 483 (Ausschnitt); Internet Archive, gemeinfrei",
                  "https://archive.org/details/StalingradToBerlinTheGermanDefeatInTheEast-nsia"),
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
    ("vizlauban", "hist", "viz:vizlauban", "Lauban in den Meldungen, März bis Mai 1945", "Lauban in the reports, March to May 1945",
     "Grafik des Apparats: wann das OKW, das Deutsche Nachrichtenbüro und die Wochenschau von Lauban sprachen, und wann Moskau: erst am 9. Mai.",
     "The apparatus's graphic: when the OKW, the German News Bureau and the newsreel spoke of Lauban, and when Moscow did: only on 9 May.",
     "#/text/lauban/moskau/6"),
    ("mzlauban", "dt", "seite:mzlauban", "„Die Stadt Lauban wieder befreit“", "“The town of Lauban liberated again”",
     "Schlagzeile der Marburger Zeitung vom 9. März 1945 über dem Wehrmachtbericht vom 8. März. Ausschnitt ohne Zeitungskopf; der Bericht darunter, der die SS mit Runen setzt, ist nicht abgebildet.",
     "Headline of the Marburger Zeitung of 9 March 1945 above the Wehrmacht report of 8 March. Excerpt without masthead; the report below, which prints the SS runes, is not reproduced.",
     "#/text/lauban/okw/3"),
    ("mzgoebbels", "dt", "seite:mzgoebbels", "„Dr. Goebbels in Lauban und Görlitz“", "“Dr Goebbels in Lauban and Görlitz”",
     "Überschrift der Meldung des Deutschen Nachrichtenbüros in der Marburger Zeitung vom 12. März 1945, mit dem Satz aus der Görlitzer Rede: „Der Feind ist zu schlagen, denn wir haben ihn oft genug geschlagen“.",
     "Headline of the German News Bureau's report in the Marburger Zeitung of 12 March 1945, with the sentence from the Görlitz speech: 'The enemy can be beaten, for we have beaten him often enough'.",
     "#/text/lauban/goebbels/4"),
    ("sib9mai", "sow", "seite:sib9mai", "Lauban in der sowjetischen Meldung vom 9. Mai", "Lauban in the Soviet report of 9 May",
     "Сообщения Советского Информбюро, Band 8, Seite 209: Prag, und „юго-восточнее Дрездена“ eine Reihe von Städten, darunter ЛАУБАН.",
     "Soobshcheniya Sovetskogo Informbyuro, vol. 8, p. 209: Prague, and 'south-east of Dresden' a row of towns, among them LAUBAN.",
     "#/text/lauban/moskau/6"),
    ("vizgegenangriff", "hist", "viz:vizgegenangriff", "Wer was wann meldete, 20. April – 1. Mai", "Who reported what and when, 20 April – 1 May",
     "Grafik des Apparats: jeder Ort an jedem Tag, wie Moskau und das OKW ihn meldeten. Kamenz ist zweimal „wieder“ deutsch; nach dem 26. April meldet Moskau den Raum nicht mehr. Ein Zeichen heißt: so gemeldet, nicht: so gewesen.",
     "The apparatus's graphic: every place on every day as Moscow and the OKW reported it. Kamenz is German 'again' twice; after 26 April Moscow no longer reports the area. A mark means: reported so, not: so it was.",
     "#/text/gegenangriff/norden/12"),
    ("mzkamenz", "dt", "seite:mzkamenz", "„Pulsnitz und Kamenz wieder in deutscher Hand“", "“Pulsnitz and Kamenz again in German hands”",
     "Schlagzeile der Marburger Zeitung vom 25. April 1945 über dem Wehrmachtbericht vom 24. April. Ausschnitt ohne Zeitungskopf.",
     "Headline of the Marburger Zeitung of 25 April 1945 above the Wehrmacht report of 24 April. Excerpt without masthead.",
     "#/text/gegenangriff/kamenz/7"),
    ("mzkamenz2", "dt", "seite:mzkamenz2", "„Kamenz und Königsbrück wurden wiedergenommen“", "“Kamenz and Königsbrück were retaken”",
     "Der Wehrmachtbericht vom 29. April in der Marburger Zeitung vom 1. Mai 1945, Seite 2: Kamenz zum zweiten Mal „wieder“.",
     "The Wehrmacht report of 29 April in the Marburger Zeitung of 1 May 1945, page 2: Kamenz 'again' for the second time.",
     "#/text/gegenangriff/norden/12"),
    ("sib25", "sow", "seite:sib25", "„В районе БАУЦЕН …“", "“In the area of BAUTZEN …”",
     "Сообщения Советского Информбюро, Band 8, Seite 186: die Meldung für den 25. April mit den abgewehrten Gegenangriffen bei Bautzen.",
     "Soobshcheniya Sovetskogo Informbyuro, vol. 8, p. 186: the report for 25 April with the counterattacks repulsed at Bautzen.",
     "#/text/gegenangriff/kamenz/9"),
    ("sib21", "sow", "seite:sib21", "„… полностью овладели городом Бауцен“", "“… took the town of Bautzen entirely”",
     "Сообщения Советского Информбюро, Band 8, Seite 180: der Bericht zum 21. April, der Bautzen als vollständig genommen meldet, „einen Knotenpunkt von vier Eisenbahnen und vielen Landstraßen“.",
     "Soobshcheniya Sovetskogo Informbyuro, vol. 8, p. 180: the account for 21 April reporting Bautzen as taken entirely, 'a junction of four railways and many highways'.",
     "#/text/meldungen/moskau/2"),
    ("mzbautzen", "dt", "seite:mzbautzen", "„Bautzen freigekämpft“", "“Bautzen fought free”",
     "Schlagzeile der Marburger Zeitung vom 27. April 1945 über dem Wehrmachtbericht vom 26. April: Bautzen als vierte Zeile, nach Bremen, Berlin und Brünn. Ausschnitt ohne Zeitungskopf.",
     "Headline of the Marburger Zeitung of 27 April 1945 above the Wehrmacht report of 26 April: Bautzen in the fourth line, after Bremen, Berlin and Brno. Excerpt without masthead.",
     "#/text/meldungen/okw/3"),
    ("mzjungen", "dt", "seite:mzjungen", "„Das sind unsere Jungen“", "“Those are our boys”",
     "Die dnb-Meldung vom 3. Mai 1945 in der Marburger Zeitung vom 4. Mai: Fünfzehn- und Sechzehnjährige aus dem Wehrertüchtigungslager in der Verteidigung von Bautzen, als Heldengeschichte erzählt.",
     "The dnb report of 3 May 1945 in the Marburger Zeitung of 4 May: fifteen- and sixteen-year-olds from the military-training camp in the defence of Bautzen, told as a hero story.",
     "#/text/meldungen/danach/4"),
    ("vizbunker", "hist", "viz:vizbunker", "Bautzen in drei Lagen", "Bautzen in three registers",
     "Grafik des Apparats: was Moskau öffentlich meldete, was das OKW öffentlich meldete, und was im Führerbunker nach Ziemke aus Bautzen wurde, vom 21. April bis zum 8. Mai.",
     "The apparatus's graphic: what Moscow publicly reported, what the OKW publicly reported, and what Bautzen became in the Führer bunker according to Ziemke, from 21 April to 8 May.",
     "#/text/bunker/wille/5"),
    ("ziemke483", "hist", "seite:ziemke483", "„when the will is there“", "“when the will is there”",
     "Earl F. Ziemke, Stalingrad to Berlin (1968), Seite 483: der 26. April als „the day of hopes“, und Schörners Angriff bei Bautzen als Beweis, dass „wenn der Wille da ist“, der Feind noch heute zu schlagen sei.",
     "Earl F. Ziemke, Stalingrad to Berlin (1968), page 483: 26 April as 'the day of hopes', and Schörner's attack at Bautzen as proof that 'when the will is there' the enemy can be defeated even today.",
     "#/text/bunker/wille/5"),
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
