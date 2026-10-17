"""Lädt die gemeinfreien Quell-PDFs nach tools/src/ (nicht im Repository):

- Ziemke, Stalingrad to Berlin (CMH Pub 30-5-1, 1987), Internet Archive StalingradToBerlinTheGermanDefeatInTheEast-nsia
- Сообщения Советского Информбюро, Bd. 8, Januar–Mai 1945 (Moskau 1945), Scan der Gebietsbibliothek Wologda (booksite.ru)
- Marburger Zeitung, 17.4.–8.5.1945, Slowenische Nationalbibliothek (dLib.si); der Abruf braucht das Cookie der Detailseite.

Lauf aus dem Repository:  python tools/fetch-quellen.py
"""
import http.cookiejar
import re
import urllib.request
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"
UA = {"User-Agent": "Mozilla/5.0 (Freigekaempft; educational; pantaleonfassbender@gmail.com)"}

FILES = {
    "ziemke-cmh-1987.pdf": "https://archive.org/download/StalingradToBerlinTheGermanDefeatInTheEast-nsia/StalingradToBerlinTheGermanDefeatInTheEast.pdf",
    "sovinformburo-t8-1945.pdf": "https://www.booksite.ru/fulltext/inform8/text.pdf",
}
# Ausgabe → dLib-URN (Suche: keywords=Marburger Zeitung, date=1945)
MZ = {"04-17": "LHUM6CVT", "04-18": "JFYILBDU", "04-19": "Q5V4ZWER", "04-20": "F2DJDGGD", "04-23": "B1MS8XKH",
      "04-24": "YMAGJV7I", "04-25": "YQUEVGVE", "04-26": "3DFFYXPQ", "04-27": "YYEMNBC2", "04-30": "ZMNXK13Y",
      "05-01": "WTLJFS5P", "05-02": "VGG2ZXXB", "05-03": "VFEMJVPW", "05-04": "J0J8RBGY", "05-07": "NAZDZ66I",
      "05-08": "P3BFFLBT"}


def get(opener, url, referer=None):
    req = urllib.request.Request(url, headers=dict(UA, **({"Referer": referer} if referer else {})))
    return opener.open(req, timeout=300).read()


def main():
    (SRC / "mz").mkdir(parents=True, exist_ok=True)
    plain = urllib.request.build_opener()
    for name, url in FILES.items():
        out = SRC / name
        if not out.exists():
            out.write_bytes(get(plain, url))
        print("ok", name, out.stat().st_size)
    jar = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    for d, doc in MZ.items():
        out = SRC / "mz" / f"mz-1945-{d}.pdf"
        if out.exists():
            continue
        det = f"https://www.dlib.si/details/URN:NBN:SI:DOC-{doc}"
        page = get(jar, det).decode("utf-8", "replace")
        pdf = re.search(rf"/stream/URN:NBN:SI:DOC-{doc}/[^\"']*/PDF", page).group(0)
        out.write_bytes(get(jar, "https://www.dlib.si" + pdf, referer=det))
        print("ok", out.name, out.stat().st_size)


if __name__ == "__main__":
    main()
