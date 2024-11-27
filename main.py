import datetime

#Lista para almacenar los experimentos
listaDeExperimentos = [
    ["Experimento 1","26/11/2024","Física", [5,6,2,7,8,9]],
]

#Funcion para agregar un nuevo experimento
def agregar_experimento():
    pass

#Funcion para eliminar un experimento
def eliminar_experimento():
    pass

#Funcion para visualizar mis experimentos
def visulizar_experimentos():
    pass

#Funcion para calular estadisticas
def calcular_estadisticas():
    pass

#Funcion de comprar experimentos
def comprar_experimentos():
    pass

#Funcion para generar informe
def generar_informe():
    pass

#Funcion para mostrar el menu
def mostar_menu():
    print("==== Menu Principal ====")
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
            print("Error: Entrada no valida. intenta de nuevo")

main()
