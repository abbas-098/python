import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):

        
        # Run validations to the recieved arguments
        assert price >= 0
        assert quantity >= 0

        # Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        @property
        # Property decorator = Read-Only Attribute
        def name(self):
            return self._name

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero.
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"
