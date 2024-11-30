from module_5_3 import House2

class House3(House2):
    houses_history = []
    def __new__(cls, *args, **kwargs):
        object = super().__new__(cls)
        cls.houses_history.append(args[0])
        return object

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House3('ЖК Эльбрус', 10)
print(House3.houses_history)
h2 = House3('ЖК Акация', 20)
print(House3.houses_history)
h3 = House3('ЖК Матрёшки', 20)
print(House3.houses_history)
del h2
del h3
print(House3.houses_history)

