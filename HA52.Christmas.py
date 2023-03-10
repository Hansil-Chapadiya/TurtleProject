import turtle as t
tt = t.Turtle()
tt.speed(10)
screen = t.Screen()
t.screensize(1000,1000)
screen.bgcolor("#00008B")
class Christmas:
    global body,Land,RightHand,LeftHand,Scaf,Eyes,word,Cros,Tree,star,Moon,Hat,Smile,IceStone,Nose
    def body():
        tt.begin_fill()
        tt.pensize(3)
        tt.color('WHITE')
        tt.circle(80)
        tt.rt(180)
        tt.circle(120)
        tt.end_fill()

    def RightHand():
        tt.penup()
        tt.lt(15)
        tt.bk(145)
        tt.pendown()
        tt.color('BROWN')
        tt.lt(60)
        tt.fd(60)
        tt.lt(125)
        tt.fd(30)
        tt.bk(30)
        tt.rt(160)
        tt.fd(39)
        tt.bk(100)

    def LeftHand():
        tt.penup()
        tt.rt(45)
        tt.fd(320)
        tt.pendown()
        tt.rt(60)
        tt.bk(60)
        tt.lt(45)
        tt.fd(70)  
        tt.bk(70)
        tt.rt(30)
        tt.bk(46) 

    def Eyes():
        tt.color('BLACK')
        tt.penup()
        tt.rt(65)
        tt.fd(160)
        tt.pendown()
        tt.begin_fill()
        tt.circle(5)
        tt.end_fill()
        tt.penup()
        tt.lt(125)
        tt.bk(50)
        tt.pendown()
        tt.begin_fill()
        tt.circle(5)
        tt.end_fill()

    def Nose():
        tt.penup()
        tt.lt(30)
        tt.fd(30)
        tt.pendown()
        tt.color('RED')
        tt.begin_fill()
        tt.rt(95)
        tt.bk(40)
        tt.rt(150)
        tt.bk(30)
        tt.rt(70)
        tt.bk(22)
        tt.end_fill()

    def Smile():
        tt.penup()
        tt.fd(30)
        tt.lt(45)
        tt.bk(20)
        tt.rt(40)
        tt.fd(30)
        tt.pendown()
        tt.color('BROWN')
        tt.circle(20,180)

    def Land():
        tt.color('#C39B77')
        tt.penup()
        tt.setpos(0,10)
        tt.bk(250)
        tt.pendown()
        tt.begin_fill()
        tt.rt(90)
        tt.bk(800)
        tt.fd(1560)
        tt.rt(90)
        tt.fd(200)
        tt.lt(90)
        tt.bk(1600)
        tt.lt(90)
        tt.fd(200)
        tt.end_fill()

    def IceStone():
        tt.color('White')
        tt.penup()
        tt.setpos(-350,-250)
        tt.rt(30)
        tt.pendown()
        tt.begin_fill()
        tt.circle(260,250)
        tt.end_fill()

    def Scaf():
        tt.color('Purple')
        tt.penup()
        tt.setpos(-39,-3)
        tt.rt(5)
        tt.pendown()
        tt.begin_fill()
        tt.circle(50,105)
        tt.end_fill()
        tt.setpos(-42,4)
        tt.rt(110)
        tt.begin_fill()
        tt.circle(50,120)
        tt.end_fill()
        tt.setpos(0,0)
        tt.begin_fill()
        tt.bk(90)
        tt.rt(45)
        tt.bk(30)
        tt.rt(135)
        tt.bk(90)
        tt.end_fill()

    def Hat():
        tt.color('Black')
        tt.penup()
        tt.goto(0,0)
        tt.rt(145)
        tt.fd(150)
        tt.pendown()
        tt.fillcolor('BLACK')
        tt.begin_fill()
        tt.left(90)
        tt.fd(45)
        tt.bk(95)
        tt.lt(90)
        tt.bk(20)
        tt.rt(90)
        tt.fd(30)
        tt.rt(90)
        tt.fd(30)
        tt.lt(90)
        tt.fd(40)
        tt.rt(90)
        tt.bk(30)
        tt.lt(90)
        tt.fd(30)
        tt.rt(90)
        tt.bk(20)
        tt.end_fill()

    def Moon():
        tt.penup()
        tt.setpos(250,250)
        tt.rt(125)
        tt.pendown()
        tt.color("#DAA520")
        tt.begin_fill()
        tt.circle(70,150)
        tt.end_fill()

    def star():
        tt.penup()
        tt.setpos(100,278)
        tt.pendown()
        tt.color('Yellow')
        tt.begin_fill()
        for i in range(5):
            tt.fd(15)            
            tt.rt(144)
        tt.end_fill()
        tt.penup()
        tt.setpos(50,178)
        tt.pendown()
        tt.begin_fill()
        for i in range(5):
            tt.fd(20)
            tt.rt(144)
        tt.end_fill()
        tt.penup()
        tt.setpos(-410,300)
        tt.pendown()
        tt.begin_fill()
        for i in range(5):
            tt.fd(40)
            tt.rt(144)
        tt.end_fill()
        tt.penup()
        tt.setpos(-210,278)
        tt.pendown()
        tt.begin_fill()
        for i in range(5):
            tt.fd(70)
            tt.rt(144)
        tt.end_fill()
        tt.penup()
        tt.setpos(-510,180)
        tt.pendown()
        tt.begin_fill()
        for i in range(5):
            tt.fd(50)
            tt.rt(144)
        tt.end_fill()
        tt.penup()
        tt.setpos(510,178)
        tt.pendown()
        tt.begin_fill()
        for i in range(5):
            tt.fd(60)
            tt.rt(144)
        tt.end_fill()

    def Tree():
        tt.color('#654321')
        tt.penup()
        tt.setpos(500,-240)
        tt.pendown()
        tt.begin_fill()
        tt.lt(60)
        tt.bk(40)
        tt.lt(90)
        tt.bk(100)
        tt.rt(90)
        tt.fd(40)
        tt.rt(90)
        tt.bk(100)
        tt.fd(100)
        tt.end_fill()
        tt.color('GREEN')
        tt.begin_fill()
        tt.lt(90)
        tt.fd(100)
        tt.rt(135)
        tt.fd(100)
        tt.lt(137)
        tt.fd(60)
        tt.rt(140)
        tt.fd(80)
        tt.lt(137)
        tt.fd(40)
        tt.rt(130)
        tt.fd(120)
        tt.end_fill()
        tt.color('GREEN')
        tt.begin_fill()
        tt.lt(-95)
        tt.fd(120)
        tt.rt(135)
        tt.fd(40)
        tt.lt(140)
        tt.fd(80)
        tt.rt(140)
        tt.fd(60)
        tt.lt(140)
        tt.fd(110)
        tt.rt(139)
        tt.fd(160)
        tt.end_fill()

    def Cros():
        tt.color('WHITE')
        tt.penup()
        tt.setpos(500,70)
        tt.pendown()
        tt.begin_fill()
        tt.rt(180)
        tt.fd(20)
        tt.lt(90)
        tt.fd(30)
        tt.rt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.rt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.rt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.lt(90)
        tt.fd(20)
        tt.rt(90)
        tt.fd(30)
        tt.end_fill()

    def word():
        tt.color('RED')
        tt.penup()
        tt.setpos(-30,-380)
        tt.pendown()
        style = ('Edwardian Script ITC',90,'bold')
        tt.write('Merry Christmas', align='center', font=style)
        t.delay(5)

    def FunctionCall():
        global body,Land,RightHand,LeftHand,Scaf,Eyes,word,Cros,Tree,star,Moon,Hat,Smile,IceStone,Nose
        body()
        RightHand()
        LeftHand()
        Eyes()
        Nose()
        Smile()
        Land()
        IceStone()
        Scaf()
        Hat()
        Moon()
        star()
        Tree()
        Cros()
        word()

    FunctionCall()

Christmas()
#t.showturtle() 
tt.hideturtle() 
t.exitonclick()
 