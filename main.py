from src.payroll import calculate_payroll


def main():
    try:
        hours_worked = int(input("Ingrese las horas trabajadas en la semana: "))
        payroll = calculate_payroll(hours_worked)
        print(f"El total a pagar es: ${payroll}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
