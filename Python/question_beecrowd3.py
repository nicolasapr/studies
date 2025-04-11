sal = float(input())

if sal <= 400:
    print(f"Novo salario: {sal*1.15:.2f}")
    print(f"Reajuste ganho: {sal*0.15:.2f}")
    print("Em percentual: 15 %")
elif sal <= 800:
    print(f"Novo salario: {sal*1.12:.2f}")
    print(f"Reajuste ganho: {sal*0.12:.2f}")
    print("Em percentual: 12 %")
elif sal <= 1200:
    print(f"Novo salario: {sal*1.10:.2f}")
    print(f"Reajuste ganho: {sal*0.10:.2f}")
    print("Em percentual: 10 %")
elif sal <= 2000:
    print(f"Novo salario: {sal*1.07:.2f}")
    print(f"Reajuste ganho: {sal*0.07:.2f}")
    print("Em percentual: 7 %")
else:
    print(f"Novo salario: {sal*1.04:.2f}")
    print(f"Reajuste ganho: {sal*0.04:.2f}")
    print("Em percentual: 4 %")

