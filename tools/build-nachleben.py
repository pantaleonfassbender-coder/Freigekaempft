"""Modul 8 „Nachleben“: wie die Schlacht erinnert, gezählt und benannt wurde.

Quellen, an den Seitenbildern gelesen:
- Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), „Note on Sources“, S. 507 und 510 (gemeinfrei).
Die übrigen Abschnitte sind Referate, keine Quellentexte. Sie folgen der Commons-Beschreibung des Gedenksteins in Bautzen,
den Übersichten zur Schlacht und zur Literatur (die Bücher lagen nicht vor) und den Titeln der genannten Artikel, die nur
als Titel zitiert werden. Was sich bibliographisch nicht bestätigen ließ, ist weggelassen.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "nachleben.json"


def u(n, pg, titel, titel_en, orig, en="", de="", lang="", note="", note_en=""):
    d = {"n": n, "pg": pg, "titel": titel, "titel_en": titel_en, "orig": orig.strip()}
    if en:
        d["en"] = en.strip()
    if lang:
        d["lang"] = lang
    if de:
        d["de"] = de.strip()
    if note:
        d["note"], d["note_en"] = note, note_en
    return d


REF = ("Redaktioneller Text des Apparats, kein Quellentext.", "Editorial text of the apparatus, not a source text.")

QUELLEN = [
    u(1, "Ziemke S. 507", "„the best source“", "“the best source”",
      """In the continuing absence of significant Soviet documentary evidence the German military records remain the best source for the study of German and Soviet operations in World War II. Of the German collections the Armed Forces High Command (OKW), Army High Command (OKH), and field commands (army groups, armies, corps) are the most useful.""",
      de="""Solange es weiterhin an bedeutenden sowjetischen Dokumenten fehlt, bleiben die deutschen Militärakten die beste Quelle für das Studium der deutschen und sowjetischen Operationen im Zweiten Weltkrieg. Von den deutschen Beständen sind die des Oberkommandos der Wehrmacht (OKW), des Oberkommandos des Heeres (OKH) und der Kommandobehörden im Feld (Heeresgruppen, Armeen, Korps) die nützlichsten.""",
      lang="en",
      note="Aus Ziemkes Bemerkung über die Quellen am Ende des Buches. Sie erklärt, warum seine Darstellung der Schlacht die der deutschen Akten ist: Bautzen erscheint bei ihm als Lage der Heeresgruppe und als Hoffnung im Bunker (Bunker [1]–[6]). Die 2. Polnische Armee, gegen die der Gegenangriff lief, nennt sein Text in den Kapiteln über 1945 nicht; sie steht nur auf Karte 42 („Second (Polish)“), und das Register führt unter den polnischen Armeen nur die 1. Polnische Armee (S. 330, 345) und die Heimatarmee. Die Verluste der polnischen und sowjetischen Truppen bei Bautzen gibt Ziemke nicht an.",
      note_en="From Ziemke's note on the sources at the end of the book. It explains why his account of the battle is that of the German files: Bautzen appears in it as the army group's situation and as hope in the bunker (Bunker [1]–[6]). The Polish Second Army, against which the counterattack ran, is not named in his text in the chapters on 1945; it stands only on Map 42 ('Second (Polish)'), and the index lists among the Polish armies only the Polish First Army (pp. 330, 345) and the Home Army. Ziemke gives no losses for the Polish and Soviet troops at Bautzen."),
    u(2, "Ziemke S. 510", "„anthologies of the wartime communiqués“", "“anthologies of the wartime communiqués”",
      """In the postwar period up to and for several years after Stalin's death, the few Soviet histories of military operations in World War II that appeared read like anthologies of the wartime communiqués from Moscow, which, in fact, they for the most part were. Interpretation was restricted to panegyrics to Stalin and vituperative blasts against former friends and enemies alike.""",
      de="""In der Nachkriegszeit bis einige Jahre nach Stalins Tod lasen sich die wenigen sowjetischen Darstellungen der militärischen Operationen im Zweiten Weltkrieg, die erschienen, wie Sammlungen der Kriegsmeldungen aus Moskau, und das waren sie zum größten Teil tatsächlich. Die Deutung beschränkte sich auf Lobreden auf Stalin und Schmähungen früherer Freunde und Feinde gleichermaßen.""",
      lang="en",
      note="Die „communiqués from Moscow“ sind die Meldungen, die dieser Apparat aus dem achten Band des Sowjetischen Informationsbüros abdruckt (Lage [9]–[11], Meldungen [1]–[2]). Für Bautzen heißt das: Wer die sowjetische Darstellung jener Jahre las, las die Meldung vom 21. April, Bautzen sei „vollständig genommen“, und nach dem 26. April nichts mehr. Ziemke urteilt hier über die sowjetische Geschichtsschreibung; dass seine eigene auf den deutschen Akten ruht, sagt er drei Seiten vorher selbst (Nachleben [1]).",
      note_en="The 'communiqués from Moscow' are the reports this apparatus prints from the eighth volume of the Soviet Information Bureau (Situation [9]–[11], Reports [1]–[2]). For Bautzen this means: whoever read the Soviet account of those years read the report of 21 April that Bautzen was 'taken entirely', and after 26 April nothing more. Ziemke is judging Soviet historiography here; that his own rests on the German files he says himself three pages earlier (Afterlife [1])."),
]

