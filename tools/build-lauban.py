"""Modul 2 „Lauban: die Wochenschau einer Gegenoffensive“: die Rückeroberung von Lauban (Lubań) Anfang März 1945, wie
OKW-Bericht, Nachrichtenbüro und Wochenschau sie zum Vorbild machten, und wie Moskau schwieg.

Quellen, an den Seitenbildern gelesen:
- Wehrmachtberichte vom 5., 7. und 8. März 1945 in der Marburger Zeitung Nr. 65 (6.3.), Nr. 67 (8.3.) und Nr. 68 (9.3.),
  jeweils S. 1 (dLib.si). Nicht gezeichnete amtliche Bekanntmachungen, gemeinfrei.
- Meldung des Deutschen Nachrichtenbüros (dnb) „Dr. Goebbels in Lauban und Görlitz“, Berlin, 11. März 1945, in der
  Marburger Zeitung Nr. 71 (12.3.1945), S. 1. Nicht namentlich gezeichnete Agenturmeldung, gemeinfrei. Gekürzt ([…]).
- Сообщения Советского Информбюро, Bd. 8 (Moskau 1945), S. 209: Оперативная сводка за 9 мая. Amtlich, gemeinfrei.
Die Deutsche Wochenschau wird nicht gezeigt; der Film ist im Holocaust Memorial Museum Washington katalogisiert
(Film ID 2886, Bundesarchiv), Rechte beim Bundesarchiv. Die Zeitleiste verlinkt den Katalogeintrag.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "lauban.json"


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


OKW = [
    u(1, "Marburger Zeitung, 6.3.1945, S. 1", "Bericht vom 5. März: „im Raum von Lauban“", "Report of 5 March: “in the area of Lauban”",
      """Führerhauptquartier, 5. März
Das Oberkommando der Wehrmacht gibt bekannt: […] Unsere Panzer und Panzergrenadiere hielten im Raum von Lauban ihre an den Vortagen gewonnenen Stellungen gegen zahlreiche Gegenangriffe der Bolschewisten und erzielten in wendiger Kampfführung weiteren Geländegewinn. […]""",
      en="""Führer headquarters, 5 March
The High Command of the Wehrmacht announces: […] Our tanks and panzer grenadiers held the positions won on the previous days in the area of Lauban against numerous counterattacks by the Bolsheviks and gained further ground in agile fighting. […]""",
      lang="de",
      note="Lauban, heute Lubań in Polen, liegt zwischen Görlitz und Bunzlau am Queis. Die Stadt war zuvor in sowjetische Hand gekommen; wann, sagen die hier abgedruckten Quellen nicht. Der deutsche Gegenangriff begann Anfang März, also gerade dort, wo Schörner im April den sowjetischen Hauptangriff erwartete (Lage [2]).",
      note_en="Lauban, today Lubań in Poland, lies between Görlitz and Bunzlau on the Queis. The town had come into Soviet hands before; when, the sources printed here do not say. The German counterattack began early in March, precisely where in April Schörner expected the main Soviet attack (Situation [2])."),
    u(2, "Marburger Zeitung, 8.3.1945, S. 1", "Bericht vom 7. März: „Einschließung“", "Report of 7 March: “encirclement”",
      """Führerhauptquartier, 7. März
Das Oberkommando der Wehrmacht gibt bekannt: […] Unsere Gegenangriffe beiderseits Lauban führten trotz erbitterter Gegenwehr sowjetischer Panzerverbände zur Einschließung einer feindlichen Kräftegruppe nordöstlich der Stadt. […]""",
      en="""Führer headquarters, 7 March
The High Command of the Wehrmacht announces: […] Our counterattacks on both sides of Lauban, in spite of bitter resistance by Soviet armoured formations, led to the encirclement of an enemy force north-east of the town. […]""",
      lang="de",
      note="Die Zeitung machte daraus die Schlagzeile „Sowjetkräfte bei Lauban eingeschlossen“. Auf derselben Seite stand, die Sowjets würden „jedes Haus und Gehöft, das nicht für militärische Zwecke benötigt wird“, niederbrennen; die Meldungen über Gewalt der Roten Armee und über den eigenen Gegenangriff erschienen in diesen Wochen nebeneinander.",
      note_en="The newspaper turned it into the headline 'Soviet forces encircled at Lauban'. The same page said the Soviets were burning down 'every house and farmstead not needed for military purposes'; in these weeks reports of Red Army violence and of the German counterattack appeared side by side."),
    u(3, "Marburger Zeitung, 9.3.1945, S. 1", "Bericht vom 8. März: „Die Stadt ist befreit“", "Report of 8 March: “The town is liberated”",
      """Führerhauptquartier, 8. März
