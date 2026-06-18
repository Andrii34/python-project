class Cars:
    def __init__(self,color,mark,model):
        self.color = color
        self.mark = mark
        self.model = model

car1 = Cars("orange","LAMBORGINI","HURACANE")
print(f"{car1.mark},{car1.model},in color {car1.color}")


car2 = Cars("red","toyota","supra")
print(car2.color)
print(car2.mark)
print(car2.model)

car3 = Cars("blue","BMW","M4 COMPETION")
print(car3.color)
print(car3.mark)
print(car3.model)
