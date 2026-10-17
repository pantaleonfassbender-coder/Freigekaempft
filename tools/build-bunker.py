"""Modul 5 „Der Bunker: die Meldung wird zur Weisung“: wie der örtliche Gegenangriff bei Bautzen im Führerbunker zur
Grundlage von Weisungen wurde, vom 21. April bis zur Kapitulation.

Quellen, an den Seitenbildern gelesen:
- Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 477–479, 483, 486, 493–494, 498 (Internet Archive
  StalingradToBerlinTheGermanDefeatInTheEast-nsia, PDF-Seite = Seite + 12). Werk der US-Bundesregierung, gemeinfrei.
- dnb-Meldung „Goebbels und Keitel gefallen“, 6. Mai 1945, Marburger Zeitung Nr. 127 (7.5.1945), S. 1 (dLib.si).
Ziemke gibt die deutschen Akten englisch wieder; die deutschen Fassungen hier sind Rückübersetzungen, nicht der Wortlaut.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "bunker.json"


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


RUECK = ("Ziemke gibt die Worte der Akten englisch wieder; die deutsche Fassung oben ist eine Rückübersetzung, nicht der Wortlaut der Akte.",
         "Ziemke gives the words of the files in English; the German wording of the files is not available.")

WEISUNG = [
    u(1, "Ziemke S. 477", "21. April: aus der Illusion eine „Grundweisung“", "21 April: from the illusion a “basic order”",
      """The 21st, although the First Russian artillery shells fell in Berlin that day, brought a glimmer of good news; Fourth Panzer Army made some local progress in a counterattack northwest of Goerlitz. Hitler saw in it the makings of a major thrust that would close the 40-mile gap between the Army Group Vistula–Army Group Center flanks, and from that illusion he derived a "basic order" which Krebs transmitted to the army group by phone in the midafternoon. The "successful" attack at Army Group Center would soon close the front at Spremberg; therefore, it was "absolutely necessary" to hold the corner post at Cottbus. (Ninth Army had taken command the day before of Fourth Panzer Army's left flank corps at and north of Cottbus.) Ninth Army would set up a front facing west between Koenigswusterhausen and Cottbus and attack west into the flank of the Russians going toward Berlin from the south.""",
      de="""Der 21., obwohl an diesem Tag die ersten russischen Artilleriegranaten in Berlin einschlugen, brachte einen Schimmer guter Nachricht; die 4. Panzerarmee kam in einem Gegenangriff nordwestlich von Görlitz örtlich voran. Hitler sah darin die Anfänge eines großen Stoßes, der die vierzig Meilen breite Lücke zwischen den Flanken der Heeresgruppen Weichsel und Mitte schließen würde, und aus dieser Illusion leitete er eine „Grundweisung“ ab, die Krebs am Nachmittag fernmündlich an die Heeresgruppe durchgab. Der „erfolgreiche“ Angriff bei der Heeresgruppe Mitte werde bald die Front bei Spremberg schließen; darum sei es „unbedingt notwendig“, den Eckpfeiler Cottbus zu halten. (Die 9. Armee hatte am Vortag den Befehl über das linke Flügelkorps der 4. Panzerarmee bei und nördlich von Cottbus übernommen.) Die 9. Armee solle zwischen Königs Wusterhausen und Cottbus eine Front nach Westen aufbauen und nach Westen in die Flanke der Russen angreifen, die von Süden auf Berlin vorgingen.""",
      lang="en",
      note="Der Gegenangriff, aus dem die Weisung hervorging, ist der von Bautzen (Gegenangriff [1]). Vierzig Meilen sind etwa 64 Kilometer. Ziemke stützt sich auf einen Vermerk der Heeresgruppe Weichsel vom 21.4.45. Die Anführungszeichen markieren Worte der Akte; " + RUECK[0],
      note_en="The counterattack from which the order arose is the one at Bautzen (Counterattack [1]). Ziemke relies on a memorandum of Army Group Vistula of 21 April 1945. " + RUECK[1]),
    u(2, "Ziemke S. 478", "„with your head“", "“with your head”",
      """To the tactical directive Hitler added, "Officers who do not accept this order without reservation are to be arrested and shot instantly. You yourself I make responsible with your head for its execution."
As soon as he received the order Steiner called the army group headquarters to report that it could not be carried out. […]
When Krebs phoned a résumé of the Steiner order to the army group headquarters, Heinrici asked him to impress on Hitler the necessity for taking back Ninth Army, which was being encircled and even then could no longer withdraw toward Berlin but would have to go around the lake chain south of the capital. If Hitler insisted on keeping his previous orders in force, then Heinrici asked to be relieved because he could not execute them and he could not reconcile them with his conscience and his responsibility to the troops. Krebs answered that the Fuehrer took the responsibility for his own orders.""",
      de="""Der taktischen Weisung fügte Hitler hinzu: „Offiziere, die diesen Befehl nicht vorbehaltlos annehmen, sind festzunehmen und sofort zu erschießen. Sie selbst mache ich mit Ihrem Kopf für seine Ausführung verantwortlich.“
Sobald Steiner den Befehl erhalten hatte, rief er das Hauptquartier der Heeresgruppe an und meldete, er sei nicht ausführbar. […]
Als Krebs eine Zusammenfassung des Befehls an Steiner der Heeresgruppe durchtelefonierte, bat Heinrici ihn, Hitler die Notwendigkeit vorzustellen, die 9. Armee zurückzunehmen, die eingeschlossen wurde und schon jetzt nicht mehr auf Berlin ausweichen konnte, sondern um die Seenkette südlich der Hauptstadt herum musste. Wenn Hitler auf seinen bisherigen Befehlen bestehe, bitte er, Heinrici, um seine Ablösung, weil er sie nicht ausführen und nicht mit seinem Gewissen und seiner Verantwortung für die Truppe vereinbaren könne. Krebs antwortete, der Führer übernehme die Verantwortung für seine eigenen Befehle.""",
      lang="en",
      note="Der Zusatz galt dem Befehl an Steiner, nördlich von Berlin anzugreifen; er zeigt den Ton, in dem am selben 21. April die Weisungen ausgingen, die auch Bautzen betrafen. Heinrici führte die Heeresgruppe Weichsel nördlich der Lausitz. " + RUECK[0],
      note_en="The addition concerned the order to Felix Steiner to attack north of Berlin; it shows the tone in which, on the same 21 April, the orders that also concerned Bautzen went out. Heinrici commanded Army Group Vistula north of Lusatia. " + RUECK[1]),
    u(3, "Ziemke S. 479", "22. April: „Schoerner's attack east of Bautzen was succeeding“", "22 April: “Schoerner's attack east of Bautzen was succeeding”",
      """At the afternoon situation conference on the 22d Hitler broke down. When, having waited impatiently through the morning and early afternoon for a report from Steiner, he learned that Steiner had not attacked, he fell into a tearful rage, declared that the war was lost, blamed it all on the generals, and announced that he would stay in Berlin to the end and kill himself before the Russians could take him prisoner. […]
Before the conference ended, Krebs was on the phone to Heinrici telling him the Fuehrer was making the decision; Schoerner and Wenck would be briefed; Wenck would attack east; Schoerner's attack east of Bautzen was succeeding; Ninth Army would have to hold Cottbus and the Oder line to the south of Frankfurt. In short, Hitler was back at trying to build a front east of Berlin.""",
      de="""In der Lagebesprechung am Nachmittag des 22. brach Hitler zusammen. Als er, nachdem er den Morgen und den frühen Nachmittag ungeduldig auf eine Meldung von Steiner gewartet hatte, erfuhr, dass Steiner nicht angegriffen hatte, geriet er in eine tränenreiche Wut, erklärte, der Krieg sei verloren, gab den Generälen die ganze Schuld und kündigte an, er werde bis zum Ende in Berlin bleiben und sich töten, bevor die Russen ihn gefangen nehmen könnten. […]
Noch bevor die Besprechung zu Ende war, telefonierte Krebs mit Heinrici und sagte ihm, der Führer treffe die Entscheidung; Schörner und Wenck würden unterrichtet; Wenck werde nach Osten angreifen; Schörners Angriff östlich Bautzen habe Erfolg; die 9. Armee müsse Cottbus und die Oderlinie südlich Frankfurt halten. Kurz, Hitler versuchte wieder, eine Front östlich Berlins aufzubauen.""",
      lang="en",
      note="Am Mittag desselben Tages erklärte Hitler den Krieg für verloren; am Abend war Bautzen wieder ein Baustein der Front, die er aufbauen wollte. Öffentlich meldete das OKW für den 22. April: „Die Besatzung von Bautzen verteidigte sich hartnäckig“ (Gegenangriff [3]). Walther Wenck führte die neu aufgestellte 12. Armee an der Elbe. " + RUECK[0],
      note_en="At midday that day Hitler declared the war lost; by evening Bautzen was again a building block of the front he meant to build. Publicly the OKW reported for 22 April: 'The garrison of Bautzen defended itself stubbornly' (Counterattack [3]). Walther Wenck commanded the newly formed Twelfth Army on the Elbe. " + RUECK[1]),
]

