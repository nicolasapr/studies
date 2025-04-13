testes = []
contador = 0
while True:
    k, n = map(int, input().split())
    count = 0
    countcomplement = 0
    if k == 0 and n == 0:
        break
    contador += 1
    t = input()
    ptransformed = ""
    p = input()
    for i in p[::-1]:
        if i == "A":
            ptransformed += "T"
        elif i == "T":
            ptransformed += "A"
        elif i == "C":
            ptransformed += "G"
        elif i == "G":
            ptransformed += "C"

    #funcão importante
    for i in range(len(p)):
        if p[i:len(p)].startswith(t):
            count += 1
    for i in range(len(ptransformed)):
        if ptransformed[i:len(ptransformed)].startswith(t):
            countcomplement += 1

    # Armazenar os resultados em uma lista de dicionários
    testes.append({
        "teste": contador,
        "direta": count,
        "complementar": countcomplement
    })

# Exibir os resultados
for i in testes:
    print(f"Teste : {i['teste']}")
    print(f"Direta : {i['direta']}")
    print(f"Complementar : {i['complementar']}")*






