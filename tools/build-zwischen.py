"""Modul 7 „Zwischen den Fronten“: Rückgeführte, Gesuchte, Befreite, und wer in den Meldungen nicht vorkommt.

Quellen, an den Seitenbildern gelesen:
- Marburger Zeitung Nr. 109 (19.4.1945), S. 2; Nr. 120 (30.4.1945), S. 2; Nr. 127 (7.5.1945), S. 2 (dLib.si). Nicht
  gezeichnete Meldungen, gemeinfrei.
- Сообщения Советского Информбюро, Bd. 8 (Moskau 1945), S. 186. Amtlich, gemeinfrei.
Der letzte Abschnitt ist ein Referat, kein Quellentext.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "zwischen.json"


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


GESUCHT = [
    u(1, "Marburger Zeitung, 19.4.1945, S. 2", "„Suchkarteien für Rückgeführte“", "“Search card indexes for evacuees”",
      """Suchkarteien für Rückgeführte
Zur Erleichterung der Nachfrage nach rückgeführten Angehörigen hat die NSV Suchkarteien sämtlicher im Reich weilenden Rückgeführten hergestellt. Zur Vermeidung langer Postwege sind Anfragen nach Rückgeführten an die für den Wohnsitz des Anfragenden zuständigen NSV-Orts- und -Kreisämter zu richten, die sich ihrerseits mit den Aufnahmegauen mittels Suchlisten in Verbindung setzen. Diese Anfragen sind nur im Postkartenformat zulässig und dürfen lediglich Vor- und Zunamen, Geburtsdatum und bisherige Anschrift des Gesuchten sowie die Anschrift des Anfragenden enthalten. Die Erfassung der Rückgeführten erfolgt unmittelbar durch die NSV-Dienststellen. Es liegt jedoch auch im eigenen Interesse der Rückgeführten, sich selbst bei der für ihren neuen Wohnsitz zuständigen NSV-Dienststelle unter Angabe von Vor- und Zunamen, Geburtsdatum, bisheriger und jetziger Anschrift zu melden. […]""",
      en="""Search card indexes for evacuees
To make it easier to inquire after evacuated relatives, the NSV has prepared search card indexes of all evacuees living in the Reich. To avoid long postal routes, inquiries about evacuees are to be addressed to the NSV local and district offices responsible for the inquirer's place of residence, which in turn contact the receiving Gaue by means of search lists. These inquiries are permitted only in postcard format and may contain only the first name and surname, date of birth and previous address of the person sought and the address of the inquirer. The registration of evacuees is carried out directly by the NSV offices. It is, however, also in the evacuees' own interest to register themselves with the NSV office responsible for their new residence, giving first name and surname, date of birth, previous and present address. […]""",
      lang="de",
      note="„Rückgeführte“ war das amtliche Wort für die Menschen, die vor der Front aus dem Osten fortgebracht worden oder geflohen waren; das Wort „Flüchtling“ vermied die Sprache der Behörden. Die NSV, die Nationalsozialistische Volkswohlfahrt, führte die Karteien. Die Meldung erschien am vierten Tag der Offensive an Oder und Neiße (Lage [3]); die Lausitz nennt sie nicht.",
      note_en="'Rückgeführte' ('those brought back') was the official word for people moved away from the front in the east or who had fled; official language avoided the word 'refugee'. The NSV, the National Socialist People's Welfare, kept the indexes. The notice appeared on the fourth day of the offensive on the Oder and Neisse (Situation [3]); it does not name Lusatia."),
    u(2, "Marburger Zeitung, 30.4.1945, S. 2", "„Mit 101 Jahren aus Oberschlesien nach Oberdonau“", "“At 101 from Upper Silesia to Upper Danube”",
      """Mit 101 Jahren aus Oberschlesien nach Oberdonau. Unter den vielen aus dem Gau Schlesien Rückgeführten befanden sich auch 28 Pfleglinge eines Altersheims in Oppeln. Sie wurden in Bad Ischl untergebracht. Die älteste ist die 101jährige Frau Adolfine Salomon, die, wie alle ihre Leidensgenossinnen, glücklich ist, nach den Strapazen der letzten Wochen wieder eine Stätte der Ruhe gefunden zu haben.""",
      en="""At 101 from Upper Silesia to Upper Danube. Among the many evacuated from the Gau of Silesia were also 28 residents of an old people's home in Oppeln. They were housed in Bad Ischl. The oldest is 101-year-old Mrs Adolfine Salomon, who, like all her companions in suffering, is happy to have found a place of rest again after the hardships of the last weeks.""",
      lang="de",
      note="Eine von vielen kurzen Meldungen dieser Wochen, die das Elend der Flucht in eine Geschichte vom glücklichen Ankommen verwandeln. Oppeln (Opole) liegt in Oberschlesien; Bad Ischl im heutigen Oberösterreich hieß damals „Oberdonau“. Die Lausitz war im April voll von Menschen aus Schlesien, die nach Westen zogen; die hier abgedruckten Meldungen beziffern sie nicht.",
      note_en="One of many short notices of these weeks that turn the misery of flight into a story of happy arrival. Oppeln (Opole) lies in Upper Silesia; Bad Ischl in today's Upper Austria was then called 'Oberdonau'. In April Lusatia was full of people from Silesia moving west; the reports printed here give no figures for them."),
    u(3, "Marburger Zeitung, 7.5.1945, S. 2", "„Schlesischer Suchdienst“: „nur um Volksgenossen“", "“Silesian search service”: “only national comrades”",
      """Schlesischer Suchdienst. Der Sender Görlitz bringt täglich im Anschluß an den 22-Uhr-Nachrichtendienst einen Suchdienst für schlesische Volksgenossen, die ihren früheren Wohnsitz vorübergehend verlassen haben. Ausdrücklich sei betont, daß es sich bei diesem Suchdienst nur um Volksgenossen handelt, die ihren ständigen Wohnsitz in Schlesien hatten. Zuschriften für diesen Suchdienst sind unter dem Kennwort „Schlesischer Suchdienst“ nach Reichenberg, Sudetenland, Postleitzahl 11 a, postlagernd zu senden.""",
      en="""Silesian search service. The Görlitz radio station broadcasts daily after the 10 p.m. news a search service for Silesian national comrades who have temporarily left their former place of residence. It is expressly emphasised that this search service is only for national comrades whose permanent residence was in Silesia. Letters for this search service are to be sent under the code word 'Silesian search service' to Reichenberg, Sudetenland, postal code 11 a, poste restante.""",
      lang="de",
      note="Am Tag vor der Kapitulation: „vorübergehend“ verlassen, und „nur“ für „Volksgenossen“. Der Suchdienst schloss aus, wer nach der Sprache des Regimes nicht zur „Volksgemeinschaft“ gehörte: Zwangsarbeiter, Kriegsgefangene, KZ-Häftlinge, die in Schlesien und der Lausitz ebenfalls unterwegs waren. Görlitz lag am Neiße-Ufer, um das seit dem 16. April gekämpft wurde; Reichenberg ist Liberec.",
      note_en="On the day before the capitulation: left 'temporarily', and 'only' for 'national comrades' (Volksgenossen). The search service excluded those who in the regime's language did not belong to the 'national community': forced labourers, prisoners of war, concentration-camp prisoners who were also on the roads in Silesia and Lusatia. Görlitz lay on the Neisse, fought over since 16 April; Reichenberg is Liberec."),
]