WILLE = [
    u(4, "Ziemke S. 483", "25. April: „without regard for flanks and neighbors“", "25 April: “without regard for flanks and neighbors”",
      """Half an hour after midnight on the night of 25 April a directive that Hitler had written the evening before reached the OKW headquarters at Neu Roofen. It called for the "fastest execution of all relief attacks, without regard for flanks and neighbors." Although he must have known that his time was running pitifully short, Hitler still insisted on attempting nothing less than to restore a complete and solid front on the east. Twelfth Army was to attack northwest from Belzig to Ferch at the tip of the twin lakes south of Potsdam while Ninth Army attacked west to meet it. After they had joined, both armies were to advance toward Berlin from the south "on a broad front." Ninth Army, meanwhile, was also to hold its eastern front so that Army Group Center could close up from the south.""",
      de="""Eine halbe Stunde nach Mitternacht in der Nacht zum 25. April erreichte eine Weisung, die Hitler am Abend zuvor geschrieben hatte, das Hauptquartier des OKW in Neu Roofen. Sie verlangte „schnellste Durchführung aller Entsatzangriffe, ohne Rücksicht auf Flanken und Nachbarn“. Obwohl er gewusst haben muss, dass ihm erbärmlich wenig Zeit blieb, bestand Hitler noch immer darauf, nichts Geringeres zu versuchen, als eine geschlossene und feste Front im Osten wiederherzustellen. Die 12. Armee sollte von Belzig nach Nordwesten auf Ferch an der Spitze der Zwillingsseen südlich Potsdam angreifen, während die 9. Armee ihr nach Westen entgegen angriff. Nach ihrer Vereinigung sollten beide Armeen „auf breiter Front“ von Süden auf Berlin vorgehen. Die 9. Armee sollte unterdessen auch ihre Ostfront halten, damit die Heeresgruppe Mitte von Süden aufschließen konnte.""",
      lang="en",
      note="„Von Süden aufschließen“: Damit war die Heeresgruppe Mitte gemeint, deren Angriff bei Bautzen nach Ziemke in diesen Tagen etwa vierzig Meilen von der 9. Armee entfernt stand (Gegenangriff [10]). " + RUECK[0],
      note_en="'Close up from the south' meant Army Group Centre, whose attack at Bautzen in these days, according to Ziemke, stood about forty miles from the Ninth Army (Counterattack [10]). " + RUECK[1]),
    u(5, "Ziemke S. 483", "26. April: „when the will is there“", "26 April: “when the will is there”",
      """Weidling remembered 26 April as "the day of hopes"; Krebs repeatedly phoned him at his command post in the Bendlerstrasse to announce good news. The naval liaison officer's morning report to Doenitz reflected the interpretation that was being put on Jodl's message in the Fuehrer bunker: the Ninth and Twelfth Armies were having "gratifying successes"; Steiner was "making progress"; and Schoerner's attack at Bautzen showed that "when the will is there, the enemy can be defeated even today." Hitler's resurgent confidence found expression in his reply to Jodl.""",
      de="""Weidling erinnerte sich an den 26. April als „den Tag der Hoffnungen“; Krebs rief ihn immer wieder in seinem Gefechtsstand in der Bendlerstraße an, um gute Nachrichten durchzugeben. Die Morgenmeldung des Marineverbindungsoffiziers an Dönitz gab die Deutung wieder, die man im Führerbunker Jodls Nachricht gab: Die 9. und die 12. Armee hätten „erfreuliche Erfolge“; Steiner mache „Fortschritte“; und Schörners Angriff bei Bautzen zeige, dass „man, wenn der Wille da ist, den Feind auch heute noch schlagen kann“. Hitlers wiedererwachte Zuversicht kam in seiner Antwort an Jodl zum Ausdruck.""",
      lang="en",
      note="Der Tag, an dem das OKW meldete, die Besatzung von Bautzen sei freigekämpft (Meldungen [3]), und an dem Ziemke Schörners Angriff „nahe am Stillstand“ sah (Gegenangriff [10]). Weidlings Erinnerung zitiert Ziemke nach einer sowjetischen Zeitschrift von 1961, die Morgenmeldung nach der Lagebeurteilung des Admirals Voss vom 26.4.45. Hier wird Bautzen zum Beweis für eine Haltung: Der Wille siegt. " + RUECK[0],
      note_en="The day on which the OKW reported that the garrison of Bautzen had been fought free (Reports [3]) and on which Ziemke saw Schörner's attack 'close to a standstill' (Counterattack [10]). Ziemke cites Weidling's recollection from a Soviet journal of 1961, the morning report from Admiral Voss's situation assessment of 26 April 1945. Here Bautzen becomes proof of an attitude: the will prevails. " + RUECK[1]),
    u(6, "Ziemke S. 486", "27. April: „keep on attacking north from Bautzen“", "27 April: “keep on attacking north from Bautzen”",
      """[Hitler had called on the Ninth and Twelfth Armies to do their duty, to unite and attack toward Berlin,] and so attain "the decisive turning point of the war." To the order to the armies Keitel added, "History and the German people will despise everyone who does not do his utmost to save the situation and the Fuehrer." Keitel directed Schoerner, in case contact with the OKW was lost, to keep on attacking north from Bautzen toward the Ninth and Twelfth Armies.""",
      de="""[Hitler hatte die 9. und die 12. Armee aufgerufen, ihre Pflicht zu tun, sich zu vereinigen und auf Berlin anzugreifen,] und so „die entscheidende Wende des Krieges“ herbeizuführen. Dem Befehl an die Armeen fügte Keitel hinzu: „Die Geschichte und das deutsche Volk werden jeden verachten, der nicht sein Äußerstes tut, um die Lage und den Führer zu retten.“ Keitel wies Schörner an, für den Fall, dass die Verbindung mit dem OKW abreiße, weiter von Bautzen nach Norden auf die 9. und 12. Armee anzugreifen.""",
      lang="en",
      note="Der Satz in eckigen Klammern steht auf der vorigen Seite. Die Weisung an Schörner ist die „Weisung für die Kampfführung im Südraum für den Fall, dass unmittelbare Führung durch Chef OKW nicht mehr gewährleistet ist“ (27.4.45, Akte H 22/389, nach Ziemke). Am nächsten Tag meldete das OKW öffentlich: „Nordwestlich Bautzen … sind unsere Truppen zum Angriff nach Norden angetreten“ (Gegenangriff [11]). " + RUECK[0],
      note_en="The sentence in square brackets is on the previous page. The order to Schörner is the 'directive for the conduct of operations in the southern area in case direct command by the Chief of OKW is no longer assured' (27 April 1945, file H 22/389, according to Ziemke). The next day the OKW reported publicly: 'North-west of Bautzen … our troops have gone over to the attack northward' (Counterattack [11]). " + RUECK[1]),
]

