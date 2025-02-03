faturamento = 1200 # tipo: int -> numero inteiro
custo = 750.0 # tipo: float -> ponto flutuante (número com casa decimal)

novas_vendas = 100

faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("Faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", lucro)
print("A margem de lucro foi de ", round(margem_lucro, 2))

mensagem = "O faturamento da loja foi de tanto" # tipo: string
email = "emailqualquer@gmail.com" 
teve_lucro = True # tipo boolean 

#Mod -> %

#print (10 % 3)
tempo_contrato = 170 #meses

tempo_anos = 170 / 12

print("Tempo em anos ", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses ", int(tempo_meses))