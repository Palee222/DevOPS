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