Das Oberkommando der Wehrmacht gibt bekannt: […] Beiderseits Lauban haben Truppen des Heeres, der Waffen-SS und Volkssturmeinheiten, hervorragend durch die Luftwaffe unterstützt, starke Teile der sowjetischen 3. Garde-Panzerarmee verlustreich geschlagen. Die Stadt ist befreit. 162 feindliche Panzer, 159 Geschütze, 74 Granatwerfer und 106 Kraftfahrzeuge wurden vernichtet oder erbeutet. […]""",
      en="""Führer headquarters, 8 March
The High Command of the Wehrmacht announces: […] On both sides of Lauban troops of the army, the Waffen-SS and Volkssturm units, outstandingly supported by the Luftwaffe, have defeated strong parts of the Soviet 3rd Guards Tank Army with heavy losses. The town is liberated. 162 enemy tanks, 159 guns, 74 mortars and 106 motor vehicles were destroyed or captured. […]""",
      lang="de",
      note="Schlagzeile der Zeitung: „Die Stadt Lauban wieder befreit“. Die Zeitung setzt für „SS“ die Runen; hier steht der Name in Buchstaben. Die Zahlen der Beute lassen sich aus den hier abgedruckten Quellen nicht prüfen. Es ist die 3. Garde-Panzerarmee, die die deutsche Feindaufklärung im April aus den Augen verlor und östlich von Bunzlau vermutete (Lage [2]).",
      note_en="The newspaper's headline: 'The town of Lauban liberated again'. The newspaper prints the SS runes; here the name is spelled out. The figures of booty cannot be checked from the sources printed here. It is the 3rd Guards Tank Army that German intelligence lost track of in April and placed east of Bunzlau (Situation [2])."),
]

GOEBBELS = [
    u(4, "Marburger Zeitung, 12.3.1945, S. 1", "Goebbels auf dem Markt von Lauban", "Goebbels in the market square of Lauban",
      """Dr. Goebbels in Lauban und Görlitz
»Der Feind ist zu schlagen, denn wir haben ihn oft genug geschlagen«
dnb Berlin, 11. März
Reichsminister Dr. Goebbels weilte in diesen Tagen an der schlesischen Front, wo er der kämpfenden Truppe, verschiedenen Stäben und frontnahen Städten Besuche abstattete. Unmittelbar nachdem Truppen des Heeres, der Waffen-SS und Volkssturmeinheiten die Stadt Lauban wieder freigekämpft und dabei starke Teile der sowjetischen 3. Gardepanzerarmee verlustreich geschlagen hatten, sprach Dr. Goebbels auf dem Marktplatz zu den hier angetretenen Befreiern der Stadt, unter ihnen, neben bewährten Volkssturmmännern auch tapfere Hitler-Jungen, die soeben mit dem Eisernen Kreuz ausgezeichnet worden waren.
Der Oberbefehlshaber einer Heeresgruppe, Generaloberst Schörner, begrüßte in dieser denkwürdigen Stunde, da der Feind erneut die ungebrochene Angriffskraft unserer Truppen zu verspüren bekam, Dr. Goebbels im Namen aller seiner Soldaten, die heute entschlossener denn je und mit politischem Fanatismus den verhaßten Feind bekämpften.
In seiner Ansprache an die Befreier Laubans dankte Dr. Goebbels all den namenlosen Kämpfern und Helden, die mit altem Angriffsschwung soeben ein neues Ruhmesblatt in die Geschichte dieses Krieges eingefügt hätten. […]
Während Dr. Goebbels sprach, fanden sich immer mehr Soldaten auf dem Marktplatz Laubans ein, der, zerstört wie andere Teile der Stadt, die Zeichen des sinnlosen Wütens der bolschewistischen Horden trägt. Es klang wie ein Schwur, der sich mit dem Lärm des nahen Kampfes mischte, als die auf dem Marktplatz Angetretenen in das Sieg-Heil einstimmten, das Dr. Goebbels auf den Führer ausbrachte.""",
      en="""Dr Goebbels in Lauban and Görlitz
