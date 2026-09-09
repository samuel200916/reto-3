## 📥 Datos de Entrada

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
| :--- | :--- | :--- | :--- |
| **Presion** | Presión barométrica atmosférica medida por los sensores del cohete | Real | hPa |
| **Aceleracion** | Aceleración vertical experimentada por la nave durante el trayecto | Real | m/s² |
| **Temperatura** | Temperatura registrada por los sensores del cohete | Real | °C |
| **Continuar** | Opción ingresada por el operador para seguir o finalizar la simulación | Texto | S/N |

---

## 📤 Datos de Salida

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
| :--- | :--- | :--- | :--- |
| **Altitud** | Altitud calculada a partir de la presión atmosférica | Real | m |
| **Estado_Vuelo** | Estado actual del cohete (Ascenso, Ascenso por Inercia, Apogeo/Caída Libre o Paracaídas) | Texto | N/A |
| **Alerta_Temperatura** | Indica si la temperatura supera el límite de seguridad | Booleano | N/A |
| **Altitud_Maxima** | Mayor altitud alcanzada durante toda la simulación | Real | m |
| **Promedio_Temperatura** | Temperatura promedio de todas las lecturas registradas | Real | °C |
| **Aceleracion_Maxima** | Mayor aceleración registrada durante el vuelo | Real | m/s² |
| **Apogeo_Detectado** | Indicador que confirma si ya se alcanzó el punto más alto del vuelo | Booleano | N/A |

---

## ⚙️ Operaciones y Fórmulas

| NOMBRE | FÓRMULA / OPERACIÓN | DESCRIPCIÓN |
| :--- | :--- | :--- |
| **Calculo_Altitud** | `44330 * (1 - (Presion / 1013.25)^0.1903)` | Convierte la presión atmosférica en altitud sobre el nivel del mar |
| **Deteccion_Apogeo** | `Altitud_Actual < Altitud_Previa` | Determina cuándo el cohete comienza a descender |
| **Altitud_Maxima** | `Altitud_Actual > Altitud_Maxima` | Actualiza la máxima altitud alcanzada |
| **Promedio_Temperatura** | `Suma_Temperaturas / Contador_Datos` | Calcula la temperatura promedio |
| **Alerta_Temperatura** | `Temperatura >= 80` | Verifica si existe riesgo por alta temperatura |
| **Aceleracion_Maxima** | `Aceleracion > Aceleracion_Maxima` | Actualiza la aceleración máxima registrada |

---

## 🔍 Notas sobre Funciones Utilizadas

| FUNCIÓN | DESCRIPCIÓN |
| :--- | :--- |
| **calcular_altitud(presion_hpa)** | Calcula la altitud a partir de la presión barométrica usando la fórmula indicada en el reto |
| **determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)** | Determina la fase actual del cohete según el comportamiento de la altitud y aceleración |
| **evaluar_alerta_temperatura(temp_celsius)** | Evalúa si la temperatura supera el umbral crítico establecido |
| **main()** | Coordina la ejecución general del programa y el ciclo principal de simulación |

---

## 📋 Variables Principales

| VARIABLE | DEFINICIÓN | TIPO |
| :--- | :--- | :--- |
| **altitud_actual** | Altitud calculada en la iteración actual | float |
| **altitud_previa** | Altitud registrada en la iteración anterior | float |
| **altitud_maxima** | Máxima altitud alcanzada durante la simulación | float |
| **apogeo_detectado** | Bandera para detectar el apogeo una única vez | bool |
| **suma_temperaturas** | Acumulador de temperaturas | float |
| **contador_datos** | Contador de lecturas procesadas | int |
| **aceleracion_maxima** | Mayor aceleración registrada | float |
| **continuar** | Controla la continuación o finalización del ciclo | str |

---
