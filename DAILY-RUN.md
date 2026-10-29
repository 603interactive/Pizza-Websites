# Daily run (8:30 AM ET)

1. Pull the lead notes: clone https://github.com/grahamcunan-eng/Pizza-Leads (each `leads/*.md` is one shop).
2. For every lead without a folder in `sites/`, collect the shop's own content (menu, copy, photos) into `clients/<slug>/data.json` + `img/`.
3. Design a new bespoke site: own template/fonts/layout in `engine/templates`, a `engine/build_<slug>.py`, and ONE major distinct selling point. Never reuse another site's look. No AI-generated food images.
4. Build (`python3 engine/build_<slug>.py`), then QA (`python3 engine/qa2.py <slug>`) at 390px and 1440px.
5. Copy `dist/<slug>/site`, `preview.html` and `LEAD-NOTES.md` into `sites/<slug>/`, commit, push to main.
Each `sites/<slug>/site` is a complete, Netlify-ready website (drag onto app.netlify.com/drop).
