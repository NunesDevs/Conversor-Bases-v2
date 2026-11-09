"""Conversão posicional para decimal com validação de cada dígito."""
DIGITS = "0123456789ABCDEFGHIJ"
BASES = (2, 4, 8, 16, 20)
MENU = {"1": 2, "2": 8, "3": 16, "4": 20}


def to_decimal(value, base):
    if isinstance(base, bool) or not isinstance(base, int) or base not in BASES:
        raise ValueError("Base não suportada")
    if not isinstance(value, str):
        raise TypeError("Informe os dígitos como texto")
    text = value.strip().upper()
    sign = -1 if text.startswith("-") else 1
    if text.startswith(("-", "+")):
        text = text[1:]
    if not text:
        raise ValueError("Informe ao menos um dígito")
    result = 0
    for digit in text:
        position = DIGITS.find(digit)
        if position < 0 or position >= base:
            raise ValueError(f"Dígito inválido para base {base}: {digit}")
        result = result * base + position
    return sign * result


def conversao(valor, opt):
    result = to_decimal(valor, opt)
    print("Resultado da conversão:", result)
    return result


def main():
    while True:
        try:
            option = input("Base de origem: 1-Binário 2-Octal 3-Hexadecimal 4-Vigesimal: ").strip()
            if option not in MENU:
                print("Opção inválida.")
                continue
            value = input("Valor para converter: ")
            conversao(value, MENU[option])
        except ValueError as error:
            print(error)
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando...")
            return
        try:
            again = input("Deseja realizar outra conversão? [S/N]: ").strip().casefold()
        except (EOFError, KeyboardInterrupt):
            again = "n"
        if again != "s":
            print("Encerrando...")
            return


if __name__ == "__main__":
    main()
