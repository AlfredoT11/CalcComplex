import matplotlib.pyplot as plt
import numpy as np

from math import pi, atan, cos, sin, exp, log

class Complejo:
    def __init__(self, x=0, y=0, nombre="z", color='black', marker='o', markersize=5):
        """Inicia el valor del numero complejo"""
        self.x = x
        self.y = y
        self.nombre = nombre
        self.color = color
        self.marker = marker
        self.markersize = markersize

    @staticmethod
    def modulo(z1):
        modulo = (z1.x**2 + z1.y**2)**(1/2)
        return modulo
    
    @staticmethod
    def argumento(z):

        if z.x > 0 and z.y == 0:
            theta = 0
        elif z.x == 0 and z.y > 0:
            theta = pi / 2
        elif z.x < 0 and z.y == 0:
            theta = pi
        elif  z.x == 0 and z.y < 0:
            theta = 3*pi/2
        elif z.x > 0 and z.y > 0:
            theta = atan(z.y/z.x)
        elif z.x < 0 and z.y > 0:
            theta = pi - atan(z.y/abs(z.x))
        elif z.x < 0 and z.y < 0:
            theta = pi + atan(abs(z.y)/abs(z.x))
        elif z.x > 0 and z.y < 0:
            theta = 2*pi - atan(abs(z.y)/z.x) 
        
        return theta

    @staticmethod
    def suma(z1, z2):
        zsuma = Complejo(nombre="Suma", color="blue")
        zsuma.x = z1.x + z2.x
        zsuma.y = z1.y + z2.y
        return zsuma

    @staticmethod
    def resta(z1, z2):
        zresta = Complejo(nombre="Resta", color="red")
        zresta.x = z1.x - z2.x
        zresta.y = z1.y - z2.y
        return zresta

    @staticmethod
    def producto(z1, z2):
        zproducto = Complejo(nombre="Producto", color="#0087B2")
        zproducto.x = z1.x*z2.x - z1.y*z2.y
        zproducto.y = z1.x*z2.y + z1.y*z2.x
        return zproducto
    
    @staticmethod
    def division(z1, z2):
        d = z2.x**2 + z2.y**2

        zdivision = Complejo(nombre="Division", color="yellow")
        zdivision.x = (z1.x*z2.x + z1.y*z2.y)/d
        zdivision.y = (z1.y*z2.x - z1.x*z2.y)/d
        return zdivision
    
    @staticmethod
    def conjugado(z1):
        zconjugado = Complejo(nombre="Conjugado", color="cyan")
        zconjugado.x = z1.x
        zconjugado.y = -1*z1.y
        return zconjugado

    @staticmethod
    def potencia(z1, n):
        zpotencia = Complejo(z1.x, z1.y, nombre="Potencia", color="magenta")

        for i in range(0, n-1):
            zpotencia=Complejo.producto(zpotencia, z1)

        return zpotencia

    @staticmethod
    def raiz(z, n):
        raices = []

        r = (z.x**2 + z.y**2)**(1/2)
        rn = r**(1/n)

        if z.x > 0 and z.y == 0:
            theta = 0
        elif z.x == 0 and z.y > 0:
            theta = pi / 2
        elif z.x < 0 and z.y == 0:
            theta == pi
        elif  z.x == 0 and z.y < 0:
            theta = 3*pi/2
        elif z.x > 0 and z.y > 0:
            theta = atan(z.y/z.x)
        elif z.x < 0 and z.y > 0:
            theta = pi - atan(z.y/abs(z.x))
        elif z.x < 0 and z.y < 0:
            theta = pi + atan(abs(z.y)/abs(z.x))
        elif z.x > 0 and z.y < 0:
            theta = 2*pi - atan(abs(z.y)/z.x)

        for i in range(0, n):
            zx = rn * cos((theta + 2*pi*i) / n)
            zy = rn * sin((theta + 2*pi*i) / n)
            raices.append(Complejo(zx, zy, nombre="raiz".join(str(i)) ,color="green"))
        
        '''for zaux in raices:
            print("x: ",zaux.x," y: ", zaux.y)'''

        return raices

    @staticmethod
    def distancia(z1, z2):
        sum = (z1.x**2)+(z1.y**2)+(z2.x**2)+(z2.y**2)-2*z1.x*z2.x-2*z1.y*z2.y
        d = sum**(1/2)


        return "Distancia: "+str(d)+"\n"
    @staticmethod
    def expo(z1):
        zexpo = Complejo(nombre="Exponencial", color="blue")
        zexpo.x = exp(z1.x)*cos(z1.y)
        zexpo.y = exp(z1.x)*sin(z1.y)
        return zexpo

    @staticmethod
    def potenciaCompleja(z1, z2):
        zpotC = Complejo(nombre="Potencia compleja", color="#109C83")
        
        '''auxP = Complejo.producto(z2, Complejo.logaritmo(z1))
        aux = Complejo.expo(auxP)

        zpotC.x = aux.x
        zpotC.y = aux.y'''

        zaux1 = z1.x + z1.y*1j
        zaux2 = z2.x + z2.y*1j    

        zfin = zaux1**zaux2
        zpotC.x = zfin.real
        zpotC.y = zfin.imag   

        return zpotC

    
    @staticmethod
    def sin(z1):
        zsin = Complejo(nombre="Seno", color="red")
        
        aux1 = Complejo(-1*z1.y, z1.x)
        aux1 = Complejo.expo(aux1)

        aux2 = Complejo(z1.y, -1*z1.x)
        aux2 = Complejo.expo(aux2)

        aux3 = Complejo.division(Complejo.resta(aux1, aux2), Complejo(0,2))
        zsin.x = aux3.x
        zsin.y = aux3.y
        return zsin

    @staticmethod
    def cos(z1):
        zcos = Complejo(nombre="Coseno", color="green")

        aux1 = Complejo(-1*z1.y, z1.x)
        aux1 = Complejo.expo(aux1)

        aux2 = Complejo(z1.y, -1*z1.x)
        aux2 = Complejo.expo(aux2)

        aux3 = Complejo.division(Complejo.suma(aux1, aux2), Complejo(2,0))
        zcos.x = aux3.x
        zcos.y = aux3.y
        return zcos

    @staticmethod
    def tan(z1):
        ztan = Complejo(nombre="Tangente", color="#CC52CB")

        aux = Complejo.division(Complejo.sin(z1), Complejo.cos(z1))
        ztan.x = aux.x
        ztan.y = aux.y
        return ztan

    @staticmethod
    def sec(z1):
        zsec = Complejo(nombre="Secante", color="#B22035")

        aux = Complejo.division(Complejo(1,0), Complejo.cos(z1))
        zsec.x = aux.x
        zsec.y = aux.y
        return zsec

    @staticmethod
    def csc(z1):
        zcsc = Complejo(nombre="Cosecante", color="#239C20")

        aux = Complejo.division(Complejo(1,0), Complejo.sin(z1))
        zcsc.x = aux.x
        zcsc.y = aux.y
        return zcsc

    @staticmethod
    def cot(z1):
        zcot = Complejo(nombre="Cotangente", color="#88ABCC")

        aux = Complejo.division(Complejo(1,0), Complejo.tan(z1))
        zcot.x = aux.x
        zcot.y = aux.y
        return zcot

    @staticmethod
    def sinh(z1):
        zsinh = Complejo(nombre="SenoHiperbolico", color="#6320B2")

        aux1 = Complejo.resta(Complejo.expo(z1), Complejo.expo(Complejo(-1*z1.x, -1*z1.y)))
        aux1 = Complejo.division(aux1, Complejo(2,0))

        zsinh.x = aux1.x
        zsinh.y = aux1.y
        return zsinh

    @staticmethod
    def cosh(z1):
        zcosh = Complejo(nombre="CosenoHiperbolico", color="#9C2220")

        aux1 = Complejo.suma(Complejo.expo(z1), Complejo.expo(Complejo(-1*z1.x, -1*z1.y)))
        aux1 = Complejo.division(aux1, Complejo(2,0))

        zcosh.x = aux1.x
        zcosh.y = aux1.y
        return zcosh

    @staticmethod
    def tanh(z1):
        ztanh = Complejo(nombre="TangenteHiperbolica", color="#1DB232")

        aux = Complejo.division(Complejo.sinh(z1), Complejo.cosh(z1))
        ztanh.x = aux.x
        ztanh.y = aux.y
        return ztanh

    @staticmethod
    def sech(z1):
        zsech = Complejo(nombre="SecanteHiperbolica", color="#911E9C")

        aux = Complejo.division(Complejo(1,0), Complejo.cosh(z1))
        zsech.x = aux.x
        zsech.y = aux.y
        return zsech

    @staticmethod
    def csch(z1):
        zcsch = Complejo(nombre="CosecanteHiperbolica", color="#9C9226")

        aux = Complejo.division(Complejo(1,0), Complejo.sinh(z1))
        zcsch.x = aux.x
        zcsch.y = aux.y
        return zcsch

    @staticmethod
    def coth(z1):
        zcoth = Complejo(nombre="CotangenteHiperbolica", color="#B22D1D")

        aux = Complejo.division(Complejo(1,0), Complejo.tanh(z1))
        zcoth.x = aux.x
        zcoth.y = aux.y
        return zcoth

    @staticmethod
    def logaritmo(z1):
        zlogaritmo = Complejo(nombre="Logaritmo", color="#8A356F")

        zlogaritmo.x = log(Complejo.modulo(z1))
        zlogaritmo.y = Complejo.argumento(z1)
        return zlogaritmo
    
    @staticmethod
    def arcsin(z1):
        zarcsin = Complejo(nombre="ArcoSeno", color="#9C0021")

        auxraiz = Complejo.raiz(Complejo.resta(Complejo(1,0),Complejo.potencia(z1,2)), 2)[0]
        auxprod = Complejo.producto(Complejo(0,1), z1)
        auxLn = Complejo.logaritmo(Complejo.suma(auxprod, auxraiz))

        aux = Complejo.producto(Complejo(0,-1), auxLn)

        zarcsin.x = aux.x
        zarcsin.y = aux.y
        return zarcsin
    
    @staticmethod
    def arccos(z1):
        zarccos = Complejo(nombre="ArcoCoseno", color="#3370B2")
        
        aux = Complejo.producto(Complejo(-1,0),Complejo.arcsin(z1))

        zarccos.x = aux.x + (1/2)*pi
        zarccos.y = aux.y
        return zarccos   

    @staticmethod
    def arctan(z1):
        zarctan = Complejo(nombre="ArcoTangente", color="#8C40B2")
        
        auxLn1 = Complejo.logaritmo(Complejo.resta(Complejo(1,0), Complejo.producto(Complejo(0,1), z1)))
        auxLn2 = Complejo.logaritmo(Complejo.suma(Complejo(1,0), Complejo.producto(Complejo(0,1), z1)))
        auxResta = Complejo.resta(auxLn1, auxLn2)
        aux = Complejo.producto(Complejo(0,0.5),auxResta)

        zarctan.x = aux.x
        zarctan.y = aux.y
        return zarctan

    @staticmethod
    def arcsec(z1):
        '''Hacer esta funcion en funcion de arccsc'''
        zarcsec = Complejo(nombre="ArcoSecante", color="#505DCC")

        auxresta = Complejo.resta(Complejo(1,0), Complejo.division(Complejo(1,0), Complejo.potencia(z1, 2)))
        auxraiz = Complejo.raiz(auxresta, 2)[0]

        auxsuma = Complejo.suma(auxraiz, Complejo.division(Complejo(0,1),z1))

        aux = Complejo.producto(Complejo(0,1), Complejo.logaritmo(auxsuma))

        zarcsec.x = aux.x + (1/2)*pi
        zarcsec.y = aux.y
        return zarcsec

    @staticmethod
    def arccsc(z1):
        zarccsc = Complejo(nombre="ArcoCosecante", color="#CC0FBC")

        auxresta = Complejo.resta(Complejo(1,0), Complejo.division(Complejo(1,0), Complejo.potencia(z1, 2)))
        auxraiz = Complejo.raiz(auxresta, 2)[0]

        auxsuma = Complejo.suma(auxraiz, Complejo.division(Complejo(0,1),z1))

        aux = Complejo.producto(Complejo(0,-1), Complejo.logaritmo(auxsuma))

        zarccsc.x = aux.x
        zarccsc.y = aux.y
        return zarccsc

    @staticmethod
    def arccot(z1):
        zarccot = Complejo(nombre="ArcoCotangente", color="#86008A")

        auxint1 = Complejo.division(Complejo.resta(z1, Complejo(0,1)), z1)
        auxint2 = Complejo.division(Complejo.suma(z1, Complejo(0,1)), z1)

        auxint = Complejo.resta(Complejo.logaritmo(auxint1), Complejo.logaritmo(auxint2))
        aux = Complejo.producto(Complejo(0, 0.5), auxint)

        zarccot.x = aux.x
        zarccot.y = aux.y
        return zarccot
    
    @staticmethod
    def arcsinh(z1):
        '''Arcosenohiperbolico en función del arcoseno'''
        
        zarcsinh = Complejo(nombre="ArcoSenoHiperbolico", color="#049C2D")

        auxasin = Complejo.arcsin(Complejo.producto(Complejo(0,1),z1))
        aux = Complejo.producto(Complejo(0,-1), auxasin)

        zarcsinh.x = aux.x
        zarcsinh.y = aux.y
        return zarcsinh
    
    @staticmethod
    def arccosh(z1):
        zarccosh = Complejo(nombre="ArcoCosenoHiperbolico", color="#9C970B")

        auxraiz1 = Complejo.raiz(Complejo.suma(z1, Complejo(1,0)), 2)[0]
        auxraiz2 = Complejo.raiz(Complejo.resta(z1, Complejo(1,0)), 2)[0]

        auxsuma = Complejo.suma(z1, Complejo.producto(auxraiz1, auxraiz2))
        aux = Complejo.logaritmo(auxsuma)

        zarccosh.x = aux.x
        zarccosh.y = aux.y
        return zarccosh

    @staticmethod
    def arctanh(z1):
        '''Arcotangentehiperbolica en funcion de arcotangente'''
        zarctanh = Complejo(nombre="ArcoTangenteHiperbolica", color="#46CC9E")

        auxarctan = Complejo.arctan(Complejo.producto(Complejo(0,1),z1))
        aux = Complejo.producto(Complejo(0,-1),auxarctan)

        zarctanh.x = aux.x
        zarctanh.y = aux.y
        return zarctanh

    @staticmethod
    def arcsech(z1):
        zarcsech = Complejo(nombre="ArcoSecanteHiperbolica", color="#409C5B")

        auxint1 = Complejo.resta(Complejo.division(Complejo(1,0),z1), Complejo(1,0))
        auxraiz1 = Complejo.raiz(auxint1,2)[0]

        auxint2 = Complejo.suma(Complejo.division(Complejo(1,0),z1), Complejo(1,0))
        auxraiz2 = Complejo.raiz(auxint2,2)[0]

        auxint = Complejo.suma(Complejo.producto(auxraiz1, auxraiz2), Complejo.division(Complejo(1,0),z1))
        aux = Complejo.logaritmo(auxint)

        zarcsech.x = aux.x
        zarcsech.y = aux.y
        return zarcsech

    @staticmethod
    def arccsch(z1):
        zarccsch = Complejo(nombre="ArcoCosecanteHiperbolica", color="#9C1A12")

        auxintr = Complejo.suma(Complejo(1,0), Complejo.division(Complejo(1,0), Complejo.potencia(z1,2)))
        auxraiz = Complejo.raiz(auxintr,2)[0]

        auxint = Complejo.suma(auxraiz, Complejo.division(Complejo(1,0), z1))
        aux = Complejo.logaritmo(auxint)

        zarccsch.x = aux.x
        zarccsch.y = aux.y
        return zarccsch

    @staticmethod
    def arccoth(z1):
        zarccoth = Complejo(nombre="ArcoCotangenteHiperbolica", color="#8A0703")

        auxln1 = Complejo.suma(Complejo(1,0), Complejo.division(Complejo(1,0), z1))
        auxln2 = Complejo.resta(Complejo(1,0), Complejo.division(Complejo(1,0), z1))        

        auxlog1 = Complejo.logaritmo(auxln1)
        auxlog2 = Complejo.logaritmo(auxln2)
        auxint = Complejo.resta(auxlog1, auxlog2)

        aux = Complejo.producto(Complejo(0.5,0),auxint)

        zarccoth.x = aux.x
        zarccoth.y = aux.y
        return zarccoth

    #Derivadas
    @staticmethod
    def derz2mas2z(z, n):
        derz2mas2z = Complejo(nombre="DerivadaZcuadmas2z", color="#3D288A")
        aux = Complejo()

        if n == 1:
            aux = Complejo.producto(Complejo(2,0), z)
            aux = Complejo.suma(aux, Complejo(2,0))
        elif n == 2:
            aux.x = 2
            aux.y = 0

        derz2mas2z.x = aux.x
        derz2mas2z.y = aux.y
        return derz2mas2z

    @staticmethod
    def derZ(z, n):
        derZ = Complejo(nombre="DerZ", color="#6B38CC")
        if n == 1:
            derZ.x = 1
        
        return derZ

    @staticmethod
    def der3i(n):
        return Complejo(nombre="Der3i", color="#B28654")

    @staticmethod
    def senhDer(z, n):
        zDerSenh = Complejo(nombre="DerivadaSenH", color="#8A287A")
        aux = Complejo(0, 0)

        if n%2 == 0:
            aux = Complejo.sinh(z)
        else:
            aux = Complejo.cosh(z)

        zDerSenh.x = aux.x
        zDerSenh.y = aux.y
        return zDerSenh

    @staticmethod
    def cosDer(z, n):
        zDerCos = Complejo(nombre="DerivadaSenH", color="#459C97")
        aux = Complejo()

        if n%4 == 0:
            aux = Complejo.cos(z)
        elif n%4 == 1:
            aux = Complejo.producto(Complejo(-1,0), Complejo.sin(z))
        elif n%4 == 2:
            aux = Complejo.producto(Complejo(-1,0), Complejo.cos(z))
        elif n%4 == 3:
            aux = Complejo.sin(z)

        zDerCos.x = aux.x
        zDerCos.y = aux.y
        return zDerCos
    

    def toString(self):
        if(self.y<0):
            print(self.nombre,' = {0}{1}i'.format(self.x, self.y))
            return str(self.nombre+' = {0}{1}i\n'.format(self.x, self.y))
        else:
            print(self.nombre,' = {0}+{1}i'.format(self.x, self.y))
            return str(self.nombre+' = {0}+{1}i\n'.format(self.x, self.y))

    def graficar(self):
        plt.plot([self.x], [self.y], marker=self.marker, markersize=self.markersize, color=self.color)