sal = float(input())
taxes = 0.0
if sal <= 2000:
    print("Isento")
elif sal <= 3000:
    taxes = (sal - 2000) * 0.08
    print(f"R$ {taxes:.2f}")
elif sal <= 4500:
    taxes = (sal - 3000) * 0.18 + (1000 * 0.08)
    print(f"R$ {taxes:.2f}")
else:
    taxes = (sal - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {taxes:.2f}")