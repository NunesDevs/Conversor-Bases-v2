def conversao(valor, opt):
    if opt == 16 or 20:
        lista1 = list(valor)           
        lista2 = []
        for i in lista1:
            if opt == 16 or 20:
                if i == 'A' or i == 'a':
                    i = 10
                if i == 'B' or i == 'b':
                    i = 11
                if i == 'C' or i == 'c':
                    i = 12
                if i == 'D' or i == 'd':
                    i = 13
                if i == 'E' or i == 'e':
                    i = 14
                if i == 'F' or i == 'f':
                    i = 15
            if opt == 20:
                if i == 'G' or i == 'g':
                    i = 16
                if i == 'H' or i == 'h':
                    i = 17
                if i == 'I' or i == 'i':
                    i = 18
                if i == 'J' or i == 'j':
                    i = 19
            lista2.append(i)    
        values = []
        for i in lista2:
            i = int(i)
            values.append(i) 
        n = len(values) -1
        values.reverse()
        decimal = 0
        index = 0
        while n >= 0:
            for item in values:
                decimal = decimal + (item * (opt ** index))
                n -= 1
                index += 1
            print('Resultado da conversão: ', decimal)  
    else:    
        n = len(str(valor))
        memory = valor
        decimal = 0
        index = 0 
        while n >= 0:
            resto = memory % 10
            decimal = decimal + (resto * (opt ** index))
            n -= 1
            index += 1
            memory = memory // 10
        print('Resultado da conversão: ', decimal)

def _menu():
    global menu
    global opt
    print('Escolha a base que queira converte para decimal')
    menu = int(input(
    """
    1 - Binário
    2 - Octal
    3 - Hexadecimal
    4 - Vigésimal
    Opção: """))
    if menu == 1:
        opt = 2
    elif menu == 2:
        opt = 8
    elif menu == 3:
        opt = 16
    elif menu == 4:
        opt = 20
    return opt

while True:
    _menu() 
    if menu == 3 or 4:
        valor = input("Valor para converter: ")
   
    elif menu == 1 or 2:
        valor = int(input("Valor para converter: "))
    
    conversao(valor,opt)
    
    retorno = input("Deseja realizar outra conversão? [S/N] ")
    
    if retorno == 'S' or retorno == 's':
        print('Retornando')
        opt = 0
    elif retorno == 'N' or retorno == 'n':     
        print('Encerrando...')
        break