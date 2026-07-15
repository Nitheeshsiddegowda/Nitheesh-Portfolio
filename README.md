# Your Name — Portfolio (Django)

Same dark portfolio site, rebuilt as a Django project. Every section is its
own small template file, and **all your content lives in one Python file**
so you never have to dig through HTML to update your info.

## Folder structure
```
django_portfolio/
├── manage.py
├── requirements.txt
├── portfolio_project/          ← Django project config (rarely touched)
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── portfolio/                  ← the app — this is where you'll work
│   ├── data.py                  ⭐ EDIT THIS FILE with your real info
│   ├── views.py                 (just passes data.py to the template — no edits needed)
│   ├── urls.py
│   ├── templates/portfolio/
│   │   ├── base.html            (page shell: head, nav, footer, scripts)
│   │   ├── index.html           (stitches the sections together)
│   │   └── partials/
│   │       ├── nav.html
│   │       ├── hero.html
│   │       ├── about.html
│   │       ├── experience.html
│   │       ├── projects.html
│   │       ├── certs.html
│   │       ├── achievements.html
│   │       ├── contact.html
│   │       └── footer.html
│   └── static/portfolio/
│       ├── css/style.css        (theme — colors/fonts are CSS variables at the top)
│       └── js/main.js           (typewriter, scroll reveal, count-up, tilt effect)
└── media/                       ← put your resume.pdf here
```

Each section template is under 60 lines and only handles layout — no content
is hardcoded in them, so you can restyle a section without touching your data,
and update your data without touching HTML.

## 1. Set up a virtual environment and install Django
```bash
cd django_portfolio
python -m venv venv

# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## 2. Run the dev server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** — you should see the portfolio with placeholder data.

## 3. Add your info — the only file you need to edit for content
Open **`portfolio/data.py`**. It's one big `PORTFOLIO` dictionary, grouped
into clearly commented sections:

- `name`, `role_titles`, `location`, `summary` → hero section
- `email`, `phone`, `linkedin_url`, `github_url`, `address` → used in the hero, contact section, and nav icons
- `resume_file` → filename Django looks for inside `/media`
- `stats` → the "At a Glance" numbers (count up automatically on scroll)
- `about_paragraphs`, `skills`, `tools`, `education` → About section
- `experience` → a list of dicts, one per job — add/remove entries freely
- `projects` → a list of dicts, one per project (`featured: True` adds the amber highlight border)
- `certifications` → a list of dicts
- `achievements` → a list of dicts

Add or remove list items to add/remove timeline entries, project cards, etc. —
the templates loop over whatever is in the list, so you don't need to touch
HTML to add a 4th project or a 3rd job.

## 4. Add your resume
Drop your PDF into the `media/` folder using the filename set in
`resume_file` inside `data.py` (default: `resume.pdf`).

## 5. Restyling
- Colors and fonts: `portfolio/static/portfolio/css/style.css`, under the
  `:root { ... }` block at the top.
- Animations (typewriter speed, reveal timing, etc.): `portfolio/static/portfolio/js/main.js`.

## Deploying
This site has no database requirements beyond what Django needs by default.
Before deploying:
1. Set `DEBUG = False` in `portfolio_project/settings.py`.
2. Set a real `SECRET_KEY` (load it from an environment variable, don't hardcode it).
3. Set `ALLOWED_HOSTS` to your real domain.
4. Run `python manage.py collectstatic` and serve `/staticfiles` and `/media`
   through your host, a CDN, or a package like `whitenoise`.

Any host that supports Django (Render, Railway, PythonAnywhere, a VPS, etc.)
will work — this project has no extra dependencies beyond Django itself.
