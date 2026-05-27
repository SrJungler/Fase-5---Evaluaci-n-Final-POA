# Nombre Dayan de Jesus Wilches Lozano
# Grupo     : 213022_142
# Programa  : Ingeniería de Sistemas
# Fundamentos de Programación - Código: 213022A_2201
# Fase 5 - Evaluación Final POA: Control de Horas Semanales del Equipo

# Matriz: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo = [
    ["Carlos Ramírez",  9, 8, 10, 9, 8],
    ["Laura Gómez",     7, 8,  7, 6, 7],
    ["Pedro Herrera",  10, 9, 10, 8, 9],
    ["Ana Martínez",    8, 8,  8, 8, 8]
]

UMBRAL_HORAS = 40

def calcular_jornada(recurso):
    total_horas = 0
    for dia in range(1, 6):
        total_horas = total_horas + recurso[dia]

    if total_horas > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion

print("=" * 55)
print("   INFORME DE HORAS SEMANALES DEL EQUIPO")
print("=" * 55)
print(f"{'Nombre':<20} {'Total Horas':>12} {'Clasificación':>18}")
print("-" * 55)

for recurso in equipo:
    nombre = recurso[0]
    total, clasificacion = calcular_jornada(recurso)
    print(f"{nombre:<20} {total:>12} horas  {clasificacion:>15}")

print("=" * 55)
print(f"  Umbral de horas estándar: {UMBRAL_HORAS} horas/semana")
print("=" * 55)
