from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, field_validator
from models import db
import tasks

# make a web server
app = FastAPI()

# validate the text
class Translation(BaseModel):
    text : str
    @field_validator('text')
    @classmethod
    def validator(cls, text):
        if text is None or text.strip() == "":
            raise ValueError("Text cannot be empty!")
        return text

# Route 1: \
# root node to check everything is fine
# returns {"message" : "Hello World"}
@app.get("/")
def get_root():
    return {"message" : "Hello World"}

# Route 2: /translation
# store a translation and run in background tasks
# returns a translation_id
@app.post("/translation")
def post_translation(t: Translation, background_tasks: BackgroundTasks):
    if db.is_closed():
        db.connect()
    task_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, task_id)
    return {"task_id" : task_id}


# Route 3: /results
# takes in a translation_id 
# returns the final translation
@app.get("/results")
def get_translation(task_id: int):
    return {"translation" : tasks.find_translation(task_id)}