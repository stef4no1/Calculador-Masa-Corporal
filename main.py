height = input("Ingresa tu altura en metros:");
weight = input("Ingresa tu peso en KG:");

bmi = float(weight) / float(height) ** 2;
bmi_int = int(bmi);

print("Tu índice de masa corporal es de: " + str(bmi_int));