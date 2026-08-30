ejecutando = True

while ejecutando:
    nombre = input("Ingresa tu nombre: ")
    apellido_paterno = input("Ingresa tu apellido paterno: ")
    apellido_materno = input("Ingresa tu apellido materno: ")

    if nombre == "" or apellido_paterno == "" or apellido_materno == "":
        print("Error: Ningún nombre o apellido puede quedar vacío. Intenta de nuevo.\n")
        continue

    try:
        edad = int(input("Ingresa tu edad: "))
        peso = float(input("Ingresa tu peso en kg: "))
        estatura_cm = float(input("Ingresa tu estatura en centimetros: "))
    except ValueError:
        print("Error: Debes ingresar valores numéricos para edad, peso y estatura. Intenta de nuevo.\n")
        continue

    estatura = estatura_cm / 100

    if edad <= 0 or peso <= 0 or estatura <= 0:
        print("Error: La edad, el peso y la estatura deben ser mayores a 0. Intenta de nuevo.\n")
        continue

    IMC = peso / (estatura ** 2)
    diagnostico = ""

    if IMC < 16.00:
        diagnostico = "Delgadez severa"
    elif IMC < 17.00:
        diagnostico = "Delgadez moderada"
    elif IMC < 18.50:
        diagnostico = "Delgadez leve"
    elif IMC < 25.00:
        diagnostico = "Normal"
    elif IMC < 30.00:
        diagnostico = "Sobrepeso"
    elif IMC < 35.00:
        diagnostico = "Obesidad leve"
    elif IMC < 40.00:
        diagnostico = "Obesidad media"
    else:
        diagnostico = "Obesidad mórbida"

    print("\n--- RESUMEN ---")
    print("Nombre completo:", nombre, apellido_paterno, apellido_materno)
    print("Edad:", edad, "años")
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "m")
    print("IMC:", IMC, "| Diagnóstico:", diagnostico)

    ejecutando = False