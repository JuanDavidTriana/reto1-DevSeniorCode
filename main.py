import datetime

#Lista para almacenar los experimentos
listaDeExperimentos = [
    ["Experimento 1","26/11/2024","Física", [5,6,2,7,8,9]],
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
    if not listaDeExperimentos:
        print("\033[1;33m"+"No existen experimentos registrados"+'\033[0;m')
        return
    print("==== Experimentos ====")
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        print(f"{i}. Nombre: {experimento[0]}, Fecha: {experimento[1]}, Tipo: {experimento[2]}, Resultados: {experimento[3]}")

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
    pass

#Funcion para generar informe
def generar_informe():
    pass

#Funcion para mostrar el menu
def mostar_menu():
    print("==== Menu Principal ====")
    print("========================")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("6. Generar informe")
    print("7. Salir")

#Funcion principal
def main():
    while True:
        print("========================")
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
