"""Modul 4 „Zwei Meldungen, eine Stadt“: die sowjetische Meldung vom 21. April, Bautzen sei ganz genommen, die deutsche vom
26. April, die Besatzung von Bautzen sei freigekämpft, und was die deutsche Presse danach aus Bautzen machte.

Quellen, an den Seitenbildern gelesen:
- Сообщения Советского Информбюро, Bd. 8 (Moskau 1945), S. 180: Оперативная сводка за 21 апреля und der folgende Bericht.
- Wehrmachtbericht vom 26. April 1945, Marburger Zeitung Nr. 117 (27.4.1945), S. 1 (dLib.si).
- dnb-Meldung „Das sind unsere Jungen“, 3. Mai 1945, Marburger Zeitung Nr. 124 (4.5.1945), S. 1.
- „Die Kampfkraft der Front. Vom Heldentum unserer Soldaten und Hitler-Jungen“, Marburger Zeitung Nr. 127 (7.5.1945), S. 1
  (nicht gezeichnet).
Nicht gezeichnete amtliche Bekanntmachungen und Agenturmeldungen von 1945, gemeinfrei.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "meldungen.json"


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


MOSKAU = [
    u(1, "Совинформбюро, Bd. 8, S. 180", "Meldung für den 21. April: „besetzten … Kamenz, Bautzen“", "Report for 21 April: “occupied … Kamenz, Bautzen”",
      """ОПЕРАТИВНАЯ СВОДКА ЗА 21 АПРЕЛЯ
В течение 21 апреля Центральная группа наших войск продолжала вести наступательные бои западнее реки ОДЕР и реки НЕЙСЕ.
В результате этих боёв наши войска на ДРЕЗДЕНСКОМ направлении заняли города КАЛАУ, ЛЮККАУ, НОЙ-ВЕЛЬЦОВ, ЗЕНФТЕНБЕРГ, ЛАУТАВЕРК, КАМЕНЦ, БАУЦЕН и вели бой за КЕНИГСБРЮК.""",
      en="""OPERATIONAL SUMMARY FOR 21 APRIL
In the course of 21 April the Central Group of our forces continued offensive fighting west of the river ODER and the river NEISSE.
As a result of these battles our forces on the DRESDEN axis occupied the towns of CALAU, LUCKAU, NEU-WELZOW, SENFTENBERG, LAUTAWERK, KAMENZ, BAUTZEN and were fighting for KÖNIGSBRÜCK.""",
      de="""OPERATIVE MELDUNG FÜR DEN 21. APRIL
Im Laufe des 21. April führte die Zentrale Gruppe unserer Truppen weiter Angriffskämpfe westlich der Flüsse ODER und NEISSE.
Im Ergebnis dieser Kämpfe besetzten unsere Truppen in Richtung DRESDEN die Städte CALAU, LUCKAU, NEU-WELZOW, SENFTENBERG, LAUTAWERK, KAMENZ, BAUTZEN und kämpften um KÖNIGSBRÜCK.""",
      lang="ru",
      note="Die kurze Meldung, die der Rundfunk am Abend verlas und die Zeitungen am nächsten Morgen druckten. Bautzen steht als letzter genommener Name vor Königsbrück. Am selben 21. April begann der deutsche Gegenangriff (Gegenangriff [1]); die Meldung kennt ihn nicht.",
      note_en="The short summary the radio read out in the evening and the newspapers printed the next morning. Bautzen stands as the last name taken before Königsbrück. On the same 21 April the German counterattack began (Counterattack [1]); the summary does not know of it."),
    u(2, "Совинформбюро, Bd. 8, S. 180", "Der Bericht dazu: „полностью овладели городом Бауцен“", "The account with it: “took the town of Bautzen entirely”",
      """[…] Советские и польские части окружили город Каменц и ворвались на его улицы. Вражеский гарнизон оказывал упорное сопротивление, но был разгромлен. Ожесточённые бои произошли и в районе города Бауцен. Сосредоточив здесь много танков и пехоты, немцы предприняли ряд контратак. Наши подвижные подразделения и пехота измотали противника, а затем нанесли ему мощный удар. Бои переместились на улицы города. Сегодня советские бойцы подавили сопротивление немецкого гарнизона и полностью овладели городом Бауцен — узлом четырёх железных и многих шоссейных дорог.
