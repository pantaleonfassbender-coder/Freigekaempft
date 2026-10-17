"""Grafiken zu den Modulen 6–8.

- vizorte: Orte der Gewalt und des Gedenkens um Bautzen (Modul 6), nach der neueren Literatur; Orte nach heutigen
  Koordinaten, gerundet; das Denkmal auf dem Fulksberg nach den Koordinaten der Commons-Datei.
- vizzaehlung: Wer in den Meldungen vorkommt (Modul 7): Treffer in der Textschicht der Marburger Zeitung, 17.4.–8.5.1945,
  und der Meldungen des Sowinformbüros, Bd. 8, S. 177–211. Maschinell gelesene Texte; die Zahlen sind Mindestwerte.
- viznachleben: wie die Schlacht genannt wurde, 1945–2023 (Modul 8).
Lauf aus dem Repository:  python tools/viz-spaet.py
"""
import glob
import io
import json
import re
import urllib.request
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
SRC = ROOT / "tools" / "src"
SOW, DT, POL, HIST, ZIV, REZ, INK, INK2, PAPER, LINE, RIVER = ("#9b3b2e", "#59604c", "#2f6a8f", "#8a6d2f", "#3f6b3a", "#7a7064",
                                                              "#231c22", "#62585f", "#f4efe6", "#dacfc0", "#7fa3bf")


def save(fig, pid):
    buf = io.BytesIO(); fig.savefig(buf, format="png", facecolor=PAPER, bbox_inches="tight"); plt.close(fig)
    im = Image.open(buf).convert("RGB")
    big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / f"{pid}.jpg", quality=88)
    th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / f"{pid}_t.jpg", quality=84)
    print("ok", pid, big.size)


