try:
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    imc = peso/(altura**2)
    if imc < 17:
        print(f"Muito abaixo do peso - IMC: {imc:.1f}")
    elif 18.49 >= imc >= 17:
        print(f"Abaixo do peso - IMC: {imc:.1f}")
    elif 24.99 >= imc > 18.49:
        print(f"Peso normal - IMC: {imc:.1f}")
    elif 29.99 >= imc > 24.99:
        print(f"Acima do peso - IMC: {imc:.1f}")
    elif 34.99 >= imc > 29.99:
        print(f"Obesidade I - IMC: {imc:.1f}")
    elif 39.99 >= imc > 34.99:
        print(f"Obesidade II (severa) - IMC: {imc:.1f}")
    elif imc > 39.99:
        print(f"Obesidade III (mórbida) - IMC: {imc:.1f}")

except ValueError:
    print("Entrada inválida")
