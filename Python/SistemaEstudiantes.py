def crear_estudiante():
    try:
        estudiante = {
                "nombre" : input("Ingrese el nombre del estudiante: \n") ,
                "apellido": input("Ingrese el apellido del estudiante: \n"),
                "edad": int(input("Ingrese la edad del estudiante (numeros): \n")),
                "carrera": input("Ingrese la carrera del estudiante: \n")     
            } 
        
        return estudiante
    except:
        print("No se pudo crear el estudiante, en edad solo se aceptan numeros enteros")
        return

def agregar_estudante(list_estudiantes):
    
    estudiante = crear_estudiante()
    
    for i in list_estudiantes:
        if (i['nombre'] == estudiante['nombre']):
            print(f"el estudiante {estudiante["nombre"]} ya fue agregado anteriormente")
            return
                
    list_estudiantes.append(estudiante)
    print(f"estudiante {estudiante["nombre"]} ingresado con exito!!!")

def listar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes para mostrar...")
        return
    
    for indice, i in enumerate(lista_estudiantes, start= 1):
        print(f"{indice}.{i["nombre"]} {i["apellido"]}")

def imprimir_estudiante(lista_estudiantes, dato, i = None):
    
    if type(dato) == str:
        print(f"nombre: {lista_estudiantes[i]["nombre"]}")
        print(f"apellido: {lista_estudiantes[i]["apellido"]}")
        print(f"edad: {lista_estudiantes[i]["edad"]}")
        print(f"carrera: {lista_estudiantes[i]["carrera"]}")
        
    elif type(dato) == int:
        print(f"nombre: {lista_estudiantes[dato]["nombre"]}")
        print(f"apellido: {lista_estudiantes[dato]["apellido"]}")
        print(f"edad: {lista_estudiantes[dato]["edad"]}")
        print(f"carrera: {lista_estudiantes[dato]["carrera"]}") 
        
def eliminar_estudiantes(lista_estudiantes):
    listar_estudiantes(estudiantes)
    try:
        eliminar = int(input("ingrese el numero del estudiante que desea eliminar:\n"))
        lista_estudiantes.pop(eliminar-1)
    except:
        print("Por favor ingrese solo los numeros que ve en la lista")
        return
    
def buscar_estudiante(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes para buscar...")
        return
    
    nombre = input("ingrese el nombre del estudiante a buscar:\n")
    for indice, i in enumerate(lista_estudiantes, start=0):
        if (nombre == i["nombre"]):
           imprimir_estudiante(lista_estudiantes, nombre, indice)
        return
        
    print("no existe el estudiante")

def editar_estudiante(lista_estudiantes):
    listar_estudiantes(lista_estudiantes)
    try:
        num = int(input("ingrese el numero del estudiante que desea editar"))-1
        imprimir_estudiante(lista_estudiantes, num)
    except:
        print("Ingrese solo los numeros de la lista porfavor")
        
    clave = input("Ingrese el atributo a editar: [nombre] [apellido] [edad] [carrera]\n")
    valor = input("Digite el nuevo atributo:\n")
    
    try:
        lista_estudiantes[num][clave] = valor
    except:
        print("Por favor elija un atributo de la lista y recuerde que la edad solo permite numeros")
        return

def menu_estudiantes():
    print("\n==== SISTEMA DE ESTUDIANTES ====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Buscar estudiante")
    print("5. Editar estudiantes")
    print("6. salir")

estudiantes = []

while True:
    
    menu_estudiantes()
    
    try:
        opcion = int(input("Seleccione una opcion: \n"))
    except:
        print("Elija un numero del menu >:(")
    
    match opcion:
        case 1:
            agregar_estudante(estudiantes)
        case 2:
            listar_estudiantes(estudiantes)
        case 3:
            eliminar_estudiantes(estudiantes)
        case 4:
            buscar_estudiante(estudiantes)
        case 5:
            editar_estudiante(estudiantes)
        case 6:
            break

            
            
    
    

    


          
   
                