ENDE = [
    u(7, "Ziemke S. 493", "30. April: „The attempt to relieve Berlin has failed“", "30 April: “The attempt to relieve Berlin has failed”",
      """At exactly the time the SS-men were disposing of Hitler's body behind the pile of rubble that had been the Reichs Chancellory, Keitel transmitted a directive to Winter at the Command Staff B. The first sentence read: "The attempt to relieve Berlin has failed." […] The mission for the south was to form "a great ring" with the main effort in the east "to preserve as much territory as possible from Bolshevism." "The battle to win political time," the directive concluded, "must be continued. Every attempt at military or political dissolution must be put down with ruthless force."
[…] (Three couriers carrying copies of the testament for Doenitz and for Schoerner—whom Hitler had appointed his successor as Commander in Chief, Army—had left the bunker on the 29th. None of them reached his destination.)""",
      de="""Genau zu der Zeit, als die SS-Männer Hitlers Leiche hinter dem Trümmerhaufen beseitigten, der die Reichskanzlei gewesen war, übermittelte Keitel eine Weisung an Winter beim Führungsstab B. Der erste Satz lautete: „Der Versuch, Berlin zu entsetzen, ist gescheitert.“ […] Der Auftrag für den Süden war, einen „großen Ring“ zu bilden, mit dem Schwerpunkt im Osten, „um so viel Gebiet wie möglich vor dem Bolschewismus zu bewahren“. „Der Kampf um politischen Zeitgewinn“, schloss die Weisung, „muss fortgesetzt werden. Jeder Versuch einer militärischen oder politischen Auflösung ist mit rücksichtsloser Gewalt niederzuschlagen.“
[…] (Drei Kuriere mit Abschriften des Testaments für Dönitz und für Schörner, den Hitler zu seinem Nachfolger als Oberbefehlshaber des Heeres bestimmt hatte, hatten den Bunker am 29. verlassen. Keiner von ihnen erreichte sein Ziel.)""",
      lang="en",
      note="Hitler hatte sich am Nachmittag des 30. April das Leben genommen (Ziemke S. 492). Der „Süden“ ist der Raum der Heeresgruppe Mitte, zu der Bautzen gehörte. Der letzte Satz der Weisung galt den eigenen Soldaten und den Menschen in den noch gehaltenen Gebieten: Wer aufgab, sollte mit Gewalt daran gehindert werden. Wie Schörners Standgerichte das umsetzten, soll ein späteres Modul belegen. Der Teil des Absatzes zwischen Testament und Kurieren steht auf S. 493–494. " + RUECK[0],
      note_en="Hitler had killed himself in the afternoon of 30 April (Ziemke p. 492). The 'south' is the area of Army Group Centre, to which Bautzen belonged. The last sentence of the directive was aimed at its own soldiers and at the people in the areas still held: anyone giving up was to be stopped by force. How Schörner's courts martial carried this out a later module is to document. " + RUECK[1]),
    u(8, "Marburger Zeitung, 7.5.1945, S. 1", "6. Mai: „Goebbels und Keitel gefallen“", "6 May: “Goebbels and Keitel fallen”",
      """Goebbels und Keitel gefallen
dnb, 6. Mai
Reichspropagandaminister Dr. Josef Goebbels, der Chef des Oberkommandos der Wehrmacht Generalfeldmarschall Keitel, Reichsleiter Martin Bormann und der Staatssekretär im Reichspropagandaministerium Werner Naumann sind beim Schicksalskampf um die Reichshauptstadt gegen den Bolschewismus kämpfend in der Reichskanzlei gefallen. Sie haben ihre Treue zu Führer, Volk und Reich mit dem Tode besiegelt.""",
      en="""Goebbels and Keitel fallen
dnb, 6 May
Reich Propaganda Minister Dr Joseph Goebbels, the Chief of the High Command of the Wehrmacht Field Marshal Keitel, Reichsleiter Martin Bormann and the State Secretary in the Reich Propaganda Ministry Werner Naumann have fallen fighting in the Reich Chancellery in the fateful battle for the Reich capital against Bolshevism. They have sealed their loyalty to Führer, people and Reich with death.""",
      lang="de",
      note="Die letzte Meldung aus dem Bunker, die diese Zeitung druckte, war falsch. Goebbels und seine Frau nahmen sich das Leben, nachdem sie ihre Kinder getötet hatten (Ziemke S. 494). Keitel lebte: Am 8. Mai richtete Kesselring noch ein Fernschreiben an „OKW, Feldmarschall Keitel“ (Ziemke S. 498, Anm. 118). Bormann kam nach Ziemke „wahrscheinlich“ beim Versuch um, aus Berlin herauszukommen (S. 494). Die Meldung stand auf derselben Seite wie die 14.600 Toten „im Großraum von Bautzen“ (Meldungen [5]).",
      note_en="The last report from the bunker this newspaper printed was false. Goebbels and his wife killed themselves after killing their children (Ziemke p. 494). Keitel was alive: on 8 May Kesselring still sent a signal to 'OKW, Field Marshal Keitel' (Ziemke p. 498, note 118). Bormann, according to Ziemke, 'probably' died trying to get out of Berlin (p. 494). The report stood on the same page as the 14,600 dead 'in the greater Bautzen area' (Reports [5])."),
    u(9, "Ziemke S. 498", "8. Mai: Schörner", "8 May: Schörner",
      """Schoerner had reported on 2 May that he had a tight hold on his troops and was starting to manufacture his own ammunition and motor fuel. The last that had been heard from him was that he intended to fight his army group through to the line of the Elbe and Vltava (Moldau) before surrendering. On the 8th an OKW staff colonel with an American officer escort went to Schoerner's headquarters. The colonel reported that Schoerner had ordered the surrender terms observed but claimed he did not have the means to make certain they were carried out everywhere. […] Schoerner deserted his troops on the 8th and in civilian clothes flew a light plane out of Czechoslovakia. He was arrested in Austria ten days later by First Panzer Army troops and turned over to the Americans.""",
      de="""Schörner hatte am 2. Mai gemeldet, er habe seine Truppen fest in der Hand und beginne, eigene Munition und eigenen Treibstoff herzustellen. Zuletzt hatte man von ihm gehört, er wolle seine Heeresgruppe bis an die Linie von Elbe und Moldau durchschlagen, bevor er kapituliere. Am 8. ging ein Oberst des OKW-Stabes mit amerikanischer Offiziersbegleitung in Schörners Hauptquartier. Der Oberst berichtete, Schörner habe befohlen, die Kapitulationsbedingungen einzuhalten, behaupte aber, er habe nicht die Mittel, sicherzustellen, dass sie überall durchgeführt würden. […] Schörner verließ seine Truppen am 8. und flog in Zivil mit einem leichten Flugzeug aus der Tschechoslowakei. Zehn Tage später wurde er in Österreich von Truppen der 1. Panzerarmee festgenommen und den Amerikanern übergeben.""",
      lang="en",
      note="Der Oberbefehlshaber, dessen Angriff bei Bautzen im Bunker den „Willen“ bewies und der seine Soldaten nach Goebbels' Wort „mit politischem Fanatismus“ kämpfen ließ (Lauban [4]), verließ sie am Tag der Kapitulation. Ziemke nennt als Quelle u. a. einen Zeitungsbericht der New York Times vom 21. Mai 1945.",
      note_en="The commander-in-chief whose attack at Bautzen proved the 'will' in the bunker, and who, in Goebbels's word, had his soldiers fight 'with political fanaticism' (Lauban [4]), left them on the day of the capitulation. Ziemke's sources include a New York Times report of 21 May 1945."),
]

