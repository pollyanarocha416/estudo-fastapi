from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, db
from config import engine
from datetime import date

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(db.get_db)):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/")
def read_items(db: Session = Depends(db.get_db)):
    return db.query(models.Item).all()


@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(db.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{item_id}")
def update_item(
    item_id: int, name: str, description: str, db: Session = Depends(db.get_db)
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = name
    db_item.description = description
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(db.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}

@app.get("/clientes/{nome_cliente}")
def get_cliente(nome_cliente:str, db:Session = Depends(db.get_db)):
    db_cliente = db.query(models.Item).filter(models.Item.name == nome_cliente).all()
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return db_cliente


#######################################
@app.post("/alunos/{nome}/{idade}/{periodo}")
def create_aluno(nome: str, idade: int, periodo:str, db: Session = Depends(db.get_db)):
    db_aluno = models.Alunos(nome=nome, idade=idade, periodo=periodo)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno
