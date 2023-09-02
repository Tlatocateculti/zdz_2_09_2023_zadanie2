class ListaZakupow:
    def __init__(self):
        self.__lista = {}

    def dodaj(self,produkt, ilosc=1):
        try:
            self.__lista[produkt] += ilosc
        except:
            self.__lista[produkt] = ilosc

    def dodaj_produkty(self, produkty, ilosc=1):
        for prod in produkty:
            self.dodaj(prod,ilosc)

    def sciagnij(self, produkt, ilosc=1):
        try:
            self.__lista[produkt] -= ilosc
        except:
            self.__lista[produkt] = 0
        pass

    def sciagnij_produkty(self, produkty, ilosc=1):
        for prod in produkty:
            self.sciagnij(prod, ilosc)

    def __str__(self):
        str_ret = "Aktualna lista produktów:\n\n"
        for prod in self.__lista:
            str_ret += prod + ": " + str(self.__lista[prod]) + "\n"
        return str_ret + "\n"


lista = ListaZakupow()
lista.dodaj("kukurydza", 2)
lista.dodaj("chleb")
lista.dodaj("bułka", 10)
print(lista)
lista.sciagnij("kukurydza")
lista.sciagnij("marchew")
lista.sciagnij("bułka", 3)
print(lista)

lista.dodaj_produkty(('banany', 'kukurydza', 'pomidory', 'masło', 'olej'), 2)
print(lista)
lista.sciagnij_produkty(('banany', 'kukurydza', 'pomidory', 'masło', 'olej'), 1)
print(lista)
#Stworzyć klasę lista zakupów

#Klasa powinna posiadać słownik o następującej konstrukcji

#lista = { 'produkt1' : 1, 'produkt2': 0} (itd)

#jeżeli jakiegoś produktu nie będzie w słowniku, trzeba będzie go dodać

#klasa powinna posiadać następujące metody:

#dodaj(produkt, ilosc=1)

#dodaj_produkty(lista_nazw_produkow, ilosc=1)

#zdejmij_ilosc(produkt, ilosc=1)

#zdejmij_ilosc_produkty(lista_nazw_produktow, ilosc=1)

#Po każdym wykonaniu którejkolwiek z metod program powinien wyświetlać aktualną listę produktów
