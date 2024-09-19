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


#93
print("93")
R = 20 #Resistans
L = 0.2 #Henry, Indukdans
f = 50 #Hz, 
Xl = 2*math.pi*f*L
Z = math.sqrt(R**2+Xl**2)
tanfi = math.degrees(math.atan(Xl/R))
I = 230 / Z

print(f"a) Xl = {Xl:.2f} Omh")
print(f"b) Z = {Z:.2f} Ohm")
print(f"c) Fasförskjutningvinkeln är : {tanfi:.2f} grader")
print(f"d) Strömmen om spänningen är 230V är : {I:.2f} A")

#94
print("94")
Xl=90
f = 50
U = 48
I = 0.1
L = 90/f/2/math.pi
print(f"b) Indukdansen = {L:.2f} H")
Xl = 2*math.pi*f*L
Ul = I * Xl
fiRad = (math.sin(Ul/U))
Z = Xl/fiRad
print(f"Z = {Z:.3g}")
R = math.sqrt(Z**2-Xl**2)
print(f"REsistansen (R) = {R:.3g}")
print(f"Fasförskjutningsvinkeln = {math.degrees(fiRad):.2f} grader")

#95
print("95")
L = "?" #Indukdans 
Xl = 42 #Reaktans
f = 200 #Hz
# Xl= 2*Pi*f*L
L = Xl/(2*math.pi*f)
print(f"a) Induktansen är : {L:.3g} H. Kan också skrivas som {L*10**-3:.3g}")

#96
print("96")
R = 17
Xl = 12
Z = "?" #Impedansen
print(f"Impedansen är : {math.sqrt(R**2+Xl**2):.4g}")


#97
print("97")

# 1. Löser ut Xc
# 2. Löser ut Uc genom att ta I genom Xc
# Beräkna U? 
C = 2*10**-6 #F
print(C)
f = 50
I = 0.015
Xc = 1/(2*math.pi*f*C)
print(f"Reaktansen är : {Xc:.2f}")

Uc = I * Xc

print(f"Uc = {Uc:.2f} V")

#98
print("98")
R = 20
Xc = 40
Z = math.sqrt(R**2+Xc**2)
f = 50
print(f"Z är {Z:.2f} Ohm")
print(f"Kondensatorn kapacitet är {1/(2*math.pi*f*Xc)*10**6:.2f} microFarat")

#99
print("99")
Xc = "?"
C = 220*10**-6
f = 50
print(f"Reaktansen(Xc) är {1/(2*math.pi*f*C):.2f} Ohm")

#111
print("111")
R = 22
Xc = 12
U = 48
f = 50
I = "?"
Z = math.sqrt(R**2+Xc**2)
I = U/Z
print(f"Strömmen beräknades med U/Z och är i kretsen {I:.2g} A")

#112
print("112")
R = 48
Xc = 12
print(f"Impedansen beräknades med Z²=R²+Xc² och är {math.sqrt(R**2+Xc**2):.2f}")

#113
print("113")
U = 127
I = 1.7
Ur = 87
Uc = math.sqrt(U**2-Ur**2)
Ux = Uc/I
print(f"Uc = {Uc:.2f} V")
print(f"Ux = {Ux:.2f} V")


#114
print("114")
R = 20
C = 8*10**-6
f = 50
U = 20
f = 100
Xc = 1/(2*math.pi*f*C)
Z = math.sqrt(Xc**2+R**2)
I = U/Z
S = U * I
P = U * I * math.cos(R/Z)
cosfi = P/S
Nfasvinkelfi = math.degrees(math.acos(R/Z))
print(f"Z = {Z:.2f} Ohm")
print(f"Strömmen I är {I*10**3:.2f} mA")
print(f"Effektfaktorn är {cosfi:.2f} ")
print(f"Fi = {Nfasvinkelfi:.2f} grader")
