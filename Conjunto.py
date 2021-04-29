class Conjunto:
    __lista = []

    def __init__(self, lista):
        self.__lista = lista

    def getlista(self):
        return self.__lista

    def __add__(self, c2):
        l2 = c2.getlista()
        res = [*self.__lista, *l2]
        return Conjunto(res)

    def __sub__(self, c2):
        l2 = c2.getlista().copy()
        res = []
        for i in range(len(self.__lista)):
            b = False
            for j in range(len(l2)):
                if self.__lista[i] == l2[i]:
                    b = True
            if b is False:
                res.append(self.__lista[i])
        for i in range(len(l2)):
            b = False
            for j in range(len(self.__lista)):
                if self.__lista[j] == l2[i]:
                    b = True
            if b is False:
                res.append(l2[i])
        return Conjunto(res)

    def __eq__(self, c2):
        aux = c2.getlista().copy()
        b = False
        if len(aux) == len(self.__lista):
            for i in range(len(aux)):
                for j in range(len(self.__lista)):
                    if aux[i] == self.__lista[j]:
                        b = True
                    else:
                        b = False
            if b is True:
                b = True
            else:
                b = False
        else:
            b = False
        return b

