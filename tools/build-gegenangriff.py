"""Modul 3 „Der Gegenangriff, 21. April – 1. Mai“: der Verlauf in den Meldungen beider Seiten, Tag für Tag, und das
Urteil der Akten.

Quellen, an den Seitenbildern gelesen:
- Wehrmachtberichte vom 21., 22., 23., 24., 25., 28., 29. April und 1. Mai 1945 in der Marburger Zeitung Nr. 113 (23.4.),
  S. 1–2; Nr. 114 (24.4.), Nr. 115 (25.4.), Nr. 116 (26.4.), S. 1; Nr. 120 (30.4.), S. 2; Nr. 121 (1.5.), S. 2;
  Nr. 122 (2.5.), S. 1 (dLib.si). Der Bericht vom 26. April steht im Modul „Zwei Meldungen, eine Stadt“; die Berichte
  vom 27. und 30. April fehlen, weil an den Folgetagen keine Ausgabe erschien.
- Сообщения Советского Информбюро, Bd. 8 (Moskau 1945), S. 181, 183, 186–188 (Оперативные сводки за 22, 23, 25 и 26 апреля).
  Die Meldung für den 21. April steht im Modul „Zwei Meldungen, eine Stadt“.
- Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 477 und 485.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "gegenangriff.json"


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


ANGRIFF = [
    u(1, "Ziemke S. 477", "21. April: „a glimmer of good news“", "21 April: “a glimmer of good news”",
      """The 21st, although the First Russian artillery shells fell in Berlin that day, brought a glimmer of good news; Fourth Panzer Army made some local progress in a counterattack northwest of Goerlitz.""",
      de="""Der 21., obwohl an diesem Tag die ersten russischen Artilleriegranaten in Berlin einschlugen, brachte einen Schimmer guter Nachricht; die 4. Panzerarmee kam in einem Gegenangriff nordwestlich von Görlitz örtlich voran.""",
      lang="en",
      note="Mit diesem Satz beginnt bei Ziemke der Gegenangriff bei Bautzen. Was Hitler aus dem „Schimmer“ machte, folgt im selben Absatz (Modul „Der Bunker“, in Vorbereitung). „First“ ist im Druck groß geschrieben. Angegriffen wurde die Flanke der 2. Polnischen und der 52. sowjetischen Armee (Lage [1]).",
      note_en="With this sentence Ziemke's account of the counterattack at Bautzen begins. What Hitler made of the 'glimmer' follows in the same paragraph (module 'The bunker', in preparation). 'First' is capitalised in the print. The attack struck the flank of the Polish Second and the Soviet 52nd Army (Situation [1])."),
    u(2, "Marburger Zeitung, 23.4.1945, S. 2", "Bericht vom 21. April: „Gegenangriffe gewannen an einzelnen Stellen Boden“", "Report of 21 April: “counterattacks gained ground at individual points”",
      """Führerhauptquartier, 21. April
Das Oberkommando der Wehrmacht gibt bekannt: »In der großen Schlacht zwischen den Sudeten und dem Stettiner Haff wehren sich unsere Truppen mit verbissener Entschlossenheit gegen den massierten Ansturm der Bolschewisten. Auf engem Raum zusammengefaßte Panzerarmeen des Feindes haben die Front an mehreren Stellen aufgerissen. An stehengebliebenen Frontteilen und in der Tiefe des Schlachtfeldes leisten eigene Kampfgruppen hartnäckigen Widerstand und fesseln starke Kräfte der Sowjets. Nordwestlich Görlitz stehen unsere Panzer in der Abwehr heftiger Angriffe. Gegenangriffe gewannen an einzelnen Stellen Boden. Aus der Einbruchslücke südlich Spremberg trieb der Feind seine Panzerspitzen bis in den Raum Kamenz vor. Die tapferen Besatzungen von Bautzen und Spremberg zerschlugen alle Angriffe. […]""",
      en="""Führer headquarters, 21 April
