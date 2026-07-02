carros = []

def crear_carro():
    carro = {
            'placa' : input("Ingrese la placa del vehiculo: "),
            'owner' : input("Ingrese el nombre del dueño: "),
            'color' : input("Ingrese el color del vehiculo: "),
            'modelo' : input("Ingrese el modelo del vehiculo: ")
            }
    
    print("carro creado con exito")
    return carro

def imprimir_carro(lista_carros, dato, i = None):
    
    if type(dato) == int:
        print(f"carro de {lista_carros[dato]["owner"]}")
        print(f"Placa: {lista_carros[dato]["placa"]}")
        print(f"Color: {lista_carros[dato]["color"]}")
        print(f"Modelo: {lista_carros[dato]["modelo"]}")
        
    elif type(dato) == str:
        print(f"carro de {lista_carros[i]["owner"]}")
        print(f"Placa: {lista_carros[i]["placa"]}")
        print(f"Color: {lista_carros[i]["color"]}")
        print(f"Modelo: {lista_carros[i]["modelo"]}")
    
def menu_carros():
    print("========== Menu De Carros ===========")
    print("1. agregar carros")
    print("2. editar carros")
    print("3. buscar carros")
    print("4. mostrar carros")
    print("5. listar carros")
    print("6. eliminar carro")
    print("7. salir")
    
    try:
        opcion = int(input("ingrese una opcion....\n"))
        return opcion
    except:
        print("solo se aceptan numeros")
        return
        
def agregar_carros(lista_carros):
    carro = crear_carro()
    
    for i in lista_carros:
        if i["placa"] == carro["placa"]:
            print(f"El carro con la placa {i["placa"]} ya se encuentra registrado")
            return
        
    lista_carros.append(carro)
    print(f"carro guardado con exito con la placa {carro['placa']}")
        
def editar_carros(lista_carros):
    if not lista_carros:
        print("lo sentimos no hay carros para editar")
        return
    
    num = mostrar_detalles_carros(lista_carros)
    
    atributo = input("Escriba abajo la caracteristica  que desea editar: [placa] [owner] [color] [modelo] \n")
    valor = input("Ingrese el nuevo la nueva caracteristica...\n")
    try:
        lista_carros[num][atributo] = valor
    except:
        print("Error al editar el carro, elija una caracteristica de la lista...")
    
def eliminar_carros(lista_carros):
    if not list:
        print("lo sentimos no hay carros para eliminar")
        return
    
    listar_carros(lista_carros)
    num = int(input("ingrese el numero del carro que desea eliminar... \n"))
    lista_carros.pop(num-1)

def listar_carros(lista_carros):
    if not list:
        print("lo sentimos no hay carros para mostrar")
        return
    
    for index, i in enumerate(lista_carros, start= 1):
        print(f"{index}. {i["placa"]} - {i["modelo"]}")
        
def mostrar_detalles_carros(lista_carros):
    listar_carros(lista_carros)
    try:
        num = int(input("Ingrese el numero del carro al que desea ver detalles... \n"))-1
        imprimir_carro(lista_carros, num)
        return num
    except:
        print("Solo se aceptan numeros, intentelo de nuevo")
        return
 
def buscar_carro_placas(lista_carros):
    placa = input("Ingrese las placas del carro a buscar... \n")
    for indice, i in enumerate(lista_carros, start=0):
        if i["placa"] == placa:
            imprimir_carro(lista_carros, placa, indice)
            return
        print(f"la placa {placa} no se encuentra registrada")
        
while True:
    
    opcion = menu_carros()
    
    match opcion:
        case 1:
            agregar_carros(carros)
        case 2:
            editar_carros(carros)
        case 3:
            buscar_carro_placas(carros)
        case 4:
            mostrar_detalles_carros(carros)
        case 5:
            listar_carros(carros)
        case 6:
            eliminar_carros(carros)
        case 7:
            break
        