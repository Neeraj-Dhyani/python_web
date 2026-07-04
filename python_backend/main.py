from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dataBase import engine, sessionLocal
from models import Todo, Base
from schema import TodoCtreate

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()  

@app.get('/')
def home():
    return {'message':"hello from server"}


@app.post('/add_todo')
def create_todo(todo:TodoCtreate, db:Session= Depends(get_db)):
    try:
        newtodo = Todo(title=todo.title)
        db.add(newtodo)
        db.commit()
        db.refresh(newtodo)
        return {'stetus_code':200,'message':'todo add successfully'}

    except Exception as error:
        return{'status_code':500, 'message':error}    
   

@app.get('/all_todo')
def get_todos(db:Session=Depends(get_db)):
    try:
        todos = db.query(Todo).all()
        return {"status_code":200, "data":todos}
    except Exception as error:
        return{'status_code':500, 'message':error}
    

    
@app.put('/complete/{todo_id}')
def complete_todo(todo_id:int, db:Session=Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
             raise HTTPException(
                status_code_code=404,
                detail="Todo not found"
            )
        db.query(Todo).filter(Todo.id == todo.id).update({"complete":True})
        db.commit()
        db.refresh(todo)
        return {'status_code':200, 'data':todo}
    except Exception as error:
        return {'status_code':500, 'message':error}
    


@app.get('/get_todo_by_id/{todo_id}')
def get_todo_by_id(todo_id:int, db:Session=Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id==todo_id).first()
        if not todo:
            raise HTTPException(
                status_code_code=404,
                detail="Todo not found"
            )
        return {'status_code':200, 'todo':todo}
    except Exception as error:
        return{'status_code':500, 'message':error}

@app.put('/update_todo/{todo_id}')
def modify_todo(todo_id:int, text:str,db:Session=Depends(get_db) ):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo: 
            raise HTTPException(
                status_code_code=404,
                detail="Todo not found"
            )
        
        db.query(Todo).filter(Todo.id == todo.id).update({"title":text})
        db.commit()
        return {'status_code_code':200, "message":f"your todo successfully updated {todo}"}
    except Exception as error:
        return{'status_code':500, 'message':error}


@app.delete("/delete_todo/{todo_id}")
def remove_todo(todo_id:int, db:Session=Depends(get_db)):
    try:
        todo_data = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo_id:
            raise HTTPException(
                status_code_code=404,
                detail="Todo not found"
            )
        db.delete(todo_data)
        db.commit()
        return {"status_code":200, "data":'Todo Deleted Successfully!'}

    except Exception as error:
        return{'status_code':500, 'message':error}

