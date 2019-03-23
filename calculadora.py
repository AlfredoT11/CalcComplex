from Complejo import Complejo
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

class Principal(Screen):
    def calcular(self):

        if self.ids.r1.text != "":
            r1 = float(self.ids.r1.text)
        else:
            r1 = 0.0000001

        if self.ids.im1.text != "":
            im1 = float(self.ids.im1.text)
        else:
            im1 = 0.0000001

        if self.ids.r2.text != "":
            r2 = float(self.ids.r2.text)
        else:
            r2 = 0.0000001

        if self.ids.im2.text != "":
            im2 = float(self.ids.im2.text)
        else:
            im2 = 0.0000001                        
        
        if self.ids.n.text != "":
            n = int(self.ids.n.text)
        else:
            n = 1

        z1 = Complejo(r1, im1)
        z2 = Complejo(r2, im2)

        print("Presionado. :D", r1, im1, r2, im2, n)
        self.ids.resultados.text = ""

        if self.ids.suma.active:
            suma = Complejo.suma(z1, z2)
            #suma.toString()
            self.ids.resultados.text += suma.toString()
            suma.graficar()

        if self.ids.resta.active:
            resta = Complejo.resta(z1, z2)
            self.ids.resultados.text += resta.toString()
            resta.graficar()

        if self.ids.producto.active:
            producto = Complejo.producto(z1, z2)
            self.ids.resultados.text += producto.toString()
            producto.graficar()

        if self.ids.division.active:
            division = Complejo.division(z1, z2)
            self.ids.resultados.text += division.toString()
            division.graficar()

        if self.ids.potencia.active:
            potencia = Complejo.potencia(z1, n)
            self.ids.resultados.text += potencia.toString()
            potencia.graficar()

        if self.ids.raices.active:
            raices = Complejo.raiz(z1, n)
            for r in raices:
                self.ids.resultados.text += r.toString()
                r.graficar()

        if self.ids.conjugado.active:
            conjugado = Complejo.conjugado(z1)
            self.ids.resultados.text += conjugado.toString()
            conjugado.graficar()                                                                        

        if self.ids.distancia.active:
            self.ids.resultados.text += Complejo.distancia(z1, z2)

        if self.ids.exponencial.active:
            exp = Complejo.expo(z1)
            self.ids.resultados.text += exp.toString()
            exp.graficar()      

        if self.ids.logaritmo.active:
            log = Complejo.logaritmo(z1)
            self.ids.resultados.text += log.toString()
            log.graficar() 

        if self.ids.potCompleja.active:
            potCom = Complejo.potenciaCompleja(z1, z2)
            self.ids.resultados.text += potCom.toString()
            potCom.graficar()          

        if self.ids.sen.active:
            sen = Complejo.sin(z1)
            self.ids.resultados.text += sen.toString()
            sen.graficar()    

        if self.ids.cos.active:
            cos = Complejo.cos(z1)
            self.ids.resultados.text += cos.toString()
            cos.graficar()

        if self.ids.tan.active:
            tan = Complejo.tan(z1)
            self.ids.resultados.text += tan.toString()
            tan.graficar()   

        if self.ids.csc.active:
            csc = Complejo.csc(z1)
            self.ids.resultados.text += csc.toString()
            csc.graficar()

        if self.ids.sec.active:
            sec = Complejo.sec(z1)
            self.ids.resultados.text += sec.toString()
            sec.graficar()

        if self.ids.cot.active:
            cot = Complejo.cot(z1)
            self.ids.resultados.text += cot.toString()
            cot.graficar()

        if self.ids.asen.active:
            asen = Complejo.arcsin(z1)
            self.ids.resultados.text += asen.toString()
            asen.graficar()    

        if self.ids.acos.active:
            acos = Complejo.arccos(z1)
            self.ids.resultados.text += acos.toString()
            acos.graficar()

        if self.ids.atan.active:
            atan = Complejo.arctan(z1)
            self.ids.resultados.text += atan.toString()
            atan.graficar()   

        if self.ids.acsc.active:
            acsc = Complejo.arccsc(z1)
            self.ids.resultados.text += acsc.toString()
            acsc.graficar()

        if self.ids.asec.active:
            asec = Complejo.arcsec(z1)
            self.ids.resultados.text += asec.toString()
            asec.graficar()

        if self.ids.acot.active:
            acot = Complejo.arccot(z1)
            self.ids.resultados.text += acot.toString()
            acot.graficar()

        if self.ids.senh.active:
            senh = Complejo.sinh(z1)
            self.ids.resultados.text += senh.toString()
            senh.graficar()    

        if self.ids.cosh.active:
            cosh = Complejo.cosh(z1)
            self.ids.resultados.text += cosh.toString()
            cosh.graficar()

        if self.ids.tanh.active:
            tanh = Complejo.tanh(z1)
            self.ids.resultados.text += tanh.toString()
            tanh.graficar()   

        if self.ids.csch.active:
            csch = Complejo.csch(z1)
            self.ids.resultados.text += csch.toString()
            csch.graficar()

        if self.ids.sech.active:
            sech = Complejo.sech(z1)
            self.ids.resultados.text += sech.toString()
            sech.graficar()

        if self.ids.coth.active:
            coth = Complejo.coth(z1)
            self.ids.resultados.text += coth.toString()
            coth.graficar()

        if self.ids.asenh.active:
            asenh = Complejo.arcsinh(z1)
            self.ids.resultados.text += asenh.toString()
            asenh.graficar()    

        if self.ids.acosh.active:
            acosh = Complejo.arccosh(z1)
            self.ids.resultados.text += acosh.toString()
            acosh.graficar()

        if self.ids.atanh.active:
            atanh = Complejo.arctanh(z1)
            self.ids.resultados.text += atanh.toString()
            atanh.graficar()   

        if self.ids.acsch.active:
            acsch = Complejo.arccsch(z1)
            self.ids.resultados.text += acsch.toString()
            acsch.graficar()

        if self.ids.asech.active:
            asech = Complejo.arcsech(z1)
            self.ids.resultados.text += asech.toString()
            asech.graficar()

        if self.ids.acoth.active:
            acoth = Complejo.arccoth(z1)
            self.ids.resultados.text += acoth.toString()
            acoth.graficar()         

        plt.grid(True)
        plt.axis('equal')
        plt.axis([-50, 50, -50, 50])                              

    def graficar(self):



        '''plt.plot([10000], [10000])
        plt.plot([-10000], [10000])
        plt.plot([-10000], [-10000])
        plt.plot([10000], [-10000])'''
        plt.show()             

class Elemental(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my2.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    myApp = MyApp()
    myApp.run()  