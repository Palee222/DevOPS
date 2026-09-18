## Short description

This project is about a security incident notebook combined with a password hygene checker for stakeholders like a small company who needs a lightweight, local tool to track incidents and promote better password practices.

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
