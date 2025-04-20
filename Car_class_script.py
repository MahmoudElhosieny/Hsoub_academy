class Car:
    type = 'vehicle'

    def __init__(self, color, distance, engine, year):
        self.color = color
        self.distance = distance
        self.engine = engine
        self.year = year

    def reset_counter(self):
        self.distance = 0

    def increase_counter(self, new_distance):
        self.distance += new_distance

    def decrease_counter(self, new_distance):
        self.distance -= new_distance


car01 = Car('Red', 120, 'EN1500', 2015)
car02 = Car('Black', 150, 'EN1200', 2019)

print(car01.color)
print(car01.type)
car02.increase_counter(25)
print(car02.distance)
print(car02.type)