К исходу дня наши войска вели бои за город Кенигсбрюк, находящийся в 24 километрах от Дрездена.""",
      en="""[…] Soviet and Polish units surrounded the town of Kamenz and broke into its streets. The enemy garrison offered stubborn resistance but was routed. Fierce fighting also took place in the area of the town of Bautzen. Having concentrated many tanks and infantry here, the Germans undertook a series of counterattacks. Our mobile units and infantry wore the enemy down and then dealt him a powerful blow. The fighting moved into the streets of the town. Today Soviet soldiers crushed the resistance of the German garrison and took entire possession of the town of Bautzen, a junction of four railways and many highways.
By the end of the day our forces were fighting for the town of Königsbrück, which lies 24 kilometres from Dresden.""",
      de="""[…] Sowjetische und polnische Truppenteile schlossen die Stadt Kamenz ein und drangen in ihre Straßen ein. Die feindliche Besatzung leistete hartnäckigen Widerstand, wurde aber zerschlagen. Erbitterte Kämpfe fanden auch im Raum der Stadt Bautzen statt. Nachdem die Deutschen hier viele Panzer und Infanterie zusammengezogen hatten, unternahmen sie eine Reihe von Gegenangriffen. Unsere beweglichen Einheiten und die Infanterie zermürbten den Gegner und versetzten ihm dann einen mächtigen Schlag. Die Kämpfe verlagerten sich in die Straßen der Stadt. Heute haben sowjetische Kämpfer den Widerstand der deutschen Besatzung niedergeschlagen und die Stadt Bautzen vollständig genommen, einen Knotenpunkt von vier Eisenbahnen und vielen Landstraßen.
Gegen Ende des Tages kämpften unsere Truppen um die Stadt Königsbrück, die 24 Kilometer von Dresden entfernt liegt.""",
      lang="ru",
      note="„Полностью“, vollständig: Nach der neueren Literatur hielt sich in Bautzen eine deutsche Besatzung in der Ortenburg, bis der Gegenangriff sie erreichte; das ist hier nicht am Original geprüft. Die deutschen Gegenangriffe, von denen der Bericht spricht, gab es: Sie sind der Beginn der Offensive, die dieser Apparat behandelt. Die polnischen Truppen erscheinen hier einmal, bei Kamenz; in den sowjetischen Meldungen der folgenden Tage nicht mehr. Am 22. April wurden in Niederkaina, heute ein Stadtteil von Bautzen, nach der neueren Literatur rund zweihundert gefangene Volkssturmmänner von Rotarmisten in einer Scheune verbrannt (Modul „Horka, Niederkaina, das Außenlager“, in Vorbereitung).",
      note_en="'Полностью', entirely: according to recent literature a German garrison held out in Bautzen in the Ortenburg castle until the counterattack reached it; that has not been checked against an original here. The German counterattacks the account speaks of were real: they are the beginning of the offensive this apparatus deals with. The Polish troops appear here once, at Kamenz; in the Soviet reports of the following days no more. On 22 April at Niederkaina, today part of Bautzen, around two hundred captured Volkssturm men were, according to recent literature, burned in a barn by Red Army soldiers (module 'Horka, Niederkaina, the subcamp', in preparation)."),
]

OKW = [
    u(3, "Marburger Zeitung, 27.4.1945, S. 1", "Bericht vom 26. April: „Die tapfere Besatzung von Bautzen wurde freigekämpft“", "Report of 26 April: “The brave garrison of Bautzen was fought free”",
      """Führerhauptquartier, 26. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Bei dem für die Zukunft des Reiches und für das Leben Europas entscheidenden Kampf um Berlin wurden gestern von beiden Seiten Reserven in die Schlacht geworfen. Im Südteil der Reichshauptstadt toben schwere Straßenkämpfe in Zehlendorf, Steglitz und am Südrand des Tempelhofer Feldes. Im Osten und Norden leisten unsere Truppen, tapfer unterstützt von Einheiten der Hitler-Jugend, der Partei und des Volkssturms, am Schlesischen und Görlitzer Bahnhof sowie zwischen Tegel und Siemensstadt erbitterten Widerstand. […]