The High Command of the Wehrmacht announces: 'In the great battle between the Sudeten mountains and the Stettin Lagoon our troops are defending themselves with dogged determination against the massed onslaught of the Bolsheviks. Enemy tank armies concentrated in a narrow space have torn the front open at several points. In parts of the front that have held and in the depth of the battlefield our own battle groups are offering stubborn resistance and tying down strong Soviet forces. North-west of Görlitz our tanks are fighting off heavy attacks. Counterattacks gained ground at individual points. From the gap south of Spremberg the enemy drove his armoured spearheads into the area of Kamenz. The brave garrisons of Bautzen and Spremberg smashed all attacks. […]""",
      lang="de",
      note="Die Ausgabe vom 23. April, einem Montag, druckte die Berichte vom 21. und vom 22. April. Am 21. April meldete Moskau Kamenz und Bautzen als genommen (Modul „Zwei Meldungen, eine Stadt“). „Die Besatzungen … zerschlugen alle Angriffe“: In Bautzen hielt sich nach der Literatur nur die Besatzung der Ortenburg, während die Stadt umkämpft war.",
      note_en="The issue of 23 April, a Monday, printed the reports of 21 and 22 April. On 21 April Moscow reported Kamenz and Bautzen as taken (module 'Two reports, one town'). 'The garrisons … smashed all attacks': according to the literature, in Bautzen only the garrison of the Ortenburg castle held out while the town was fought over."),
    u(3, "Marburger Zeitung, 23.4.1945, S. 1", "Bericht vom 22. April: „die Frontlücke … geschlossen“", "Report of 22 April: “the gap in the front … closed”",
      """Führerhauptquartier, 22. April
Das Oberkommando der Wehrmacht gibt bekannt: […] In der Doppelschlacht zwischen den Sudeten und dem Stettiner Haff stehen unsere Truppen weiter in schwerem Kampf. Nordwestlich Görlitz wurde die Frontlücke durch erfolgreiche Gegenangriffe geschlossen. Die Besatzung von Bautzen verteidigte sich hartnäckig gegen den mit starken Kräften angreifenden Feind. Nach Westen vorstoßend, drangen die Sowjets in Bischofswerda und Königsbrück ein. […]""",
      en="""Führer headquarters, 22 April
The High Command of the Wehrmacht announces: […] In the double battle between the Sudeten mountains and the Stettin Lagoon our troops remain in heavy fighting. North-west of Görlitz the gap in the front was closed by successful counterattacks. The garrison of Bautzen defended itself stubbornly against the enemy attacking with strong forces. Pushing westward, the Soviets penetrated into Bischofswerda and Königsbrück. […]""",
      lang="de",
      note="Hier stimmen die beiden Seiten einmal überein: Bischofswerda meldete auch Moskau für den 22. April (Gegenangriff [4]). Die „geschlossene Frontlücke“ ist der Schimmer, aus dem Hitler am 21. eine Weisung machte (Gegenangriff [1]).",
      note_en="Here, for once, the two sides agree: Moscow also reported Bischofswerda for 22 April (Counterattack [4]). The 'closed gap in the front' is the glimmer from which Hitler made an order on the 21st (Counterattack [1])."),
    u(4, "Совинформбюро, Bd. 8, S. 181", "Meldung für den 22. April: Bischofswerda, „mehr als 10.000“", "Report for 22 April: Bischofswerda, “more than 10,000”",
      """ОПЕРАТИВНАЯ СВОДКА ЗА 22 АПРЕЛЯ
В течение 22 апреля Центральная группа наших войск продолжала вести наступательные бои на ДРЕЗДЕНСКОМ и БЕРЛИНСКОМ направлениях.
На ДРЕЗДЕНСКОМ направлении наши войска заняли города ЛЮБЕНАУ, ДАМЕ, ШЛИБЕН, ЗОННЕВАЛЬДЕ, ФИНСТЕРВАЛЬДЕ, РУЛАНД, ЕЛЬСТЕРВЕРДА, ШВЕПНИТЦ, БУРКАУ, БИШОФСВЕРДА. По предварительным данным, с 17 по 21 апреля на этом направлении наши войска взяли в плен более 10.000 немецких солдат и офицеров и захватили 96 самолётов и свыше 150 танков и самоходных орудий противника.""",
      en="""OPERATIONAL SUMMARY FOR 22 APRIL
In the course of 22 April the Central Group of our forces continued offensive fighting on the DRESDEN and BERLIN axes.
On the DRESDEN axis our forces occupied the towns of LÜBBENAU, DAHME, SCHLIEBEN, SONNEWALDE, FINSTERWALDE, RULAND, ELSTERWERDA, SCHWEPNITZ, BURKAU, BISCHOFSWERDA. According to preliminary figures, from 17 to 21 April our forces on this axis took more than 10,000 German soldiers and officers prisoner and captured 96 aircraft and more than 150 tanks and self-propelled guns of the enemy.""",
      de="""OPERATIVE MELDUNG FÜR DEN 22. APRIL
Im Laufe des 22. April setzte die Zentrale Gruppe unserer Truppen die Angriffskämpfe in Richtung DRESDEN und BERLIN fort.
In Richtung DRESDEN besetzten unsere Truppen die Städte LÜBBENAU, DAHME, SCHLIEBEN, SONNEWALDE, FINSTERWALDE, RULAND, ELSTERWERDA, SCHWEPNITZ, BURKAU, BISCHOFSWERDA. Nach vorläufigen Angaben haben unsere Truppen in dieser Richtung vom 17. bis 21. April mehr als 10.000 deutsche Soldaten und Offiziere gefangen genommen und 96 Flugzeuge und über 150 Panzer und Selbstfahrlafetten des Gegners erbeutet.""",
      lang="ru",
      note="Burkau und Bischofswerda liegen westlich von Bautzen, an der Straße nach Dresden: die Spitzen, die nach dem OKW-Bericht vom 24. April zurückgenommen werden mussten (Gegenangriff [7]). Vom deutschen Gegenangriff, der am Vortag begonnen hatte, sagt die Meldung nichts.",
      note_en="Burkau and Bischofswerda lie west of Bautzen on the road to Dresden: the spearheads which, according to the OKW report of 24 April, had to be pulled back (Counterattack [7]). Of the German counterattack that had begun the day before, the report says nothing."),
]

