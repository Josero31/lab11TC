"""Ejemplos sencillos para el Laboratorio 11 de Teoria de la Computacion.

Antes de ejecutarlo, instalar la libreria con:
    pip install z3-solver

Luego ejecutar:
    python programa_z3_lab11.py
"""

from z3 import Distinct, Implies, Int, Not, Solver, sat, unsat


def ejemplo_contradiccion():
    print("EJEMPLO 1: CONTRADICCION")
    x = Int("x")
    solver = Solver()
    solver.add(x > 5)
    solver.add(x < 3)

    resultado = solver.check()
    print("Restricciones: x > 5 y x < 3")
    print("Resultado:", resultado)
    if resultado == unsat:
        print("Conclusion: no existe un entero que cumpla las dos condiciones.")
    print()


def ejemplo_validez():
    print("EJEMPLO 2: COMPROBAR UNA IMPLICACION")
    x = Int("x")
    solver = Solver()

    # Para probar que una expresion es valida, Z3 busca un contraejemplo.
    # Si la negacion es insatisfacible, la expresion original es valida.
    propiedad = Implies(x > 5, x > 3)
    solver.add(Not(propiedad))

    resultado = solver.check()
    print("Propiedad: si x > 5, entonces x > 3")
    print("Resultado de buscar un contraejemplo:", resultado)
    if resultado == unsat:
        print("Conclusion: no hay contraejemplo, por lo tanto la propiedad es valida.")
    print()


def ejemplo_horarios():
    print("EJEMPLO 3: ASIGNACION DE HORARIOS")
    print("Turnos: 0 = manana, 1 = tarde, 2 = noche")

    ana = Int("turno_ana")
    luis = Int("turno_luis")
    marta = Int("turno_marta")

    solver = Solver()

    # Cada persona recibe un turno valido.
    for turno in (ana, luis, marta):
        solver.add(turno >= 0, turno <= 2)

    # No se repiten turnos.
    solver.add(Distinct(ana, luis, marta))

    # Restricciones particulares.
    solver.add(ana != 2)   # Ana no puede trabajar de noche.
    solver.add(luis != 0)  # Luis no puede trabajar por la manana.

    resultado = solver.check()
    print("Resultado:", resultado)

    if resultado == sat:
        modelo = solver.model()
        nombres = {0: "manana", 1: "tarde", 2: "noche"}
        print("Ana:", nombres[modelo[ana].as_long()])
        print("Luis:", nombres[modelo[luis].as_long()])
        print("Marta:", nombres[modelo[marta].as_long()])
        print("Conclusion: Z3 encontro una asignacion que cumple todas las reglas.")
    else:
        print("No existe una asignacion que cumpla todas las reglas.")
    print()


if __name__ == "__main__":
    ejemplo_contradiccion()
    ejemplo_validez()
    ejemplo_horarios()

