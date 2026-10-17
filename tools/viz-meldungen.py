"""Grafiken zu den Modulen 2 und 3: wer was wann meldete.

- vizlauban: Lauban in den Meldungen, 1. März – 10. Mai 1945 (OKW, dnb und Wochenschau, Moskau).
- vizgegenangriff: Orte und Tage, 20. April – 1. Mai 1945, nach OKW-Berichten und sowjetischen Meldungen.
Alle Angaben nach den in den Modulen abgedruckten Stellen (Lauban [1]–[6], Gegenangriff [1]–[13], Lage [10]; die beiden
Siegesmeldungen über Bautzen vom 21. und 26. April nach dem Modul „Zwei Meldungen, eine Stadt“). Schreibt
assets/plates/<id>.jpg und _t.jpg.  Lauf aus dem Repository:  python tools/viz-meldungen.py
"""
import io
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
SOW, DT, INK, INK2, PAPER, LINE = "#9b3b2e", "#59604c", "#231c22", "#62585f", "#f4efe6", "#dacfc0"


def save(fig, pid):
    buf = io.BytesIO(); fig.savefig(buf, format="png", facecolor=PAPER, bbox_inches="tight"); plt.close(fig)
    im = Image.open(buf).convert("RGB")
    big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / f"{pid}.jpg", quality=88)
    th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / f"{pid}_t.jpg", quality=84)
    print("ok", pid, big.size)


def lauban():
    d0 = date(1945, 3, 1)
    x = lambda d: (d - d0).days
    rows = [("OKW-Bericht", DT), ("dnb und Wochenschau", DT), ("Moskau", SOW)]
    ev = [  # Zeile, Datum, Text, dx, dy, Ausrichtung
        (0, date(1945, 3, 5), "5.3.: Stellungen\n„im Raum von Lauban“", -0.5, 0.3, "right"),
        (0, date(1945, 3, 7), "7.3.: „Einschließung“", 0, -0.3, "center"),
        (0, date(1945, 3, 8), "8.3.: „Die Stadt ist befreit“", 1.0, 0.3, "left"),
        (1, date(1945, 3, 11), "11.3.: Goebbels in Lauban\nund Görlitz (dnb)", -0.5, -0.3, "right"),
        (1, date(1945, 3, 16), "16.3.: Wochenschau\n(Produktionsdatum)", 0, 0.3, "center"),
        (1, date(1945, 3, 22), "22.3.: letzte Ausgabe\nder Wochenschau", 0.8, 0.3, "left"),
        (2, date(1945, 5, 9), "9.5.: Lauban, sechster Name\nin einer Reihe genommener Städte", 0, 0.3, "right"),
    ]
    fig, ax = plt.subplots(figsize=(11, 4.4), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    for i, (lab, col) in enumerate(rows):
        y = 2 - i
        ax.plot([0, 70], [y, y], color=LINE, lw=1.2, zorder=1)
        ax.text(-1.2, y, lab, ha="right", va="center", fontsize=10.5, color=col, weight="bold")
    ax.add_patch(plt.Rectangle((x(date(1945, 3, 1)), -0.25), x(date(1945, 5, 9)) - 0.6, 0.5, color=SOW, alpha=.08, zorder=0))
    ax.text(x(date(1945, 4, 4)), 0.0, "kein Wort über Lauban", ha="center", va="center", fontsize=10, color=SOW, style="italic")
    for r, d, t, dx, dy, ha in ev:
        y = 2 - r
        ax.plot([x(d)], [y], "o", color=rows[r][1], ms=8, zorder=3)
        ax.text(x(d) + dx, y + dy, t, fontsize=8.8, color=INK, ha=ha, va="bottom" if dy > 0 else "top")
    ticks = [date(1945, 3, 1), date(1945, 3, 15), date(1945, 4, 1), date(1945, 4, 15), date(1945, 5, 1)]
    ax.set_xticks([x(t) for t in ticks]); ax.set_xticklabels([f"{t.day}.{t.month}." for t in ticks], fontsize=9, color=INK2)
    ax.set_yticks([]); ax.set_xlim(-0.5, 72); ax.set_ylim(-0.7, 2.9)
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LINE)
    ax.set_title("Lauban in den Meldungen, März bis Mai 1945", fontsize=13, color=INK, loc="left")
    fig.text(0.01, -0.04, "Grafik des Apparats nach den Wehrmachtberichten vom 5., 7. und 8.3. (Marburger Zeitung), der dnb-Meldung vom 11.3., "
             "dem Katalog des US Holocaust Memorial Museum (Film 2886) und Совинформбюро Bd. 8. CC BY 4.0.", fontsize=7, color=INK2)
    save(fig, "vizlauban")