KAMENZ = [
    u(5, "Marburger Zeitung, 24.4.1945, S. 1", "Bericht vom 23. April: „abgeschnitten“", "Report of 23 April: “cut off”",
      """Führerhauptquartier, 23. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Zwischen den Sudeten und dem Stettiner Haff wird schwer gekämpft. Starke feindliche Kräfte wurden durch schwungvoll geführte Gegenangriffe nordwestlich Görlitz von ihren rückwärtigen Verbindungen abgeschnitten und dadurch am weiteren Vordringen nach Westen verhindert. Die tapfere Besatzung von Bautzen hielt auch gestern zahlreichen bolschewistischen Angriffen stand. Auch bei Spremberg leisteten unsere Truppen dem Ansturm sowjetischer Kräfte Widerstand. Dagegen ging Kottbus nach zäher Verteidigung verloren. […]""",
      en="""Führer headquarters, 23 April
The High Command of the Wehrmacht announces: […] Heavy fighting is going on between the Sudeten mountains and the Stettin Lagoon. Strong enemy forces were cut off from their rear communications by vigorously led counterattacks north-west of Görlitz and thereby prevented from advancing further west. The brave garrison of Bautzen again withstood numerous Bolshevik attacks yesterday. At Spremberg too our troops resisted the onslaught of Soviet forces. Cottbus, however, was lost after a tenacious defence. […]""",
      lang="de",
      note="Die „abgeschnittenen“ Kräfte waren nach der Literatur Teile der 2. Polnischen Armee und das sowjetische 7. mechanisierte Korps, deren Spitzen bis vor Dresden standen. Dass es polnische Soldaten waren, sagt der Bericht so wenig wie die sowjetische Meldung.",
      note_en="According to the literature the 'cut off' forces were parts of the Polish Second Army and the Soviet 7th Mechanised Corps, whose spearheads stood before Dresden. That they were Polish soldiers the report says no more than the Soviet one."),
    u(6, "Совинформбюро, Bd. 8, S. 183", "Meldung für den 23. April: Pulsnitz", "Report for 23 April: Pulsnitz",
      """[…] Одновременно на ДРЕЗДЕНСКОМ направлении войска фронта с боями заняли города ЭССЕН, КИРХХАЙН, ФАЛЬКЕНБЕРГ, МЮЛЬБЕРГ, ПУЛЬСНИТЦ и вышли на реку ЭЛЬБА северо-западнее ДРЕЗДЕНА.""",
      en="""[…] At the same time on the DRESDEN axis the troops of the front took with fighting the towns of ESSEN, KIRCHHAIN, FALKENBERG, MÜHLBERG, PULSNITZ and reached the river ELBE north-west of DRESDEN.""",
      de="""[…] Gleichzeitig nahmen die Truppen der Front in Richtung DRESDEN kämpfend die Städte ESSEN, KIRCHHAIN, FALKENBERG, MÜHLBERG, PULSNITZ und erreichten nordwestlich DRESDEN die ELBE.""",
      lang="ru",
      note="Die Meldung für den 23. April nennt erstmals die 1. Ukrainische Front beim Namen; die Ortsnamen sind wie gedruckt wiedergegeben. Pulsnitz liegt zwischen Kamenz und Dresden. Am nächsten Tag meldete das OKW: „Pulsnitz und Kamenz sind wieder in deutscher Hand“ (Gegenangriff [7]).",
      note_en="The report for 23 April names the First Ukrainian Front for the first time; the place names are given as printed. Pulsnitz lies between Kamenz and Dresden. The next day the OKW reported: 'Pulsnitz and Kamenz are again in German hands' (Counterattack [7])."),
    u(7, "Marburger Zeitung, 25.4.1945, S. 1", "Bericht vom 24. April: „Pulsnitz und Kamenz sind wieder in deutscher Hand“", "Report of 24 April: “Pulsnitz and Kamenz are again in German hands”",
      """Führerhauptquartier, 24. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Im Südabschnitt der großen Schlacht zwischen den Sudeten und der Pommerschen Bucht drangen unsere Truppen in schwungvollen Gegenangriffen bis in den Raum hart östlich Görlitz vor. Die Stadt verteidigt sich zäh weiter gegen zahlreiche Angriffe. Durch die Unterbrechung seiner rückwärtigen Verbindungen nordwestlich Bautzen wurde der Gegner gezwungen, seine auf Dresden vorgestoßenen Angriffsspitzen zurückzunehmen. Pulsnitz und Kamenz sind wieder in deutscher Hand. […]""",
      en="""Führer headquarters, 24 April
The High Command of the Wehrmacht announces: […] In the southern sector of the great battle between the Sudeten mountains and the Pomeranian Bay our troops in vigorous counterattacks advanced into the area just east of Görlitz. The town continues to defend itself tenaciously against numerous attacks. Through the cutting of his rear communications north-west of Bautzen the enemy was forced to pull back his spearheads that had pushed forward towards Dresden. Pulsnitz and Kamenz are again in German hands. […]""",
      lang="de",
      note="Die Zeitung setzte darüber: „Schwungvoller Gegenangriff drang bis Görlitz vor — Pulsnitz und Kamenz wieder in deutscher Hand“. Welche „Stadt“ sich „zäh weiter“ verteidigt, sagt der Satz nicht; nach dem Zusammenhang Bautzen. Moskau hatte Kamenz am 21. April als genommen gemeldet und meldete die Stadt danach nicht mehr (Modul „Zwei Meldungen, eine Stadt“).",
      note_en="The newspaper's headline: 'Vigorous counterattack pushed through to Görlitz — Pulsnitz and Kamenz again in German hands'. Which 'town' continues to defend itself the sentence does not say; from the context, Bautzen. Moscow had reported Kamenz as taken on 21 April and did not report the town again (module 'Two reports, one town')."),
    u(8, "Marburger Zeitung, 26.4.1945, S. 1", "Bericht vom 25. April: „Weißenburg wurde wieder vom Feinde befreit“", "Report of 25 April: “Weißenburg was freed from the enemy again”",
      """Führerhauptquartier, 25. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Unsere Gegenangriffe machten im Raum Görlitz—Bautzen—Kamenz weiter gute Fortschritte. Weißenburg wurde wieder vom Feinde befreit. Die Bolschewisten hatten in diesen Kämpfen sehr hohe blutige Verluste. Umfangreiche Beute wurde gemacht. […]""",
      en="""Führer headquarters, 25 April
The High Command of the Wehrmacht announces: […] Our counterattacks in the area Görlitz–Bautzen–Kamenz continued to make good progress. Weißenburg was freed from the enemy again. The Bolsheviks suffered very heavy bloody losses in this fighting. Extensive booty was taken. […]""",
      lang="de",
      note="„Weißenburg“ ist ein Druck- oder Übermittlungsfehler für Weißenberg (sorbisch Wóspork) zwischen Bautzen und Görlitz. Dort war nach der Literatur die sowjetische 294. Schützendivision eingeschlossen, die am 24. April unter schweren Verlusten ausbrach. Die „sehr hohen blutigen Verluste“ waren auch polnische und sowjetische Verwundete und Gefangene; was mit ihnen geschah, steht im Modul „Horka, Niederkaina, das Außenlager“ (in Vorbereitung).",
      note_en="'Weißenburg' is a printing or transmission error for Weißenberg (Sorbian Wóspork) between Bautzen and Görlitz. According to the literature the Soviet 294th Rifle Division was encircled there and broke out with heavy losses on 24 April. The 'very heavy bloody losses' also meant Polish and Soviet wounded and prisoners; what happened to them is the subject of the module 'Horka, Niederkaina, the subcamp' (in preparation)."),
    u(9, "Совинформбюро, Bd. 8, S. 186–188", "Meldungen für den 25. und 26. April: „bis zu 40 deutsche Panzer“", "Reports for 25 and 26 April: “up to 40 German tanks”",
      """ОПЕРАТИВНАЯ СВОДКА ЗА 25 АПРЕЛЯ
[…] В районе БАУЦЕН наши войска отбивали контратаки крупных сил пехоты и танков противника и нанесли ему большой урон. […]
* * *
[…] В районе города Бауцен крупные силы пехоты и танков противника контратаковали наши войска. Завязались ожесточённые бои. Отражая вражеские контратаки, советские артиллеристы сожгли и подбили до 40 немецких танков и самоходных орудий. На подступах к нашим позициям осталось много вражеских трупов.
ОПЕРАТИВНАЯ СВОДКА ЗА 26 АПРЕЛЯ
[…] В районе БАУЦЕНА войска фронта продолжали отбивать контратаки крупных сил пехоты и танков противника. […]""",
      en="""OPERATIONAL SUMMARY FOR 25 APRIL
[…] In the area of BAUTZEN our forces repulsed counterattacks by large enemy forces of infantry and tanks and inflicted heavy damage on him. […]
* * *
[…] In the area of the town of Bautzen large enemy forces of infantry and tanks counterattacked our troops. Fierce fighting broke out. Repulsing the enemy counterattacks, Soviet gunners burned and knocked out up to 40 German tanks and self-propelled guns. Many enemy corpses remained on the approaches to our positions.
OPERATIONAL SUMMARY FOR 26 APRIL
[…] In the area of BAUTZEN the troops of the front continued to repulse counterattacks by large enemy forces of infantry and tanks. […]""",
      de="""OPERATIVE MELDUNG FÜR DEN 25. APRIL
[…] Im Raum BAUTZEN wehrten unsere Truppen Gegenangriffe großer Kräfte feindlicher Infanterie und Panzer ab und fügten ihm großen Schaden zu. […]
* * *
[…] Im Raum der Stadt Bautzen griffen große Kräfte feindlicher Infanterie und Panzer unsere Truppen an. Es entbrannten erbitterte Kämpfe. Beim Abwehren der feindlichen Gegenangriffe verbrannten und beschossen sowjetische Artilleristen bis zu 40 deutsche Panzer und Selbstfahrlafetten. Vor unseren Stellungen blieben viele feindliche Leichen liegen.
OPERATIVE MELDUNG FÜR DEN 26. APRIL
[…] Im Raum BAUTZEN wehrten die Truppen der Front weiter Gegenangriffe großer Kräfte feindlicher Infanterie und Panzer ab. […]""",
      lang="ru",
      note="Die einzigen sowjetischen Meldungen, die den Gegenangriff nennen, und sie nennen ihn als abgewehrt. Nach dem 26. April kommt der Raum Bautzen in den Meldungen bis zur Kapitulation nicht mehr vor (Durchsicht des Textes von Band 8); gemeldet werden Berlin, Pommern, die Elbe, Torgau. Am selben 25. April meldete das OKW „gute Fortschritte“ (Gegenangriff [8]).",
      note_en="The only Soviet reports that name the counterattack, and they name it as repulsed. After 26 April the Bautzen area does not appear in the reports again until the capitulation (search of the text of vol. 8); they report Berlin, Pomerania, the Elbe, Torgau. On the same 25 April the OKW reported 'good progress' (Counterattack [8])."),
]

