import datetime
from prettytable import PrettyTable

#Lista para almacenar los experimentos
listaDeExperimentos = [
    ["Experimento 1","26/11/2024","Física", [5,6,2,7,8,9]],
    ["Experimento 1","26/11/2024","Física", [5,6,2,7,8,9]]
]

#Funcion para agregar un nuevo experimento
def agregar_experimento():
    
    nombre = input("Ingrese el nombre del experimento: ")
    fecha = input("Ingrese la fecha del experimento: ")
    tipo = input("Ingrese el tipo de expeimento (Quimica, Biologia, Fisica): ")
    
    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y") #Validar la fecha
        resultados = list(map(int, input("Ingrese los resultados numericos separados por comeas: ").split(",")))
        listaDeExperimentos.append([nombre,fecha,tipo,resultados])
        print("\033[1;32m"+"Experimentos agregados con exito"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

#Funcion para eliminar un experimento
def eliminar_experimento():
    visulizar_experimentos()
    
    try:
        indice = int(input("Ingrese el indice del experimento a eliminar: ")) - 1
        if 0 <= indice < len(listaDeExperimentos):
            listaDeExperimentos.pop(indice)
            print("\033[1;32m"+"Experimentos Eliminado con exito"+'\033[0;m')
        else:
            print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

#Funcion para visualizar mis experimentos
def visulizar_experimentos():
    
    tablaExperimentos = PrettyTable()
    
    tablaExperimentos.field_names = ["id", "Nombre", "Fecha", "Tipo","Resultados"]
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        tablaExperimentos.add_row([i, experimento[0], experimento[1], experimento[2],experimento[3]], divider=True)
        
    print(tablaExperimentos)
    
    """
    if not listaDeExperimentos:
        print("\033[1;33m"+"No existen experimentos registrados"+'\033[0;m')
        return
    print("==== Experimentos ====")
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        print(f"{i}. Nombre: {experimento[0]}, Fecha: {experimento[1]}, Tipo: {experimento[2]}, Resultados: {experimento[3]}")
    """

#Funcion para calular estadisticas
def calcular_estadisticas():
    visulizar_experimentos()
    
    try:
        indice = int(input("Ingrese el indice del experimento a calcular estadisticas: ")) - 1
        if 0 <= indice < len(listaDeExperimentos):
            resultados = listaDeExperimentos[indice][3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            print(f"\033[1;32m Estadisticas del experimento: {listaDeExperimentos[indice][0]}"+'\033[0;m')
            print(f"Promedio: {promedio}, Maximo: {maximo}, Minimo: {minimo}")
        else:
            print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

#Funcion de comprar experimentos
def comprar_experimentos():
    visulizar_experimentos()
    
    try: 
        indices = list(map(int, input("Ingrese los indices de los experimentos a comprar separados por comas: ").split(",")))
        comprarciones = []
        for indice in indices:
            if 1 <= indice <= len(listaDeExperimentos):
                resultados = listaDeExperimentos[indice-1][3]
                promedio = sum(resultados) / len(resultados)
                comprarciones.append((listaDeExperimentos[indice-1][0],promedio))
            else:
                print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
        comprarciones.sort(key=lambda x: x[1], reverse=True)
        for nombre, promedio in comprarciones:
            print(f"Experimento: {nombre}, Promedio: {promedio}")
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')
    

#Funcion para generar informe
def generar_informe():
    if not listaDeExperimentos:
        print("\033[1;33m"+"No existen experimentos registrados"+'\033[0;m')
        return
    with open("informe.txt", "w") as archivo:
        archivo.write("==== Informe ====\n")
        archivo.write("=================\n")
        for experimento in listaDeExperimentos:
            resultados = experimento[3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            archivo.write(f"Nombre: {experimento[0]} \n")
            archivo.write(f"Fecha: {experimento[1]}\n")
            archivo.write(f"Tipo: {experimento[2]}\n")
            archivo.write(f"Resultados: {experimento[3]}\n")
            archivo.write(f"Promedio: {promedio}\n")
            archivo.write(f"Maximo: {maximo}\n")
            archivo.write(f"Minimo: {minimo}\n")
            archivo.write("=================\n")
        print("\033[1;32m"+"Informe generado con exito"+'\033[0;m')

#Funcion para mostrar el menu
def mostar_menu():
    
    
    tablaMenu = PrettyTable()
    tablaMenu.align = "l"
    tablaMenu.field_names = ["Menu Principal"]
    tablaMenu.add_row(["1. Agregar experimento"])
    tablaMenu.add_row(["2. Visualizar experimentos"])
    tablaMenu.add_row(["3. Eliminar experimentos"])
    tablaMenu.add_row(["4. Calcular estadisticas"])   
    tablaMenu.add_row(["5. Comparar experimentos"])
    tablaMenu.add_row(["6. Generar informe"])
    tablaMenu.add_row(["7. Salir"])
        
    print(tablaMenu)

    """
    print("===== Menu Principal =====")
    print("==========================")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("6. Generar informe")
    print("7. Salir")
    
    """
    
#Funcion principal
def main():
    while True:

        mostar_menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                agregar_experimento()
            elif opcion == 2:
                visulizar_experimentos()
            elif opcion == 3:
                eliminar_experimento()
            elif opcion == 4:
                calcular_estadisticas()
            elif opcion == 5:
                comprar_experimentos()
            elif opcion == 6:
                generar_informe()
            elif opcion == 7:
                print("Gracias por usar el programa ¡Vuelva pronto!")
                break
        except:
            print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

main()
