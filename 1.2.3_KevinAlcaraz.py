#   a123_apple_1.py
import turtle as trtl
import random as rand
 
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

screen_width = 400
screen_height = 400
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","I","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
current_letter = "A"

current_letters = []
apple_list = []
number_of_apples = 5


#background
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

 
wn.bgpic("background.gif")
#apple = trtl.Turtle()
#apple.penup()
wn.tracer(False)
 

 
# given a turtle, set that turtle to be shaped by the image file

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0, length_of_list)
    current_letter = letter_list.pop(index)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    draw_apple(active_apple,current_letter)
    current_letters.append(current_letter)

def draw_apple(active_apple, letter):
 active_apple.shape(apple_image)
 active_apple.st()
 draw_letter(letter, active_apple)
 wn.update() 

def apple_fall(letter):
    wn.tracer(True)
    index = current_letters.index(letter)
    current_letters.pop(index)
    active_apple = apple_list.pop(index)
    active_apple.goto(active_apple.xcor(), ground_height)
    active_apple.clear()
    active_apple.ht()
    wn.tracer(False)
    reset_apple(active_apple)
    apple_list.append(active_apple)

def draw_letter(letter, active_apple):
    active_apple.color("white")
    remeber_position = active_apple.position()
    active_apple.setpos(active_apple.xcor() + apple_letter_x_offset, active_apple.ycor() + apple_letter_y_offset)
    active_apple.write(letter, font= ("Ariel", 74, "bold"))
    active_apple.setpos(remeber_position)

for i in range(number_of_apples):
    active_apple= trtl.Turtle(shape = apple_image)
    active_apple.penup()
    reset_apple(active_apple)
    apple_list.append(active_apple)








def check_letter_A():
  if ("A" in current_letters):
    apple_fall("A")
def check_letter_B():
  if ("B" in current_letters):
    apple_fall("B")
def check_letter_C():
  if ( "C"in current_letters):
    apple_fall("C")
def check_letter_D():
  if ("D" in current_letters):
    apple_fall("D")
def check_letter_E():
  if ("E" in current_letters):
    apple_fall("E")
def check_letter_F():
  if ("F" in current_letters):
    apple_fall("F")
def check_letter_G():
  if ("G" in current_letters):
    apple_fall("G")
def check_letter_H():
  if ( "H"in current_letters):
    apple_fall("H")
def check_letter_I():
  if ( "I"in current_letters):
    apple_fall("I")
def check_letter_J():
  if ( "J"in current_letters):
    apple_fall("J")
def check_letter_K():
  if ( "K"in current_letters):
    apple_fall("K")
def check_letter_L():
  if ("L" in current_letters):
    apple_fall("L")
def check_letter_M():
  if ("M" in current_letters):
    apple_fall("M")
def check_letter_N():
  if ("N" in current_letters):
    apple_fall("N")
def check_letter_O():
  if ("O" in current_letters):
    apple_fall("O")
def check_letter_P():
  if ("P" in current_letters):
    apple_fall("P")
def check_letter_Q():
  if ("Q" in current_letters):
    apple_fall("Q")
def check_letter_R():
  if ("R" in current_letters):
    apple_fall("R")
def check_letter_S():
  if ("S" in current_letters):
    apple_fall("S")
def check_letter_T():
  if ("T" in current_letters):
    apple_fall("T")
def check_letter_U():
  if ("U" in current_letters):
    apple_fall("U")
def check_letter_V():
  if ("V" in current_letters):
    apple_fall("V")
def check_letter_W():
  if ("W" in current_letters):
    apple_fall("W")
def check_letter_X():
  if ("X" in current_letters):
    apple_fall("X")
def check_letter_Y():
  if ("Y" in current_letters):
    apple_fall("Y")
def check_letter_Z():
  if ("Z" in current_letters):
    apple_fall("Z")


draw_apple(active_apple, "A" )
wn.onkeypress(check_letter_A, "a")
wn.onkeypress(check_letter_B, "b")
wn.onkeypress(check_letter_C, "c")
wn.onkeypress(check_letter_D, "d")
wn.onkeypress(check_letter_E, "e")
wn.onkeypress(check_letter_F, "f")
wn.onkeypress(check_letter_G, "g")
wn.onkeypress(check_letter_H, "h")
wn.onkeypress(check_letter_I, "i")
wn.onkeypress(check_letter_J, "j")
wn.onkeypress(check_letter_K, "k")
wn.onkeypress(check_letter_L, "l")
wn.onkeypress(check_letter_M, "m")
wn.onkeypress(check_letter_N, "n")
wn.onkeypress(check_letter_O, "o")
wn.onkeypress(check_letter_P, "p")
wn.onkeypress(check_letter_Q, "q")
wn.onkeypress(check_letter_R, "r")
wn.onkeypress(check_letter_S, "s")
wn.onkeypress(check_letter_T, "t")
wn.onkeypress(check_letter_U, "u")
wn.onkeypress(check_letter_V, "v")
wn.onkeypress(check_letter_W, "w")
wn.onkeypress(check_letter_X, "x")
wn.onkeypress(check_letter_Y, "y")
wn.onkeypress(check_letter_Z, "z")


wn.listen()
wn.mainloop()
