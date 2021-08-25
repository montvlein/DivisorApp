#-*-coing: utf-8-*-

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

def gasto_total(personas): #define el total gastado
    gastos_totales = 0
    for p in personas:
        gastos_totales += personas[p]
    return gastos_totales

class DivisorCuenta(GridLayout):

    def __init__(self, **kwargs):
        super(DivisorCuenta, self).__init__(**kwargs)
        self.cols = 1
        self.names = {}
        self.gastos = {}
        self.total = 0
        self.promedio = 0

    def listarPersonas(self, arg): # evalua el valor ingresado para agregar los input de las personas que participan
        try:
            num = int(arg.text)
            for n in range(num):
                self.add_widget(Label(text='nombre'))
                self.nombre = TextInput(multiline=False)
                self.add_widget(self.nombre)
                
                self.add_widget(Label(text='aporte'))
                self.aporte = TextInput(multiline=False)
                self.add_widget(self.aporte)

                self.names[self.nombre] = self.aporte
                            
            self.btndividir = Button(text="dividir")    
            self.add_widget(self.btndividir)
            self.btndividir.bind(on_press = self.calcularDivision)
                            
        except:
            self.ids.cantPersonas.text = "favor de ingresar un número"

    def calcularDivision(self, btn):
        for i in self.names:
            try:
                self.gastos[i] = int(self.names[i].text)
            except:
                self.names[i].text = "ingresa un numero"
        self.total = gasto_total(self.gastos)
        self.promedio = self.total/len(self.gastos)
        self.resultado()

    def resultado(self):
        self.ids.total.text = f"gasto total: ${self.total}"
        self.ids.promedio.text = f"gasto promedio por persona: ${self.promedio}"
        self.add_widget(Label(text='Resultado'))
        self.add_widget(Label(text=f"gasto total: ${self.total}"))
        self.add_widget(Label(text=f"gasto promedio por persona: ${self.promedio}"))
        
        self.cols = 3

        self.add_widget(Label(text='Nombre'))
        self.add_widget(Label(text='Aportó'))
        self.add_widget(Label(text='Conclusión'))

        for p in self.gastos:
            vuelto = self.gastos[p] - self.promedio
            self.add_widget(Label(text=f'{p.text}'))
            self.add_widget(Label(text=f'${self.gastos[p]}'))
            if vuelto >=0 :
                self.add_widget(Label(text=f'debe recibir ${vuelto}'))
            else:
                self.add_widget(Label(text=f'debe agregar ${abs(vuelto)}'))

class Resultado():
    pass

class DivisorCuentaApp(App):

    def build(self):
        return  DivisorCuenta()

if __name__ == '__main__':
    DivisorCuentaApp().run()