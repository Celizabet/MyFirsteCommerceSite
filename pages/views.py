import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
import time

#Clase Padre -- Realizar una orden en el sitio web de un eCommerce.
class MakeAnOrder():
    
    def __init__(self,user,address,item,price,monthly):
        self.user = user
        self.address = address
        self.item = item
        self.price = price
        self.monthly = monthly
    
    #Método 1. Clase Padre -- Con los stributos de la clase el sitio web muestra el detalle del pedido
    def order_description(self):
        print("\n\t.:ORDER DETAIL :.")
        print("""User: {} \nAddress:  {} \nItem:  {}    Price:  ${} \nMonthly payment:  {}
        """.format(self.user,self.address,self.item,self.price,self.monthly))
        
        confirmation = input("\nAll of the details are correct?\n").lower()
        if confirmation == "yes":
            print("Do payment")
        else:
            print("Change information")

    #Método 2. Clase Padre -- El usuario puede ver cuales son las formas de pago aceptadas
    def show_payment_methods(self):
        methods = ["credit/debit card", "cash", "gift card"]
        print(".: ACCEPTED PAYMENT METHODS :.")
        for i,method in enumerate(methods, start=1):
            print("{}. {}".format(i,method))
    
    #Método 3. Clase Padre -- Con este método el usuario elige la forma de pago que quiera
    def choosing_payment_method(self):
        choice = int(input("Choose one payment method introducing one number between 1-3 \n"))
        if choice == 1:
            print("Chosen payment method: CREDIT/DEBIT CARD\n")
            print("\t\t.: PAYMENT METHOD DESCRIPTION :.")
            print("All credit and debit cards are accepted,you can split payment between them")
        elif choice == 2:
            print("Chosen payment method: CASH\n")
            print("\t\t.: PAYMENT METHOD DESCRIPTION :.")
            print("You don't need a credit or debit card if you want to buy, pay in one of the participating store")
        elif choice == 3:
            print("Chosen payment method: GIFT CARD\n")
            print("\t\t.: PAYMENT METHOD DESCRIPTION :.")
            print("The newest Payment Method, you can buy a gift card in any participating store")
        else:
            print("\nYour choice does not exist!!")

#Clase Hija -- En este caso la clase hija es la realización del pago de la compra con una tarjeta de crédito o débito

class DoPaymentCard(MakeAnOrder):    
    
    def __init__(self,user,address,item,price,monthly,bank,card_number,cvv):
        super().__init__(user,address,item,price,monthly)
        self.bank = bank
        self.card_number = card_number
        self.cvv = cvv
    
    #Método 1. Clase Hija -- Valida los datos de la tarjeta introducida por el usuario
    def card_validation(self):        
        start_time = 0
        increment = 1
        while start_time <= 15:
            mins, secs = divmod(start_time, 60)        
            validating = "Validating Card{}".format("-"*increment)        
            print(validating, end='\r')        
            time.sleep(1)        
            start_time += 1    
            increment += 1
        print("           .:.: CARD ACCEPTED :.:.           ")
    
    #Método 2. Clase Hija -- Genera el recibo de la compra realizada por el usuario
    def shopping_receipt(self):
        print("  .: SUCCESFUL PURCHASE :.")
        print("""Bank: {} \nCard Number: {} \nAmount: {}   Months to Pay: {}
        """.format(self.bank,self.card_number,self.price,self.monthly))
    
    #Método 2. Clase Hija -- Informa al usuario si su tarjeta tiene acceso a descuento o promociones
    def promotions_discounts(self):
        participating_banks = ["BBVA","Banamex","Banorte","ScotiaBank","HSBC"]
        print("\t.: PARTICIPATING BANKS :.")
        for participant in participating_banks:
            if len(participating_banks)-1 == participating_banks.index(participant):
                print(participant,end = "")
            else:
                print(participant, end = ", ")
        
        if self.bank in participating_banks:
            print("\nYour credit/debit card has discount benefits!!!")

#Creación del objeto perteneciente a la Clase Padre
order1 = MakeAnOrder("ceut100512","Old road #123, CDMX","funko",11.45,1)
#Creación del objeto perteneciente a la Clase Hija
payment1 = DoPaymentCard("ceut100512","Old road #123, CDMX","funko",11.45,1,"BBVA",1234876510111312,913)

def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + " Usuario: "+order1.user,
        "python_ver": os.environ["PYTHON_VERSION"] + " Banco: "+payment1.bank,
    }

    return render(request, "pages/home.html", context)