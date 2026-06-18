from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Habit(BaseModel):
    id: int
    name: str
    completed: bool = False

habits = []

@app.post('/habits/', response_model=Habit)
def create_habit(habit: Habit):
    habits.append(habit)
    return habit

@app.get('/habits/')
def read_habits():
    return habits

@app.put('/habits/{habit_id}', response_model=Habit)
def update_habit(habit_id: int, habit: Habit):
    for index, h in enumerate(habits):
        if h.id == habit_id:
            habits[index] = habit
            return habit
    raise HTTPException(status_code=404, detail='Habit not found')

@app.delete('/habits/{habit_id}')
def delete_habit(habit_id: int):
    global habits
    habits = [h for h in habits if h.id != habit_id]
    return {'detail': 'Habit removed'}

@app.get('/api/test')
def test_endpoint():
    return {'message': 'Success'}