NORDEN = [
    u(10, "Ziemke S. 485", "26. April: „close to a standstill“", "26 April: “close to a standstill”",
      """Off Ninth Army's south flank, Schoerner's attack, having made about fifteen miles in six days, was close to a standstill with forty miles yet to go.""",
      de="""Vor der Südflanke der 9. Armee war Schörners Angriff, nachdem er in sechs Tagen etwa fünfzehn Meilen gewonnen hatte, nahe am Stillstand, mit vierzig Meilen noch vor sich.""",
      lang="en",
      note="Fünfzehn Meilen sind etwa 24 Kilometer, vierzig Meilen etwa 64. Ziel war die Verbindung mit der 9. Armee, die südöstlich Berlins im Kessel von Halbe stand. Ziemke stützt sich auf die Telefonnotizen der Heeresgruppe Weichsel vom 26. April (Akte H. Gr. Weichsel 75122/7).",
      note_en="Fifteen miles are about 24 kilometres, forty miles about 64. The aim was to link up with the Ninth Army, encircled south-east of Berlin in the Halbe pocket. Ziemke relies on Army Group Vistula's notes of telephone conversations of 26 April (file H. Gr. Weichsel 75122/7)."),
    u(11, "Marburger Zeitung, 30.4.1945, S. 2", "Bericht vom 28. April: „zum Angriff nach Norden angetreten“", "Report of 28 April: “gone over to the attack northward”",
      """Führerhauptquartier, 28. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Nordwestlich Bautzen, wo bei Meißen die Verbindung mit der Westfront an der Elbe hergestellt wurde, sind unsere Truppen zum Angriff nach Norden angetreten. […]""",
      en="""Führer headquarters, 28 April
The High Command of the Wehrmacht announces: […] North-west of Bautzen, where the link with the western front on the Elbe was established near Meissen, our troops have gone over to the attack northward. […]""",
      lang="de",
      note="Zwei Tage nach Ziemkes „Stillstand“ meldet das OKW einen neuen Angriff „nach Norden“: das ist die Richtung, die Keitel Schörner am 27. April befohlen hatte (Modul „Der Bunker“, in Vorbereitung). Die „Westfront an der Elbe“ ist die deutsche Front gegen die Amerikaner; am 25. April hatten sich Amerikaner und Sowjets bei Torgau getroffen.",
      note_en="Two days after Ziemke's 'standstill' the OKW reports a new attack 'northward': the direction Keitel had ordered Schörner on 27 April (module 'The bunker', in preparation). The 'western front on the Elbe' is the German front against the Americans; on 25 April Americans and Soviets had met at Torgau."),
    u(12, "Marburger Zeitung, 1.5.1945, S. 2", "Bericht vom 29. April: „Kamenz und Königsbrück wurden wiedergenommen“", "Report of 29 April: “Kamenz and Königsbrück were retaken”",
      """Führerhauptquartier, 29. April
Das Oberkommando der Wehrmacht gibt bekannt: […] Im Kampfraum Bautzen—Meißen drang unser Angriff weiter nach Norden vor. Kamenz und Königsbrück wurden wiedergenommen, die Sowjets unter hohen Verlusten zurückgeworfen. […]""",
      en="""Führer headquarters, 29 April
The High Command of the Wehrmacht announces: […] In the battle area Bautzen–Meissen our attack advanced further northward. Kamenz and Königsbrück were retaken, the Soviets thrown back with heavy losses. […]""",
      lang="de",
      note="Zum zweiten Mal „wieder“ Kamenz: Am 24. April hatte das OKW die Stadt schon als „wieder in deutscher Hand“ gemeldet (Gegenangriff [7]), und kein Bericht dazwischen nennt sie verloren. Aus den hier abgedruckten Quellen lässt sich nicht entscheiden, ob Kamenz zwischen dem 24. und dem 29. April noch einmal den Besitzer wechselte oder ob dieselbe Rückeroberung zweimal gemeldet wurde; Moskau meldete Kamenz nach dem 21. April nicht mehr, Ziemke nennt die Stadt nicht. Neuere Darstellungen sehen die polnisch-sowjetische Linie Ende April bei Kamenz; das ist hier nicht am Original geprüft. Die Zeitung setzte darüber: „Deutscher Angriff auch aus dem Raum Bautzen—Meißen gegen Norden“.",
      note_en="Kamenz 'again' for the second time: on 24 April the OKW had already reported the town 'again in German hands' (Counterattack [7]), and no report in between calls it lost. From the sources printed here it cannot be decided whether Kamenz changed hands once more between 24 and 29 April or whether the same recapture was reported twice; Moscow did not report Kamenz after 21 April, Ziemke does not name the town. Recent accounts place the Polish-Soviet line near Kamenz at the end of April; that has not been checked against an original here. The newspaper's headline: 'German attack also from the area Bautzen–Meissen northward'."),
    u(13, "Marburger Zeitung, 2.5.1945, S. 1", "Bericht vom 1. Mai: „Säuberungskämpfe … abgeschlossen“", "Report of 1 May: “mopping-up … completed”",
      """Führerhauptquartier, 1. Mai
Das Oberkommando der Wehrmacht gibt bekannt: […] Die Säuberungskämpfe in den wieder befreiten Gebieten von Bautzen, Kamenz und Königsbrück wurden abgeschlossen. Der Feind hatte hohe blutige Verluste. Zahlreiche Gefangene und umfangreiche Beute wurden eingebracht. […]""",
      en="""Führer headquarters, 1 May
The High Command of the Wehrmacht announces: […] The mopping-up fighting in the liberated areas of Bautzen, Kamenz and Königsbrück was completed. The enemy suffered heavy bloody losses. Numerous prisoners and extensive booty were brought in. […]""",
      lang="de",
      note="„Säuberungskämpfe“ heißt: die Suche nach versprengten polnischen und sowjetischen Soldaten in Wäldern und Dörfern. Was in diesen Tagen mit Gefangenen und Verwundeten geschah, in Horka am 26. April und an anderen Orten, ist Gegenstand des Moduls „Horka, Niederkaina, das Außenlager“ (in Vorbereitung). Derselbe Bericht beginnt: „Im Stadtkern von Berlin verteidigt sich die tapfere Besatzung, um unseren Führer geschart“, und die Zeitung setzte darüber „Um unsern Führer geschart“. Hitler hatte sich am Nachmittag des 30. April das Leben genommen (Ziemke S. 492).",
      note_en="'Mopping-up fighting' means: the hunt for scattered Polish and Soviet soldiers in woods and villages. What happened to prisoners and wounded in these days, at Horka on 26 April and elsewhere, is the subject of the module 'Horka, Niederkaina, the subcamp' (in preparation). The same report begins: 'In the centre of Berlin the brave garrison is defending itself, gathered around our Führer', and the newspaper's headline was 'Gathered around our Führer'. Hitler had killed himself in the afternoon of 30 April (Ziemke p. 492)."),
]