def gegenangriff():
    days = [date(1945, 4, d) for d in range(20, 31)] + [date(1945, 5, 1)]
    col = {d: i for i, d in enumerate(days)}
    places = ["Spremberg", "Bischofswerda", "Pulsnitz", "Königsbrück", "Kamenz", "Bautzen", "Weißenberg"]
    row = {p: len(places) - 1 - i for i, p in enumerate(places)}
    # (Ort, Tag, Seite, Art): Art taken = als genommen gemeldet, fight = Kampf/Annäherung/abgewehrt,
    # held = als gehalten oder (wieder) deutsch gemeldet, entered = Feind eingedrungen (nach OKW)
    M = [
        ("Spremberg", 20, "sow", "taken"), ("Spremberg", 21, "dt", "held"), ("Spremberg", 23, "dt", "held"),
        ("Bischofswerda", 22, "sow", "taken"), ("Bischofswerda", 22, "dt", "entered"),
        ("Pulsnitz", 23, "sow", "taken"), ("Pulsnitz", 24, "dt", "held"),
        ("Königsbrück", 21, "sow", "fight"), ("Königsbrück", 22, "dt", "entered"), ("Königsbrück", 29, "dt", "held"), ("Königsbrück", 1, "dt", "held"),
        ("Kamenz", 20, "sow", "fight"), ("Kamenz", 21, "sow", "taken"), ("Kamenz", 21, "dt", "entered"), ("Kamenz", 24, "dt", "held"),
        ("Kamenz", 29, "dt", "held"), ("Kamenz", 1, "dt", "held"),
        ("Bautzen", 20, "sow", "fight"), ("Bautzen", 21, "sow", "taken"), ("Bautzen", 21, "dt", "held"), ("Bautzen", 22, "dt", "held"),
        ("Bautzen", 23, "dt", "held"), ("Bautzen", 25, "sow", "fight"), ("Bautzen", 26, "sow", "fight"), ("Bautzen", 26, "dt", "held"),
        ("Bautzen", 1, "dt", "held"),
        ("Weißenberg", 25, "dt", "held"),
    ]
    fig, ax = plt.subplots(figsize=(11.5, 5.4), dpi=150)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    for p, r in row.items():
        ax.plot([-0.5, len(days) - 0.5], [r, r], color=LINE, lw=1, zorder=0)
        ax.text(-0.7, r, p, ha="right", va="center", fontsize=10.5, color=INK)
    for d, c in col.items():
        ax.text(c, len(places) - 0.35, f"{d.day}.{d.month}.", ha="center", fontsize=8.5, color=INK2)
    st = {("sow", "taken"): dict(marker="s", mfc=SOW, mec=SOW, ms=11), ("sow", "fight"): dict(marker="s", mfc="white", mec=SOW, mew=2, ms=10),
          ("dt", "held"): dict(marker="o", mfc=DT, mec=DT, ms=11), ("dt", "entered"): dict(marker="o", mfc="white", mec=DT, mew=2, ms=10)}
    for p, day, side, kind in M:
        d = date(1945, 5, 1) if day == 1 else date(1945, 4, day)
        off = -0.17 if side == "sow" else 0.17
        ax.plot([col[d] + off], [row[p]], linestyle="none", zorder=3, **st[(side, kind)])
    # Kamenz: zweimal „wieder“
    for d in (date(1945, 4, 24), date(1945, 4, 29)):
        ax.annotate("„wieder“", (col[d] + .17, row["Kamenz"]), xytext=(col[d] + .17, row["Kamenz"] + .55), ha="center", fontsize=8.5,
                    color=DT, arrowprops=dict(arrowstyle="-", color=DT, lw=1))
    ax.annotate("Moskau: „vollständig genommen“", (col[date(1945, 4, 21)] - .17, row["Bautzen"]), xytext=(1.7, row["Bautzen"] - .62),
                fontsize=8.5, color=SOW, arrowprops=dict(arrowstyle="-", color=SOW, lw=1))
    ax.annotate("OKW: „freigekämpft“", (col[date(1945, 4, 26)] + .17, row["Bautzen"]), xytext=(col[date(1945, 4, 26)] + .9, row["Bautzen"] - .62),
                fontsize=8.5, color=DT, arrowprops=dict(arrowstyle="-", color=DT, lw=1))
    ax.axvspan(col[date(1945, 4, 26)] + .5, len(days) - .5, color=SOW, alpha=.06, zorder=0)
    ax.text(col[date(1945, 4, 29)], -0.75, "Moskau meldet den Raum nicht mehr", ha="center", fontsize=8.8, color=SOW, style="italic")
    for d in (date(1945, 4, 27), date(1945, 4, 30)):
        ax.text(col[d], -0.75 if d.day == 27 else -1.05, "", fontsize=8)
    ax.text(col[date(1945, 4, 27)], len(places) - .75, "kein\nOKW-Bericht\ngedruckt", ha="center", va="top", fontsize=7.2, color=INK2)
    ax.text(col[date(1945, 4, 30)], len(places) - .75, "kein\nOKW-Bericht\ngedruckt", ha="center", va="top", fontsize=7.2, color=INK2)
    leg = [Line2D([], [], linestyle="none", **st[("sow", "taken")], label="Moskau: genommen"),
           Line2D([], [], linestyle="none", **st[("sow", "fight")], label="Moskau: Kampf, Annäherung, Gegenangriff abgewehrt"),
           Line2D([], [], linestyle="none", **st[("dt", "held")], label="OKW: gehalten oder (wieder) in deutscher Hand"),
           Line2D([], [], linestyle="none", **st[("dt", "entered")], label="OKW: Feind dringt ein")]
    ax.legend(handles=leg, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=8.8, frameon=False)
    ax.set_xlim(-0.6, len(days) - 0.4); ax.set_ylim(-1.2, len(places) - 0.1)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("Wer was wann meldete: Orte und Tage, 20. April – 1. Mai 1945", fontsize=13, color=INK, loc="left")
    fig.text(0.01, -0.13, "Grafik des Apparats nach den Wehrmachtberichten in der Marburger Zeitung (23.4.–2.5.) und Совинформбюро Bd. 8 "
             "S. 178–188. Ein Zeichen heißt: so gemeldet, nicht: so gewesen. Der „Raum Görlitz–Bautzen–Kamenz“ (25.4.) ist nicht eingetragen. CC BY 4.0.",
             fontsize=7, color=INK2)
    save(fig, "vizgegenangriff")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    lauban(); gegenangriff()
