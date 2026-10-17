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