DATA = {
    "titel": "Der Gegenangriff, 21. April – 1. Mai 1945",
    "titel_en": "The counterattack, 21 April – 1 May 1945",
    "autor": "Oberkommando der Wehrmacht, Sowjetisches Informationsbüro (1945), Earl F. Ziemke (1968)",
    "autor_en": "High Command of the Wehrmacht, Soviet Information Bureau (1945), Earl F. Ziemke (1968)",
    "jahr": "21. April – 1. Mai 1945",
    "jahr_en": "21 April – 1 May 1945",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Wehrmachtberichte vom 21.–25., 28. und 29. April und 1. Mai 1945 in der Marburger Zeitung Nr. 113–116 und 120–122 (23.4.–2.5.1945; dLib.si); Сообщения Советского Информбюро, т. 8 (Москва 1945), S. 181, 183, 186–188; Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 477, 485.",
    "hinweis": "Der Verlauf des Gegenangriffs, wie die beiden Seiten ihn Tag für Tag meldeten, und Ziemkes Urteil aus den Akten. Die beiden Siegesmeldungen über Bautzen selbst, die sowjetische vom 21. und die deutsche vom 26. April, stehen im Modul „Zwei Meldungen, eine Stadt“. Die 2. Polnische Armee, gegen die sich der Angriff vor allem richtete, kommt in keiner der Meldungen dieser Tage vor: Moskau spricht von „unseren Truppen“, das OKW von „Sowjets“ und „Bolschewisten“. Polnische Dokumente werden gesucht. Texte nach den Seitenbildern; die Wehrmachtberichte sind auf die Lausitz gekürzt ([…]). Zahlen von Panzern, Toten und Beute lassen sich aus diesen Quellen nicht prüfen und werden nicht übernommen.",
    "hinweis_en": "The course of the counterattack as the two sides reported it day by day, and Ziemke's judgement from the files. The two victory reports about Bautzen itself, the Soviet one of 21 April and the German one of 26 April, are in the module 'Two reports, one town'. The Polish Second Army, against which the attack was mainly directed, appears in none of the reports of these days: Moscow speaks of 'our forces', the OKW of 'Soviets' and 'Bolsheviks'. Polish documents are being sought. Texts from the page images; the Wehrmacht reports are cut to Lusatia ([…]). Figures of tanks, dead and booty cannot be checked from these sources and are not adopted.",
    "sections": [
        {"id": "angriff", "titel": "Der Angriff, 21. und 22. April", "titel_en": "The attack, 21 and 22 April", "zk": "Gegenangriff",
         "blurb": "Ein Schimmer guter Nachricht im Führerhauptquartier, eine geschlossene Frontlücke im Wehrmachtbericht, und in Moskau Bischofswerda und zehntausend Gefangene.",
         "blurb_en": "A glimmer of good news at Führer headquarters, a closed gap in the front in the Wehrmacht report, and in Moscow Bischofswerda and ten thousand prisoners.",
         "units": ANGRIFF},
        {"id": "kamenz", "titel": "Pulsnitz, Kamenz, Weißenberg, 23.–25. April", "titel_en": "Pulsnitz, Kamenz, Weißenberg, 23–25 April", "zk": "Gegenangriff",
         "blurb": "Moskau meldet Pulsnitz, das OKW Pulsnitz und Kamenz „wieder in deutscher Hand“; Moskau meldet am 25. und 26. April abgewehrte Gegenangriffe bei Bautzen und verstummt dann.",
         "blurb_en": "Moscow reports Pulsnitz, the OKW Pulsnitz and Kamenz 'again in German hands'; Moscow reports counterattacks at Bautzen repulsed and then falls silent.",
         "units": KAMENZ},
        {"id": "norden", "titel": "Nach Norden, 26. April – 1. Mai", "titel_en": "Northward, 26 April – 1 May", "zk": "Gegenangriff",
         "blurb": "Ziemke: nahe am Stillstand. Das OKW: ein neuer Angriff nach Norden, Kamenz zum zweiten Mal „wieder“, die „Säuberungskämpfe“.",
         "blurb_en": "Ziemke: close to a standstill. The OKW: a new attack northward, Kamenz 'again' for the second time, the 'mopping-up fighting'.",
         "units": NORDEN},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