'The enemy can be beaten, for we have beaten him often enough'
dnb Berlin, 11 March
Reich Minister Dr Goebbels was at the Silesian front in these days, where he visited the fighting troops, various staffs and towns near the front. Immediately after troops of the army, the Waffen-SS and Volkssturm units had fought the town of Lauban free again and in doing so had defeated strong parts of the Soviet 3rd Guards Tank Army with heavy losses, Dr Goebbels spoke in the market square to the liberators of the town assembled there, among them, besides proven Volkssturm men, brave Hitler Youths who had just been decorated with the Iron Cross.
The commander-in-chief of an army group, Colonel-General Schörner, in this memorable hour, when the enemy once more felt the unbroken striking power of our troops, welcomed Dr Goebbels in the name of all his soldiers, who today fought the hated enemy more resolutely than ever and with political fanaticism.
In his address to the liberators of Lauban Dr Goebbels thanked all the nameless fighters and heroes who with their old offensive dash had just added a new page of glory to the history of this war. […]
While Dr Goebbels was speaking, more and more soldiers gathered in the market square of Lauban, which, destroyed like other parts of the town, bears the marks of the senseless raging of the Bolshevik hordes. It sounded like an oath, mingling with the noise of the nearby fighting, when those assembled in the market square joined in the Sieg Heil that Dr Goebbels called for the Führer.""",
      lang="de",
      note="Das Wort, das im April über Bautzen stehen wird, steht hier schon über Lauban: die Stadt sei „wieder freigekämpft“. Die Meldung nennt den Tag der Rede nicht („in diesen Tagen“). Unter den Ausgezeichneten waren Hitlerjungen; die Wochenschau zeigte einen von ihnen, den sechzehnjährigen Wilhelm Hübner (Katalog des US Holocaust Memorial Museum, Film 2886). Schörner wurde am 5. April Generalfeldmarschall (Lage [2]).",
      note_en="The word that in April will stand over Bautzen already stands here over Lauban: the town had been 'fought free again'. The report does not give the day of the speech ('in these days'). Among those decorated were Hitler Youths; the newsreel showed one of them, sixteen-year-old Wilhelm Hübner (catalogue of the US Holocaust Memorial Museum, film 2886). Schörner became a field marshal on 5 April (Situation [2])."),
    u(5, "Marburger Zeitung, 12.3.1945, S. 1", "Görlitz am Abend: „Schlagt die Bolschewisten, wo ihr sie trefft!“", "Görlitz in the evening: “Beat the Bolsheviks wherever you meet them!”",
      """Am Abend sprach Reichsminister Dr. Goebbels in der Frontstadt Görlitz zu Tausenden von Soldaten, Volkssturmmännern, Frauen, Hitler-Jungen und Rüstungsarbeitern. […] Neben Rüstungsarbeitern bemerkte man zahlreiche Frauen, die tapfer auf ihren kriegswichtigen Posten ausharren, aber man sah auch jene unglücklichen Mütter, die das Wüten und die Grausamkeit der bolschewistischen Soldateska über sich hatten ergehen lassen müssen und die noch das Bild ihrer zu Tode gequälten Kinder vor Augen hatten. […]
Der Schock, der die unmittelbar Bedrohten zuerst befallen habe, könne uns deshalb nicht mehr schrecken, und statt der Panik, die der verhaßte Feind bei uns zu verbreiten suche, begegne er heute der einheitlichen Parole von Hunderttausenden von Ostfrontsoldaten: »Schlagt die Bolschewisten, wo ihr sie trefft!« […] „Es bleibt uns zu tun übrig, wenn anders wir nicht unser eigenes und das Leben unseres Volkes für jetzt und für alle Zukunft um den billigsten Preis verkaufen wollen, in Ost und West und in der kämpfenden Heimatfront beharrlich stehen zu bleiben und fanatisch zu kämpfen.“""",
      en="""In the evening Reich Minister Dr Goebbels spoke in the front-line town of Görlitz to thousands of soldiers, Volkssturm men, women, Hitler Youths and armaments workers. […] Besides armaments workers one noticed numerous women who bravely hold out at their posts important to the war, but one also saw those unhappy mothers who had had to suffer the raging and the cruelty of the Bolshevik soldiery and who still had the picture of their children tortured to death before their eyes. […]
