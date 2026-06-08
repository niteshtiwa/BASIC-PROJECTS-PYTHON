class Car :
  def __init__(self, make , model, year):
       self.make = make
       self.model = model
       self.year= year
  def display_details(self):
      print(f"{self.year} {self.make} {self.model}")
  
my_car = Car("toyota", "corolla",2022)
my_car.display_details()