"""Generate materials/index.html: links to the ORIGINAL Google Classroom files.
Nothing is re-hosted here; each link opens in Google and needs Margot's school sign-in."""
import html, pathlib

D = lambda i: f"https://docs.google.com/document/d/{i}/edit"
P = lambda i: f"https://docs.google.com/presentation/d/{i}/edit"
F = lambda i: f"https://drive.google.com/file/d/{i}/view"

SUBJECTS = [
  {"cls": "avg", "subj": "Maths", "title": "Averages", "when": "Quiz Tuesday 17 November, 11:15", "icon": "📊",
   "app": "../maths/", "classwork": "https://classroom.google.com/w/ODc3MjE5OTk2Njc5/t/all",
   "groups": [
     ("Notes and worksheets (9–11 Nov)", [
       ("Intro to averages notes", "PDF", F("19-NOutYfTlD5zV3lvOtqKN0R_h9PH57J")),
       ("Sheet 1.1: basic mean, median, mode and range", "PDF", F("104vwlSlatVQrOyO82sEHPq-BcEIc9H5l")),
       ("Sheet 2.1: frequency tables Q1–5", "PDF", F("1c87fIcoCAiJ3ZhHleLl7lV8jNk1v41Ae")),
       ("Grouped frequency tables (notes)", "PDF", F("1JzAa-RQfuGr4J_c7oy4EhdgBBK9vCWLL")),
       ("Homework 2.4: averages from a frequency table", "PDF", F("1Kb7kDKxHYkBPSDPFvJheR8vSlN6wEwTh")),
     ]),
   ]},
  {"cls": "met", "subj": "Geography", "title": "Meteorology", "when": "Test Monday 16 November", "icon": "⛅",
   "app": "../meteorology/", "classwork": "https://classroom.google.com/w/ODc3MTYzNzUzMjA4/t/all",
   "groups": [
     ("Start here", [
       ("Revision task: Home Learning 1 (in the Population Dynamics booklet, weeks 1 and 2)", "Doc", D("1MGu3EtC3UxmsS1GDz9vHcrFheAedNeyjjX06ibz2dcU")),
       ("Meteorology Home Learning Booklet", "Doc", D("18YUvM4QVW61yh7yS0dIDOSF1T4vktUzz_S8JfRrsDw8")),
     ]),
     ("Lesson slides", [
       ("1. Factors Influencing Climate", "Slides", P("12cn5Nr7tVXCyFeAk6_Lxz6S1sKdpJUYDhMTxVImvCMc")),
       ("2. Types of Rainfall", "Slides", P("1HKA8k_pX6b3E2RAUd_mVoalFaTXnKV3HlJtwHIsHCr4")),
       ("3. Air Pressure", "Slides", P("1IJn5oi4thTuPtOjyRWARisr8-nm-JaaFT4sYesbrNGM")),
       ("4. What is a Weather Front?", "Slides", P("1qTjB5IgT4Y0nkCPHqJw4m5_I8sPLs2T6ZJIWZOoGOA0")),
       ("5. Global Atmospheric Circulation", "Slides", P("13bMbqDFclN0u8IAuNVYBn9yV1SWGpN6Lm_bmSqAQZ-0")),
       ("6. Global Climate Zones", "Slides", P("1DUR8mY-mOwvquo6RcSV9iI6Cm4MP6QjXCy6IUxCuku0")),
       ("7. The Climate of the UK", "Slides", P("1Mf91HIDI-jfHZ0e9fzkE_AMp5bhcQtfO26UuWSKvRfY")),
       ("8. Causes of Climate Change: natural causes sheet", "PDF", F("1HhjPsFZ8HlyIhfJ-muLOgnyX3WpxDuyZ")),
     ]),
   ]},
  {"cls": "spa", "subj": "Spanish", "title": "El pretérito · Las vacaciones", "when": "Assessment Tuesday 17 November", "icon": "🧳",
   "app": "../spanish/", "classwork": "https://classroom.google.com/w/ODI2MTQxMTc1NDE0/t/all",
   "groups": [
     ("Start here", [
       ("Revision list: November Progress Assessment", "Word", F("1y5nvZySmt4BIfrFYcwKfWm9eiPf6KX1k")),
       ("Preterite revision slides (13 Nov)", "Slides", P("1QxHzHroEseEnjqbIoVbKAWteq298s5PoUlBRO_ntBzU")),
       ("Revision worksheet: Las vacaciones / preterite", "Doc", D("1Y01a1pjk6d8jRagzTlRUJFhxhkxkLQclyg3FdjZB0YU")),
     ]),
     ("Preterite lessons (Oct–Nov)", [
       ("Lessons 1–3: introducing the preterite", "PowerPoint", F("1XGzwoTsIKNufE8WN2--LBmF00OTOdMov")),
       ("Lesson 4: El pretérito, -ar/-er/-ir activities", "PowerPoint", F("1dRqdONeB_yPb0N-WTXuorjg5GtCUp5R1")),
       ("Lesson 5", "PowerPoint", F("1kZCj6lUKMGeqAw0c---eoIT_CYvprsAe")),
       ("El pretérito: deberes worksheet", "PDF", F("19pjSPfqeutGqVwck0BashDrd4_3OstVW")),
       ("Deberes (2 Nov)", "Slides", P("1sSbnbKjQYAUgNvxdsiNjFu56OoIRZU5zBMrNUBW_e6c")),
       ("Lesson 6: improving our October assessment", "Slides", P("1h3QJ9XLuNhBF8pwKgC0In7j0EEH5aGhf3s-0AwlGhkU")),
       ("Lesson 7", "Slides", P("1-Ore6-PVM9owuYlj_8V-a3gNVKTSKGF7wl7G85Tb52o")),
     ]),
     ("Las vacaciones (Sept) and vocab", [
       ("October assessment revision list + full vocab list", "Doc", D("1OYNAvA_IaUO_oP3VH5EycrFWvGmEOriiG4LBFjwNR9o")),
       ("Lesson 1: ¿Qué haces en tus vacaciones?", "Slides", P("1dd8M7pVzS9lM4qPHbkYoxfeRrr8VhMz3MMUIRmCzfLk")),
       ("Lesson 2", "Slides", P("16qARZS7vsuaUbyZ2jP8rlYmBdXdymXXpX-RLpm0JN5U")),
       ("Lesson 3", "Slides", P("11jjRG8F3x1FfqGQBq2geplZwj0O_f51NI92k71fpmFw")),
       ("Lesson 4", "Slides", P("1BGjb9sPSHhyjio12gLc9B4NfOALOWCuWGSE9ihy0LUw")),
       ("Lesson 6", "Slides", P("1CWfp8xZcM2S5wQXzFUvwM6wAAA1qFHojMyfwlRg7qE8")),
       ("Homework sheet", "Doc", D("1cedsKGeRFH5wQSZzpenAASZWKlV6sRIeDlif-byuY9E")),
       ("Homelearning 1: Las vacaciones", "Doc", D("1mArIr12X0DwAS7FyL_NEV9nArQx-PfJEXoZ-jMyWflU")),
     ]),
     ("Quizlet sets (open without signing in)", [
       ("Y8 Spanish October assessment flashcards", "Quizlet", "https://quizlet.com/gb/1084928200/y8-spanish-october-assessment-flash-cards/"),
       ("¿Qué hiciste? Vacaciones", "Quizlet", "https://quizlet.com/gb/663598946/que-hiciste-vacaciones-flash-cards/"),
       ("Viva 2 Unit 1: ¿Qué hiciste?", "Quizlet", "https://quizlet.com/nz/119369743/viva-2-unit-1-que-hiciste-flash-cards/"),
       ("Question words", "Quizlet", "https://quizlet.com/170227011/spanish-interrogative-words-question-words-flash-cards/"),
     ]),
   ]},
]

e = html.escape
sections = []
for s in SUBJECTS:
    groups = "".join(
        f'<h3>{e(g)}</h3><ul>' + "".join(
            f'<li><a href="{e(u)}" target="_blank" rel="noopener"><span class="name">{e(n)}</span><span class="type t-{e(t.lower())}">{e(t)}</span></a></li>'
            for n, t, u in items) + "</ul>"
        for g, items in s["groups"])
    sections.append(f'''<section class="subject {s["cls"]}">
  <div class="sh"><div class="icon">{s["icon"]}</div><div><div class="subj">{e(s["subj"])}</div><h2>{e(s["title"])}</h2><div class="when">{e(s["when"])}</div></div></div>
  <div class="actions"><a class="btn primary" href="{s["app"]}">Open the revision app →</a><a class="btn" href="{s["classwork"]}" target="_blank" rel="noopener">All classwork in Google Classroom ↗</a></div>
  {groups}
</section>''')

page = (pathlib.Path(__file__).parent / "materials_template.html").read_text().replace("<!--SECTIONS-->", "\n".join(sections))
out = pathlib.Path(__file__).resolve().parent.parent / "materials" / "index.html"
out.write_text(page)
print("wrote", out)
