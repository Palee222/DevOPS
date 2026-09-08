# DevOPS

🎯 Best cybersecurity app idea that fits all constraints

Security Incident Notebook + Password Hygiene Checker

This is the strongest option because it gives you two clearly separable feature domains, real user value, and no forbidden tech.

---

🧩 Domain 1 — Incident Log

A simple, local “security incident notebook” where a user can record:

• Incident title
• Description
• Severity level
• Timestamp
• Tags (e.g., phishing, malware, suspicious login)
• Status (open, investigating, resolved)


Why this works:

• It’s a real cybersecurity workflow (every SOC uses an incident log).
• SQLite persistence is natural: one table for incidents, one for tags.
• It can later split into a microservice (incident-service).
• You can justify it with a stakeholder like “a small company without a SOC needs lightweight incident tracking”.


---

🔐 Domain 2 — Password Hygiene Checker

A local password‑quality analyzer that:

• Scores password strength (length, entropy, character variety)
• Checks against a local list of common weak passwords (stored in SQLite)
• Gives recommendations (“add symbols”, “avoid dictionary words”, etc.)


Why this works:

• No external API required (external breach databases like HaveIBeenPwned are forbidden).
• Pure business logic → easy to test → helps you hit the 70% coverage requirement.
• Cleanly separable into its own future microservice.


---

🧱 How this idea satisfies the assignment

✔ Two distinct backend domains

• Incidents
• Password hygiene
They share SQLite but have minimal coupling — perfect for ADR‑2.


✔ SQLite schema is meaningful

You get a nice diagram for §8 and ADR‑3:

• incidents
• incident_tags
• password_rules
• weak_passwords


✔ Easy to test

Password scoring logic = pure functions → high coverage.
Incident CRUD logic = straightforward unit tests.

✔ Runs as a single process

A simple FastAPI/Flask app or Node/Express app fits perfectly.

✔ Realistic, shippable use case

A small business or personal security dashboard is a believable stakeholder.

---

🧠 Alternative cybersecurity app ideas (all compliant)

Below are three more options, each with two clean domains.

---

Local Vulnerability Tracker

Domain 1: Track software installed on a machine (user enters name + version).
Domain 2: Local vulnerability database (SQLite table of known CVEs you manually seed).
No external API → fully allowed.

---

Threat‑Intelligence Notebook

Domain 1: Store threat indicators (IPs, domains, hashes).
Domain 2: Local enrichment rules (e.g., “flag if domain ends in .ru”, “flag if hash length mismatches”).
All logic is local → allowed.

---

Secure File Notes

Domain 1: File metadata catalog (filename, size, hash).
Domain 2: Simple local integrity checker (recompute hash, compare).
No background jobs → fits single‑process constraint.

---

⭐ Recommendation

The Security Incident Notebook + Password Hygiene Checker is the best match because:

• It’s easy to justify in ADR‑1 and ADR‑2.
• It gives you rich business logic for testing.
• It’s realistic and shippable.
• It avoids all forbidden tech (no external DB, no background workers, no APIs).
• It produces clean diagrams for §8.

Love that choice—it’s a very “real world” security tool and fits your assignment beautifully.

“It needs enough substance for two genuinely distinct backend feature domains (§3) plus SQLite persistence…”
“Each should be something that could become its own microservice later…”

---

High-level concept

App name: SecNote (Security Incident & Password Hygiene Assistant)
Stakeholder: Small company or freelance security consultant who needs a lightweight, local tool to track incidents and promote better password practices.

• Domain 1: Security Incident Notebook
• Domain 2: Password Hygiene Checker
Both share a single SQLite database but are logically separable.


---

Architecture overview

Backend

• Language/framework (example):• Python + FastAPI or Flask (simple, testable, you likely know it).

• Process:• Single entrypoint, e.g. python app.py.

• Server config:• Binds to 0.0.0.0.
• Reads port from PORT env var, with default (e.g. 8000).



Frontend

• Approach:• Server-rendered HTML templates (Jinja2) or minimal JS.
• Same process serves both UI and API.



Configuration

