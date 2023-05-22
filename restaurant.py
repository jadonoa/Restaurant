class Table:

    bill = list()


    def __init__(self, num_of_people: int):
        self.num_of_people = num_of_people


    def order(self, item: str, price: float, quantity: int = 1):
        menu_item = {"item": item, "price": price, "quantity": quantity}

        # iterate through the bill to see if the item is already in the bill
        for i in range(0, len(self.bill)):

            # if the item is in the bill then just increase the quantity of the item by however many we are ordering
            if self.bill[i]["item"] == item and self.bill[i]["price"] == price:
                self.bill[i]["quantity"] += quantity
                return

        # otherwise add the dictionary with the current order to the bill
        self.bill.append(menu_item)


    def remove(self, item: str, price: float, quantity: int = 1) -> bool:
        # iterate through the bill to find the item on the bill
        for i in range(0, len(self.bill)):

            # check if the item is in the bill
            if self.bill[i]["item"] == item and self.bill[i]["price"] == price:

                # if the quantity of the item in the bill is greater than the removal quantity
                # then we can just subtract the removal quantity from the bill
                if self.bill[i]["quantity"] > quantity:
                    self.bill[i]["quantity"] -= quantity

                # if the quantity is equal or less than the removal quantity
                # then just remove the item off the bill
                elif self.bill[i]["quantity"] == quantity:
                    menu_item = {"item": item, "price": price, "quantity": quantity}
                    self.bill.remove(menu_item)

                # if the corresponding item has a quantity less than the quantity desired for removal return `False` and make no change to the bill
                else:
                    return False

                return True

        # if there is not an item with the corresponding item name and price return `False` and make no change to the bill
        return False


    def get_subtotal(self) -> float:
        subtotal = 0

        # calculate subtotal by multiplying the items price and quantity
        for item in self.bill:
            subtotal += (item["price"] * item["quantity"])

        return round(subtotal, 2)


    def get_total(self, service_charge_percentage: float = 0.1) -> dict:
        subtotal = self.get_subtotal()
        service_charge = service_charge_percentage * subtotal
        total = subtotal + service_charge

        return {"Sub Total": "£" + str(round(subtotal, 2)), "Service Charge": "£" + str(round(service_charge, 2)), "Total": "£" + str(round(total, 2))}


    def split_bill(self) -> float:
        subtotal = self.get_subtotal()
        return round(float(subtotal / self.num_of_people), 2)

    def clear_bill(self):
        self.bill = list()
