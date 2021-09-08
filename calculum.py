print('Calculadora Simples')

operac = input('\nAdição \tSubtração \tMultiplicação \tDivisão'
      '\n\nEscolha uma operação: ')

if operac == 'Adição':

   a = float(input('\nDigite um número: '))

   b = float(input('\nDigite outro número: '))

   c = a + b

   print('\nRESULTADO: %.2f' % c)

elif operac == 'Subtração':

    a = float(input('\nDigite um número: '))

    b = float(input('\nDigite outro número: '))

    c = a - b

    print('\nRESULTADO: %.2f' % c)

elif operac == 'Multiplicação':

    a = float(input('\nDigite um número: '))

    b = float(input('\nDigite outro número: '))

    c = a * b

    print('\nRESULTADO: %.2f' % c)

elif operac == 'Divisão':

    a = float(input('\nDigite um número: '))

    b = float(input('\nDigite outro número: '))

    c = a / b

    print('\nRESULTADO: %.2f' % c)

else:
    print('\nOPÇÃO INVÁLIDA!')