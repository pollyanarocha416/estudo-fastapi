from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, db
from config import engine


# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Criar um novo item
@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(db.get_db)):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Obter todos os itens
@app.get("/items/")
def read_items(db: Session = Depends(db.get_db)):
    return db.query(models.Item).all()


# Obter um item específico pelo ID
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(db.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Atualizar um item existente
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


# Excluir um item
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(db.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}
