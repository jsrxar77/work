---
tags:
  - meeting
---

# Test Help

- Están divididos en lo que se esta probando: UAT, Marilyn y Mark. @diego
- Preocupación de nivel de profundidad de lo que se esta probando, desconocimiento de lo que se esta haciendo como testing. @diego
- Diego y Gonzalo ven que a veces no se hace un test completo de integración. Las precondiciones de datos no están definidas. @diego
- Diego no tiene el overview de como se esta probando. @diego
- El input de los módulos en un caso no fue bueno porque hubo un error. Pero a partir de eso hay controles adicionales. No correr los módulos y que la base esta completamente mal. @marilyn
- No hay una forma de mejorar los datos de entrada. @marilyn
- Sección en confluence de QA con todos los test cases. @marilyn
- Slavik esta pasando test cases a júpiter notebooks. @marilyn
- El concern de Gonzalo es que había inconsistencias en los valores de plata alocado en 2 ambientes: Dev y Test. Entonces Martin comenzó a preguntar y era que los valores de General Ledger eran distintos. @gonzalo
- Mark mete mano y lo hace en un ambiente y no en otro. @marilyn
- Preocupación de que los valores están bien antes de probar el modulo. @diego
- Marilyn considera que el concern de Diego es valido para plantear. @marilyn
- Testing no tiene el nivel de profundidad que requiere para pasar UAT porque se encontraron errores que son básicos. @diego

La solución: es validar tablas de input en ambos ambientes.