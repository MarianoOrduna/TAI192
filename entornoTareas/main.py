from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title = 'Mi PrimerAPI 192',
    description = 'Mariano',
    version = '1.0.1'
)

tareas=[
    {"id": 1,
    "Titulo": "Estudiar para el examen",
    "Descripcion": "Repasar los apuntes de TAI",
    "Vencimiento":"14-02-25",
    "Estado":"Completada"},

    {"id": 2,
    "Titulo": "Practica fastAPI",
    "Descripcion": "Hacer el reporte de fastAPI",
    "Vencimiento":"28-02-25",
    "Estado":"Pendiente"},

    {"id": 3,
    "Titulo": "Exposicion de redes",
    "Descripcion": "Realizar una presentacion acerca de como se crearon las redes",
    "Vencimiento":"30-03-25",
    "Estado":"Pendiente"},

    {"id": 4,
    "Titulo": "Investigacion fastAPI",
    "Descripcion": 'Realizar una investigacion acerca de fastAPI',
    "Vencimiento":"5-02-25",
    "Estado":"No realizada"}
]

#Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

#End point consultar tareas
@app.get("/consultarTareas", tags=['Operaciones CRUD'])
def leerTareas():
    return{'Las tareas son':tareas}

#end point para ver una tarea por su id
@app.get('/tarea/{id}', tags=['Operaciones CRUD'])
def consultarTarea(id:int):
    return{'Tarea':id}

#Crear una nueva tarea
@app.post('/tarea/',tags=['operaciones CRUD'])
def agregarTarea(tarea:dict):
    for usr in tareas:
        if usr ['id']== tarea.get("id"):
            raise HTTPException(status_code=400, detail='ID ya existente')
    tareas.append(tarea)   
    return tarea

#Endpoint para actualizar una tarea existente
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,tareaActualizada:dict):
    for index, usr in enumerate(tareas):
        if usr['id'] == id:
            tareas[index].update(tareaActualizada)
            return tareas[index]
    raise HTTPException(status_code=400, detail='La tarea no existe')


