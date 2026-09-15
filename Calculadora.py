print("=== Minha Primeira Calculadora ===")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo: "))

print(f"Soma: {n1 + n2}")
print(f"Subtracao: {n1 - n2}")
print(f"Multiplicacao: {n1 * n2}")

if n2 != 0:
    print(f"Divisao: {n1 / n2}")
else:
    print("Nao da pra dividir por zero")
