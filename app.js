/* „Freigekämpft“ – ‚Fought Free‘: Bautzen, April 1945. Die letzte Offensive der Wehrmacht im Osten in ihren Meldungen.
   Ein zweisprachiger Quellenapparat. Vanilla JS, Hash-Routen. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };

/* ------------------------------------------------------------ language */
let ui = "de";
try { ui = localStorage.getItem("frei_ui") || ""; } catch (e) { /* storage blocked */ }
if (ui !== "de" && ui !== "en") ui = /^de\b/i.test(navigator.language || "") ? "de" : "en";
let langPref = null;
try { langPref = localStorage.getItem("frei_lang"); } catch (e) { /* storage blocked */ }

const T = {
  de: {
    title: "„Freigekämpft“. Bautzen, April 1945", nav: { "": "Übersicht", texts: "Texte", compare: "Vergleich", timeline: "Zeitleiste", plates: "Tafeln", sources: "Quellen" },
    switchTo: "English", loading: "Wird geladen…", allTexts: "← Alle Texte", allCmp: "← Alle Vergleiche", citeAs: "zitiert als", cite: "Zitieren als",
    orig: "Original", both: "Original + Übersetzung", trans: "Übersetzung", or: " oder ",
    srcNote: "Quelle und Editionsnotiz", source: "Quelle", planned: "geplant", notTaken: "nicht aufgenommen",
    shipped: "Abgedruckt", plannedH: "Geplant", missingH: "Geprüft und nicht aufgenommen",
    textsTag: "Texte", textsH: "Das Korpus", textsLede: "Jedes Modul ist vollständig lesbar, das Original neben einer Übersetzung: russische und englische Texte mit deutscher, alle Texte mit englischer Übersetzung. Was geprüft und nicht aufgenommen wurde, steht unten mit Begründung.",
    cmpTag: "Vergleich", cmpH: "Zwei Meldungen, eine Stadt", tlTag: "Zeitleiste", platesTag: "Tafeln", platesH: "Karten, Seiten, Bilder",
    fail: "Der Apparat konnte nicht geladen werden: "
  },
  en: {
    title: "‘Fought Free’. Bautzen, April 1945", nav: { "": "Overview", texts: "Texts", compare: "Compare", timeline: "Timeline", plates: "Plates", sources: "Sources" },
    switchTo: "Deutsch", loading: "Loading…", allTexts: "← All texts", allCmp: "← All comparisons", citeAs: "cited as", cite: "Cite as",
    orig: "Original", both: "Original + English", trans: "English", or: " or ",
    srcNote: "Source and editorial note", source: "Source", planned: "planned", notTaken: "not included",
    shipped: "Printed here", plannedH: "Planned", missingH: "Examined and not included",
    textsTag: "Texts", textsH: "The corpus", textsLede: "Every module can be read in full, the original beside an English translation. What was examined and not included is listed below, with the reason.",
    cmpTag: "Compare", cmpH: "Two reports, one town", tlTag: "Timeline", platesTag: "Plates", platesH: "Maps, pages, pictures",
    fail: "The apparatus could not be loaded: "
  }
};
const S = k => T[ui][k];
const SIDES = {
  dt: { de: "Deutsche Seite", en: "German side" },
  sow: { de: "Sowjetische Seite", en: "Soviet side" },
  pol: { de: "Polnische Seite", en: "Polish side" },
  hist: { de: "Geschichtsschreibung", en: "Historians" },
  zivil: { de: "Opfer und Zivilisten", en: "Victims and civilians" },
  rezeption: { de: "Erinnerung", en: "Memory" }
};
const LANGS = {
  de: { de: "Deutsch", en: "German" }, fr: { de: "Französisch", en: "French" },
  ru: { de: "Russisch", en: "Russian" }, pl: { de: "Polnisch", en: "Polish" }, en: { de: "Englisch", en: "English" },
  mul: { de: "Russisch, Polnisch, Deutsch, Sorbisch", en: "Russian, Polish, German, Sorbian" }
};
/* a field in the reader's language: o.k_en in English if present, else o.k */
const L = (o, k) => (o && ui === "en" && o[k + "_en"] != null) ? o[k + "_en"] : (o ? o[k] : "");

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] ? SIDES[s][ui] : s)}</span>`;
const lname = l => LANGS[l] ? LANGS[l][ui] : l;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

function setUI(lang) {
  ui = lang;
  try { localStorage.setItem("frei_ui", ui); } catch (e) { /* storage blocked */ }
  applyUI();
  route();
}

function applyUI() {
  document.documentElement.lang = ui;
  document.title = S("title");
  document.querySelectorAll(".top nav a[data-k]").forEach(a => a.textContent = S("nav")[a.dataset.k]);
  const b = document.getElementById("uiBtn");
  b.textContent = S("switchTo");
  b.lang = ui === "de" ? "en" : "de";
}

async function boot() {
  applyUI();
  document.getElementById("uiBtn").onclick = () => setUI(ui === "de" ? "en" : "de");
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
const OVERVIEW = {
  de: {
    tag: "April 1945 · Bautzen · Budyšin · Budziszyn · Weißenberg · Kamenz · Horka",
    h: "„Die tapfere Besatzung von Bautzen wurde freigekämpft“",
    lede: "Im April 1945, als die Rote Armee Berlin einschloss, griff die Heeresgruppe Mitte in der Oberlausitz noch einmal an: vom 21. April an gegen die Flanke der 2. Polnischen Armee und der sowjetischen 52. Armee, um Bautzen, Weißenberg und Kamenz. Am 21. April meldete Moskau, Bautzen sei ganz genommen; am 26. April meldete das Oberkommando der Wehrmacht, die Besatzung von Bautzen sei freigekämpft. Im Bunker der Reichskanzlei galt der Angriff als Beweis, dass der Wille noch siege.",
    body: "Dieser Apparat folgt der letzten Offensive der Wehrmacht im Osten durch ihre Meldungen: die täglichen Berichte des Oberkommandos der Wehrmacht, wie eine Zeitung sie druckte, die Meldungen des Sowjetischen Informationsbüros, die amerikanische Armeegeschichte, die aus den erbeuteten deutschen Akten schrieb, und, wo sie gemeinfrei sind, polnische Dokumente. Er stellt die Meldungen neben das, was geschah: die Toten der 2. Polnischen Armee, die ermordeten Verwundeten von Horka, die verbrannten Volkssturmmänner von Niederkaina, die Häftlinge des Außenlagers Bautzen, die sorbischen Dörfer zwischen den Fronten. Der Titel ist das Wort des Wehrmachtberichts vom 26. April; er steht in Anführungszeichen, weil er geprüft wird.",
    q: [
      ["Wer meldete was?", "Zwei Siegesmeldungen über eine Stadt, fünf Tage auseinander, dazu die Lagebeurteilung im Führerbunker. Die Meldungen der letzten Kriegswoche zählen Panzer, Gefangene und Tote; der Apparat legt die Zahlen nebeneinander und nennt, wer welche nennt."],
      ["Warum keine Wochenschau?", "Die Deutsche Wochenschau endete am 22. März 1945. Ihre letzte Gegenoffensive war Lauban, Anfang März, mit Goebbels auf dem Markt. Für Bautzen blieben der Wehrmachtbericht, der Rundfunk und die Zeitung."],
      ["Wessen Gewalt?", "Die Kämpfe trafen Soldaten, Gefangene, Verwundete, Häftlinge und Dörfer. Der Apparat nennt die Verbrechen aller Seiten mit ihren Belegen und sagt, wo die Belege dünn oder umstritten sind."],
      ["Lässt sich das spielen?", "Das Begleitspiel „Freigekämpft“ ist ein Hexspiel auf der Karte des Deutschen Reiches, in dem die eigene Abendmeldung nach oben wirkt und der Bunker sie beim Wort nimmt. Verbrechen sind darin nie ein Spielzug; sie stehen als Chronik mit ihrer Quelle in diesem Apparat. Es erscheint auf itch.io (leofassb.itch.io/freigekaempft); der Link steht unten auf jeder Seite."]
    ],
    none: "Die ersten Module sind in Arbeit; die Seite „Texte“ nennt sie mit ihren Quellen.",
    have: "Was der Apparat enthält", qs: "Die Fragen"
  },
  en: {
    tag: "April 1945 · Bautzen · Budyšin · Budziszyn · Weißenberg · Kamenz · Horka",
    h: "“The brave garrison of Bautzen was fought free”",
    lede: "In April 1945, as the Red Army encircled Berlin, Army Group Centre attacked once more in Upper Lusatia: from 21 April against the flank of the Polish Second Army and the Soviet 52nd Army, around Bautzen, Weißenberg and Kamenz. On 21 April Moscow reported that Bautzen had been taken entirely; on 26 April the High Command of the Wehrmacht reported that the garrison of Bautzen had been fought free. In the bunker of the Reich Chancellery the attack was taken as proof that will could still prevail.",
    body: "This apparatus follows the last offensive of the Wehrmacht in the East through its reports: the daily communiqués of the High Command of the Wehrmacht as a newspaper printed them, the reports of the Soviet Information Bureau, the American army history written from the captured German files and, where they are in the public domain, Polish documents. It sets the reports beside what happened: the dead of the Polish Second Army, the murdered wounded of Horka, the Volkssturm men burned at Niederkaina, the prisoners of the Bautzen subcamp, the Sorbian villages between the fronts. The title is the word of the Wehrmacht report of 26 April; it stands in quotation marks because it is being examined.",
    q: [
      ["Who reported what?", "Two victory reports about one town, five days apart, and the situation report in the Führer bunker. The reports of the last week of the war count tanks, prisoners and dead; the apparatus sets the figures side by side and says who gives which."],
      ["Why no newsreel?", "The German newsreel ended on 22 March 1945. Its last counteroffensive was Lauban, early in March, with Goebbels in the market square. For Bautzen there remained the Wehrmacht report, the radio and the newspaper."],
      ["Whose violence?", "The fighting struck soldiers, prisoners, wounded men, camp prisoners and villages. The apparatus names the crimes of all sides with their evidence and says where the evidence is thin or disputed."],
      ["Can it be played?", "The companion game \"Fought Free\" is a hex game on the map of the German Reich in which your own evening report travels upward and the bunker takes it at its word. Crimes are never a move in it; they appear as chronicle with their source in this apparatus. It is published on itch.io (leofassb.itch.io/freigekaempft); the link is at the foot of every page."]
    ],
    none: "The first modules are in preparation; the Texts page lists them with their sources.",
    have: "What the apparatus contains", qs: "The questions"
  }
};

function overview() {
  const O = OVERVIEW[ui];
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">${esc(O.tag)}</span>
      <h1>${esc(O.h)}</h1>
      <p class="lede">${esc(O.lede)}</p>
      <p class="readable">${esc(O.body)}</p>
    </div>
  </div>

  <h2>${esc(O.have)}</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">${esc(O.none)}</p>`}

  <h2>${esc(O.qs)}</h2>
  <div class="grid g2">${O.q.map(([h, p]) => `<div class="panel"><h3>${esc(h)}</h3><p>${esc(p)}</p></div>`).join("")}</div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p></a>`;
}

/* the translation shown: German for French originals in the German interface, else English */
const tr = (u, ul) => (ui === "de" && ul !== "de" && u.de) ? u.de : u.en;
const trLang = (u, ul) => (ui === "de" && ul !== "de" && u.de) ? "de" : "en";

/* ------------------------------------------------------------ texts */
function texts() {
  const other = (list, label) => list.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">${esc(label)}</span></div>
      <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p><p class="fine"><b>${esc(S("source"))}:</b> ${esc(m.quelle)}</p></div>`).join("");
  view.innerHTML = `
    <span class="tag">${esc(S("textsTag"))}</span><h1>${esc(S("textsH"))}</h1>
    <p class="lede">${esc(S("textsLede"))}</p>
    ${D.mods.shipped.length ? `<h2>${esc(S("shipped"))}</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>${esc(S("plannedH"))}</h2><div class="grid g2">${other(D.mods.planned, S("planned"))}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">${esc(S("missingH"))}</h2><div class="grid g2">${other(D.mods.missing, S("notTaken"))}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">${esc(S("loading"))}</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig && trLang(u, u.lang || t.orig_sprache) !== (u.lang || t.orig_sprache));
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  // Voreinstellung: nur das Original, wenn es in der Sprache der Oberfläche ist, sonst Original und Übersetzung
  const pref = langPref || (langs.every(l => l === ui) ? "orig" : "both");
  const lang = bilingual ? pref : "en";
  const origName = langs.length === 1 && langs[0] !== "de" ? `Original (${lname(langs[0])})` : S("orig");
  const labels = { both: S("both"), orig: origName, en: S("trans") };
  view.innerHTML = `
    <p class="fine"><a href="#/texts">${esc(S("allTexts"))}</a></p>
    <span class="tag">${side(m.side)} ${esc(L(t, "jahr"))} · ${esc(S("citeAs"))} ${esc(sec.zk)} [n]</span>
    <h1>${esc(L(t, "titel"))}</h1>
    <p class="fine">${esc(L(t, "autor"))}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(L(s, "titel"))}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(L(sec, "titel"))}</h3><p>${esc(L(sec, "blurb"))}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${["orig", "both", "en"].map(k => `<button data-l="${k}" class="${k === lang ? "on" : ""}">${esc(labels[k])}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">${esc(S("srcNote"))}</span>
      <p><b>${esc(S("source"))}.</b> ${esc(t.quelle)}</p><p>${esc(L(t, "hinweis"))}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const ul = u.lang || t.orig_sprache;
    // ein englisches Original in der englischen Oberfläche braucht keine Übersetzung daneben
    const dup = !!u.orig && trLang(u, ul) === ul;
    const showO = u.orig && (lang !== "en" || dup), showE = (!u.orig || lang !== "orig") && !dup;
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="${esc(S("cite"))} ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg">${esc(t.pg_label || "")} ${esc(pgL(u.pg))}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(L(u, "titel"))}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(lname(u.lang))})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="orig" lang="${esc(ul)}">${esc(u.orig)}</div>` : ""}
            ${showE ? `<div class="text" lang="${trLang(u, ul)}">${esc(tr(u, ul))}</div>` : ""}
          </div></div>
        ${L(u, "note") ? `<div class="note">${esc(L(u, "note"))}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("frei_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

// Seitenangaben "S. 20–21" in der englischen Oberfläche als "pp. 20–21"
const pgL = pg => ui === "en" ? pg.replace(/\bAusg\. /g, "ed. ").replace(/\bS\. (\d+)\s*[–-]\s*(\d+)/g, "pp. $1–$2").replace(/\bS\. /g, "p. ").replace(/, Anm\.$/, ", note") : pg;

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(S("cmpH"))}</h1>
      <p class="lede">${esc(L(CMP, "lede"))}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side(v.side || (D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(L(p, "titel"))}</h3><p class="fine">${esc(L(p, "frage"))}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p><p class="fine">${esc(S("loading"))}</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(v.side || m.side)} <b>${esc(v.autor ? L(v, "autor") : L(t, "autor"))}</b><br><span class="fine">${esc(L(t, "jahr"))} · ${esc(L(sec, "titel"))}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(L(u, "titel"))}` : ""}</div>
        <div class="text">${esc(u.orig && (u.lang || t.orig_sprache) === ui ? u.orig : tr(u, u.lang || t.orig_sprache))}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p>
    <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(L(pair, "titel"))}</h1>
    <p class="lede">${esc(L(pair, "frage"))}</p>
    <div class="panel readable"><p>${esc(L(pair, "note"))}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const TL = D.timeline;
  view.innerHTML = `
    <span class="tag">${esc(S("tlTag"))}</span><h1>${esc(L(TL, "span") || "")}</h1>
    <p class="lede">${esc(L(TL, "lede"))}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${TL.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(L(s, "d"))} · ${side(s.side)}</div><h3>${esc(L(s, "titel"))}</h3><p>${esc(L(s, "text"))}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(L(s, "citeLabel"))}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}" title="${esc(L(p, "titel"))}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">${esc(S("platesTag"))}</span><h1>${esc(S("platesH"))}</h1>
    <p class="lede">${esc(L(D.plates, "lede"))}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}"></a>
      <figcaption>${side(p.side)} <b>${esc(L(p, "titel"))}</b><br>${esc(L(p, "caption"))}${p.cite ? ` <a href="${p.cite}">✦</a>` : ""}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(L(D.plates, "credit"))}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(L(p, "titel"))}"><figcaption class="cap"><b>${esc(L(p, "titel"))}.</b> ${esc(L(p, "caption"))}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
