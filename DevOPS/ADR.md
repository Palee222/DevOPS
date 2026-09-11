## Security Incident Notebook + Password Hygiene Checker

Date: 2026-10-DD

Status: Decided

Context: I have been interested in cybersecurity for a while and I tought this is the right time to start doing something towards that interest. So, I decided something that seems easy, but is very hard for me as there are many things I don't know as I have never done such a project alone. Also, the other reason why I do this project is I have had some security issues and would like to keep it more organized.

Decision: I have chosen a security incident notebook combined with a password hygiene checker which can be used by smaller firms or individuals.

Alternatives considered: at least one real alternative, and why you rejected it

Consequences: 1-2 sentences, what this costs or enables later

Backend language/framework: explain why you chose it and what it buys you. Example: using Django when nothing needs it over Flask/FastAPI is graded down as poor judgment, not banned. the justification from §1b (what it buys you, what you rejected). How you scoped your two feature domains to be independently modularizable.

Whether to add authentication/login.

Any pattern beyond the basics (GraphQL, WebSockets, in-process background task, heavier ORM), as long as it fits the single-process constraint.

Frontend approach: plain HTML/CSS/JS, templates, or heavier, served by the same process.

Dependency count: soft cap ~12 third-party packages.

File count: rough guidance ~15-50 files (excluding lockfiles/venvs/node_modules).

One entry required for each:

A data-model/schema decision in SQLite: e.g. how the two domains' data relates. Should visually match the database diagram in §8.

Your testing approach: what you prioritized toward the 70% bar, what you left thinner, and why.
One thing you deliberately chose not to build, and why.