DATA = {
    "titel": "Der Bunker: die Meldung wird zur Weisung",
    "titel_en": "The bunker: the report becomes an order",
    "autor": "Earl F. Ziemke (1968), nach den Akten von OKH und OKW; Deutsches Nachrichtenbüro (1945)",
    "autor_en": "Earl F. Ziemke (1968), from the files of OKH and OKW; German News Bureau (1945)",
    "jahr": "21. April – 8. Mai 1945",
    "jahr_en": "21 April – 8 May 1945",
    "orig_sprache": "en",
    "pg_label": "",
    "quelle": "Earl F. Ziemke, Stalingrad to Berlin: The German Defeat in the East (Washington: U.S. Army Center of Military History, 1968; CMH Pub 30-5-1, 1987), S. 477–479, 483, 486, 493–494, 498 (Internet Archive StalingradToBerlinTheGermanDefeatInTheEast-nsia); dnb-Meldung „Goebbels und Keitel gefallen“, Marburger Zeitung Nr. 127 (7.5.1945), S. 1 (dLib.si, URN:NBN:SI:DOC-NAZDZ66I).",
    "hinweis": "Was im Führerbunker aus dem Gegenangriff bei Bautzen wurde: eine Grundweisung am 21. April, ein Baustein der Front am 22., ein Beweis des Willens am 26., ein Befehl, nach Norden weiterzugreifen, am 27., und am 30. April die Weisung, im Süden einen „großen Ring“ zu halten und jede Auflösung mit Gewalt niederzuschlagen. Ziemke schrieb das 1968 aus den erbeuteten Akten von OKH und OKW, die damals in amerikanischer Hand waren; er gibt sie englisch wieder. Die deutschen Fassungen hier sind deshalb Rückübersetzungen, nicht der Wortlaut der Akten. Dazu die letzte Meldung aus dem Bunker, die die Marburger Zeitung druckte, und das Ende Schörners.",
    "hinweis_en": "What became of the counterattack at Bautzen in the Führer bunker: a basic order on 21 April, a building block of the front on the 22nd, proof of the will on the 26th, an order to keep attacking northward on the 27th, and on 30 April the directive to hold 'a great ring' in the south and to put down every dissolution by force. Ziemke wrote this in 1968 from the captured files of OKH and OKW, then in American hands; he gives them in English. Added are the last report from the bunker the Marburger Zeitung printed, and Schörner's end.",
    "sections": [
        {"id": "weisung", "titel": "Aus einer Meldung eine Weisung, 21. und 22. April", "titel_en": "From a report an order, 21 and 22 April", "zk": "Bunker",
         "blurb": "Ein örtlicher Fortschritt nordwestlich Görlitz wird zur „Grundweisung“; am Tag danach erklärt Hitler den Krieg für verloren, und am Abend hat Schörners Angriff „Erfolg“.",
         "blurb_en": "Local progress north-west of Görlitz becomes a 'basic order'; the next day Hitler declares the war lost, and by evening Schörner's attack is 'succeeding'.",
         "units": WEISUNG},
        {"id": "wille", "titel": "„Wenn der Wille da ist“, 25.–27. April", "titel_en": "“When the will is there”, 25–27 April", "zk": "Bunker",
         "blurb": "Entsatzangriffe ohne Rücksicht auf Flanken, der Tag der Hoffnungen, und Keitels Befehl an Schörner, von Bautzen nach Norden weiterzugreifen.",
         "blurb_en": "Relief attacks without regard for flanks, the day of hopes, and Keitel's order to Schörner to keep attacking north from Bautzen.",
         "units": WILLE},
        {"id": "ende", "titel": "Das Ende, 30. April – 8. Mai", "titel_en": "The end, 30 April – 8 May", "zk": "Bunker",
         "blurb": "Der „große Ring“ im Süden, ein falscher Heldentod in der Zeitung, und Schörner im Leichtflugzeug.",
         "blurb_en": "The 'great ring' in the south, a false hero's death in the newspaper, and Schörner in a light plane.",
         "units": ENDE},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
