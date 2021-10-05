from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('hp', 'usb')
raton1 = Raton('hp', 'usb')
monitor1 = Monitor('LG', '19')
computadora1 = Computadora('hp', teclado1, raton1, monitor1)

teclado2 = Teclado('hp', 'usb')
raton2 = Raton('hp', 'usb')
monitor2 = Monitor('LG', '19')
computadora2 = Computadora('hp', teclado2, raton2, monitor2)
teclado3 = Teclado('hp', 'usb')
raton3 = Raton('hp', 'usb')
monitor3 = Monitor('LG', '19')
computadora3 = Computadora('lenovo', teclado3, raton3, monitor3)
computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)