GEDENKEN = [
    u(3, "Gedenkstein in Bautzen, Inschrift (Foto 2006)", "„… bei Wuischke ermordet wurden“", "“… murdered near Wuischke”",
      """ВЕЧНАЯ СЛАВА ВОИНАМ СОВЕТСКОЙ АРМИИ И ВОЙСКА ПОЛЬСКОГО · ПАВШИМ В СОВМЕСТНОЙ БОРЬБЕ ПРОТИВ ФАШИЗМА

WIECZNA SŁAWA ŻOŁNIERZOM ARMII RADZIECKIEJ I WOJSKA POLSKIEGO · KTÓRZY OFIAROWALI ŻYCIE W WALCE S FASZYZMOM

ZUM GEDENKEN DER 92 SOWJETISCHEN UND POLNISCHEN BÜRGER · DIE IN DEN LETZTEN KRIEGSTAGEN VON 1945 BEI WUISCHKE ERMORDET WURDEN

K WOPOMNJEĆU 92 SOWJETSKICH A PÓLSKICH STAĆANOW ZAMORDOWANYCH W POSLEDNICH DNJACH WÓJNY 1945 POLA WUJEŽKA""",
      en="""[Russian] Eternal glory to the soldiers of the Soviet Army and the Polish Army who fell in the common struggle against fascism.

[Polish] Eternal glory to the soldiers of the Soviet Army and the Polish Army who gave their lives in the fight against fascism.

[German] In memory of the 92 Soviet and Polish citizens who were murdered near Wuischke in the last days of the war in 1945.

[Sorbian] In memory of the 92 Soviet and Polish citizens murdered in the last days of the war in 1945 near Wuischke.""",
      de="""[Russisch] Ewiger Ruhm den Soldaten der Sowjetarmee und der Polnischen Armee, gefallen im gemeinsamen Kampf gegen den Faschismus.

[Polnisch] Ewiger Ruhm den Soldaten der Sowjetarmee und der Polnischen Armee, die im Kampf gegen den Faschismus ihr Leben hingaben.

[Deutsch] Zum Gedenken der 92 sowjetischen und polnischen Bürger, die in den letzten Kriegstagen von 1945 bei Wuischke ermordet wurden.

[Sorbisch] Zum Gedenken an 92 sowjetische und polnische Bürger, ermordet in den letzten Tagen des Krieges 1945 bei Wuischke.""",
      lang="mul",
      note="Am Foto von 2006 gelesen (Tafel); Zeilenumbrüche des Steins aufgelöst, die Trennpunkte des Steins beibehalten, „S FASZYZMOM“ wie auf dem Stein. Die Beschreibung der Bilddatei nennt ihn ein Denkmal für die polnischen und sowjetischen Gefallenen der Schlacht. Das sagen nur die russische und die polnische Inschrift. Die deutsche und die sorbische sprechen von 92 „Bürgern“, die „ermordet“ wurden, bei Wuischke (Wuježk) im Kreis Bautzen: nicht von Gefallenen, sondern von Opfern eines Verbrechens. Wer sie waren, wer sie tötete und wann genau, sagt der Stein nicht, und keine Meldung dieses Apparats nennt Wuischke. Im Bundesarchiv liegt unter den Akten der Bezirksverwaltung Dresden des Ministeriums für Staatssicherheit eine Akte über „Erschießungen ausländischer Kriegsgefangener bzw. Zwangsarbeiter im Jahr 1945 im Kreis Bautzen“ mit Berichten und Fotos von den Exhumierungen der Massengräber, „u. a. in den Ortschaften Wuischke und Soritz“ (BArch MfS BV Ddn AS/13/64); sie wurde hier nicht eingesehen. Wann der Stein gesetzt wurde, ist hier nicht belegt.",
      note_en="Read from the 2006 photograph (plate); the stone's line breaks resolved, its separating dots kept, 'S FASZYZMOM' as on the stone. The description of the image file calls it a memorial to the Polish and Soviet fallen of the battle. Only the Russian and Polish inscriptions say that. The German and Sorbian ones speak of 92 'citizens' who were 'murdered' near Wuischke (Wuježk) in the district of Bautzen: not of fallen soldiers but of victims of a crime. Who they were, who killed them and exactly when, the stone does not say, and no report in this apparatus names Wuischke. In the Bundesarchiv, among the files of the Dresden district administration of the Ministry for State Security, there is a file on 'shootings of foreign prisoners of war or forced labourers in 1945 in the district of Bautzen' with reports and photographs of the exhumations of the mass graves, 'among others in the villages of Wuischke and Soritz' (BArch MfS BV Ddn AS/13/64); it has not been consulted here. When the stone was set up is not documented here."),
    u(4, "Referat: Gedenkorte", "Referat: Denkmäler in der Lausitz und in Warschau", "Summary: memorials in Lusatia and in Warsaw",
      """Auf dem Fulksberg (Fulkec hórka) bei Crostwitz, nahe Horka, stehen zwei Denkmäler für die polnischen Soldaten, von 1967 und von 1980, mit Inschriften in polnischer, deutscher und sorbischer Sprache; Crostwitz lag damals in der DDR. In Bautzen steht der Gedenkstein mit den vier Inschriften (Nachleben [3]). Für das Außenlager des KZ Groß-Rosen wurde 1979 ein Gedenkstein gesetzt, 1993 entfernt und 1997 ersetzt (Verbrechen [5]). In Niederkaina erinnert eine Tafel an die getöteten Volkssturmmänner; sie wurde im April 2018 zerstört und ersetzt. Am Grab des Unbekannten Soldaten in Warschau nennt eine Tafel „BUDZISZYN“; nach der polnischen Übersicht zur Schlacht trug sie nach 1945 die Daten 21.–26. April 1945, seit 1990 die Daten 23.–28. April.""",
      en="""On the Fulksberg (Fulkec hórka) near Crostwitz, close to Horka, stand two memorials to the Polish soldiers, of 1967 and 1980, with inscriptions in Polish, German and Sorbian; Crostwitz then lay in the GDR. In Bautzen stands the memorial stone with the four inscriptions (Afterlife [3]). For the Groß-Rosen subcamp a memorial stone was set up in 1979, removed in 1993 and replaced in 1997 (Crimes [5]). At Niederkaina a plaque commemorates the Volkssturm men who were killed; it was destroyed in April 2018 and replaced. At the Tomb of the Unknown Soldier in Warsaw a plaque names 'BUDZISZYN'; according to the Polish overview of the battle it bore the dates 21–26 April 1945 after 1945, and since 1990 the dates 23–28 April.""",
      lang="de",
      note=REF[0] + " Nach den Referaten der Module 6 und 7 und der polnischen Übersicht zur Schlacht. Wer die Denkmäler auf dem Fulksberg errichten ließ und was ihre Inschriften genau sagen, ist hier nicht geprüft; der Wortlaut wird nachgetragen, wenn ein lesbares freies Bild vorliegt.",
      note_en=REF[1] + " After the summaries of modules 6 and 7 and the Polish overview of the battle. Who had the memorials on the Fulksberg erected and what their inscriptions say exactly has not been checked here; the wording will be added when a legible free image is available."),
]

