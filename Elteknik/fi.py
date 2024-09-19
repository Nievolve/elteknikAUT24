import math

#81
# fi = cos^-1 = Ur/U
print("81")
print(f"Vinkel fi = {math.degrees(math.acos(8/10)):.2f}")

#82
# Cos(30)=80/x
print("82")
print(f"U = {80 / math.cos(math.radians(30))}")

#83
# Voltmeter visar som kopplas in över hela kretsen?
Ur = 5
Ul = 12
# U²=Ur²+Ul²
print("83")
print(f"Spänningen är {math.sqrt(Ur**2 + Ul**2):.2f}")

#84
# Ul²=U²-Ur²
U = 28
Ur = 19
print("84")
print(f"Spänningen över spolen (Ul) = {math.sqrt(U**2 - Ur**2):.2f}")


#85
omhmeter = 13.3
U = 12
f = 50
I = 0.6
#Ur=R*I
Ur = omhmeter*I
#Ul²=U²-Ur²
Ul = math.sqrt(U**2-Ur**2)

print("85")
print(f"Spänningen över Ur = {Ur:.2f}")
print(f"Spänningen över Ul = {Ul:.2f}")


#90
Ur = 10
Uc = 20
U = math.sqrt(Ur**2+Uc**2)
fi = math.degrees(math.acos(Ur/U))
print("90")
print(f"Spänningen är : {U:.2f}")
print(f"Viknel fi är : {fi:.2f}")

#91
U = 100
fi = 40 #grader
Ur = "?"
Uc = "?"
# Ur= Cos(40)* U
Ur = math.cos(math.radians(40))*U
print("91")
print(f"Ur = {Ur:.2f}")
#Uc²=U²-Ur²
Uc = math.sqrt(U**2-Ur**2)
print(f"UC = {Uc:.2f}")