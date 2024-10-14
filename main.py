import lib, lib2
import autenticacao as aut

print()
print("User: ", aut.credenciais['username'])
print("Password: ", aut.credenciais['password'])

a = 2
b = 5

print()
print("***********************************")
print("O resultado da soma é: ", lib.soma(a, b))
print("O resultado da subtração é: ", lib.subtracao(a, b))
print("O resultado da potenciacao é: ", lib2.potenciacao(a, b)) 