DEUTUNG = [
    u(5, "Referat: Übersichten zur Schlacht; Grzelak/Stańczyk/Zwoliński 2002; Domański 2009; Kania 2023", "Referat: Sieg, Niederlage, Schweigen in Polen", "Summary: victory, defeat, silence in Poland",
      """In der Volksrepublik Polen wurde die Schlacht als blutiger polnischer Sieg dargestellt; dass die 2. Polnische Armee bei Bautzen schwer geschlagen worden war, wurde nach den neueren Übersichten verschwiegen, und um ihren Befehlshaber Karol Świerczewski entstand ein Heldenbild. Nach 1989 haben polnische Historiker die Führung der Armee scharf kritisiert, vor allem Świerczewskis Entscheidung, mit Teilen der Armee auf Dresden vorzustoßen, während ihre Flanke bei Bautzen offen lag. Die amtlichen polnischen Zahlen, die die Übersichten ohne eigenen Beleg wiedergeben, nennen 4.902 Tote, 10.532 Verwundete und 2.798 Vermisste. Die Titel der neueren Bücher zeigen die Richtung: Grzelak, Stańczyk und Zwoliński, „Armia Berlinga i Żymierskiego“ (2002); Domański, „Budziszyn 1945“ (2009); Kopociński und Kopociński, „Horka – łużycka Golgota“ (2021); Kania, „Budziszyn 1945. Ostatnia kontrofensywa Wehrmachtu: fakty i mity“ (2023), „Fakten und Mythen“.""",
      en="""In the Polish People's Republic the battle was presented as a bloody Polish victory; that the Polish Second Army had been badly beaten at Bautzen was, according to recent overviews, passed over in silence, and a hero's image grew up around its commander Karol Świerczewski. After 1989 Polish historians sharply criticised the army's leadership, above all Świerczewski's decision to push towards Dresden with part of the army while its flank at Bautzen lay open. The official Polish figures, which the overviews reproduce without a source of their own, give 4,902 dead, 10,532 wounded and 2,798 missing. The titles of the recent books show the direction: Grzelak, Stańczyk and Zwoliński, 'Armia Berlinga i Żymierskiego' (2002); Domański, 'Budziszyn 1945' (2009); Kopociński and Kopociński, 'Horka – łużycka Golgota' (2021); Kania, 'Budziszyn 1945. Ostatnia kontrofensywa Wehrmachtu: fakty i mity' (2023), 'facts and myths'.""",
      lang="de",
      note=REF[0] + " Nach den Übersichten zur Schlacht in der polnischen Wikipedia und im Portal dzieje.pl (Krzysztof Fudalej) und nach den Katalogeinträgen der genannten Bücher; die Bücher lagen nicht vor. Die Verlustzahlen sind die einzigen in diesem Apparat für eine der Armeen; die sowjetischen und deutschen Verluste bei Bautzen sind nicht belegt, und die 14.600 „Toten“ der deutschen Presse vom 7. Mai (Meldungen [5]) sind keine Zählung.",
      note_en=REF[1] + " After the overviews of the battle in the Polish Wikipedia and on the portal dzieje.pl (Krzysztof Fudalej) and the catalogue entries of the books named; the books themselves were not available. The loss figures are the only ones in this apparatus for any of the armies; the Soviet and German losses at Bautzen are not documented, and the 14,600 'dead' of the German press of 7 May (Reports [5]) are not a count."),
    u(6, "Referat: Junge Freiheit 2020; RBTH 2021", "Referat: „ein letzter Sieg“", "Summary: “a last victory”",
      """In populären Darstellungen wird die Schlacht auch als „letzter Sieg“ erzählt. Die Wochenzeitung Junge Freiheit überschrieb 2020 einen Artikel „Schlacht um Bautzen 1945: Ein letzter Sieg“; das russische Auslandsportal Russia Beyond (RBTH) veröffentlichte 2021 einen Artikel von Boris Egorov unter dem Titel „Germany’s last victory over the Red Army in WWII“. Der Titel dieses Apparats, „Freigekämpft“, ist das Wort des Wehrmachtberichts vom 26. April 1945 (Meldungen [3]); er nimmt das Etikett beim Wort und prüft es an den Meldungen, den Akten und den Opfern.""",
      en="""Popular accounts also tell the battle as a 'last victory'. The weekly Junge Freiheit headed an article in 2020 'Schlacht um Bautzen 1945: Ein letzter Sieg' ('The battle for Bautzen 1945: a last victory'); the Russian foreign-audience portal Russia Beyond (RBTH) published an article by Boris Egorov in 2021 under the title 'Germany's last victory over the Red Army in WWII'. The title of this apparatus, 'Freigekämpft' ('fought free'), is the word of the Wehrmacht report of 26 April 1945 (Reports [3]); it takes the label at its word and tests it against the reports, the files and the victims.""",
      lang="de",
      note=REF[0] + " Die Titel sind als Titel zitiert, nicht als Urteil; ihr Inhalt wird hier nicht referiert. Was die Module dieses Apparats zeigen: Bautzen wurde zurückgewonnen und blieb bis zur Kapitulation in deutscher Hand; der Angriff nach Norden kam nach Ziemke nahe an den Stillstand (Gegenangriff [10]); im Bunker wurde der Erfolg zur Weisung, in einem Krieg, der verloren war (Bunker [2]–[6]); und die Gewalt, die in denselben Tagen geschah, kommt in keiner Siegesmeldung vor (Verbrechen [3]–[5]).",
      note_en=REF[1] + " The titles are quoted as titles, not as judgements; their content is not summarised here. What the modules of this apparatus show: Bautzen was regained and remained in German hands until the capitulation; according to Ziemke the attack northward came close to a standstill (Counterattack [10]); in the bunker the success became an order, in a war that was lost (Bunker [2]–[6]); and the violence that took place in the same days appears in no victory report (Crimes [3]–[5])."),
]

