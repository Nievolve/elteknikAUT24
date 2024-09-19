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
print("83")
print(f"Spänningen är {math.sqrt(Ur**2 + Ul**2):.2f}")

#84
# Ul = ?
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

