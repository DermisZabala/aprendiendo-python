def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
