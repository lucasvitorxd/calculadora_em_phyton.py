#eu nao usei a função while

#perguntas
numb1 = int(input("digite primeiro valor:\n"))

numb2 = int(input("digite segundo valor:\n"))

operador = input("qual operador:\n")
  
#variavel operador
mult = numb1 * numb2
som = numb1 + numb2
div = numb1 / numb2
sub = numb1 - numb2
if (operador == "*"):
    print(f"{numb1} * {numb2} = {mult}")
elif (operador == "+"):
    print(f"{numb1} + {numb2} = {som}")
elif (operador == "-"):
    print(f"{numb1} - {numb2} = {sub}")
elif (operador == "/"):
    print(f"{numb1} / {numb2} = {div}")
