"""Modul 6 „Horka, Niederkaina, das Außenlager“: Gewalt aller Seiten in und um die Schlacht, und was die gemeinfreien
Quellen dazu sagen und verschweigen.

Quellen, an den Seitenbildern gelesen:
- Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 488–490 (gemeinfrei).
Der zweite Abschnitt ist ein Referat der neueren Literatur, kein Quellentext: Für Horka, Niederkaina und das Außenlager
liegen in den hier benutzten gemeinfreien Drucken keine Belege vor. Referiert wird nach den zugänglichen Übersichten
über Kopociński/Kopociński (2021), Kania (2023) und Seidel (2005) und nach dem Gedenkstättenportal der Bundeszentrale
für politische Bildung; die Bücher selbst lagen nicht vor.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "verbrechen.json"


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
    u(1, "Ziemke S. 488–489", "„what they could expect of their own leadership“", "“what they could expect of their own leadership”",
      """Berlin did not go down, as Hitler had imagined, in a Wagnerian burst of glory but in a ragged wave of destruction and despair. Corpses hanging in the streets, the work of single-officer flying courts-martial that passed only death sentences, showed soldiers and civilians what they could expect of their own leadership. But that leadership was operating on residual momentum, it could no longer formulate, deliver, or enforce purposeful orders. Individuals might be hanged; whole units could hide out.""",
      de="""Berlin ging nicht, wie Hitler es sich vorgestellt hatte, in einem wagnerischen Glanz unter, sondern in einer zerfetzten Welle von Zerstörung und Verzweiflung. Leichen, die in den Straßen hingen, das Werk fliegender Standgerichte aus einem einzigen Offizier, die nur Todesurteile fällten, zeigten Soldaten und Zivilisten, was sie von ihrer eigenen Führung zu erwarten hatten. Aber diese Führung lief nur noch aus Trägheit weiter; sie konnte keine sinnvollen Befehle mehr fassen, übermitteln oder durchsetzen. Einzelne mochten gehängt werden; ganze Einheiten konnten sich verstecken.""",
      lang="en",
      note="Ziemke spricht von Berlin. Für die Lausitz und Schörners Heeresgruppe sagen die hier abgedruckten Quellen nur, was befohlen war: Am 30. April sollte „jeder Versuch einer militärischen oder politischen Auflösung … mit rücksichtsloser Gewalt“ niedergeschlagen werden (Bunker [7]). Wie das in der Oberlausitz umgesetzt wurde, wer dort gehängt oder erschossen wurde, ist hier nicht belegt; ein gemeinfreier Beleg wird gesucht.",
      note_en="Ziemke is speaking of Berlin. For Lusatia and Schörner's army group the sources printed here say only what was ordered: on 30 April 'every attempt at military or political dissolution' was to be put down 'with ruthless force' (Bunker [7]). How this was carried out in Upper Lusatia, who was hanged or shot there, is not documented here; a public-domain record is being sought."),
    u(2, "Ziemke S. 489–490", "„What had happened in East Prussia, Pomerania, and Silesia“", "“What had happened in East Prussia, Pomerania, and Silesia”",
      """In an attempt to stiffen the Berliner's resistance, Goebbels had, since January, saturated the news broadcasts with refugees' accounts of Russian atrocities […]. What had happened in East Prussia, Pomerania, and Silesia also happened in Berlin, but by then Soviet policy discouraged personal acts of license and vengeance. As indication of an intent, at least, to restore order quickly, General Polkovnik N. Z. Berzarin took control as city commandant on 28 April.""",
      de="""Um den Widerstand der Berliner zu stärken, hatte Goebbels seit Januar die Nachrichtensendungen mit Berichten von Flüchtlingen über russische Gewalttaten überschwemmt […]. Was in Ostpreußen, Pommern und Schlesien geschehen war, geschah auch in Berlin, aber inzwischen hielt die sowjetische Politik von persönlicher Willkür und Rache ab. Als Zeichen zumindest der Absicht, rasch Ordnung herzustellen, übernahm Generaloberst N. S. Bersarin am 28. April die Stadt als Kommandant.""",
      lang="en",
      note="Beides steht in einem Satz: die Gewalt der Roten Armee gegen deutsche Zivilisten, die Ziemke für Ostpreußen, Pommern, Schlesien und Berlin feststellt, und ihr Gebrauch durch die Propaganda, die damit zum Weiterkämpfen trieb (Lauban [5]). Ausgelassen ist ein Beispiel, das Ziemke aus den Sendungen anführt. In der Oberlausitz gehört zur Gewalt der Roten Armee, nach der neueren Literatur, die Tötung gefangener Volkssturmmänner in Niederkaina (Verbrechen [4]).",
      note_en="Both stand in one sentence: Red Army violence against German civilians, which Ziemke states for East Prussia, Pomerania, Silesia and Berlin, and its use by propaganda to drive people to fight on (Lauban [5]). An example Ziemke cites from the broadcasts is omitted. In Upper Lusatia, according to recent literature, Red Army violence includes the killing of captured Volkssturm men at Niederkaina (Crimes [4])."),
]

REFERAT = [
    u(3, "Referat: Kopociński/Kopociński 2021; Kania 2023", "Referat: Horka, 26. April 1945", "Summary: Horka, 26 April 1945",
      """Am 26. April 1945 geriet bei Horka, einem Dorf bei Crostwitz (Chrósćicy), eine Kolonne des 15. Selbständigen Sanitätsbataillons der polnischen 9. Infanteriedivision in deutsche Hand: nach der neueren polnischen Literatur über dreihundert Menschen, darunter 282 Verwundete, auf Lastwagen mit dem Roten Kreuz. Die Division war bei ihrem befohlenen Rückzug in den Gegenangriff geraten. Die Verwundeten und das Sanitätspersonal wurden zum großen Teil getötet; die Literatur nennt zwischen 150 und 300 Tote. Als Täter nennt sie Soldaten der Panzergrenadier-Division „Brandenburg“, möglicherweise mit Angehörigen einer ukrainischen Kollaborationseinheit. Eine polnische Militärkommission öffnete am 8. Mai 1945 Gräber, barg 44 Tote, von denen 19 identifiziert wurden, und fand Spuren von Misshandlung. Bestraft wurde niemand.""",
      en="""On 26 April 1945 near Horka, a village near Crostwitz (Chrósćicy), a column of the 15th Independent Medical Battalion of the Polish 9th Infantry Division fell into German hands: according to recent Polish literature more than three hundred people, among them 282 wounded, on trucks marked with the Red Cross. The division had run into the counterattack during its ordered retreat. Most of the wounded and the medical staff were killed; the literature gives between 150 and 300 dead. As perpetrators it names soldiers of the Panzergrenadier Division 'Brandenburg', possibly with members of a Ukrainian collaborationist unit. A Polish military commission opened graves on 8 May 1945, recovered 44 bodies, of whom 19 were identified, and found traces of ill-treatment. No one was punished.""",
      lang="de",
      note=REF[0] + " Nach den Übersichten über Zbigniew und Krzysztof Kopociński, Horka – łużycka Golgota służby zdrowia 2. Armii Wojska Polskiego (2021), und Leszek Kania, Budziszyn 1945 (2023); die Bücher lagen nicht vor. Kopociński/Kopociński halten 150 bis 200 Tote für wahrscheinlicher als 300. Der Bericht der Kommission von 1945 und die Fotos der Exhumierung liegen nach diesen Übersichten in polnischen Archiven; ein zugängliches gemeinfreies Exemplar wird gesucht. Am selben 26. April meldete das OKW Bautzen „freigekämpft“ (Meldungen [3]), am 1. Mai „zahlreiche Gefangene“ aus den „Säuberungskämpfen“ (Gegenangriff [13]).",
      note_en=REF[1] + " After the overviews of Zbigniew and Krzysztof Kopociński, Horka – łużycka Golgota służby zdrowia 2. Armii Wojska Polskiego (2021), and Leszek Kania, Budziszyn 1945 (2023); the books themselves were not available. The Kopocińskis consider 150 to 200 dead more likely than 300. According to these overviews the commission's 1945 report and the exhumation photographs are in Polish archives; an accessible public-domain copy is being sought. On the same 26 April the OKW reported Bautzen 'fought free' (Reports [3]), on 1 May 'numerous prisoners' from the 'mopping-up' (Counterattack [13])."),
    u(4, "Referat: Kania 2023; Seidel 2005", "Referat: Niederkaina, 22. April 1945", "Summary: Niederkaina, 22 April 1945",
      """In Niederkaina (Delnja Kina), heute ein Stadtteil von Bautzen, wurden am 22. April 1945 nach der neueren Literatur rund zweihundert gefangene Volkssturmmänner getötet, die meisten in einer Scheune verbrannt. Kania nennt als Täter Rotarmisten der 254. Schützendivision, deren Kommandeur Puteiko am 20. April tödlich verwundet worden war. Seidel schrieb die Tat polnischen Soldaten zu; Kania hält das für unbegründet, weil die polnischen Truppen nördlich von Bautzen kämpften. Weitere Gefangene sollen in Bautzen erschossen worden sein. Eine Gedenktafel in Niederkaina wurde im April 2018 zerstört und im Oktober 2018 ersetzt.""",
      en="""At Niederkaina (Delnja Kina), today part of Bautzen, around two hundred captured Volkssturm men were killed on 22 April 1945 according to recent literature, most of them burned in a barn. Kania names as perpetrators Red Army soldiers of the 254th Rifle Division, whose commander Puteiko had been mortally wounded on 20 April. Seidel attributed the crime to Polish soldiers; Kania considers this unfounded because the Polish troops were fighting north of Bautzen. Further prisoners are said to have been shot in Bautzen. A memorial plaque in Niederkaina was destroyed in April 2018 and replaced in October 2018.""",
      lang="de",
      note=REF[0] + " Nach den Übersichten über Leszek Kania, Budziszyn 1945 (2023), und Theodor Seidel, Kriegsverbrechen in Sachsen (2005), und nach Presseberichten von 2018; die Bücher lagen nicht vor. Die Zahl der Toten schwankt zwischen 195 und etwa 200. Am Tag zuvor hatte Moskau gemeldet, sowjetische Kämpfer hätten den Widerstand der deutschen Besatzung von Bautzen „niedergeschlagen“ (Meldungen [2]); von Gefangenen sagt die Meldung nichts.",
      note_en=REF[1] + " After the overviews of Leszek Kania, Budziszyn 1945 (2023), and Theodor Seidel, Kriegsverbrechen in Sachsen (2005), and press reports of 2018; the books themselves were not available. The number of dead varies between 195 and about 200. The day before, Moscow had reported that Soviet soldiers had 'crushed' the resistance of the German garrison of Bautzen (Reports [2]); of prisoners the report says nothing."),
    u(5, "Referat: Gedenkstättenportal der bpb", "Referat: Das Außenlager Bautzen", "Summary: the Bautzen subcamp",
      """Von Oktober 1944 bis April 1945 bestand auf dem Gelände der Waggonbau- und Maschinenfabrik Bautzen ein Außenlager des Konzentrationslagers Groß-Rosen. Die Häftlinge arbeiteten für die Rüstung und mussten auch Panzersperren und Schützengräben bauen, also die Stellungen, um die im April gekämpft wurde. Mitte April 1945 wurde das Lager geräumt; die Häftlinge mussten in Richtung Nixdorf (Mikulášovice) in Böhmen marschieren, und viele überlebten den Marsch nicht. Ein Gedenkstein von 1979 wurde 1993 bei Bauarbeiten entfernt; seit 1997 steht ein neuer außerhalb des Werksgeländes.""",
      en="""From October 1944 to April 1945 a subcamp of the Groß-Rosen concentration camp existed on the grounds of the Waggonbau- und Maschinenfabrik Bautzen, a railway-carriage works. The prisoners worked for the armaments industry and also had to build anti-tank barriers and trenches, that is, the positions fought over in April. In mid-April 1945 the camp was cleared; the prisoners had to march towards Nixdorf (Mikulášovice) in Bohemia, and many did not survive the march. A memorial stone of 1979 was removed during building work in 1993; since 1997 a new one has stood outside the works.""",
      lang="de",
      note=REF[0] + " Nach dem Eintrag „Gedenkstein Außenlager KZ Groß-Rosen“ im Gedenkstättenportal der Bundeszentrale für politische Bildung. Die Zahl der Häftlinge, ihre Herkunft und die Zahl der Toten nennt der Eintrag nicht; Unterlagen liegen nach der Literatur im Bundesarchiv und bei den Arolsen Archives. In keiner der Meldungen dieses Apparats, deutschen wie sowjetischen, kommen die Häftlinge vor.",
      note_en=REF[1] + " After the entry 'Memorial stone, Groß-Rosen subcamp' in the memorial-sites portal of the Federal Agency for Civic Education. The entry does not give the number of prisoners, their origin or the number of dead; according to the literature, records are held by the Bundesarchiv and the Arolsen Archives. In none of the reports in this apparatus, German or Soviet, do the prisoners appear."),
]

DATA = {
    "titel": "Horka, Niederkaina, das Außenlager",
    "titel_en": "Horka, Niederkaina, the subcamp",
    "autor": "Earl F. Ziemke (1968); Referat der neueren Literatur",
    "autor_en": "Earl F. Ziemke (1968); summary of recent literature",
    "jahr": "April 1945",
    "jahr_en": "April 1945",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Earl F. Ziemke, Stalingrad to Berlin (CMH 1968/1987), S. 488–490 (Internet Archive StalingradToBerlinTheGermanDefeatInTheEast-nsia). Referate nach Kopociński/Kopociński, Horka (2021), Kania, Budziszyn 1945 (2023), Seidel, Kriegsverbrechen in Sachsen (2005), und dem Gedenkstättenportal der Bundeszentrale für politische Bildung (bpb.de).",
    "hinweis": "Die Meldungen von 1945 schweigen von den Verbrechen in und um die Schlacht: Das OKW meldet „Säuberungskämpfe“ und „zahlreiche Gefangene“, Moskau eine „niedergeschlagene“ Besatzung, und keine Seite nennt Verwundete, Gefangene oder Häftlinge. Gemeinfreie Belege zu Horka, Niederkaina und dem Außenlager Bautzen konnten für diesen Apparat bisher nicht beschafft werden. Der Abschnitt „Was die neuere Literatur berichtet“ ist deshalb ein Referat, ausdrücklich als solches gekennzeichnet; er übernimmt keine Wortlaute, sondern fasst zusammen, was in den zugänglichen Übersichten über die neuere polnische und deutsche Forschung steht, mit ihren Abweichungen. Gewalt wird hier keiner Seite zugerechnet, wo die Literatur es nicht tut. Im Spiel zu diesem Apparat sind diese Ereignisse nie ein Spielzug.",
    "hinweis_en": "The reports of 1945 are silent about the crimes in and around the battle: the OKW reports 'mopping-up fighting' and 'numerous prisoners', Moscow a garrison 'crushed', and neither side names wounded men, prisoners or camp prisoners. Public-domain records on Horka, Niederkaina and the Bautzen subcamp have not yet been obtained for this apparatus. The section 'What recent literature reports' is therefore a summary, expressly marked as such; it quotes nothing but summarises what the accessible overviews of recent Polish and German research say, with their divergences. Violence is attributed to no side where the literature does not do so. In the game accompanying this apparatus these events are never a move.",
    "sections": [
        {"id": "quellen", "titel": "Was die Quellen sagen", "titel_en": "What the sources say", "zk": "Verbrechen",
         "blurb": "Ziemke über die Standgerichte der eigenen Führung und über die Gewalt der Roten Armee, beides am Beispiel Berlins.",
         "blurb_en": "Ziemke on the courts martial of the Germans' own leadership and on Red Army violence, both from the example of Berlin.",
         "units": QUELLEN},
        {"id": "literatur", "titel": "Was die neuere Literatur berichtet (Referat)", "titel_en": "What recent literature reports (summary)", "zk": "Verbrechen",
         "blurb": "Horka, Niederkaina und das Außenlager Bautzen, zusammengefasst nach der neueren Forschung, mit ihren Abweichungen. Kein Quellentext.",
         "blurb_en": "Horka, Niederkaina and the Bautzen subcamp, summarised from recent research, with its divergences. Not a source text.",
         "units": REFERAT},
    ],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
