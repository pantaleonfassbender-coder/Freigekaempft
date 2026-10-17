"""Grafik zu Modul 1: drei Lagebilder vom 19. und 20. April 1945 in der Lausitz.

Was das Sowjetische Informationsbüro als genommen meldete (Lage [9], [10]), wohin das OKW die „schmalen Angriffskeile“
reichen ließ (Lage [8]) und wo Schörner den Angriff erwartet hatte (Lage [2]). Flüsse aus Natural Earth (gemeinfrei,
beim Bau geladen), Orte nach heutigen Koordinaten (gerundet). Schreibt assets/plates/vizlage.jpg und _t.jpg.
Lauf aus dem Repository:  python tools/viz-lage.py
"""
import io
import json
import urllib.request
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_rivers_lake_centerlines.geojson"
CACHE = ROOT / "tools" / "src" / "ne_10m_rivers_lake_centerlines.geojson"
BOX = (13.55, 15.75, 50.95, 51.82)
SOW, DT, HIST, INK, RIVER, PAPER = "#9b3b2e", "#59604c", "#8a6d2f", "#231c22", "#7fa3bf", "#f4efe6"

# Name, lon, lat, Klasse (taken19 / taken20 / near20 / ort), Beschriftung links oder rechts
PLACES = [
    ("Forst", 14.64, 51.74, "taken19", "r"), ("Muskau", 14.72, 51.55, "taken19", "r"), ("Weißwasser", 14.64, 51.50, "taken19", "l"),
    ("Rothenburg", 14.96, 51.34, "taken19p", "r"), ("Klitten", 14.61, 51.35, "taken20", "l"), ("Niesky", 14.82, 51.29, "taken20", "r"),
    ("Spremberg", 14.38, 51.57, "taken20", "l"), ("Hoyerswerda", 14.25, 51.44, "taken20", "l"),
    ("Kamenz", 14.09, 51.27, "near20", "l"), ("Bautzen", 14.42, 51.18, "near20", "l"),
    ("Görlitz", 14.99, 51.15, "ort", "r"), ("Dresden", 13.74, 51.05, "ort", "r"), ("Cottbus", 14.33, 51.76, "ort", "l"),
    ("Weißenberg", 14.66, 51.20, "ort", "r"), ("Löwenberg", 15.59, 51.11, "ort", "l"), ("Bunzlau", 15.57, 51.26, "ort", "l"),
]
STYLE = {
    "taken19": dict(marker="o", color=SOW, ms=8, mfc=SOW), "taken19p": dict(marker="o", color=SOW, ms=8, mfc="white", mew=2.2),
    "taken20": dict(marker="s", color=SOW, ms=7, mfc=SOW), "near20": dict(marker="s", color=SOW, ms=8, mfc="white", mew=2),
    "ort": dict(marker="o", color=INK, ms=3.5, mfc=INK),
}


def rivers():
    if not CACHE.exists():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_bytes(urllib.request.urlopen(urllib.request.Request(NE, headers={"User-Agent": "Freigekaempft/0.1"}), timeout=120).read())
    gj = json.loads(CACHE.read_text(encoding="utf-8"))
    out = []
    for f in gj["features"]:
        g = f["geometry"]
        lines = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
        for ln in lines:
            if any(BOX[0] - .3 <= x <= BOX[1] + .3 and BOX[2] - .3 <= y <= BOX[3] + .3 for x, y in ln):
                out.append(ln)
    return out


def main():
    fig, ax = plt.subplots(figsize=(11, 7.4), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    for ln in rivers():
        ax.plot([p[0] for p in ln], [p[1] for p in ln], color=RIVER, lw=1.4, zorder=1)
    for lab, x, y in [("Elbe", 13.62, 51.14)]:
        ax.text(x, y, lab, color="#4f7593", fontsize=9, style="italic", zorder=2)
    # OKW 19.4.: „schmale Angriffskeile … bis in den Raum östlich Bautzen und an die Spree beiderseits Spremberg“
    for (x0, y0), (x1, y1) in [((14.98, 51.24), (14.55, 51.19)), ((14.62, 51.52), (14.42, 51.58))]:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=DT, lw=2.6, mutation_scale=18), zorder=3)
    ax.text(14.70, 51.105, "OKW 19.4.: „schmale Angriffskeile …\nbis in den Raum östlich Bautzen“", color=DT, fontsize=9, ha="center", zorder=4)
    ax.text(14.36, 51.645, "OKW 19.4.: „an die Spree\nbeiderseits Spremberg“", color=DT, fontsize=9, ha="center", zorder=4)
    # Schörner, 10.4.: Angriff erwartet zwischen Görlitz und Löwenberg; dort die Hälfte der Reserven
    ax.add_patch(plt.Rectangle((15.08, 51.03), 0.6, 0.27, fill=False, ec=HIST, lw=2, ls="--", zorder=2))
    ax.text(15.38, 50.985, "Schörner, 10.4.: Angriff erwartet\nzwischen Görlitz und Löwenberg", color=HIST, fontsize=9, ha="center", va="top", zorder=4)
    for name, x, y, cls, side in PLACES:
        st = STYLE[cls]
        ax.plot([x], [y], linestyle="none", zorder=5, **st)
        ax.text(x + (0.035 if side == "r" else -0.035), y, name, fontsize=9.5 if cls != "ort" else 8.5,
                color=INK, ha="left" if side == "r" else "right", va="center", zorder=6)
    leg = [plt.Line2D([], [], linestyle="none", **STYLE["taken19"], label="Moskau, 19.4.: genommen"),
           plt.Line2D([], [], linestyle="none", **STYLE["taken19p"], label="Moskau, 19.4.: von der 2. Polnischen Armee besetzt"),
           plt.Line2D([], [], linestyle="none", **STYLE["taken20"], label="Moskau, 20.4.: genommen"),
           plt.Line2D([], [], linestyle="none", **STYLE["near20"], label="Moskau, 20.4.: „näherten sich“"),
           plt.Line2D([], [], color=DT, lw=2.6, label="OKW, 19.4.: „schmale Angriffskeile“"),
           plt.Line2D([], [], color=HIST, lw=2, ls="--", label="Schörner, 10.4.: erwarteter Schwerpunkt (nach Ziemke)")]
    ax.legend(handles=leg, loc="upper left", bbox_to_anchor=(0, -0.01), ncol=2, fontsize=8.5, frameon=True, facecolor="white", edgecolor="#dacfc0")
    ax.set_xlim(BOX[0], BOX[1]); ax.set_ylim(BOX[2], BOX[3]); ax.set_aspect(1 / 0.63)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#dacfc0")
    ax.set_title("Drei Lagebilder der Lausitz, 19. und 20. April 1945", fontsize=13, color=INK, loc="left")
    fig.text(0.01, -0.075, "Grafik des Apparats nach Совинформбюро Bd. 8 S. 177–178, Marburger Zeitung 20.4.1945 S. 2 und Ziemke S. 473. "
             "Orte nach heutigen Koordinaten, Elbe nach Natural Earth; Neiße und Spree sind dort nicht verzeichnet und fehlen. CC BY 4.0.", fontsize=7, color="#62585f")
    buf = io.BytesIO(); fig.savefig(buf, format="png", facecolor=PAPER, bbox_inches="tight"); plt.close(fig)
    im = Image.open(buf).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / "vizlage.jpg", quality=88)
    th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / "vizlage_t.jpg", quality=84)
    print("ok vizlage", big.size)


if __name__ == "__main__":
    main()