def orte():
    places = [  # Name, lon, lat, Farbe, Text, Namensposition (x, y), Ausrichtung
        ("Bautzen", 14.43, 51.18, DT, "Außenlager des KZ Groß-Rosen\n(Waggonbaufabrik), Okt. 1944 – Apr. 1945", (14.455, 51.174), "left"),
        ("Niederkaina", 14.47, 51.20, SOW, "22.4.: rund 200 gefangene\nVolkssturmmänner getötet", (14.49, 51.247), "left"),
        ("Fulksberg bei Crostwitz", 14.2416, 51.2410, POL, "Horka, 26.4.: Sanitätskolonne der\npoln. 9. Division; Denkmäler 1967, 1980", (14.222, 51.237), "right"),
        ("Kamenz", 14.09, 51.27, INK2, "", (14.07, 51.27), "right"),
        ("Weißenberg", 14.66, 51.20, INK2, "", (14.68, 51.20), "left"),
        ("Görlitz", 14.99, 51.15, INK2, "", (14.97, 51.15), "right"),
        ("Nixdorf (Mikulášovice)", 14.36, 50.97, ZIV, "Ziel des Todesmarsches\nder Häftlinge, Mitte April", (14.385, 50.985), "left"),
    ]
    fig, ax = plt.subplots(figsize=(10.5, 6.6), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    ax.annotate("", xy=(14.36, 50.98), xytext=(14.428, 51.172), arrowprops=dict(arrowstyle="-|>", color=ZIV, lw=2, ls="--"))
    for name, x, y, col, txt, (tx, ty), ha in places:
        big = bool(txt)
        ax.plot([x], [y], "o", color=col, ms=9 if big else 4, zorder=3)
        if big:
            ax.plot([x, tx], [y, ty], color=col, lw=0.6, zorder=2)
            ax.text(tx, ty, name, fontsize=10, color=INK, weight="bold", ha=ha, va="top")
            ax.text(tx, ty - 0.016, txt, fontsize=8.6, color=col, ha=ha, va="top")
        else:
            ax.text(tx, ty, name, fontsize=8.5, color=INK, ha=ha, va="center")
    ax.set_xlim(13.95, 15.1); ax.set_ylim(50.93, 51.33); ax.set_aspect(1 / 0.63)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(LINE)
    ax.set_title("Orte der Gewalt um Bautzen, April 1945", fontsize=13, color=INK, loc="left")
    ax.text(0, -0.03, "Grafik des Apparats nach der neueren Literatur (Referate im Modul „Horka, Niederkaina, das Außenlager“), nicht nach Quellen von 1945. "
            "Orte nach heutigen Koordinaten, gerundet. CC BY 4.0.", fontsize=7, color=INK2, transform=ax.transAxes, va="top")
    save(fig, "vizorte")


def zaehlung():
    mz = " ".join(p.get_text() for f in sorted(glob.glob(str(SRC / "mz" / "mz-1945-0[45]-*.pdf"))) for p in pymupdf.open(f))
    mz = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", mz))
    sb = pymupdf.open(SRC / "sovinformburo-t8-1945.pdf")
    si = re.sub(r"\s+", " ", re.sub(r"[\-­]\s*\n\s*|­", "", " ".join(sb[i].get_text() for i in range(175, 210))))
    MZ = [("Frauen", r"Frauen"), ("Volkssturm", r"Volks.?sturm"), ("Hitler-Jugend, Hitler-Jungen", r"Hitler.?(Jug|Jung)"),
          ("Flüchtlinge, Rückgeführte, Trecks", r"Flüch|Rückgef|Treck"), ("Kriegsgefangene", r"Kriegsgefangen"),
          ("Zwangs-, Ost-, Fremdarbeiter", r"Zwangsarbeit|Ostarbeit|Fremdarbeit"), ("KZ-Häftlinge, Konzentrationslager", r"Häftling|Konzentrationslager|\bKZ\b"),
          ("polnische Truppen an der Front", r"polnische[nrs]? (Armee|Truppe|Division)"), ("Sorben, Wenden", r"Sorb|\bWenden\b|wendisch")]
    SI = [("Volkssturm (фольксштурм)", r"(?i)фольксштурм"), ("Zivilbevölkerung (население, мирные жители)", r"(?i)мирн\w* (жител|населен)|населени"),
          ("Kriegsgefangene (военнопленные)", r"(?i)военнопленн"), ("polnische Truppen (польск-, поляк)", r"(?i)польск|поляк"),
          ("Lager (лагерь)", r"(?i)лагер"), ("Sorben (лужичане, сорбы)", r"(?i)лужич|сорб")]
    a = [(k, len(re.findall(v, mz))) for k, v in MZ]
    b = [(k, len(re.findall(v, si))) for k, v in SI]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6), dpi=150, gridspec_kw=dict(width_ratios=[1.15, 1], wspace=0.95))
    fig.patch.set_facecolor(PAPER)
    for ax, data, col, title in [(ax1, a, DT, "Marburger Zeitung, 17. April – 8. Mai 1945 (16 Ausgaben)"),
                                 (ax2, b, SOW, "Совинформбюро, Meldungen 19. April – 9. Mai 1945")]:
        ax.set_facecolor(PAPER)
        labels = [k for k, _ in data][::-1]; vals = [v for _, v in data][::-1]
        ax.barh(labels, vals, color=[col if v else "#c9bfb2" for v in vals])
        for i, v in enumerate(vals):
            ax.text(v + max(vals) * 0.02 + 0.2, i, str(v), va="center", fontsize=9, color=INK)
        ax.set_title(title, fontsize=10, color=INK, loc="left")
        ax.tick_params(labelsize=8.6, colors=INK)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.set_xlim(0, max(vals) * 1.18 + 1)
    fig.suptitle("Wer in den Meldungen vorkommt", fontsize=13, color=INK, x=0.01, ha="left")
    fig.text(0.01, -0.06, "Treffer in der maschinellen Texterkennung der Digitalisate; die Zahlen sind Mindestwerte. „Polen“ kommt in der Zeitung oft vor, "
             "aber als „Polenfrage“ der Konferenz von San Francisco; polnische Truppen an der Front nennt sie nie. Das einzige „Konzentrationslager“ ist ein sowjetisches\n"
             "Lager bei Lublin. Moskau nennt polnische Truppen zweimal, bei Rothenburg (19.4.) und bei Kamenz (21.4.). Grafik des Apparats, CC BY 4.0.", fontsize=7, color=INK2)
    save(fig, "vizzaehlung")
    return a, b