The shock that had first seized those directly threatened could therefore no longer frighten us, and instead of the panic the hated enemy sought to spread among us, he met today the united watchword of hundreds of thousands of soldiers of the Eastern Front: 'Beat the Bolsheviks wherever you meet them!' […] 'What remains for us to do, unless we want to sell our own life and the life of our people, now and for all the future, at the cheapest price, is to stand firm in East and West and in the fighting home front and to fight fanatically.'""",
      lang="de",
      note="Die Gewalt der Roten Armee gegen deutsche Zivilisten in Schlesien war wirklich; sie war im März 1945 aber auch das wichtigste Mittel, mit dem die Propaganda zum Weiterkämpfen trieb. Die Wochenschau zeigte in Lauban Leichen von Zivilisten, und ihr Sprecher nannte die Täter „Untermenschen“ (Katalog des US Holocaust Memorial Museum, Film 2886). Von deutscher Gewalt, von den Häftlingen, die in der Lausitz an den Stellungen schanzten, spricht die Meldung nicht (Modul „Horka, Niederkaina, das Außenlager“, in Vorbereitung).",
      note_en="Red Army violence against German civilians in Silesia was real; but in March 1945 it was also the propaganda's chief means of driving people to fight on. In Lauban the newsreel showed bodies of civilians, and its narrator called the perpetrators 'subhumans' (catalogue of the US Holocaust Memorial Museum, film 2886). Of German violence, of the camp prisoners digging the positions in Lusatia, the report says nothing (module 'Horka, Niederkaina, the subcamp', in preparation)."),
]

MOSKAU = [
    u(6, "Совинформбюро, Bd. 8, S. 209", "Moskau, 9. Mai: Lauban, beiläufig", "Moscow, 9 May: Lauban, in passing",
      """ОПЕРАТИВНАЯ СВОДКА ЗА 9 МАЯ
[…] Войска 1-го УКРАИНСКОГО фронта, в результате стремительного ночного манёвра танковых соединений и пехоты, сломили сопротивление противника и 9 мая в 4 часа утра освободили от немецких захватчиков столицу союзной нам ЧЕХОСЛОВАКИИ город ПРАГУ, а также заняли на территории ЧЕХОСЛОВАКИИ города ХОМУТОВ, КАДАНЬ, БИЛИНА, ЛОУНЫ. Юго-восточнее ДРЕЗДЕНА войска фронта, продвигаясь вперёд, заняли города ПИРНА, ЗЕБНИТЦ, НОЙГЕРСДОРФ, ЦИТТАУ, ФРИДЛАНТ, ЛАУБАН, ГРАЙФФЕНБЕРГ, ГИРШБЕРГ, ВАРМБРУНН. […]""",
      en="""OPERATIONAL SUMMARY FOR 9 MAY
[…] Troops of the 1st UKRAINIAN Front, as a result of a swift night manoeuvre by tank formations and infantry, broke the enemy's resistance and at 4 o'clock in the morning of 9 May liberated from the German invaders the capital of our ally CZECHOSLOVAKIA, the city of PRAGUE, and also occupied in CZECHOSLOVAKIA the towns of CHOMUTOV, KADAŇ, BÍLINA, LOUNY. South-east of DRESDEN the troops of the front, advancing, occupied the towns of PIRNA, SEBNITZ, NEUGERSDORF, ZITTAU, FRIEDLAND, LAUBAN, GREIFFENBERG, HIRSCHBERG, WARMBRUNN. […]""",
      de="""OPERATIVE MELDUNG FÜR DEN 9. MAI
