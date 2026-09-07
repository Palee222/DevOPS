# DevOPS

A strong cybersecurity‑themed app can absolutely fit your assignment constraints — as long as it stays monolithic, uses SQLite, has two clean feature domains, and avoids anything requiring external services or background workers. Below is a set of realistic, shippable, DevOps‑friendly ideas that satisfy the assignment while still being meaningful in cybersecurity.

---

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