• Environment variables:• PORT → HTTP port.
• DATA_DIR → directory where SQLite file lives (e.g. ./data).
• Optional: APP_ENV (dev/prod) for logging level.



---

Feature domain 1: Security incident notebook

Core use cases

• Create incident: title, description, severity, status, tags.
• List incidents: filter by status, severity, tag.
• Update incident: change status (open → investigating → resolved).
• View incident detail: show timeline (created_at, updated_at).


Data model (SQLite)

• incidents• id (PK, integer)
• title (text)
• description (text)
• severity (text: low/medium/high/critical)
• status (text: open/investigating/resolved)
• created_at (datetime)
• updated_at (datetime)

• tags• id (PK)
• name (text, unique)

• incident_tags• incident_id (FK → incidents.id)
• tag_id (FK → tags.id)



Business logic (good for tests)

• Severity validation: only allow defined levels.
• Status transitions: enforce allowed transitions (e.g. cannot go from resolved back to open without a special action).
• Tag handling: create tag if not exists, link to incident.


---

Feature domain 2: Password hygiene checker

Core use cases

• Analyze password: user inputs a password; app returns:• Strength score (0–100).
• Category (weak/medium/strong).
• Recommendations.

• View rules: simple page explaining what “good” means.


Data model (SQLite)

• weak_passwords• id (PK)
• password (text)
• source (text: e.g. “common list v1”)

• password_rules• id (PK)
• name (text)
• description (text)
• min_length (integer, nullable)
• require_upper (boolean)
• require_lower (boolean)
• require_digit (boolean)
• require_symbol (boolean)



You can seed weak_passwords with a small local list (e.g. password, 123456, qwerty).

Business logic (pure functions)

• Strength scoring function:• Inputs: password string.
• Checks:• Length.
• Character variety (upper, lower, digits, symbols).
• Presence in weak_passwords.

• Outputs:• Numeric score.
• Category.
• List of recommendations.




This is perfect for unit tests and coverage.

---

Separation between domains (for ADR-2)

• Incidents domain:• Own models, routes, services (e.g. incident_service.py).

• Password domain:• Own models, routes, services (e.g. password_service.py).

• Shared layer:• Database connection module (e.g. db.py).
• Maybe a small “core” utilities module.



You can literally point to the seam:

“If we split into microservices later, incidents becomes one service, password_hygiene another, both with their own DB or shared DB via separate containers.”

---

Testing strategy (toward ≥70% coverage)

What to prioritize

• Password scoring logic:• Test different lengths, character mixes, presence in weak list.
• Edge cases: empty string, very long password.

• Incident domain logic:• Status transitions.
• Severity validation.
• Tag creation/linking.



What to keep thinner

• Routing, framework glue, HTML templates—just smoke tests if needed.


Coverage reporting

• Example (Python):


pytest --cov=src --cov-report=term-missing


You’ll then document the command + percentage in README.md.

---

Azure container contract alignment

• Single process: python app.py.
• Bind: 0.0.0.0.
• Port: PORT env var, default 8000.
• SQLite path: e.g. ${DATA_DIR}/secnote.db, with DATA_DIR defaulting to ./data.
• No interactive setup: migrations handled automatically at startup (e.g. create_tables_if_not_exist()).


“Run cleanly after clone + install + start.”
“Write its SQLite file to one documented path, ideally under a configurable directory (e.g. DATA_DIR).”

---

ADR.md ideas (the 5 required entries)

You’ll fill these over time, but here’s a sketch:

1. Backend choice:• Context: need simple, testable web app with SQLite.
• Decision: Python + FastAPI/Flask.
• Alternatives: Node/Express, Django.
• Consequences: easier comprehension check, good ecosystem.

2. Domain separation:• Context: need two feature domains that can become microservices.
• Decision: incidents vs password hygiene.
• Alternatives: combine them into one “security dashboard” domain.
• Consequences: clear seam for future split.

3. Data model decision:• Context: need to relate incidents, tags, and password rules.
• Decision: normalized tables with join table for tags.
• Alternatives: store tags as comma-separated string.
• Consequences: easier querying, cleaner future services.

