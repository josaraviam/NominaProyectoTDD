import pytest
from src.payroll import calculate_payroll


# Prueba para horas fuera del rango permitido (menos de 0 horas).
# Se espera que la función arroje un ValueError cuando las horas son menores a 0.
def test_invalid_hours_below_0():
    with pytest.raises(ValueError, match="Número de horas no válido."):
        calculate_payroll(-1)


# Prueba para horas fuera del rango permitido (más de 64 horas).
# Se espera que la función arroje un ValueError cuando las horas son mayores a 64.
def test_invalid_hours_above_64():
    with pytest.raises(ValueError, match="Número de horas no válido."):
        calculate_payroll(65)


# Prueba para el caso de 0 horas trabajadas.
# Si no se trabajaron horas, el resultado debe ser 0 (0 horas trabajadas * $200).
def test_zero_hours():
    assert calculate_payroll(0) == 0


# Prueba para el caso de hasta 40 horas trabajadas (tarifa normal).
# Si se trabajaron exactamente 40 horas, se deben pagar a la tarifa normal ($200).
# El resultado esperado es 8000 (40 horas * $200).
def test_normal_hours_40():
    assert calculate_payroll(40) == 8000  # 40 horas * $200


# Prueba para el caso de 50 horas trabajadas (tarifa normal + tarifa doble).
# Si se trabajaron 50 horas, las primeras 40 se pagan a tarifa normal y las siguientes 10 a tarifa doble.
# El resultado esperado es 40*200 + 10*400 = 12000.
def test_overtime_hours_50():
    # 40 horas normales + 10 horas extra dobles
    assert calculate_payroll(50) == (40 * 200) + (10 * 400)


# Prueba para el caso de 56 horas trabajadas (tarifa normal + tarifa doble).
# Si se trabajaron 56 horas, las primeras 40 se pagan a tarifa normal y las siguientes 16 a tarifa doble.
# El resultado esperado es 40*200 + 16*400 = 14400.
def test_overtime_hours_56():
    # 40 horas normales + 16 horas extra dobles
    assert calculate_payroll(56) == (40 * 200) + (16 * 400)


# Prueba para el caso de 64 horas trabajadas (tarifa normal + doble + triple).
# Si se trabajaron 64 horas, las primeras 40 se pagan a tarifa normal, las siguientes 16 a tarifa doble,
# y las últimas 8 a tarifa triple. El resultado esperado es 40*200 + 16*400 + 8*600 = 19200.
def test_triple_overtime_hours_64():
    # 40 horas normales + 16 horas dobles + 8 horas triples
    assert calculate_payroll(64) == (40 * 200) + (16 * 400) + (8 * 600)
