def calculate_payroll(hours_worked):
    """
    Calcula la nómina semanal de un empleado según las horas trabajadas.

    Parámetros:
    - hours_worked (int): Número de horas trabajadas en la semana. Debe estar entre 0 y 64.

    Retorna:
    - int: El total a pagar en pesos según el esquema de tarifas.

    Excepciones:
    - ValueError: Si el número de horas trabajadas está fuera del rango permitido (0 a 64).
    """

    # Validación de entrada: verifica que las horas estén en el rango permitido.
    if hours_worked < 0 or hours_worked > 64:
        raise ValueError("Número de horas no válido. Debe estar entre 0 y 64.")

    # Tarifas definidas en pesos por hora
    normal_rate = 200         # Tarifa por hora para las primeras 40 horas
    overtime_rate = 400       # Tarifa doble por hora para las horas de 41 a 56
    triple_rate = 600         # Tarifa triple por hora para las horas de 57 a 64

    # Caso 1: Horas trabajadas entre 0 y 40
    # - Si el total de horas trabajadas es 40 o menos, se aplica solo la tarifa normal.
    if hours_worked <= 40:
        return hours_worked * normal_rate

    # Caso 2: Horas trabajadas entre 41 y 56
    # - Las primeras 40 horas se pagan a tarifa normal.
    # - Las horas entre 41 y 56 se pagan al doble.
    elif hours_worked <= 56:
        normal_hours = 40
        overtime_hours = hours_worked - normal_hours
        return (normal_hours * normal_rate) + (overtime_hours * overtime_rate)

    # Caso 3: Horas trabajadas entre 57 y 64
    # - Las primeras 40 horas se pagan a tarifa normal.
    # - Las siguientes 16 horas (de 41 a 56) se pagan al doble.
    # - Las horas restantes (de 57 a 64) se pagan al triple.
    else:
        normal_hours = 40
        overtime_hours = 16
        triple_hours = hours_worked - normal_hours - overtime_hours
        return (normal_hours * normal_rate) + (overtime_hours * overtime_rate) + (triple_hours * triple_rate)