def nachleben():
    ev = [  # Jahr, Zeile, Text
        (1945.3, 0, "OKW: „Bautzen freigekämpft“"), (1945.3, 1, "Moskau: Bautzen „vollständig genommen“"),
        (1967, 2, "Denkmal für die polnischen Soldaten\nauf dem Fulksberg bei Crostwitz"),
        (1968, 4, "Ziemke: „close to a standstill“;\ndie 2. Polnische Armee nur auf der Karte"),
        (1980, 2, "zweites Denkmal\nauf dem Fulksberg"),
        (1997, 2, "Neuer Gedenkstein für das\nAußenlager (der alte 1993 entfernt)"), (1999, 4, "Berndt: „Die Kämpfe um\nWeißenberg und Bautzen“"),
        (2002, 3, "Grzelak, Stańczyk, Zwoliński:\n„Armia Berlinga i Żymierskiego“"), (2009, 3, "Domański:" + chr(10) + "„Budziszyn 1945“"),
        (2018, 2, "Tafel in Niederkaina zerstört\nund ersetzt"),
        (2020, 4, "Junge Freiheit: „ein letzter Sieg“"), (2021, 3, "Kopociński: „Horka –\nłużycka Golgota“"),
        (2021.3, 4, "RBTH: „Germany’s last victory\nover the Red Army“"), (2023, 3, "Kania: „Ostatnia kontrofensywa\nWehrmachtu: fakty i mity“"),
    ]
    rows = [("1945: Meldungen", DT), ("", SOW), ("Gedenken vor Ort", REZ), ("Polen", POL), ("Deutschland, USA", HIST)]
    fig, ax = plt.subplots(figsize=(12.5, 5.6), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    ylab = {0: "1945: OKW", 1: "1945: Moskau", 2: "Gedenken vor Ort", 3: "Polnische Literatur", 4: "Deutsche, amerikanische,\nrussische Darstellungen"}
    cols = {0: DT, 1: SOW, 2: REZ, 3: POL, 4: HIST}
    for r in range(5):
        y = 4 - r
        ax.plot([1943, 2026], [y, y], color=LINE, lw=1, zorder=0)
        ax.text(1942, y, ylab[r], ha="right", va="center", fontsize=9.5, color=cols[r], weight="bold")
    flip = {}
    for x, r, t in ev:
        y = 4 - r
        flip[r] = not flip.get(r, True)
        ax.plot([x], [y], "o", color=cols[r], ms=7, zorder=3)
        ax.text(x + 0.4, y + (0.12 if flip[r] else -0.12), t, fontsize=7.8, color=INK, va="bottom" if flip[r] else "top")
    ax.set_xlim(1941.5, 2032); ax.set_ylim(-0.7, 4.7)
    ax.set_xticks([1945, 1960, 1975, 1990, 2005, 2020]); ax.tick_params(labelsize=8.5, colors=INK2)
    ax.set_yticks([])
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LINE)
    ax.set_title("Wie die Schlacht genannt wurde, 1945–2023", fontsize=13, color=INK, loc="left")
    fig.text(0.01, -0.03, "Grafik des Apparats. 1945 nach den Quellen dieses Apparats; danach nach Titeln und Daten der Literatur und der Denkmäler, wie die "
             "Referate im Modul „Nachleben“ sie nennen. Titel als Titel zitiert, nicht als Urteil. CC BY 4.0.", fontsize=7, color=INK2)
    save(fig, "viznachleben")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    orte(); print(zaehlung()); nachleben()
