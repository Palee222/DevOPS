#small fastapi web server
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

BASE_DIR = Path(__file__).resolve().parent
PORT = int(os.getenv("PORT", "8000"))

app = FastAPI() #creates the web application
#FastAPI is a Python framework that handles HTTP requests and responses.
#This tells FastAPI where your HTML files live:
templates = Jinja2Templates(directory=str(BASE_DIR / "src" / "templates"))

#Static files are mounted, This line makes /static serve files from a folder:
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "src" / "static")), name="static")


#The route is defined using the @app.get("/") decorator, which means that this function will be called when a GET request is made to the root URL ("/") of the application.
@app.get("/") #tells FastAPI: “when someone visits the root URL /, run this function”
def home(request: Request): #request contains the browser request information
    return templates.TemplateResponse( #TemplateResponse loads the HTML template file base.html
        request=request,
        name="base.html",
        context={"request": request}, #the browser gets the rendered HTML page back
    )
'''
So when you open: http://localhost:8001/ the function runs and returns the HTML page.
'''


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT) #This line starts the server:

'''
source /Users/Laura/venvs/myapp/bin/activate
cd /Users/Laura
python3 /Users/Laura/Desktop/app.py
'''

'''
This is the request flow:

1. Browser requests http://localhost:8001/
2. FastAPI route / matches
3. home() function runs
4. It loads base.html
5. The HTML is returned to the browser
6. Browser renders it and shows:
Hello from FastAPI
'''