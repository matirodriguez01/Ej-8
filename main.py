import os

from Conjunto import Conjunto


def cero():
    print('Hasta luego')
    input('Presione enter para continuar...')


def uno():
    print('Conjunto 1: ', c1.getlista())
    print('Conjunto 2: ', c2.getlista())
    suma = c1 + c2
    print('Union:', suma.getlista())
    input('Presione enter para continuar...')


def dos():
    print('Conjunto 1: ', c1.getlista())
    print('Conjunto 2: ', c2.getlista())
    resultado = c1 - c2
    print('Resta: ', resultado.getlista())
    input('Presione enter para continuar...')


def tres():
    print('Conjunto 1: ', c1.getlista())
    print('Conjunto 2: ', c2.getlista())
    if c1 == c2:
        print('El conjunto 1 es igual al conjunto 2')
    else:
        print('El conjunto 1 es distinto al conjunto 2')
    input('Presione enter para continuar...')


switcher = {
    0: cero,
    1: uno,
    2: dos,
    3: tres
}


def switch(opc):
    func = switcher.get(opc, lambda: print('Opción incorrecta'))
    func()


if __name__ == '__main__':
    # Testeo
    # Conjunto 1
    x1 = int(input("Ingrese el primer valor del primer conjunto:"))
    x2 = int(input("Ingrese el segundo valor del primer conjunto:"))
    x3 = int(input("Ingrese el tercero valor del primer conjunto:"))
    l1 = [x1, x2, x3]
    c1 = Conjunto(l1)
    # Conjunto 2
    y1 = int(input("Ingrese el primer valor del segundo conjunto:"))
    y2 = int(input("Ingrese el segundo valor del segundo conjunto:"))
    y3 = int(input("Ingrese el tercero valor del segundo conjunto:"))
    l2 = [y1, y2, y3]
    c2 = Conjunto(l2)

    b = False
    while not b:
        os.system('cls')
        print('\n--------MENU--------')
        print('1- Unir 2 conjuntos')
        print('2- Restar 2 conjuntos')
        print('3- Comprobar si 2 conjuntos son iguales')
        print('0- Salir')
        op = int(input('Ingrese una opción: '))
        switch(op)
        b = int(op) == 0