Angriffe gegen die Westfront von Breslau brachen bis auf geringe örtliche Einbrüche zusammen. Die tapfere Besatzung von Bautzen wurde freigekämpft. […]""",
      en="""Führer headquarters, 26 April
The High Command of the Wehrmacht announces: […] In the battle for Berlin, decisive for the future of the Reich and for the life of Europe, reserves were thrown into the battle by both sides yesterday. In the southern part of the Reich capital heavy street fighting is raging in Zehlendorf, Steglitz and on the southern edge of Tempelhof field. In the east and north our troops, bravely supported by units of the Hitler Youth, the Party and the Volkssturm, are offering bitter resistance at the Silesian and Görlitz stations and between Tegel and Siemensstadt. […]
Attacks on the western front of Breslau collapsed except for minor local penetrations. The brave garrison of Bautzen was fought free. […]""",
      lang="de",
      note="Die Zeitung setzte das Wort in die Schlagzeile: „Bautzen freigekämpft“. Im Bericht selbst ist es ein Satz am Ende eines langen Absatzes, nach Breslau; vorne stehen Straßenkämpfe in Berlin, in denen Hitlerjungen eingesetzt sind. Moskau meldete am selben 26. April nur weiter abgewehrte Gegenangriffe „im Raum Bautzen“ (Gegenangriff [9]), danach nichts mehr. Wann genau die Ortenburg erreicht wurde, sagen die hier abgedruckten Quellen nicht.",
      note_en="The newspaper put the word into the headline: 'Bautzen fought free'. In the report itself it is one sentence at the end of a long paragraph, after Breslau; ahead of it stand street fights in Berlin in which Hitler Youths are deployed. On the same 26 April Moscow reported only counterattacks 'in the area of Bautzen' still being repulsed (Counterattack [9]), and nothing after that. When exactly the Ortenburg was reached, the sources printed here do not say."),
]

DANACH = [
    u(4, "Marburger Zeitung, 4.5.1945, S. 1", "3. Mai: „Das sind unsere Jungen“", "3 May: “Those are our boys”",
      """Das sind unsere Jungen
dnb, 3. Mai
Aus Bautzen wird berichtet: Als die Bolschewisten immer wieder mit überlegenen Kräften die Stadt stürmten und der Verteidigungsring immer enger wurde, waren es nicht nur Soldaten oder Volkssturmmänner, die in dem erbitterten Ringen der Übermacht trotzten, sondern auch Jungen aus dem Wehrertüchtigungslager, das in einer Kaserne der Stadt untergebracht war. Ihr Führer, ein schwerverwundeter Offizier, war ihnen nicht nur Vorgesetzter, sondern auch Kamerad. Der Stadtkommandant wußte, als die Kämpfe immer härter wurden, daß er sich auf diese Jungen verlassen konnte und daß er in ihnen eine scharfe Waffe zur Verteidigung der Stadt hatte.
So kämpften die 15- und 16jährigen an der Seite ihrer Kameraden von Wehrmacht und Volkssturm sechs Tage lang ohne Wasser und zuletzt ohne Verpflegung, sechs Nächte ohne Schlaf gegen die immer stärker anrennenden Sowjets. Sie hielten und kämpften mit einer Verbissenheit wie die Soldaten. Einer von ihnen erhielt einen Kopfschuß und Durchschüsse in beiden Oberschenkeln. Trotz dieser Verwundungen überbrachte er dem Kommandeur, auf Krücken gestützt, noch eine Meldung. Vor dem Gefechtsstand warf er die Krücken weg, richtete sich auf und knallte die Hacken zusammen. Erst bei der Kehrtwendung verließ ihn die Kraft und er brach zusammen. […]""",
      en="""Those are our boys
