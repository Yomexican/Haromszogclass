import math

class Haromszog:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

def Kerulet(self):
    return self.a + self.b + self.c 

def terulet(self):
    s = self.kerulet() / 2
    return (s *(s-self.a) * (s-self.b) * (s-self.c))**(1/2)

def magassaga(self):
    return 2* self.terulet() / self.a

def magassagb(self):
    return 2* self.terulet() / self.b

def magassagc(self):
    return 2* self.terulet() / self.c

def ALF(self):
    return math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)))

def Betta(self):
    return math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2)/(2*self.a*self.c)))

def Gamma(self):
    return math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2)/(2*self.a*self.b)))
#0
print("Háromszög feldolgozása 'class' segítségével")

#1
a = input("a = ").replace(',', '.')
b = input("b = ").replace(',', '.')
c = input("c = ").replace(',', '.')

har1 = Haromszog(a, b, c)
har2 = Haromszog(10, 10, 10)

adatsor = "10,5;10,6;13,4"
har3 = Haromszog(*(adatsor.replace(',' , '.').split(';')))
#először az adtasorba kijavítjuk a hibákat és kijavítjuk 
#ezek a részek tuplebe jönnek vissza
#hogy a tuple tovább bontsuk a,b,c oldalra erre van a csillag operátor

#3
print(f"K = {har1.Kerulet():.2f}")
print(f"K = {har2.Kerulet():.2f}")
print(f"K = {har3.Kerulet():.2f}")
print()
print(f"t = {har1.terulet():.2f}")
print(f"ma = {har1.magassaga():.2f}")
print(f"mb = {har1.magassagb():.2f}")
print(f"mc = {har1.magassagc():.2f}")
print(f"alfa = {har1.Alfa():.2f}")
print(f"betta = {har1.Betta():.2f}")
print(f"gamma = {har1.Gamma():.2f}")