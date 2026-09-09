def calcular_altitud(presion_hpa):
    return 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)


def evaluar_alerta_temperatura(temp_celsius):
    return temp_celsius >= 80


def determinar_estado_vuelo(
        altitud_actual,
        altitud_previa,
        aceleracion):

    if altitud_actual > altitud_previa:

        if aceleracion > 0:
            return "Ascenso"
        else:
            return "Ascenso por inercia"

    else:

        if aceleracion < 0:
            return "Apogeo / Caida libre"
        else:
            return "Despliegue de Paracaidas"


def main():

    altitud_previa = 0
    altitud_maxima = 0

    apogeo_detectado = False

    suma_temperaturas = 0
    contador_datos = 0

    aceleracion_maxima = float("-inf")

    continuar = "S"

    while continuar.upper() == "S":

        presion = float(input("Presion (hPa): "))
        aceleracion = float(input("Aceleracion (m/s²): "))
        temperatura = float(input("Temperatura (°C): "))

        altitud_actual = calcular_altitud(presion)

        estado = determinar_estado_vuelo(
            altitud_actual,
            altitud_previa,
            aceleracion
        )

        alerta = evaluar_alerta_temperatura(
            temperatura
        )

        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        if (not apogeo_detectado and
                altitud_actual < altitud_previa):

            apogeo_detectado = True
            print("\n*** APOGEO DETECTADO ***")

        suma_temperaturas += temperatura
        contador_datos += 1

        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        print(f"\nAltitud: {altitud_actual:.2f} m")
        print(f"Estado: {estado}")

        if alerta:
            print("ALERTA: Temperatura critica")

        altitud_previa = altitud_actual

        if altitud_actual <= 0 and contador_datos > 1:
            print("\nEl cohete ha aterrizado.")
            break

        continuar = input(
            "\nContinuar simulacion (S/N): "
        )

    temperatura_promedio = (
        suma_temperaturas / contador_datos
    )

    print("\n===== REPORTE FINAL =====")
    print(f"Altitud maxima: {altitud_maxima:.2f} m")
    print(f"Temperatura promedio: {temperatura_promedio:.2f} °C")
    print(f"Aceleracion maxima: {aceleracion_maxima:.2f} m/s²")


main()
