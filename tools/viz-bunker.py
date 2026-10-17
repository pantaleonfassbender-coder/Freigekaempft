"""Grafik zu den Modulen 4 und 5: Bautzen in drei Lagen, 21. April – 8. Mai 1945: was Moskau öffentlich meldete, was das
OKW öffentlich meldete, und was im Führerbunker daraus wurde (nach Ziemke). Alle Einträge nach den abgedruckten Stellen
(Meldungen [1]–[5], Bunker [1]–[9], Gegenangriff [9]–[13]). Schreibt assets/plates/vizbunker.jpg und _t.jpg.
Lauf aus dem Repository:  python tools/viz-bunker.py
"""
import io
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
SOW, DT, HIST, INK, INK2, PAPER, LINE = "#9b3b2e", "#59604c", "#8a6d2f", "#231c22", "#62585f", "#f4efe6", "#dacfc0"

D0 = date(1945, 4, 21)
x = lambda m, d: (date(1945, m, d) - D0).days
ROWS = [("Moskau, öffentlich", SOW), ("OKW, öffentlich", DT), ("Führerbunker\n(nach Ziemke)", HIST)]
EV = [  # Zeile, Monat, Tag, Text, dy, Ausrichtung
    (0, 4, 21, "21.4.: Bautzen\n„vollständig genommen“", 0.28, "left"),
    (0, 4, 25, "25./26.4.: Gegenangriffe\n„abgewehrt“", -0.3, "left"),
    (0, 4, 26, "", 0, "left"),
    (1, 4, 21, "21.4.: Besatzungen von Bautzen\n„zerschlugen alle Angriffe“", 0.28, "left"),
    (1, 4, 26, "26.4.: „Bautzen freigekämpft“", 0.28, "left"),
    (1, 5, 3, "3.5.: „Das sind unsere Jungen“", 0.28, "center"),
    (1, 5, 7, "Zeitung vom 7.5.: 14.600 Tote;\n„Goebbels und Keitel gefallen“", -0.3, "right"),
    (2, 4, 21, "21.4.: „Grundweisung“\naus einer „Illusion“", 0.28, "left"),
    (2, 4, 22, "22.4.: Krieg „verloren“ –\nam Abend: Angriff „succeeding“", -0.32, "left"),
    (2, 4, 26, "26.4.: „wenn der Wille da ist …“", 0.28, "left"),
    (2, 4, 27, "27.4.: weiter von Bautzen\nnach Norden angreifen", -0.32, "left"),
    (2, 4, 30, "30.4.: Hitler tot;\n„großer Ring“ im Süden", 0.28, "left"),
    (2, 5, 8, "8.5.: Schörner verlässt\nseine Truppen", -0.32, "right"),
]


def main():
    fig, ax = plt.subplots(figsize=(12, 5.2), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    for i, (lab, col) in enumerate(ROWS):
        y = 2 - i
        ax.plot([0, x(5, 8) + .5], [y, y], color=LINE, lw=1.2, zorder=1)
        ax.text(-0.4, y, lab, ha="right", va="center", fontsize=10, color=col, weight="bold")
    ax.axvspan(x(4, 26) + .5, x(5, 8) + .5, ymin=0.72, ymax=0.98, color=SOW, alpha=.07, zorder=0)
    ax.text(x(5, 2), 2.0, "kein Wort mehr über Bautzen", ha="center", va="center", fontsize=9.5, color=SOW, style="italic")
    for r, m, d, t, dy, ha in EV:
        y = 2 - r
        ax.plot([x(m, d)], [y], "o", color=ROWS[r][1], ms=8, zorder=3)
        if t:
            ax.text(x(m, d) + (0.15 if ha == "left" else -0.15 if ha == "right" else 0), y + dy, t, fontsize=8.4, color=INK,
                    ha=ha, va="bottom" if dy > 0 else "top")
    ax.annotate("", xy=(x(4, 21), 0.08), xytext=(x(4, 21), 0.9), arrowprops=dict(arrowstyle="-|>", color=HIST, lw=1.4, ls="--"))
    ax.annotate("", xy=(x(4, 26), 0.08), xytext=(x(4, 26), 0.9), arrowprops=dict(arrowstyle="-|>", color=HIST, lw=1.4, ls="--"))
    ticks = [(4, 21), (4, 24), (4, 27), (4, 30), (5, 3), (5, 6), (5, 8)]
    ax.set_xticks([x(m, d) for m, d in ticks]); ax.set_xticklabels([f"{d}.{m}." for m, d in ticks], fontsize=9, color=INK2)
    ax.set_yticks([]); ax.set_xlim(-0.3, x(5, 8) + 0.8); ax.set_ylim(-0.75, 2.75)
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LINE)
    ax.set_title("Bautzen in drei Lagen: was gemeldet wurde und was im Bunker daraus wurde", fontsize=13, color=INK, loc="left")
    fig.text(0.01, -0.03, "Grafik des Apparats nach Совинформбюро Bd. 8 S. 180, 186–188; Wehrmachtberichten und dnb-Meldungen in der Marburger Zeitung "
             "(23.4.–7.5.); Ziemke, Stalingrad to Berlin, S. 477–498. Gestrichelt: Meldung, die im Bunker zur Weisung wurde. CC BY 4.0.",
             fontsize=7, color=INK2)
    buf = io.BytesIO(); fig.savefig(buf, format="png", facecolor=PAPER, bbox_inches="tight"); plt.close(fig)
    im = Image.open(buf).convert("RGB")
    big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / "vizbunker.jpg", quality=88)
    th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / "vizbunker_t.jpg", quality=84)
    print("ok vizbunker", big.size)


if __name__ == "__main__":
    main()
