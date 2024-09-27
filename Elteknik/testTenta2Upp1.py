def TillfördEffekt(U,I,cosfi,P):
    aktiveffet=U*I*cosfi
    n = P/aktiveffet
    return n
U = 230
I = 4.2
P = 500
cosfi = 0.7
P1 = "?"
n = "?"

print(f"{TillfördEffekt(U,I,cosfi,P)}")