#Import Modules
import random
from colorama import Back,Style
import time
import sys


""""""""""""

# Title: Starry Night
# Author: Srishivansh5404
# Date: January 23,2023
# Availability: geeksforgeeks.com
#function for pluto

import turtle
import math

def pluto():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed(0)
  w.tracer(0)
   
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   
  # giving the color of pen to our turtle
  # for drawing
  t.color("white")
   
  # giving title to our turtle graphics window
  w.title("Starry Sky")
   
  # making function to draw the stars
  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 70)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("tan")
   
  # start filling the color
  t.begin_fill()
   
  t.circle(30)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   



""""""""""""""""""""
#function for neptune
def neptune():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed(0)
  w.tracer(0)
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 70)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("cornflowerblue")
   
  # start filling the color
  t.begin_fill()
   
  t.circle(120)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   
  # terminated the window after clicking



""""""""""""""""""""
#function for uranus
def uranus():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed(0)
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 70)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("lightskyblue")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(140)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()



""""""""""""""""""""
#function for saturn
def saturn():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed("fastest")
   
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 170)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("mediumpurple")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(140)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   


""""""""""""""""""""
#function for jupiter
def jupiter():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed(0)
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 60)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("brown")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(10)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()

  #turtle.done()



""""""""""""""""""""
#function for mars
def mars():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed(0)
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 70)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("firebrick")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(50)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   



""""""""""""""""""""
#function for earth
def earth():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed("fastest")
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 170)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("dodgerblue")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(100)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   





""""""""""""""""""""
#function for venus
def venus():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed("fastest")
   
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 170)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("goldenrod")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(90)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   




""""""""""""""""""""
#function for mercury
def mercury():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed("fastest")
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 170)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("orangered")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(35)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   




""""""""""""""""""""
#function for sun
def sun():
  # importing libraries
  import turtle
  import random
   
   
  # creating turtle object
  t = turtle.Turtle()
   
  # to activate turtle graphics Screen
  w = turtle.Screen()
   
  # setting speed of turtle
  t.speed("fastest")
  w.tracer(0)
  
  # giving the background color of turtle
  # graphics screen
  w.bgcolor("black")
   

  # for drawing
  t.color("white")
   

  w.title("Starry Sky")
   

  def stars():
      for i in range(5):
          t.fd(10)
          t.right(144)
   
   
  # loop for making number of stars
  for i in range(100):
     
      # generating random integer values for x and y
      x = random.randint(-640, 640)
      y = random.randint(-330, 330)
       
      # calling the function stars to draw the
      # stars at random x,y value
      stars()
       
      # took up the turtle's pen
      t.up()
       
      # go at the x,y coordinate generated above
      t.goto(x, y)
       
      # took down the pen to draw
      t.down()
   
  t.up()
   
  # going at the specific coordinated
  t.goto(0, 60)
   
  # took down the pen to start drawing
  t.down()
   
  # giving color to turtle's pen
  t.color("orange")
   
  # start filling the color
  t.begin_fill()
   
  #  
  t.circle(200)
   
  # stop filling the color
  t.end_fill()
   
  # after drawing hiding the turtle from
  # the window
  t.hideturtle()
   

#Game Functions
def roll_dice(s,e):
  return random.randint(s,e)
  
def writeSlowly(text):
  for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(.05)
    
def writeSlowlyA(text,alt):
  for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(alt)
def mathGameIntro():
  
  delay()
  writeSlowly(Back.BLUE+ "Welcome to the math game! \n")
  writeSlowly("Instructions: You will be given 4 math questions. ")
  writeSlowly("If you get them all right, you move on to the next level! You get one life ")
  writeSlowly("per level and there are a total of 9 levels. \n")
  writeSlowly("Oh, and one more thing! Each level you pass, you can travel to a new planet in the solar system! \n")
  writeSlowly("You will begin on planet Pluto. \n")
  pluto()

  delay()
  
  writeSlowly("Are you ready to play!(Y/N) \n")
  ready = input()

  while (ready=="N"):
    writeSlowly("Don't worry, you will slowly improve! Don't be afraid to make mistakes! \n")
    delay()
    writeSlowly("Would you like to continue with the Math Game(M/S) \n")
    ready=input()
    if (ready=="S"):
      spellingGame()
  
  if ready == "Y" or ready=="M":
    mathGame()

