from time import sleep
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
opcao = 0
while opcao != 5:
   print('''
   [ 1 ] SOMAR
   [ 2 ] MULTIPLICAR
   [ 3 ] NUMERO MAIOR
   [ 4 ] NOVOS NÚMEROS
   [ 5 ] SAIR DO PROGRAMA''')
   opcao = int(input('>>>>> ESCOLHA UMA OPÇÃO: '))
   if opcao == 1:
       soma = num1 + num2
       print(f'A soma entre {num1} + {num2} é {soma}')
   elif opcao == 2:
       multi = num1 * num2
       print(f'A multiplicação entre {num1} x {num2} é {multi}')
   elif opcao == 3:
       if num1 > num2:
           maior = num1
       else:
           maior = num2
       print(f'Entre {num1} e {num2} o maior número é {maior}')
   elif opcao == 4:
       print('informe os números novamente: ')
       num1 = float(input('Digite o 1º número: '))
       num2 = float(input('Digite o 2º número: '))
   elif opcao == 5:
       print('Finalizando...')
   else:
       print('Opção inválida. Tente novamente!')
   print('=-=' * 10)
   sleep(2)
print('Fim do programa! Volte sempre!')