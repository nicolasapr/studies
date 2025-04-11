p1, p2 = map(float, input().split())
if p1 == 0.0 and p2 == 0.0:
    print("Origem")
elif p1 == 0.0:
    print("Eixo Y")
elif p2 == 0.0:
    print("Eixo X")
elif p1 > 0.0 and p2 > 0.0:
    print("Q1")
elif p1 < 0.0 and p2 > 0.0:
    print("Q2")
elif p1 < 0.0 and p2 < 0.0:
    print("Q3")
else:
    print("Q4")