const METHOD = {
  de: {
    tag: "Quellen, Methode, Grenzen", h: "Wie dieser Apparat gemacht ist",
    p: [
      ["Nur Gemeinfreies.", "Jeder Text stammt aus einem Druck, dessen Schutz abgelaufen ist oder der nie geschützt war: nicht gezeichnete amtliche Bekanntmachungen von 1945, amtliche sowjetische Dokumente, Werke der amerikanischen Bundesregierung. Die Quelle steht auf seiner Seite. Neuere Darstellungen, die noch geschützt sind, werden höchstens referiert."],
      ["Die Seite ist maßgeblich.", "Die Texte sind am Seitenbild gelesen, nicht aus der maschinellen Texterkennung übernommen. Schreibung und Zeichensetzung der Drucke bleiben erhalten; jede Korrektur steht in den Anmerkungen."],
      ["Propaganda wird eingeordnet.", "Die Wehrmachtberichte und die Zeitungen der letzten Kriegswochen sind Propaganda. Sie stehen hier, weil man ihre Behauptungen prüfen muss, und jede Einheit trägt eine Anmerkung, die sagt, was die anderen Quellen dazu sagen. Hakenkreuze und Hoheitszeichen werden in Bildern und Seitenausschnitten nicht gezeigt."],
      ["Übersetzungen.", "Die Übersetzungen ins Deutsche und Englische sind eigene Arbeit, nah am Original und gemeinfrei (CC0): eine Lesehilfe, keine kritische Übersetzung."],
      ["Widersprüche.", "Wo die Quellen in Stärken, Verlusten oder Uhrzeiten auseinandergehen, stehen sie nebeneinander, mit der Angabe, wer welche Zahl nennt. Der Apparat entscheidet nicht, wo die Quellen es nicht erlauben."]
    ],
    printed: "Abgedruckte Quellen", plates: "Tafeln"
  },
  en: {
    tag: "Sources, method, limits", h: "How this apparatus is made",
    p: [
      ["Public domain only.", "Every text comes from a print whose protection has expired or that was never protected: unsigned official announcements of 1945, official Soviet documents, works of the United States Government. The source is named on its page. More recent studies still under copyright are at most summarised."],
      ["The page decides.", "The texts are read against the page images, not taken from machine text recognition. Spelling and punctuation of the prints are kept; every correction is given in the notes."],
      ["Propaganda is placed in context.", "The Wehrmacht reports and the newspapers of the last weeks of the war are propaganda. They stand here because their claims have to be checked, and every unit carries a note that says what the other sources say. Swastikas and national emblems are not shown in pictures or page excerpts."],
      ["Translations.", "The German and English translations are my own, close to the original and in the public domain (CC0): a reading aid, not a critical translation."],
      ["Contradictions.", "Where the sources differ on strengths, losses or hours, they stand side by side, with who gives which figure. The apparatus does not decide where the sources do not allow it."]
    ],
    printed: "Sources printed here", plates: "Plates"
  }
};

function sources() {
  const M = METHOD[ui];
  view.innerHTML = `
    <span class="tag">${esc(M.tag)}</span><h1>${esc(M.h)}</h1>
    <div class="readable">${M.p.map(([b, p]) => `<p><b>${esc(b)}</b> ${esc(p)}</p>`).join("")}</div>
    ${D.mods.shipped.length ? `<h2>${esc(M.printed)}</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(L(m, "kurz"))}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : ""}
    ${(D.plates.plates || []).length ? `<h2>${esc(M.plates)}</h2><p class="fine readable">${esc(L(D.plates, "credit"))}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>${esc(S("fail"))}${esc(e.message)}</p>`; });
