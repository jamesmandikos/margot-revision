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
  ("2026-11-30", "", "test", "Biology", "Young Medics test (week of 30 Nov)", "Use the Young Medics learning objectives, lesson worksheets, the Biology Google Site and Educake.", CR + "/a/not-turned-in/all"),
  ("2026-12-01", "14:30", "homework", "Biology", "Test revision homework: Young Medics", "Check your knowledge against the learning objectives.", CR + "/a/not-turned-in/all"),
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

data = {"items": [dict(date=d, time=t, kind=k, subject=s, title=ti, note=n, link=l, colour=COLOURS.get(s, "#5E6E7E"))
                  for d, t, k, s, ti, n, l in ITEMS],
        "missing": [dict(date=d, subject=s, title=ti, colour=COLOURS.get(s, "#5E6E7E")) for d, s, ti in MISSING],
        "updated": UPDATED}

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "tools" / "calendar_template.html").read_text()
(root / "calendar").mkdir(exist_ok=True)
(root / "calendar" / "index.html").write_text(tpl.replace("/*DATA*/", json.dumps(data, ensure_ascii=False)))
print("wrote calendar/index.html with", len(ITEMS), "items,", len(MISSING), "missing")
