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

Starting up the things:
- Backend:
   - python3 -m venv .venv
   - source .venv/bin/activate
   - python -m pip install -r requirements.txt
   - python app.py
- Frontend
   - cd DevOPS/secnote-frontend
   - npm install
   - npm run dev

Connect the two with the following adress -> http://127.0.0.1:8000
