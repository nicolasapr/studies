numbers = list(map(float, input().split()))

if sorted(numbers)[0]+sorted(numbers)[1] > sorted(numbers)[2]:
    print(f"Perimetro = {numbers[0]+numbers[1]+numbers[2]}")
else:
    print(f"Area = {(numbers[0]+numbers[1])*numbers[2]/2}")
