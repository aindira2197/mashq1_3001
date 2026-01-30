def juft_yoki_toq(n):
    if n % 2 == 0:
        return "Juft"
    else:
        return "Toq"

print(juft_yoki_toq(7))

def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

print(faktorial(5))