dnb, 3 May
It is reported from Bautzen: when the Bolsheviks stormed the town again and again with superior forces and the ring of defence grew ever tighter, it was not only soldiers or Volkssturm men who defied the superior force in the bitter struggle, but also boys from the military-training camp housed in a barracks of the town. Their leader, a severely wounded officer, was to them not only a superior but also a comrade. The town commandant knew, as the fighting grew ever harder, that he could rely on these boys and that he had in them a sharp weapon for the defence of the town.
So the 15- and 16-year-olds fought at the side of their comrades of the Wehrmacht and Volkssturm for six days without water and at the end without food, six nights without sleep, against the Soviets charging ever harder. They held and fought with a doggedness like the soldiers. One of them received a shot in the head and wounds through both thighs. In spite of these wounds he brought the commander one more report, propped on crutches. In front of the command post he threw away the crutches, drew himself up and clicked his heels. Only as he turned about did his strength leave him and he collapsed. […]""",
      lang="de",
      note="Die Meldung erschien eine Woche nach dem „Freikämpfen“ und vier Tage nach Hitlers Tod. Sie macht aus Kindern, die in die Verteidigung einer Stadt geschickt wurden, eine Heldengeschichte; der Schwerverwundete, der die Hacken zusammenschlägt, ist ihr Bild. Die Wehrertüchtigungslager der Hitlerjugend bildeten Jugendliche militärisch aus. Ob die Geschichte so geschah, lässt sich aus den hier abgedruckten Quellen nicht prüfen; dass Fünfzehn- und Sechzehnjährige in Bautzen kämpften, sagt die Meldung selbst. Wie viele von ihnen starben, sagt sie nicht.",
      note_en="The report appeared a week after the 'fighting free' and four days after Hitler's death. It turns children sent into the defence of a town into a hero story; the badly wounded boy clicking his heels is its image. The Hitler Youth's military-training camps (Wehrertüchtigungslager) gave adolescents military training. Whether the story happened like this cannot be checked from the sources printed here; that fifteen- and sixteen-year-olds fought in Bautzen the report itself says. How many of them died, it does not say."),
    u(5, "Marburger Zeitung, 7.5.1945, S. 1", "7. Mai: „Vor der Divisionsfront wurden 14600 Tote gezählt“", "7 May: “14,600 dead were counted in front of the division”",
      """Die Kampfkraft der Front
Vom Heldentum unserer Soldaten und Hitler-Jungen
[…] In der Schlacht im Großraum von Bautzen vernichtete und erbeutete die Division eines Ritterkreuzträgers in 14 Tagen 272 Panzer und Sturmgeschütze, 350 Geschütze und Pak und 402 gepanzerte Fahrzeuge aller Art. Vor der Divisionsfront wurden 14600 Tote gezählt. 1302 Gefangene wurden eingebracht. Der Ausfall von Panzern allein bedeutet für den Gegner die Vernichtung des Panzerbestandes von etwa anderthalb Panzerbrigaden. Eine deutsche Panzerarmee, die mit ihren Divisionen maßgeblich an der Schlacht im Großraum von Bautzen beteiligt war, vernichtete oder erbeutete in den letzten 15 Tagen 942 Panzer und Sturmgeschütze. […]""",
      en="""The fighting power of the front
On the heroism of our soldiers and Hitler Youths
[…] In the battle in the greater Bautzen area the division of a Knight's Cross holder destroyed and captured in 14 days 272 tanks and assault guns, 350 guns and anti-tank guns and 402 armoured vehicles of every kind. 14,600 dead were counted in front of the division. 1,302 prisoners were brought in. The loss of tanks alone means for the enemy the destruction of the tank strength of about one and a half tank brigades. A German panzer army that took a leading part with its divisions in the battle in the greater Bautzen area destroyed or captured 942 tanks and assault guns in the last 15 days. […]""",
      lang="de",
      note="Die Meldung erschien am Tag vor der Kapitulation. Die Division ist nicht genannt, nur ihr Kommandeur als „Ritterkreuzträger“. Zum Vergleich, nicht zur Prüfung: Nach der amtlichen polnischen Zählung, die die neuere Literatur wiedergibt, verlor die ganze 2. Polnische Armee in der Schlacht 4.902 Tote; die sowjetischen Verluste sind nicht bekannt. 14.600 Tote „vor der Divisionsfront“ einer einzigen Division sind auch dann kaum möglich, wenn man die sowjetischen Toten hinzunimmt. Auf derselben Seite stand die Meldung, Goebbels und Keitel seien in der Reichskanzlei „gefallen“ (Bunker [8]).",
      note_en="The report appeared on the day before the capitulation. The division is not named, only its commander as a 'Knight's Cross holder'. For comparison, not for checking: according to the official Polish count reproduced in recent literature, the whole Polish Second Army lost 4,902 dead in the battle; the Soviet losses are not known. 14,600 dead 'in front of' a single division are hardly possible even if the Soviet dead are added. On the same page stood the report that Goebbels and Keitel had 'fallen' in the Reich Chancellery (Bunker [8])."),
]

