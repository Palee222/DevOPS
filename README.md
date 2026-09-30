## Short description

This project is about a security incident notebook combined with a password hygene checker for stakeholders like a small company who needs a lightweight, local tool to track incidents and promote better password practices.

Description of my domains
    * Incidendt notebook
        * Users can create separate incident logs into a database
    * Password checker
        * When users create a password, this domain checks wether that password is more or less good enough security
app.py                  ← entry point

db.py                   ← SQLite connection + schema

incidents/

    repository.py       ← SQL for incidents

    routes.py           ← /incidents endpoints

    service.py          ← allowed severity/status values

password/

    repository.py       ← weak-password list + rules

    routes.py           ← /password endpoints

    service.py          ← scoring algorithm

src/templates/

    base.html

    password/check.html

    password/rules.html

src/static/

To run pytests use the following command:./.venv/bin/python -m pytest \
  --cov=incidents.service \
  --cov=src.password.service \
  --cov-report=term-missing

  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
  python app.py

To run frontend locally: bun install (or npm install) and bun run dev. Point it at your FastAPI backend from the Connection page.
