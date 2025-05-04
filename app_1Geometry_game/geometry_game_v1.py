from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_As_rec(self,rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


    def area(self):
        return (self.upright.x-self.lowleft.x) * (self.lowleft.y-self.lowleft.y)



recatangle=Rectangle(Point(randint(0,400),randint(0,400)),
                     Point(randint(10,400),randint(10,400)) )

print("coordinates for rectangle:",recatangle.lowleft.x,recatangle.lowleft.y
      and recatangle.upright.x,recatangle.upright.y)

point1=Point(float(input("guess X:")),float(input("guess Y:")))
rec=point1.falls_As_rec(recatangle)
print(rec)
area_guess=float(input("guess area:"))
area=recatangle.area()
if area==area_guess:
    print("ur  correct")

else:
    print("your guessed area is off by:",area-area_guess)