DATA = {
    "titel": "Zwei Meldungen, eine Stadt",
    "titel_en": "Two reports, one town",
    "autor": "Sowjetisches Informationsbüro, Oberkommando der Wehrmacht, Deutsches Nachrichtenbüro (1945)",
    "autor_en": "Soviet Information Bureau, High Command of the Wehrmacht, German News Bureau (1945)",
    "jahr": "21. April – 7. Mai 1945",
    "jahr_en": "21 April – 7 May 1945",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 180 (booksite.ru); Wehrmachtbericht vom 26.4.1945, dnb-Meldung vom 3.5.1945 und „Die Kampfkraft der Front“ in der Marburger Zeitung Nr. 117, 124 und 127 (27.4., 4.5., 7.5.1945), S. 1 (dLib.si, URN:NBN:SI:DOC-YYEMNBC2, -J0J8RBGY, -NAZDZ66I).",
    "hinweis": "Zwei Siegesmeldungen über dieselbe Stadt, fünf Tage auseinander: Moskau meldete am 21. April, Bautzen sei vollständig genommen, das OKW am 26. April, die Besatzung von Bautzen sei freigekämpft. Keine der beiden Meldungen erwähnt die andere; die 2. Polnische Armee, gegen die der Gegenangriff sich richtete, erscheint nur einmal, als „polnische Truppenteile“ vor Kamenz im sowjetischen Bericht. Danach folgen die beiden Geschichten, die die deutsche Presse in der letzten Kriegswoche aus Bautzen machte: die Kinder im Wehrertüchtigungslager und die vierzehntausendsechshundert Toten vor einer Division. Texte nach den Seitenbildern; Auslassungen […]. Die Meldungen sind Propaganda; die Anmerkungen ordnen sie ein. Zahlen von Toten werden nicht übernommen.",
    "hinweis_en": "Two victory reports about the same town, five days apart: on 21 April Moscow reported that Bautzen had been taken entirely, on 26 April the OKW that the garrison of Bautzen had been fought free. Neither report mentions the other; the Polish Second Army, against which the counterattack was directed, appears only once, as 'Polish units' before Kamenz in the Soviet account. They are followed by the two stories the German press made out of Bautzen in the last week of the war: the children of the military-training camp and the fourteen thousand six hundred dead in front of one division. Texts from the page images; omissions […]. The reports are propaganda; the notes place them in context. Figures of dead are not adopted.",
    "sections": [
        {"id": "moskau", "titel": "Moskau, 21. April", "titel_en": "Moscow, 21 April", "zk": "Meldungen",
         "blurb": "Die Meldung und der Bericht: Kamenz und Bautzen genommen, die deutschen Gegenangriffe abgewehrt, „полностью“, vollständig.",
         "blurb_en": "The summary and the account: Kamenz and Bautzen taken, the German counterattacks beaten off, 'полностью', entirely.",
         "units": MOSKAU},
        {"id": "okw", "titel": "Das OKW, 26. April", "titel_en": "The OKW, 26 April", "zk": "Meldungen",
         "blurb": "Ein Satz am Ende eines Absatzes, eine Schlagzeile: „Bautzen freigekämpft“, am Tag, an dem in Steglitz gekämpft wurde.",
         "blurb_en": "One sentence at the end of a paragraph, one headline: 'Bautzen fought free', on the day there was fighting in Steglitz.",
         "units": OKW},
        {"id": "danach", "titel": "Was danach aus Bautzen wurde", "titel_en": "What Bautzen became afterwards", "zk": "Meldungen",
         "blurb": "Zwei Geschichten der letzten Kriegswoche: die Fünfzehn- und Sechzehnjährigen, und 14.600 Tote vor einer Division.",
         "blurb_en": "Two stories of the last week of the war: the fifteen- and sixteen-year-olds, and 14,600 dead in front of one division.",
         "units": DANACH},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