BEFREIT = [
    u(4, "Совинформбюро, Bd. 8, S. 186", "24. April: „десятки тысяч военнопленных“", "24 April: “tens of thousands of prisoners of war”",
      """[…] Наши кавалеристы в этом районе захватили 6 железнодорожных эшелонов и большое число автомашин.
Войска фронта освободили из фашистской неволи десятки тысяч военнопленных различных национальностей.""",
      en="""[…] Our cavalrymen in this area captured 6 railway trains and a large number of motor vehicles.
The troops of the front freed tens of thousands of prisoners of war of various nationalities from fascist captivity.""",
      de="""[…] Unsere Kavalleristen erbeuteten in diesem Raum 6 Eisenbahnzüge und eine große Zahl von Kraftwagen.
Die Truppen der Front befreiten Zehntausende Kriegsgefangene verschiedener Nationalitäten aus faschistischer Gefangenschaft.""",
      lang="ru",
      note="Der Bericht zum 24. April spricht vom Raum Großenhain nordwestlich Dresden, nicht von Bautzen. Wer die Befreiten waren, woher sie kamen und was aus ihnen wurde, sagt er nicht; sie bleiben „verschiedener Nationalitäten“. Wie in den Kriegsberichten oft, stehen die Befreiten als eine Zeile unter der erbeuteten Technik.",
      note_en="The account for 24 April speaks of the Großenhain area north-west of Dresden, not of Bautzen. Who the freed were, where they came from and what became of them, it does not say; they remain 'of various nationalities'. As often in the war reports, the freed stand as one line beneath the captured equipment."),
]