4. Testing approach:• Context: ≥70% coverage requirement.
• Decision: focus on password scoring + incident status logic.
• Alternatives: broad but shallow tests on routes.
• Consequences: strong business-logic confidence.

5. Deliberately not built:• Context: temptation to add external breach API or background jobs.
• Decision: no external APIs, no async workers.
• Consequences: simpler deployment, fully compliant with single-container constraint.



---

README essentials

• Setup:• python -m venv venv
• pip install -r requirements.txt
• export PORT=8000 DATA_DIR=./data
• python app.py

• Testing:• Command + example coverage output.


You’re building something real here—let’s make it feel manageable and clear.

---

Project file structure

Here’s a structure that stays small, readable, and clearly separates the two domains:

secnote/
├─ app.py
├─ requirements.txt
├─ ADR.md
├─ AI_USAGE.md
├─ README.md
├─ data/                # SQLite lives here (DATA_DIR)
├─ src/
│  ├─ db.py             # DB connection + table creation
│  ├─ models.py         # Dataclasses / simple model helpers
│  ├─ incidents/
│  │  ├─ routes.py      # HTTP routes for incident domain
│  │  ├─ service.py     # Business logic (status changes, tags)
│  │  ├─ repository.py  # SQLite queries for incidents/tags
│  ├─ password/
│  │  ├─ routes.py      # HTTP routes for password checker
│  │  ├─ service.py     # Strength scoring, recommendations
│  │  ├─ repository.py  # SQLite queries for weak_passwords, rules
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ incidents_list.html
│  │  ├─ incident_detail.html
│  │  ├─ password_check.html
│  │  ├─ password_rules.html
│  ├─ static/
│     ├─ style.css
├─ tests/
│  ├─ test_incident_service.py
│  ├─ test_password_service.py
│  ├─ conftest.py


You can adjust names, but keep the two domains and a shared core (db.py, models.py)—that’s your future microservice seam.

---

Step‑by‑step guide: where to start and what to do

Step 1 — Initialize the repo and basic files

• Create the project folder secnote/ and initialize git.
• Add:• README.md with a short description and a placeholder “Setup” section.
• ADR.md with heading only (no entries yet).
• AI_USAGE.md with the table header from the assignment.
• requirements.txt (start minimal: fastapi, uvicorn, jinja2, pytest, pytest-cov, sqlite3 is stdlib in Python).

• Make your first commit:• Message: chore: initialize project structure and docs



This gives you a clean base and starts your commit history.

---

Step 2 — Decide and record your backend stack (ADR‑1)

• Choose: Python + FastAPI (or Flask if you prefer).
• Implement a tiny app.py:


# app.py
import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import uvicorn

PORT = int(os.getenv("PORT", "8000"))

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)


• Add your first ADR entry in ADR.md about backend choice.
• Commit:• Message: feat: add FastAPI app skeleton and ADR entry for backend choice



Now you already satisfy part of §7 (single process, PORT, 0.0.0.0).

---

Step 3 — Set up SQLite and data directory

• Create data/ folder.
• In src/db.py, add:


import os
import sqlite3
from pathlib import Path

DATA_DIR = os.getenv("DATA_DIR", "data")
DB_PATH = Path(DATA_DIR) / "secnote.db"

