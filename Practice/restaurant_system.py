class Menuitem:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def display_item(self):
        print(f"Name : {self.name}\nPrice : {self.price}\nCategory : {self.category}")

class Restaurant:
    