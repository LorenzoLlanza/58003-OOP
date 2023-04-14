class Circle():

    def radius(self,radius):
        r = radius
    def peri(self,r):
        peri = 2*3.14*r
        print("Perimeter of the circle is: ",peri)

    def area(self,r):
        area = 3.142*r*r
        print("Area of the circle is: ",area)

c = Circle()
radius = int(input("Enter the radius of circle: "))
c.area(radius)
c.peri(radius)