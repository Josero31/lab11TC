# Laboratorio 11 - Teoría de la Computación

Ejemplos sencillos del solver **Z3** en Python.

## Contenido

- `programa_z3_lab11.py`: programa con tres ejemplos.
- `Reporte_Laboratorio_11_TC.pdf`: reporte del laboratorio.

## Los tres ejemplos

1. **Contradicción**: comprueba que no existe un entero `x` con `x > 5` y `x < 3`.
2. **Validez de una implicación**: comprueba que si `x > 5`, entonces `x > 3`.
3. **Asignación de horarios**: reparte turnos (mañana, tarde, noche) entre Ana, Luis y Marta con unas reglas dadas.

## Cómo ejecutarlo

1. Instalar Python 3.
2. Instalar la librería:

   ```
   pip install z3-solver
   ```

3. Ejecutar el programa:

   ```
   python programa_z3_lab11.py
   ```
