import math
from tkinter import RIGHT
from tkinter.font import BOLD
import turtle as tt
t = tt.Turtle()
screen = tt.Screen()
tt.screensize(1000,1000)
screen.bgcolor("#ffff66")
t.speed(5)
class IndianFlag:
    # draw pole
    def Pole():
        t.penup()
        t.goto(-170,-300)
        t.pendown()
        t.color("Brown")
        t.begin_fill()
        t.pensize(2)
        t.fd(100)
        t.lt(90)
        t.fd(30)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(30)
        t.end_fill()
        t.penup()
        t.goto(-130,-270)
        t.pendown()
        t.begin_fill()
        t.bk(500)  
        t.lt(90)
        t.fd(20)
        t.rt(90)
        t.fd(500)
        t.end_fill()
        t.begin_fill()
        t.bk(500)
        t.lt(90)
        t.bk(10)
        t.circle(10)
        t.end_fill()
    #---------------------------------------------------------------
    # draw flag
    def Flag():
        # Orange Region Start
        def orange():
            t.color("orange")
            t.pensize(3)
            t.penup()
            t.fd(10)
            t.down()
            t.begin_fill()
            for x in range(-110,120):
                y = math.sin(math.radians((x))) #generate angle
                t.goto(x,(y*(-20)+210))
            
            t.rt(90)
            t.fd(30)
            t.rt(90)
            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+180))

            t.end_fill() # end of orange region

        # White Region Start
        def white():
            
            t.pensize(3)
            t.penup()
            t.pendown()

            t.color("White")
            t.begin_fill()\
            # Repeating Orange Part Border
            for x in range(-110,120):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+180))
            
            t.rt(90)
            t.bk(30)
            t.rt(90)

            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+150))
            t.end_fill() #end of White Region
            
        # Green Region Start
        def green():
            t.pensize(3)
            t.color("Green")
            t.begin_fill()
            # Repeating White Part Border
            for x in range(-110,120):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+150))
        
            t.rt(90)
            t.fd(30)
            t.rt(90)

            for x in range(120,-110,-1):
                y = math.sin(math.radians((x)))
                t.goto(x,(y*(-20)+120))
            t.end_fill() # end of Green Region

        # draw Ashoka Chakra
        def Ashoka():
            t.pensize(4)
            t.penup()
            t.goto(0,179)
            t.pendown()
            t.pencolor("navy")
            t.circle(14)
            t.penup()
            t.rt(90)
            t.bk(14)
            t.pendown()
            t.pensize(1)
            for i in range(24):
                t.fd(15)
                t.bk(15)
                t.lt(15)
        # end of Ashoka Chakra

        # 75 independance day
        def SevenFive():
            t.hideturtle()
            tt.delay(15)
            t.penup()
            t.setpos(250,-185)
            t.pendown()
            t.write("75",font=("Castellar",120,"bold"),align='right')
            t.showturtle()
            t.penup()
            t.goto(220,-105)
            t.pendown()
            t.pensize(5)
            t.circle(35)
            t.rt(90)
            t.pensize(2)
            t.bk(35)
            for i in range(24):
                t.fd(33)
                t.bk(33)
                t.lt(15)
            t.hideturtle()
            t.penup()
            t.setpos(10,-185)
            t.pendown()
            t.write("Years of Independence",font=("TimesNewRoman",25))

        # functionCall       
        orange()
        white()
        green()
        Ashoka()
        SevenFive()
    
    # Whole program
    Pole() 
    Flag()       

#class 
IndianFlag()

tt.hideturtle()
tt.exitonclick()
#end of program