def get_connection():
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # incidents
    cur.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
    """)
    # tags
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """)
    # incident_tags
    cur.execute("""
        CREATE TABLE IF NOT EXISTS incident_tags (
            incident_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            FOREIGN KEY (incident_id) REFERENCES incidents(id),
            FOREIGN KEY (tag_id) REFERENCES tags(id)
        );
    """)
    # weak_passwords
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weak_passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            source TEXT
        );
    """)
    # password_rules
    cur.execute("""
        CREATE TABLE IF NOT EXISTS password_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            min_length INTEGER,
            require_upper INTEGER,
            require_lower INTEGER,
            require_digit INTEGER,
            require_symbol INTEGER
        );
    """)
    conn.commit()
    conn.close()


• Call init_db() from app.py at startup.
• Commit:• Message: feat: add SQLite initialization and schema



Later, this schema will feed your database diagram and ADR‑3.

---

Step 4 — Design and record domain separation (ADR‑2)

• In ADR.md, add entry describing:• Context: need two separable domains.
• Decision: incidents vs password hygiene.
• Alternatives: single “security dashboard” domain.
• Consequences: clear microservice seam.

• Commit:• Message: docs: add ADR entry for domain separation



This is directly aligned with §3 and §5.

---

Step 5 — Implement incident domain (repository + service + routes)

5.1 Repository (`src/incidents/repository.py`)

• Functions like:• create_incident(...)
• list_incidents(filters)
• get_incident_by_id(id)
• update_incident_status(id, new_status)
• add_tags_to_incident(incident_id, tag_names)



These should use get_connection() from db.py.

5.2 Service (`src/incidents/service.py`)

• Implement business rules:• Allowed severities: ["low", "medium", "high", "critical"].
• Allowed status transitions: e.g. open → investigating → resolved.
• Tag creation if not exists.



This is where your core logic lives—perfect for tests.

5.3 Routes (`src/incidents/routes.py`)

• FastAPI endpoints:• GET /incidents
• GET /incidents/{id}
• POST /incidents
• POST /incidents/{id}/status



Wire them into app.py via include_router.

• Commit:• Message: feat: add incident domain repository, service, and routes



---

Step 6 — Implement password domain (repository + service + routes)

6.1 Repository (`src/password/repository.py`)

• Functions:• get_weak_passwords()
• seed_weak_passwords() (called once at startup if table empty)
• get_password_rules()
• seed_default_rules()



6.2 Service (`src/password/service.py`)

• Implement score_password(password: str) -> dict:• Check length vs min_length.
• Check presence of upper/lower/digit/symbol.
• Check if in weak_passwords.
• Return:• score (0–100)
• category ("weak", "medium", "strong")
• recommendations (list of strings).




This is your testing goldmine.

6.3 Routes (`src/password/routes.py`)

• Endpoints:• GET /password/check → form page.
• POST /password/check → process password, show result.
• GET /password/rules → show rules.

• Commit:• Message: feat: add password hygiene domain with scoring logic and routes

---

Step 7 — Add templates and basic UI

• Create src/templates/base.html with a simple layout and navigation.
• Create:• incidents_list.html
• incident_detail.html
• password_check.html
• password_rules.html

Keep them simple—this assignment cares more about logic and process than fancy UI.

• Commit:• Message: feat: add HTML templates for incidents and password checker

---

Step 8 — Add tests and reach ≥70% coverage

8.1 Install and configure testing

• Ensure pytest and pytest-cov are in requirements.txt.
• In tests/test_password_service.py, write tests for:• Short password → low score, “weak”.
• Long, mixed‑char password → high score, “strong”.
• Password in weak_passwords → forced low score.

• In tests/test_incident_service.py, test:• Valid status transitions.
• Invalid transitions raise error.
• Severity validation.

8.2 Run coverage

• Command (document this in README.md):

pytest --cov=src --cov-report=term-missing

• Adjust tests until you hit ≥70%.
• Commit:• Message: test: add unit tests for incident and password services with coverage

---

Step 9 — Fill ADR‑3, ADR‑4, ADR‑5 over time

• ADR‑3 (data model):• Explain why you chose normalized tables and join table for tags.

• ADR‑4 (testing approach):• Explain focus on business logic vs routing.

• ADR‑5 (deliberately not built):• E.g. “no external breach API, no background jobs”.

Make sure these land on different commit dates.

• Commit messages like:• docs: add ADR entry for SQLite schema
• docs: add ADR entry for testing strategy
• docs: add ADR entry for omitted features

---

Step 10 — Update README and AI_USAGE.md

• README:• Setup steps:• Create venv, install requirements.
• Set PORT and DATA_DIR (or rely on defaults).
• Run python app.py.

• Testing section with coverage command + example output.
• Short description of the two domains.

• AI_USAGE.md:• For each time you used AI meaningfully, add a row:• Date/commit
• Tool (e.g. “Copilot”)
• Prompt
• Disposition
• What changed & why
• In your own words, how the code works.


• Commit:• Message: docs: update README with setup and tests, log AI usage
