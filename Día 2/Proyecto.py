print("¡Bienvenido!")
nombre = input("¿Cúal es tu nombre?: ")
ventas = input("¿Cual fue el monto de tus ventas?: ")

comision = float(ventas) * 13 /100
print(f"Hola {nombre} gracias por tu gran trabajo, tu comisión es de ${round(comision,2)} pesos sigue esforzandote!")