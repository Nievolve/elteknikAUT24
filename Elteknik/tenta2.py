import matplotlib.pyplot as plt


def tempRes(T,Ro,To,roh):
    Rt=Ro*(1+roh*(T-To))
    return Rt

roh =  0.0168
Ro = 450
To = 0
tempRange = [70,60,50, 40, 30, 20, 10]
resRange= []
for k in tempRange:
    resRange.append(tempRes(k,Ro,To,roh))


# Skapa en linjeplot
plt.plot(tempRange, resRange)

# Lägga till etiketter på axlarna och en titel
plt.xlabel('Temperatur')
plt.ylabel('Resistans')
plt.title('Funktion Temperatur')

# Visa grafen
plt.show()