DATA = {
    "titel": "Nachleben: Denkmäler und der „letzte Sieg“",
    "titel_en": "Afterlife: memorials and the 'last victory'",
    "autor": "Earl F. Ziemke (1968); Referat",
    "autor_en": "Earl F. Ziemke (1968); summary",
    "jahr": "1945–2023",
    "jahr_en": "1945–2023",
    "orig_sprache": "en",
    "pg_label": "",
    "quelle": "Earl F. Ziemke, Stalingrad to Berlin: The German Defeat in the East (Washington: Center of Military History, 1968; Nachdruck 1987), „Note on Sources“, S. 507, 510 (Internet Archive, gemeinfrei). Referate nach Commons, den Übersichten zur Schlacht und den Titeln der genannten Literatur.",
    "hinweis": "Wie die Schlacht nach 1945 erinnert, gezählt und benannt wurde. Zwei Stellen aus Ziemkes Bemerkung über die Quellen zeigen, worauf die Darstellungen ruhten: auf den deutschen Akten im Westen, auf den Moskauer Meldungen im Osten. Die Denkmäler stehen für die polnischen Soldaten, die sowjetischen Gefallenen, die Häftlinge und die getöteten Volkssturmmänner; die Deutungen reichen vom verschwiegenen Rückschlag in der Volksrepublik Polen bis zum „letzten Sieg“ der populären Publizistik. Die Inschrift des Gedenksteins ist am Foto gelesen; die übrigen Einheiten ab [4] sind Referate, ausdrücklich als solche gekennzeichnet; Titel, die sich nicht bestätigen ließen, sind weggelassen.",
    "hinweis_en": "How the battle was remembered, counted and named after 1945. Two passages from Ziemke's note on the sources show what the accounts rested on: on the German files in the West, on the Moscow reports in the East. The memorials stand for the Polish soldiers, the Soviet fallen, the prisoners and the Volkssturm men who were killed; the interpretations range from the setback passed over in silence in the Polish People's Republic to the 'last victory' of popular writing. The inscription of the memorial stone is read from the photograph; the remaining units from [4] on are summaries, expressly marked as such; titles that could not be confirmed are left out.",
    "sections": [
        {"id": "quellen", "titel": "Worauf die Darstellungen ruhten", "titel_en": "What the accounts rested on", "zk": "Nachleben",
         "blurb": "Ziemke über die deutschen Akten als „beste Quelle“ und über die sowjetischen Darstellungen als Sammlungen der Meldungen.",
         "blurb_en": "Ziemke on the German files as 'the best source' and on the Soviet accounts as collections of the communiqués.",
         "units": QUELLEN},
        {"id": "gedenken", "titel": "Gedenken", "titel_en": "Remembrance", "zk": "Nachleben",
         "blurb": "Ein Stein in vier Sprachen, der zwei verschiedene Dinge sagt; dann, als Referat, Fulksberg, Niederkaina, das Außenlager, Warschau.",
         "blurb_en": "A stone in four languages that says two different things; then, as a summary, Fulksberg, Niederkaina, the subcamp, Warsaw.",
         "units": GEDENKEN},
        {"id": "deutung", "titel": "Deutungen (Referat)", "titel_en": "Interpretations (summary)", "zk": "Nachleben",
         "blurb": "Sieg, Niederlage und Schweigen in Polen; der „letzte Sieg“ als Etikett. Kein Quellentext.",
         "blurb_en": "Victory, defeat and silence in Poland; the 'last victory' as a label. Not a source text.",
         "units": DEUTUNG},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
