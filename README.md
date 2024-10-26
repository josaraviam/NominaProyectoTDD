# Proyecto: Cálculo de Nómina Semanal utilizando TDD

Este proyecto implementa un programa en Python para calcular la nómina semanal de empleados, aplicando el enfoque de **Desarrollo Guiado por Pruebas (TDD)**. El proyecto incluye tanto el código para el cálculo de la nómina como pruebas unitarias que validan el correcto funcionamiento del programa.

## Descripción del Problema

El cálculo de la nómina se basa en la cantidad de horas trabajadas por semana, con diferentes tarifas aplicadas dependiendo del número de horas:
- **0 a 40 horas**: se aplica una tarifa normal de $200 por hora.
- **41 a 56 horas**: las primeras 40 horas se pagan a la tarifa normal y las horas adicionales se pagan al doble ($400 por hora).
- **57 a 64 horas**: las primeras 40 horas se pagan a la tarifa normal, las siguientes 16 horas al doble, y el resto (hasta un máximo de 8 horas) al triple ($600 por hora).

Si se ingresan horas fuera del rango de 0 a 64, el programa arroja un error, indicando que el número de horas es inválido.

## Criterios de Aceptación

El programa debe:
1. Calcular correctamente el pago total según las horas trabajadas y las tarifas aplicadas.
2. Validar que el número de horas esté en el rango de 0 a 64. Cualquier valor fuera de este rango debe generar un mensaje de error.
3. Proveer pruebas unitarias que cubran todos los casos posibles (horas normales, horas extras, horas triples, y entradas fuera del rango válido).

## Enfoque TDD

El desarrollo de este programa siguió el ciclo de TDD:
1. **Escritura de Pruebas**: Se escribieron pruebas unitarias para cada caso posible, incluyendo valores en los límites de cada rango.
2. **Implementación de Código**: Después de cada prueba, se implementó la funcionalidad mínima necesaria para que la prueba pasara.
3. **Refactorización**: Una vez que todas las pruebas pasaron, el código se revisó para asegurar claridad, eficiencia y cumplimiento de los requisitos.

## Ejemplos de Uso

Estos son algunos ejemplos de cómo se calcula el pago semanal según las horas trabajadas:

- **30 horas trabajadas**: `(30 * $200) = $6000`
- **50 horas trabajadas**: `(40 * $200) + (10 * $400) = $12000`
- **64 horas trabajadas**: `(40 * $200) + (16 * $400) + (8 * $600) = $19200`