def mathGame():

  
  writeSlowly("Let's Get Started! \n")
  score=0
  life=1
  level = 1
  numQuestions=0
  correct=0
    
    
  writeSlowly("Level "+str(level)+" - Pluto \n")
  delay()

  ##Level 1
  while (numQuestions<4 and life>0 and level==1):
    num1 = roll_dice(1,6)
    num2 = roll_dice(1,10)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1
    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay()
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 1! \n"+"Score: "+str(score))
      neptune()
      writeSlowly("\nYou have reached neptune! Click the screen to start your journey to the next planet. \n")
      delay()
      level+=1
      numQuestions=0
      correct=0
       
  writeSlowly("Level "+str(level)+" - Neptune \n")
  delay()

  ##Level 2
  while (numQuestions<4 and life>0 and level==2):  
    num1 = roll_dice(1,15)
    num2 = roll_dice(1,15)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 

    if (correct==4):
      writeSlowly("Congratulations! You passed level 2! \nScore: "+str(score))
      writeSlowly("\nYou have reached Uranus! \n")
      uranus()
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Uranus \n")
  delay()
  
  ##Level 3
  while (numQuestions<4 and life>0 and level==3):  
    num1 = roll_dice(10,30)
    num2 = roll_dice(10,30)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 3! \nScore: "+str(score))
      writeSlowly("\nYou have reached Saturn! \n")
      saturn()
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Saturn \n")
  delay()
  
 ##Level 4
  while (numQuestions<4 and life>0 and level==4):  
    num1 = roll_dice(10,70)
    num2 = roll_dice(10,30)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
    if (correct==4):
      writeSlowly("Congratulations! You passed level 4! \nScore: "+str(score))
      jupiter()
      writeSlowly("\nYou have reached Jupiter! \n")
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Jupiter \n")
  delay()
  
  #Level 5
  while (numQuestions<4 and life>0 and level==5):  
    num1 = roll_dice(10,99)
    num2 = roll_dice(10,99)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 5! \nScore: "+str(score))
      writeSlowly("\nYou have reached Mars! \n")
      mars()
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Mars \n")
  delay()
  
   #Level 6
  while (numQuestions<4 and life>0 and level==6):  
    num1 = roll_dice(30,99)
    num2 = roll_dice(30,99)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 6! \nScore: "+str(score))
      writeSlowly("\nYou have reached Earth! \n")
      earth()
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Earth \n")
  #Level 7
  while (numQuestions<4 and life>0 and level==7):  
    num1 = roll_dice(50,100)
    num2 = roll_dice(50,100)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 7! \nScore: "+str(score))
      writeSlowly("\nYou have reached Venus! \n")
      venus()
      delay()
      level+=1
      numQuestions=0
      correct=0

  
  writeSlowly("Level "+str(level)+" - Venus \n")
  delay()

   #Level 8
  while (numQuestions<4 and life>0 and level==8):  
    num1 = roll_dice(70,150)
    num2 = roll_dice(70,150)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed level 8! \nScore: "+str(score))
      writeSlowly("\nYou have reached Mercury! This is the last level\n")
      mercury()
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Level "+str(level)+" - Mercury \n")
  delay()
  
     #Level 9
  while (numQuestions<4 and life>0 and level==9):  
    num1 = roll_dice(100,200)
    num2 = roll_dice(80,200)
      
    writeSlowly("Question:"+str(numQuestions+1)+"\nWhat is "+str(num1)+" + "+str(num2)+"? \n")
    answer = int(input())
      
    if (answer==num1+num2):
      writeSlowly("Correct! \n")
      score+=10
      correct+=1
      numQuestions+=1

    else:
      writeSlowly("Incorrect! "+str(num1)+" + "+str(num2)+" = "+str(num1+num2)+"\n")
      life-=1
      numQuestions+=1

    if (life==0):
      writeSlowly("You lost all your lives! \n")
      delay()
      writeSlowly("Your score was "+str(score)+"\n")
      delay()
      writeSlowly("Would you like to play again? (Y/N) \n")
      playAgain=input()
      if (playAgain=="Y"):
        score=0
        numQuestions=0
        level=1
        life=1
        mathGame()
      else:
        writeSlowly("Thanks for playing! \n")
        delay() 
  
    if (correct==4):
      writeSlowly("Congratulations! You passed the Math game! \nScore: "+str(score))
      sun()
      writeSlowly("\nYou have reached the Sun! \n")
      delay()
      level+=1
      numQuestions=0
      correct=0

  writeSlowly("Now you are a shining star just like the sun!!!!!! \n")
  delay()


def spellingGame():
  writeSlowly("Welcome to the spelling game! \n")

def delay():
  writeSlowlyA("\n\n",.2)
  
#Introduction Prompt
Intro = Back.LIGHTMAGENTA_EX+ "Welcome to Space Quest! To start, please enter your name: \n"
writeSlowly(Intro)
userName = input()

#Processes User name
delay()
writeSlowlyA("\n. . .\n",.4)
writeSlowly("Welcome "+userName+"! \n")
writeSlowly("Would you like to practice your math skills or your spelling skills? (M/S)\n\n")

#Game Choice
game=input()



while(game != "M" and game != "S"):
  writeSlowly("Please enter M or S: \n")
  game=input()
  
print(Style.RESET_ALL)

if game == "M":
  mathGameIntro()

elif game=="S":
  spellingGame()




