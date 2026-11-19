"""Generate calendar/index.html: upcoming tests and homework from Google Classroom.

ITEMS is a snapshot taken from Margot's Classroom to-do list. Re-run after updating ITEMS.
The page hides anything already past, so it stays tidy between refreshes.
"""
import json, pathlib, datetime

UPDATED = "Saturday 14 November 2026"
CR = "https://classroom.google.com"

ITEMS = [
  # date, time, kind (test|homework|form), subject, title, note, link
  ("2026-11-16", "", "test", "Geography", "Meteorology test", "Revise with the Weather Station app.", "../meteorology/"),
  ("2026-11-16", "", "homework", "Geography", "Home Learning 1: Meteorology test revision", "Weeks 1–2 of the Population Dynamics booklet: rate the 10 topics, then answer questions on the weakest.", "../materials/"),
  ("2026-11-16", "10:45", "form", "Eco Committee", "Extra Curricular and Eco Form", "", CR + "/a/not-turned-in/all"),
  ("2026-11-17", "11:15", "test", "Maths", "Averages quiz", "Mean, median, mode, range, frequency and grouped tables.", "../maths/"),
  ("2026-11-17", "", "test", "Spanish", "November Assessment: el pretérito", "Preterite endings, fui/fue, a/en/con, listening, grammar, writing about holidays.", "../spanish/"),
  ("2026-11-17", "", "form", "RAISE Club", "Snow Ball: baking sign-up", "", CR + "/a/not-turned-in/all"),
  ("2026-12-04", "", "test", "Biology", "Young Medics test (postponed to Fri 4 Dec)", "Use the Young Medics learning objectives, lesson worksheets, the Biology Google Site and Educake.", CR + "/a/not-turned-in/all"),
]

# Not marked as done in Classroom (may well be done on paper)
MISSING = [
  ("2026-11-13", "Spanish", "Homelearning: revision worksheet (Las vacaciones / preterite)"),
  ("2026-11-12", "Maths", "HW: frequency tables Q1–4"),
  ("2026-11-12", "Maths", "Frequency tables sheet 2.1"),
  ("2026-11-12", "Entrepreneur Club", "Week 4: create your own fireworks display"),
  ("2026-11-11", "Mandarin", "Home learning: telling the time vocab test"),
  ("2026-11-05", "Maths", "HW: forming and solving equations sheet 3.5"),
  ("2026-11-03", "Spanish", "Deberes"),
]

COLOURS = {"Geography": "#3A86C8", "Maths": "#3D348B", "Spanish": "#A13D24", "Biology": "#B0337C",
           "Eco Committee": "#2E9E6B", "RAISE Club": "#C98F12", "Mandarin": "#D64545", "Entrepreneur Club": "#5E6E7E"}

# ── Nightly merge (19 Nov 2026) ───────────────────────────────────────────
# Scheduled/run_todo_check.sh runs ~/.local/state/classroom-check/classroom_digest.py, which
# writes classroom.json (to-do and missing, read from Margot's Classroom). Merge it in so the
# page stays current without hand edits. The curated ITEMS above win on duplicates.
import re
AUTO = pathlib.Path.home() / ".local/state/classroom-check/classroom.json"
SUBJECTS = [(r"8Ma|Mathematic", "Maths"), (r"Spanish", "Spanish"), (r"Geograph", "Geography"), (r"Biolog|-Bi\b", "Biology"),
            (r"-Ph\b|Physics", "Physics"), (r"-Ch\b|Chemistry", "Chemistry"), (r"English", "English"), (r"-Hs\b|History", "History"),
            (r"-Lt\b|Latin", "Latin"), (r"-Mn|Mandarin", "Mandarin"), (r"-Dr\b|Drama", "Drama"), (r"-Mu\b|Music", "Music"),
            (r"-Ar\b|Art\b", "Art"), (r"Design", "Design"), (r"CompSci|Computer", "Computing"), (r"-Ps\b|PSHE", "PSHE"),
            (r"-Rp\b|Religion", "Religion & Philosophy"), (r"Reg-", "Form"), (r"RAIS", "RAISE Club"), (r"Eco Committee", "Eco Committee"),
            (r"Choir", "Choir"), (r"Wind Band", "Wind Band"), (r"Orchestra", "Orchestra"), (r"Entrepreneur", "Entrepreneur Club")]
ACADEMIC = {"Maths", "Spanish", "Geography", "Biology", "Physics", "Chemistry", "English", "History", "Latin", "Mandarin",
            "Drama", "Music", "Art", "Design", "Computing", "PSHE", "Religion & Philosophy"}
def subject_of(cls):
    for pat, name in SUBJECTS:
        if re.search(pat, cls, re.I):
            return name
    return cls or "Classroom"
def kind_of(title, subj):
    if re.search(r"\b(quiz|test|assessment|exam)\b", title, re.I) and not re.search(r"vocab test.*home|test - homework|test analysis", title, re.I):
        return "test"
    if subj not in ACADEMIC or re.search(r"sign[ -]?up|form\b", title, re.I):
        return "form"
    return "homework"
if AUTO.exists():
    auto = json.loads(AUTO.read_text())
    have = {(d, s, k) for d, t, k, s, ti, n, l in ITEMS}
    have_titles = {ti.lower() for d, t, k, s, ti, n, l in ITEMS}
    for a in auto.get("todo", []):
        subj = subject_of(a.get("class", ""))
        kind = kind_of(a["title"], subj)
        if not a.get("due") or (a["due"], subj, kind) in have or a["title"].lower() in have_titles:
            continue
        note = re.sub(r"\s+", " ", a.get("notes", "")).strip()
        ITEMS.append((a["due"], a.get("time", ""), kind, subj, a["title"], (note[:160] + "…") if len(note) > 160 else note, a.get("url", CR)))
    if "missing" in auto:
        MISSING = [(m["due"], subject_of(m.get("class", "")), m["title"]) for m in auto["missing"]
                   if kind_of(m["title"], subject_of(m.get("class", ""))) != "test"]
    UPDATED = datetime.date.fromisoformat(auto["updated"]).strftime("%A %-d %B %Y")
    for subj in {s for d, t, k, s, ti, n, l in ITEMS} | {s for d, s, ti in MISSING}:
        COLOURS.setdefault(subj, "#5E6E7E")

data = {"items": [dict(date=d, time=t, kind=k, subject=s, title=ti, note=n, link=l, colour=COLOURS.get(s, "#5E6E7E"))
                  for d, t, k, s, ti, n, l in ITEMS],
        "missing": [dict(date=d, subject=s, title=ti, colour=COLOURS.get(s, "#5E6E7E")) for d, s, ti in MISSING],
        "updated": UPDATED}

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "tools" / "calendar_template.html").read_text()
(root / "calendar").mkdir(exist_ok=True)
(root / "calendar" / "index.html").write_text(tpl.replace("/*DATA*/", json.dumps(data, ensure_ascii=False)))
print("wrote calendar/index.html with", len(ITEMS), "items,", len(MISSING), "missing")
