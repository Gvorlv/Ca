from fastapi import FastAPI

from pydantic import BaseModel

# аннотации типов
# класс с типами данных параметров 
class Item(BaseModel):
    num: int
    num2: int

# создаем объект приложения
app = FastAPI()

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница с описанием проекта"}

# функция-обработчик с параметрами пути
@app.get("/users/{id}/{id2}")
def users(id:int, id2:int):
    c=id+id2
    return {"plus": c}

# функция-обработчик post запроса с параметрами
@app.post("/add")
def get_model(item:Item):
    a=item.num
    b=item.num2
    c=a+b
    return {"summa":c}
    #return {"nuhhm": item.num, "num2": item.num2}

@app.post("/subtract")
def get_model(item:Item):
    a=item.num
    b=item.num2
    c=a-b
    return {"subtract":c}

@app.post("/multiply")
def get_model(item:Item):
    a=item.num
    b=item.num2
    c=a*b
    return {"multiply":c}

@app.post("/divide")
def get_model(item:Item):
    a=item.num
    b=item.num2
    c=a/b
    return {"divide":c}