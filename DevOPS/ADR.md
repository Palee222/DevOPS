## Security Incident Notebook + Password Hygiene Checker
1. Initial ideas
Date: 2026-09-21

Status: Decided

Context: For this assignment I need two separable domains to work with. Which will be an incident logbook and a password hygiene checker so companies/individuals can keep track of their security. Also, both both support security management while addressing different needs.

I have been interested in cybersecurity for a while and I tought this is the right time to start doing something towards that interest. So, I decided something that seems easy, but is very hard for me as there are many things I don't know as I have never done such a project alone. Also, the other reason why I do this project is I have had some security issues and would like to keep it more organized.

Decision: I have chosen a security incident notebook combined with a password hygiene checker which can be used by smaller firms or individuals since this will be light weight. The incident logbook allows users to record, track, and review security incidents, while the password hygiene checker evaluates password quality without storing the passwords themselves.

Alternatives considered: I have considered making this in one domain, however I wanted to make sure that the two functions are clearly separable and won't be any conflicts or unnecessary dependencies when the application is running.

Consequences: This 2 domain solution enables that the domains can run smoothly without any serious conflicts. The application will not replace a full enterprise security platform as it is intended as a lightweight tool for individuals and small organisations.

Backend language/framework: explain why you chose it and what it buys you. Example: using Django when nothing needs it over Flask/FastAPI is graded down as poor judgment, not banned. the justification from §1b (what it buys you, what you rejected). How you scoped your two feature domains to be independently modularizable.
  * So I have chosen to code my project in python as for me who is not a proficient coder, this language makes everything a bit easier.
  * In addition I have decided to choose FastAPI as it is light weight and perfect for smaller companies.

Whether to add authentication/login. -> No authentication or login added yet. That will be added in the next phase if needed.

Any pattern beyond the basics (GraphQL, WebSockets, in-process background task, heavier ORM), as long as it fits the single-process constraint. -> None of these

Frontend approach: plain HTML/CSS/JS, templates, or heavier, served by the same process. -> I have used HTML, Javascript and CSS. I have kept it simple and easy to do as my focus is not frontend for this project.

2. Incident log
Date: 2026-09-23
Status: Decided
Context:
* I have decided on an SQLite based incident log because it can be easily handled and data can be easily retrieved if needed for further actions.
Decision:
* I have chosen to handle different severity levels.
Alternatives considered:
* I would have chosen to make the database with Django and SQL but since it was not recommended in the assignment I did not go with it.
* Also, I like to learn about new methods. :)
Consequences: 1-2 sentences, what this costs or enables later
* It enables expansion for later.

Backend language/framework choice: the justification from §1b (what it buys you, what you rejected).
* I have just simply used FastAPI, SQLite and python.
* I have chosen this as I explained earlier I decided on using this framework because it is light weight and can be easly ran on a computer or smaller server
A data-model/schema decision in SQLite: e.g. how the two domains' data relates. Should visually match the database diagram in §8.
* So the model I made for the incident log is
One thing you deliberately chose not to build, and why.
* An overly complex database and code because my goal is to make sure that with my very low level of knowledge I can build something that lives up to the assignment and I can understand it too
without using 100% AI to write my assignment.
* So I wanted to make sure that I actually learn from this assignment.

3. Password hygiene setup
Date: 2026-09-25
Status: Decided
Context: I had to decide on how to set up the password hygiene checker. How to create a database and the rules to make a decent code for the assignment
Decision: 1-2 sentences, what you chose
Alternatives considered: at least one real alternative, and why you rejected it
Consequences: 1-2 sentences, what this costs or enables later

Backend language/framework choice: the justification from §1b (what it buys you, what you rejected).
A data-model/schema decision in SQLite: e.g. how the two domains' data relates. Should visually match the database diagram in §8.
Your testing approach: what you prioritized toward the 70% bar, what you left thinner, and why.
One thing you deliberately chose not to build, and why.

4. Frontend design
Date: 2026-09-27
Status: Decided
Context: 1-3 sentences, what forced this decision
Decision: 1-2 sentences, what you chose
Alternatives considered: at least one real alternative, and why you rejected it
Consequences: 1-2 sentences, what this costs or enables later

Backend language/framework choice: the justification from §1b (what it buys you, what you rejected).
A data-model/schema decision in SQLite: e.g. how the two domains' data relates. Should visually match the database diagram in §8.
Your testing approach: what you prioritized toward the 70% bar, what you left thinner, and why.
One thing you deliberately chose not to build, and why.

5. Report writing content
Date: 2026-10-01
Status: Decided
Context: What was already in other documentation and what can I write to report
Decision: I chose to include everything and put AI disclaimers first.
Alternatives considered: None
