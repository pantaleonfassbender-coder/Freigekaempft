"""Tafeln aus Seitenbildern der Quellen (tools/src/, siehe fetch-quellen.py): Ausschnitte von Seiten und Karten.
Zeitungsausschnitte werden so gewählt, dass kein Zeitungskopf und kein Hoheitszeichen darauf steht; das wird bei jedem
neuen Ausschnitt am Bild geprüft. Schreibt assets/plates/<id>.jpg (max. 1600 px) und <id>_t.jpg.
Lauf aus dem Repository:  python tools/build-seiten.py [ids…]
"""
import io
import sys
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "src"
OUT = ROOT / "assets" / "plates"

# id: (Datei, Seitenindex im PDF, Ausschnitt in PDF-Punkten oder None für das eingebettete Bild, dpi)
SEITEN = {
    # Ziemke, Map 42 „Berlin, 16 April–7 May 1945“ (Kartenseite S. 468)
    "ziemke42": ("ziemke-cmh-1987.pdf", 480, None, 0),
    # Marburger Zeitung Nr. 110, 20.4.1945, S. 2: Schlagzeile und OKW-Bericht vom 19.4. (ohne Zeitungskopf; die Spalte
    # rechts davon, ein antisemitischer Leitartikel, liegt außerhalb des Ausschnitts)
    "mzokw20": ("mz/mz-1945-04-20.pdf", 1, (190, 505, 712, 905), 150),
    # Сообщения Советского Информбюро, Bd. 8, S. 177: Оперативная сводка за 19 апреля
    "sib19": ("sovinformburo-t8-1945.pdf", 175, (20, 345, 431, 425), 200),
    # Marburger Zeitung Nr. 68, 9.3.1945, S. 1: Schlagzeile (ohne Zeitungskopf; der Bericht darunter setzt SS-Runen und
    # bleibt außerhalb des Ausschnitts)
    "mzlauban": ("mz/mz-1945-03-09.pdf", 0, (0, 203, 600, 292), 150),
    # Marburger Zeitung Nr. 71, 12.3.1945, S. 1: Überschrift der dnb-Meldung „Dr. Goebbels in Lauban und Görlitz“
    "mzgoebbels": ("mz/mz-1945-03-12.pdf", 0, (585, 233, 1000, 290), 170),
    # Сообщения Советского Информбюро, Bd. 8, S. 209: Оперативная сводка за 9 мая (Lauban)
    "sib9mai": ("sovinformburo-t8-1945.pdf", 207, (20, 360, 431, 450), 200),
    # Marburger Zeitung Nr. 115, 25.4.1945, S. 1: Schlagzeile „… Pulsnitz und Kamenz wieder in deutscher Hand“
    "mzkamenz": ("mz/mz-1945-04-25.pdf", 0, (0, 238, 655, 312), 150),
    # Marburger Zeitung Nr. 121, 1.5.1945, S. 2: „Kamenz und Königsbrück wurden wiedergenommen“
    "mzkamenz2": ("mz/mz-1945-05-01.pdf", 1, (203, 308, 402, 362), 190),
    # Сообщения Советского Информбюро, Bd. 8, S. 186: Оперативная сводка за 25 апреля (Bautzen)
    "sib25": ("sovinformburo-t8-1945.pdf", 184, (0, 480, 431, 540), 200),
    # Сообщения Советского Информбюро, Bd. 8, S. 180: der Bericht zum 21. April (rechte Spalte)
    "sib21": ("sovinformburo-t8-1945.pdf", 178, (215, 390, 431, 562), 220),
    # Marburger Zeitung Nr. 117, 27.4.1945, S. 1: Schlagzeile mit „Bautzen freigekämpft“ (ohne Zeitungskopf)
    "mzbautzen": ("mz/mz-1945-04-27.pdf", 0, (0, 222, 600, 312), 150),
    # Marburger Zeitung Nr. 124, 4.5.1945, S. 1: dnb „Das sind unsere Jungen“, Anfang
    "mzjungen": ("mz/mz-1945-05-04.pdf", 0, (205, 1228, 405, 1462), 170),
    # Ziemke S. 483, rechte Spalte: „Weidling remembered 26 April …“
    "ziemke483": ("ziemke-cmh-1987.pdf", 495, (232, 102, 452, 270), 170),
    # Ziemke S. 488, rechte Spalte: „Corpses hanging in the streets …“
    "ziemke488": ("ziemke-cmh-1987.pdf", 500, (222, 466, 420, 556), 170),
    # Marburger Zeitung Nr. 120, 30.4.1945, S. 2: „Mit 101 Jahren aus Oberschlesien nach Oberdonau“
    "mzoppeln": ("mz/mz-1945-04-30.pdf", 1, (805, 963, 1002, 1078), 170),
    # Marburger Zeitung Nr. 127, 7.5.1945, S. 2: „Schlesischer Suchdienst“
    "mzsuch": ("mz/mz-1945-05-07.pdf", 1, (385, 972, 588, 1112), 170),
    # Ziemke S. 507, „Note on Sources“: „In the continuing absence …“
    "ziemke507": ("ziemke-cmh-1987.pdf", 519, (40, 337, 238, 396), 170),
}


def render(pid):
    f, idx, clip, dpi = SEITEN[pid]
    page = pymupdf.open(SRC / f)[idx]
    if clip is None:
        xref = page.get_images(full=True)[0][0]
        im = Image.open(io.BytesIO(pymupdf.Pixmap(page.parent, xref).tobytes("png")))
    else:
        pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(*clip))
        im = Image.open(io.BytesIO(pix.tobytes("png")))
    im = im.convert("RGB")
    big = im.copy(); big.thumbnail((1600, 1600)); big.save(OUT / f"{pid}.jpg", quality=86)
    th = im.copy(); th.thumbnail((520, 520)); th.save(OUT / f"{pid}_t.jpg", quality=82)
    print("ok", pid, big.size)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for pid in (sys.argv[1:] or SEITEN):
        render(pid)