FEHLT = [
    u(5, "Referat: Domowina; Übersichten zu Crostwitz", "Referat: Die Sorben im Kampfgebiet", "Summary: the Sorbs in the battle zone",
      """Die Dörfer, durch die im April 1945 die Front ging, waren zum großen Teil sorbisch: Crostwitz (Chrósćicy), Panschwitz-Kuckau (Pančicy-Kukow), Horka, die Gegend um Bautzen (Budyšin). Bei Panschwitz-Kuckau und Crostwitz geriet die polnische 9. Infanteriedivision am 26. April auf ihrem Rückzug in den Gegenangriff; die Verwundeten von Horka gehörten zu ihr (Verbrechen [3]). Die sorbische Organisation Domowina, 1937 vom NS-Regime verboten, nahm nach ihren eigenen Angaben am 10. Mai 1945 in Crostwitz die Arbeit wieder auf, zwei Tage nach der Kapitulation. Die Denkmäler für die polnischen Soldaten auf dem Fulksberg (Fulkec hórka) bei Crostwitz tragen Inschriften in polnischer, deutscher und sorbischer Sprache.""",
      en="""The villages the front passed through in April 1945 were largely Sorbian: Crostwitz (Chrósćicy), Panschwitz-Kuckau (Pančicy-Kukow), Horka, the area around Bautzen (Budyšin). Near Panschwitz-Kuckau and Crostwitz the Polish 9th Infantry Division ran into the counterattack on its retreat on 26 April; the wounded of Horka belonged to it (Crimes [3]). The Sorbian organisation Domowina, banned by the Nazi regime in 1937, resumed its work in Crostwitz on 10 May 1945 according to its own account, two days after the capitulation. The memorials to the Polish soldiers on the Fulksberg (Fulkec hórka) near Crostwitz bear inscriptions in Polish, German and Sorbian.""",
      lang="de",
      note="Redaktioneller Text des Apparats, kein Quellentext. Nach der Darstellung der Domowina zu ihrer Geschichte und nach Übersichten zu Crostwitz und zur Schlacht; andere Darstellungen nennen für die Wiedergründung nicht Crostwitz als Ort. In keiner Meldung dieses Apparats kommen die Sorben vor, weder in den deutschen noch in den sowjetischen; die Wehrmachtberichte nennen nur deutsche Ortsnamen. Sorbische Zeugnisse aus diesen Tagen werden gesucht; was gemeinfrei und zugänglich ist, soll nachgetragen werden.",
      note_en="Editorial text of the apparatus, not a source text. After the Domowina's account of its own history and overviews of Crostwitz and the battle; other accounts do not give Crostwitz as the place of the refounding. The Sorbs appear in none of the reports in this apparatus, neither German nor Soviet; the Wehrmacht reports give only German place names. Sorbian testimony from these days is being sought; whatever is in the public domain and accessible is to be added."),
]

DATA = {
    "titel": "Zwischen den Fronten",
    "titel_en": "Between the fronts",
    "autor": "Marburger Zeitung, Sowjetisches Informationsbüro (1945); Referat",
    "autor_en": "Marburger Zeitung, Soviet Information Bureau (1945); summary",
    "jahr": "April–Mai 1945",
    "jahr_en": "April–May 1945",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Marburger Zeitung Nr. 109, 120, 127 (19.4., 30.4., 7.5.1945), jeweils S. 2 (dLib.si, URN:NBN:SI:DOC-Q5V4ZWER, -ZMNXK13Y, -NAZDZ66I); Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 186 (booksite.ru). Referat nach der Domowina und Übersichten zu Crostwitz.",
    "hinweis": "Wer zwischen den Fronten stand, kommt in den Meldungen kaum vor. Die deutsche Presse kennt „Rückgeführte“ und „Volksgenossen“, die gesucht werden dürfen; die sowjetischen Meldungen kennen befreite Kriegsgefangene „verschiedener Nationalitäten“ als eine Zeile unter der Beute. Zwangsarbeiter, KZ-Häftlinge auf den Todesmärschen und die sorbische Bevölkerung der umkämpften Dörfer fehlen. Die Grafik zu diesem Modul zählt, wer in den Zeitungen und Meldungen dieser Wochen vorkommt. Der letzte Abschnitt ist ein Referat, ausdrücklich als solches gekennzeichnet.",
    "hinweis_en": "Those who stood between the fronts hardly appear in the reports. The German press knows 'evacuees' and 'national comrades', who may be searched for; the Soviet reports know freed prisoners of war 'of various nationalities' as one line beneath the booty. Forced labourers, concentration-camp prisoners on the death marches and the Sorbian population of the contested villages are missing. The graphic for this module counts who appears in the newspapers and reports of these weeks. The last section is a summary, expressly marked as such.",
    "sections": [
        {"id": "gesucht", "titel": "Rückgeführt und gesucht", "titel_en": "Evacuated and searched for", "zk": "Zwischen",
         "blurb": "Die NSV-Kartei, die Hundertjährige aus Oppeln, und ein Suchdienst „nur“ für „Volksgenossen“.",
         "blurb_en": "The NSV card index, the centenarian from Oppeln, and a search service 'only' for 'national comrades'.",
         "units": GESUCHT},
        {"id": "befreit", "titel": "Befreit, ohne Namen", "titel_en": "Freed, without names", "zk": "Zwischen",
         "blurb": "Eine sowjetische Meldung über befreite Kriegsgefangene: Zehntausende, ohne Namen, unter der Beute.",
         "blurb_en": "A Soviet notice of freed prisoners of war: tens of thousands, without names, beneath the booty.",
         "units": BEFREIT},
        {"id": "fehlt", "titel": "Wer fehlt (Referat)", "titel_en": "Who is missing (summary)", "zk": "Zwischen",
         "blurb": "Die Sorben in den umkämpften Dörfern, nach der neueren Literatur. Kein Quellentext.",
         "blurb_en": "The Sorbs in the contested villages, after recent literature. Not a source text.",
         "units": FEHLT},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
