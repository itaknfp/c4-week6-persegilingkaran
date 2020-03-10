import turtle

if __name__ == "__main__":
	print ('MEMBUAT PERSEGI')
	a = int(input("Masukkan sisi: "))

	n= turtle
	n.shape('turtle')
	n.color('red')
	n.down()
	n.forward(a)
	n.left(90)
	n.forward(a)
	n.left(90)
	n.forward(a)
	n.left(90)
	n.forward(a)
	n.left(90)
	n.penup()
	
	b = int (input("masukan jari-jari: "))
	turtle.color("blue")
	turtle.pencolor("black")
	turtle.begin_fill()    
	turtle.pen()
	turtle.penup()
	turtle.goto(200, -5)
	turtle.pendown()
	turtle.circle(b)
	