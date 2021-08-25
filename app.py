#-*-coing: utf-8-*-

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

def decorador_titulo(func):
    def titulo():
        print("-----------")
        func()
        print("-----------")
    return titulo

class DivisorCuenta(GridLayout):

    def __init__(self, **kwargs):
        super(DivisorCuenta, self).__init__(**kwargs)
        self.cols = 1
        self.ids.cantPersonas.text = "Ingresar el numero de personas que participan en la división"
        self.names = []

    def calcularPersonas(self, arg): # evalua el valor ingresado en el laber para elegir la cantidad de personas que participan
        try:
            num = int(arg.text)
            for n in range(num):
                self.add_widget(Label(text='nombre'))
                self.nombre = TextInput(multiline=False)
                self.add_widget(self.nombre)
                self.names.append(self.nombre)
            
            self.btndividir = Button(text="dividir")
            self.add_widget(self.btndividir)
            self.btndividir.bind(on_press = self.calcularDivision)
        except:
            self.ids.cantPersonas.text = "favor de ingresar un número"

    # @decorador_titulo
    def calcularDivision(self, btn):
        for i in self.names:
            print(i.text)

class DivisorCuentaApp(App):

    def build(self):
        return  DivisorCuenta()

if __name__ == '__main__':
    DivisorCuentaApp().run()