[…] Die Truppen der 1. UKRAINISCHEN Front haben im Ergebnis eines raschen nächtlichen Manövers von Panzerverbänden und Infanterie den Widerstand des Gegners gebrochen und am 9. Mai um 4 Uhr morgens die Hauptstadt der mit uns verbündeten TSCHECHOSLOWAKEI, die Stadt PRAG, von den deutschen Eindringlingen befreit und auf dem Gebiet der TSCHECHOSLOWAKEI die Städte CHOMUTOV, KADAŇ, BÍLINA, LOUNY besetzt. Südöstlich DRESDEN besetzten die Truppen der Front im Vorrücken die Städte PIRNA, SEBNITZ, NEUGERSDORF, ZITTAU, FRIEDLAND, LAUBAN, GREIFFENBERG, HIRSCHBERG, WARMBRUNN. […]""",
      lang="ru",
      note="Im ganzen Band der Meldungen für Januar bis Mai 1945 erscheint Lauban, nach Durchsicht seines Textes, nur hier, am Tag nach der Kapitulation, als sechster Name in einer Reihe. Weder die Einnahme der Stadt noch ihr Verlust im März wurde gemeldet. Wie bei Bautzen im April (Meldungen [1]) schwieg Moskau über Rückschläge; das OKW machte aus ihnen Schlagzeilen.",
      note_en="In the whole volume of reports for January to May 1945 Lauban appears, as far as a search of its text shows, only here, the day after the capitulation, as the sixth name in a list. Neither the taking of the town nor its loss in March was reported. As with Bautzen in April (Reports [1]), Moscow kept silent about setbacks; the OKW turned them into headlines."),
]

DATA = {
    "titel": "Lauban: die Wochenschau einer Gegenoffensive",
    "titel_en": "Lauban: the newsreel of a counteroffensive",
    "autor": "Oberkommando der Wehrmacht, Deutsches Nachrichtenbüro (März 1945), Sowjetisches Informationsbüro (Mai 1945)",
    "autor_en": "High Command of the Wehrmacht, German News Bureau (March 1945), Soviet Information Bureau (May 1945)",
    "jahr": "5.–12. März 1945",
    "jahr_en": "5–12 March 1945",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Wehrmachtberichte vom 5., 7. und 8. März 1945 in der Marburger Zeitung Nr. 65, 67, 68 (6., 8., 9.3.1945), S. 1; dnb-Meldung „Dr. Goebbels in Lauban und Görlitz“, Marburger Zeitung Nr. 71 (12.3.1945), S. 1 (dLib.si, URN:NBN:SI:DOC-RE6NCANH, -4B8FMFFJ, -WWSMFHVA, -E7P1B7LR); Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 209. Die Deutsche Wochenschau (USHMM Film 2886, Produktionsdatum 16. März 1945, Rechte Bundesarchiv) wird nur genannt.",
    "hinweis": "Die Deutsche Wochenschau endete am 22. März 1945; die letzte Gegenoffensive, die sie zeigte, war Lauban. Der Film selbst ist hier nicht zu sehen: Seine Rechte liegen beim Bundesarchiv, und der Apparat zeigt keine NS-Filme. Der Katalog des US Holocaust Memorial Museum beschreibt ihn: Goebbels und Schörner in Lauban, ein sechzehnjähriger Hitlerjunge auf dem Markt, Leichen von Zivilisten, ein Sprecher, der die Täter „Untermenschen“ nennt, und Goebbels' Rede in Görlitz. Was der Film zeigte, steht hier in den Worten der Zeitung, die dasselbe am 12. März druckte. Texte nach den Seitenbildern; Auslassungen […]. Die Meldungen sind Propaganda; die Anmerkungen ordnen sie ein.",
    "hinweis_en": "The German newsreel ended on 22 March 1945; the last counteroffensive it showed was Lauban. The film itself is not shown here: its rights lie with the Bundesarchiv, and the apparatus shows no Nazi films. The catalogue of the US Holocaust Memorial Museum describes it: Goebbels and Schörner in Lauban, a sixteen-year-old Hitler Youth in the market square, bodies of civilians, a narrator who calls the perpetrators 'subhumans', and Goebbels's speech at Görlitz. What the film showed appears here in the words of the newspaper that printed the same on 12 March. Texts from the page images; omissions […]. The reports are propaganda; the notes place them in context.",
    "sections": [
        {"id": "okw", "titel": "„Die Stadt ist befreit“", "titel_en": "“The town is liberated”", "zk": "Lauban",
         "blurb": "Drei Wehrmachtberichte vom 5. bis 8. März: gehaltene Stellungen, eine Einschließung, eine befreite Stadt und die Zahl der Beute.",
         "blurb_en": "Three Wehrmacht reports from 5 to 8 March: positions held, an encirclement, a liberated town and the count of booty.",
         "units": OKW},
        {"id": "goebbels", "titel": "Goebbels in Lauban und Görlitz", "titel_en": "Goebbels in Lauban and Görlitz", "zk": "Lauban",
         "blurb": "Die Meldung des Deutschen Nachrichtenbüros über den Besuch, den auch die Wochenschau zeigte: der Markt von Lauban, Schörner, die Hitlerjungen mit dem Eisernen Kreuz, die Rede in Görlitz.",
         "blurb_en": "The German News Bureau's report of the visit the newsreel also showed: the market square of Lauban, Schörner, the Hitler Youths with the Iron Cross, the speech at Görlitz.",
         "units": GOEBBELS},
        {"id": "moskau", "titel": "Was Moskau nicht meldete", "titel_en": "What Moscow did not report", "zk": "Lauban",
         "blurb": "Lauban kommt in den sowjetischen Meldungen bis zum 9. Mai nicht vor.",
         "blurb_en": "Lauban does not appear in the Soviet reports until 9 May.",
         "units": MOSKAU},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
