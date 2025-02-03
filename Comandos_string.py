email = "meuemail@gmail.com"

faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro/faturamento

#print("Faturamento da empresa: {}, Custo {}^, Lucro {}".format(faturamento,custo,lucro))
print(f"Faturamento da empresa: {faturamento}, Custo {custo}, Lucro {lucro}")

email_cliente = "qualquercoisa@gmail.com"

#maiusculo
email_cliente = email_cliente.upper()
#minusculo
email_cliente = email_cliente.lower()
print(email_cliente)

# como achar elementos na string
print(email_cliente.find("@")) # -1 quando não encontrar

# como pegar o caracter, Obs: se colocar " 0 : "o espaço indica que vai até o final
print(email_cliente[email_cliente.find("@") : ])

nomo_email = email_cliente.replace("gmail.com", "hotmail.com")

nome = "leo brat"

print(nome.title())
print(nome.capitalize())

#pegar o servidor do email
print(email_cliente[email_cliente.find("@") : ])
#pegar o 1 nome
print(nome[ : nome.find(" ")])
#pegar o 2 nome
print(nome[nome.find(" ")+1 : ])

#casos epeciais - formatações em texto
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo R${custo:.2f}, Lucro R${lucro:.2f}, Margem R${margem_lucro:.0%}")