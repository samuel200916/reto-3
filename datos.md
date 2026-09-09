# Sistema de Monitoreo de Vuelo para un Cohete Suborbital

## 📥 Datos de Entrada

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
|---------|------------|---------|---------|
| Presion | Presión atmosférica medida por el sensor | float | hPa |
| Aceleracion | Aceleración vertical del cohete | float | m/s² |
| Temperatura | Temperatura registrada por el sistema | float | °C |

---

## 📤 Datos de Salida

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
|---------|------------|---------|---------|
| Altitud | Altitud calculada mediante la fórmula barométrica | float | m |
| Estado_Vuelo | Fase actual del vuelo | str | Texto |
| Alerta_Temperatura | Indica si existe temperatura crítica | bool | Verdadero/Falso |
| Altitud_Maxima | Máxima altitud alcanzada | float | m |
| Promedio_Temperatura | Promedio de temperaturas registradas | float | °C |

---

## ⚙️ Operaciones y Fórmulas

### Cálculo de Altitud

```text
h = 44330 * (1 - (P / 1013.25)^0.1903)
```

Donde:

- h = Altitud
- P = Presión atmosférica

### Detección de Apogeo

```text
altitud_actual < altitud_previa
```

### Promedio de Temperatura

```text
promedio = suma_temperaturas / contador_datos
```

---

## 🔄 Funciones

### calcular_altitud(presion_hpa)

Calcula la altitud usando la fórmula barométrica.

### determinar_estado_vuelo()

Determina si el cohete se encuentra en:

- Ascenso
- Ascenso por inercia
- Apogeo / Caída libre
- Despliegue de paracaídas

### evaluar_alerta_temperatura()

Retorna verdadero cuando la temperatura supera el límite establecido.

---

## 🚩 Variables de Control

| Variable | Tipo | Función |
|-----------|-------|----------|
| altitud_previa | float | Guarda la altitud anterior |
| altitud_maxima | float | Guarda la máxima altitud |
| apogeo_detectado | bool | Indica si ya se detectó el apogeo |
| suma_temperaturas | float | Acumulador |
| contador_datos | int | Contador de lecturas |

INICIO

    Inicializar variables

    altitud_previa <- 0
    altitud_maxima <- 0
    apogeo_detectado <- FALSO

    suma_temperaturas <- 0
    contador_datos <- 0

    aceleracion_maxima <- 0

    continuar <- "S"

    MIENTRAS continuar = "S"

        Leer presion
        Leer aceleracion
        Leer temperatura

        Calcular altitud

        Determinar estado del vuelo

        Evaluar alerta de temperatura

        SI altitud_actual > altitud_maxima ENTONCES

            altitud_maxima <- altitud_actual

        FIN SI

        SI altitud_actual < altitud_previa Y
           apogeo_detectado = FALSO ENTONCES

            apogeo_detectado <- VERDADERO

            Mostrar "APOGEO DETECTADO"

        FIN SI

        Acumular temperatura

        Actualizar contador

        SI aceleracion > aceleracion_maxima ENTONCES

            aceleracion_maxima <- aceleracion

        FIN SI

        Mostrar resultados

        altitud_previa <- altitud_actual

        SI altitud_actual <= 0 ENTONCES

             Salir del ciclo

        FIN SI

        Leer continuar

    FIN MIENTRAS

    temperatura_promedio <-
    suma_temperaturas / contador_datos

    Mostrar altitud_maxima

    Mostrar temperatura_promedio

    Mostrar aceleracion_maxima

FIN
