import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
while True:
    limpiar_pantalla()
    print("Menu")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    opcion = input("Ingrese una opcion:")
    
    input(f"Opcion selecionada: {opcion}..... Presione Enter para continuar")
    
    if opcion == "3":
        break