class Menuitem:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def display_item(self):
        print(f"Name : {self.name}\nPrice : {self.price}\nCategory : {self.category}")

class Restaurant:
    
    def __init__(self,restuarant_name):
        self.restuarant_name=restuarant_name
        self.menu=[]
        self.orders=[]
        

    def add_items(self,obj_item):
        self.menu.append(obj_item)

    def display_menu(self):
        for obj_list in self.menu :
            print(f"Name : {obj_list.name}\nPrice : {obj_list.price}\nCategory : {obj_list.category}")

    def place_order(self,obj_menuitem): 
        self.orders.append(obj_menuitem)

    def show_orders(self):
        for obj_list in self.orders :
            print(f"Name : {obj_list.name}\nPrice : {obj_list.price}\nCategory : {obj_list.category}")

    def calculate_bill(self):
        sum=0
        for i in self.orders:
            sum+=i.price
        print(f"the total is {sum}")

