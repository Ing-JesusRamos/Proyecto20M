import os
import json

def crear_vehiculo():
    vehiculo = {
            'placa' : input("Ingrese la placa del vehiculo: "),
            'owner' : input("Ingrese el nombre del dueño: "),
            'color' : input("Ingrese el color del vehiculo: "),
            'modelo' : input("Ingrese el modelo del vehiculo: ")
            }
    
    print("vehiculo creado con exito")
    return vehiculo

def imprimir_vehiculo(lista_vehiculos, dato, i = None):
    
    if type(dato) == int:
        print(f"vehiculo de {lista_vehiculos[dato]["owner"]}")
        print(f"Placa: {lista_vehiculos[dato]["placa"]}")
        print(f"Color: {lista_vehiculos[dato]["color"]}")
        print(f"Modelo: {lista_vehiculos[dato]["modelo"]}")
        
    elif type(dato) == str:
        print(f"vehiculo de {lista_vehiculos[i]["owner"]}")
        print(f"Placa: {lista_vehiculos[i]["placa"]}")
        print(f"Color: {lista_vehiculos[i]["color"]}")
        print(f"Modelo: {lista_vehiculos[i]["modelo"]}")
    
def menu_vehiculos():
    print("========== Menu De vehiculos ===========")
    print("1. agregar vehiculos")
    print("2. editar vehiculos")
    print("3. buscar vehiculos")
    print("4. mostrar vehiculos")
    print("5. listar vehiculos")
    print("6. eliminar vehiculo")
    print("7. salir")
    
    try:
        opcion = int(input("ingrese una opcion....\n"))
        return opcion
    except Exception:
        print("solo se aceptan numeros")
        return
        
def agregar_vehiculos(lista_vehiculos):
    vehiculo = crear_vehiculo()
    
    for i in lista_vehiculos:
        if i["placa"] == vehiculo["placa"]:
            print(f"El vehiculo con la placa {i["placa"]} ya se encuentra registrado")
            return
        
    lista_vehiculos.append(vehiculo)
    print(f"vehiculo guardado con exito con la placa {vehiculo['placa']}")
        
def editar_vehiculos(lista_vehiculos):
    if not lista_vehiculos:
        print("lo sentimos no hay vehiculos para editar")
        return
    
    num = mostrar_detalles_vehiculos(lista_vehiculos)
    
    atributo = input("Escriba abajo la caracteristica  que desea editar: [placa] [owner] [color] [modelo] \n")
    valor = input("Ingrese el nuevo la nueva caracteristica...\n")
    try:
        lista_vehiculos[num][atributo] = valor
    except Exception:
        print("Error al editar el vehiculo, elija una caracteristica de la lista...")
    
def eliminar_vehiculos(lista_vehiculos):
    if not lista_vehiculos:
        print("lo sentimos no hay vehiculos para eliminar")
        return
    
    listar_vehiculos(lista_vehiculos)
    num = int(input("ingrese el numero del vehiculo que desea eliminar... \n"))
    lista_vehiculos.pop(num-1)

def listar_vehiculos(lista_vehiculos):
    if not lista_vehiculos:
        print("lo sentimos no hay vehiculos para mostrar")
        return
    
    for index, i in enumerate(lista_vehiculos, start= 1):
        print(f"{index}. {i["placa"]} - {i["modelo"]}")
        
def mostrar_detalles_vehiculos(lista_vehiculos):
    listar_vehiculos(lista_vehiculos)
    try:
        num = int(input("Ingrese el numero del vehiculo al que desea ver detalles... \n"))-1
        imprimir_vehiculo(lista_vehiculos, num)
        return num
    except Exception:
        print("Solo se aceptan numeros, intentelo de nuevo")
        return
 
def buscar_vehiculo_placas(lista_vehiculos):
    placa = input("Ingrese las placas del vehiculo a buscar... \n")
    for indice, i in enumerate(lista_vehiculos, start=0):
        if i["placa"] == placa:
            imprimir_vehiculo(lista_vehiculos, placa, indice)
            return
    print(f"la placa {placa} no se encuentra registrada")

def loadJSON(archivo):
    with open(archivo, "r") as bd:
        vehiculos = json.load(bd)
    return vehiculos

def saveJSON(archivo, vehiculos):
    with open(archivo, "w") as bd:
        json.dump(vehiculos, bd, indent= 4)
        
archivo = "Vehiculos.json"

if os.path.exists(archivo):
   vehiculos = loadJSON(archivo)
else:
    vehiculos = []

while True:
    
    opcion = menu_vehiculos()
    
    match opcion:
        case 1:
            agregar_vehiculos(vehiculos)
            saveJSON(archivo, vehiculos)
        case 2:
            editar_vehiculos(vehiculos)
            saveJSON(archivo, vehiculos)
        case 3:
            buscar_vehiculo_placas(vehiculos)
        case 4:
            mostrar_detalles_vehiculos(vehiculos)
        case 5:
            listar_vehiculos(vehiculos)
        case 6:
            eliminar_vehiculos(vehiculos)
            saveJSON(archivo, vehiculos)
        case 7:
            break
        