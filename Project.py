#**********************  Game.py  *********************
#
# Name: Cristian Salinas
#
# Course: CSCI 1470
#
# Assignment: Project Game
#
# Algorithm:
##      Start
##      import turtle
##      import random
##      import math
##      import os
##      ###################################################################################################
##
##      ###################################################################################################
##      #Set up Screen
##      screen = turtle.Screen()
##      screen.bgcolor("white")
##      screen.title("The Map")
##      set background pic to ("StonesHandDrawnAnti.gif")
##      set screen size to a 800 x 800 box
##
##      #Draw Border
#       Draw a border to fit the dimensions of the background picture
##
##
##      #Sword in Stone
##      turtle.register_shape("Sword in Stone.gif")
##      swordinstone = turtle.Turtle()
##      swordinstone.penup()
##      swordinstone.shape("Sword in Stone.gif")
##      swordinstone.left(90)
##      swordinstone.forward(100)
##
##      #Cavern
##      turtle.register_shape("Black.gif")
##      black = turtle.Turtle()
##      black.hideturtle()
##      black.speed(0)
##      black.penup()
##      black.shape("Black.gif")
##
##      #Bow and Arrow
##      Register all of the arrow shapes to be used later in the code 
##      turtle.register_shape("Bow Up.gif")
##      turtle.register_shape("Bow Down.gif")
##      turtle.register_shape("Bow Left.gif")
##      turtle.register_shape("Bow Right.gif")
##      turtle.register_shape("Arrow Up.gif")
##      turtle.register_shape("Arrow Down.gif")
##      turtle.register_shape("Arrow Left.gif")
##      turtle.register_shape("Arrow Right.gif")
##      turtle.register_shape("Bow and Arrow Up.gif")
##      turtle.register_shape("Bow and Arrow Down.gif")
##      turtle.register_shape("Bow and Arrow Left.gif")
##      turtle.register_shape("Bow and Arrow Right.gif")
##      bowandarrow = turtle.Turtle()
##      bow = turtle.Turtle()
##      arrow = turtle.Turtle()
##      bowandarrow.hideturtle()
##      bow.hideturtle()
##      arrow.hideturtle()
##      bowandarrow.shape("Bow and Arrow Right.gif")
##      bow.shape("Bow Right.gif")
##      arrow.shape("Arrow Right.gif")
##      arrow.turtlesize(5)
##      bowandarrow.speed(0)
##      bow.speed(0)
##      arrow.speed(0)
##      bowandarrow.penup()
##      bow.penup()
##      arrow.penup()
##
##      #Bridge
##      turtle.register_shape("Bridge.gif")
##      bridge = turtle.Turtle()
##      bridge.penup()
##      bridge.speed(0)
##      bridge.shape("Bridge.gif")
##      bridge.hideturtle()
##      ###################################################################################################
##
##      ###################################################################################################
##      #Register Shapes
##      Register all of the shapes that will be used in the entire code that havent already been registered
##      turtle.register_shape("Front.gif")
##      turtle.register_shape("Back.gif")
##      turtle.register_shape("Left.gif")
##      turtle.register_shape("Right.gif")
##      turtle.register_shape("Stone.gif")
##      turtle.register_shape("Back Stand.gif")
##      turtle.register_shape("Back Block.gif")
##      turtle.register_shape("Back Attack.gif")
##      turtle.register_shape("Front Stand.gif")
##      turtle.register_shape("Front Block.gif")
##      turtle.register_shape("Front Attack.gif")
##      turtle.register_shape("Right Stand.gif")
##      turtle.register_shape("Right Block.gif")
##      turtle.register_shape("Right Attack.gif")
##      turtle.register_shape("Left Stand.gif")
##      turtle.register_shape("Left Block.gif")
##      turtle.register_shape("Left Attack.gif")
##      turtle.register_shape("Heart.gif")
##      turtle.register_shape("Half Heart.gif")
##      turtle.register_shape("Door.gif")
##      turtle.register_shape("Skeleton.gif")
##      turtle.register_shape("Skeleton Attack.gif")
##      turtle.register_shape("Damage Skeleton.gif")
##      turtle.register_shape("Door2.gif")
##      turtle.register_shape("SkeletonStrong.gif")
##      turtle.register_shape("SkeletonStrong Attack.gif")
##      turtle.register_shape("Damage SkeletonStrong.gif")
##      turtle.register_shape("Boss.gif")
##      turtle.register_shape("Boss Attack.gif")
##      turtle.register_shape("Damage Boss.gif")
##      ###################################################################################################
##
##      ###################################################################################################
##      #Door
##      Create all doors that will be used in the code 
##      door = turtle.Turtle()
##      door.shape("Door.gif")
##      door.penup()
##      door.speed(0)
##      door.setposition(-3, 305)
##
##      #Room 1
##      door_open = turtle.Turtle()
##      door_open.hideturtle()
##      door_open.penup()
##      door_open.turtlesize(5)
##      door_open.left(90)
##      door_open.setposition(0,265)
##
##      #Door 2
##      door2 = turtle.Turtle()
##      door2.hideturtle()
##      door2.shape("Door2.gif")
##      door2.turtlesize(5)
##      door2.penup()
##      door2.speed(0)
##      door2.setposition(305, 3)
##
##      #Room 2
##      door2_open = turtle.Turtle()
##      door2_open.hideturtle()
##      door2_open.penup()
##      door2_open.turtlesize(5)
##      door2_open.setposition(310,0)
##
##      #Door 3
##      door3 = turtle.Turtle()
##      door3.hideturtle()
##      door3.shape("Door2.gif")
##      door3.turtlesize(5)
##      door3.penup()
##      door3.speed(0)
##      door3.setposition(305, 3)
##
##      #Room 3
##      door3_open = turtle.Turtle()
##      door3_open.hideturtle()
##      door3_open.penup()
##      door3_open.turtlesize(5)
##      door3_open.setposition(310,0)
##
##      #Door 4
##      door4 = turtle.Turtle()
##      door4.hideturtle()
##      door4.left(90)
##      door4.shape("Door.gif")
##      door4.turtlesize(5)
##      door4.penup()
##      door4.speed(0)
##      door4.setposition(-3, 305)
##
##      #Room 4
##      door4_open = turtle.Turtle()
##      door4_open.left(90)
##      door4_open.hideturtle()
##      door4_open.penup()
##      door4_open.turtlesize(5)
##      door4_open.setposition(0,265)
##
##      ###################################################################################################
##
##      ###################################################################################################
##      #Create Enemies
##      Create every enemy and boss that will be diplayed in the game and set their position far away so that they cant be seen
##      enemy = turtle.Turtle()
##      enemy.hideturtle()
##      enemy.shape("Skeleton.gif")
##      enemy.turtlesize(5)
##      enemy.penup()
##      enemy.speed(0)
##      enemy.setposition(0,600)
##
##      enemy2 = turtle.Turtle()
##      enemy2.hideturtle()
##      enemy2.shape("Skeleton.gif")
##      enemy2.turtlesize(5)
##      enemy2.penup()
##      enemy2.speed(0)
##      enemy2.setposition(0,600)
##
##      enemy3 = turtle.Turtle()
##      enemy3.hideturtle()
##      enemy3.shape("Skeleton.gif")
##      enemy3.turtlesize(5)
##      enemy3.penup()
##      enemy3.speed(0)
##      enemy3.setposition(0,600)
##
##      enemy4 = turtle.Turtle()
##      enemy4.hideturtle()
##      enemy4.shape("Skeleton.gif")
##      enemy4.turtlesize(5)
##      enemy4.penup()
##      enemy4.speed(0)
##      enemy4.setposition(0,600)
##
##      enemy5 = turtle.Turtle()
##      enemy5.hideturtle()
##      enemy5.shape("Skeleton.gif")
##      enemy5.turtlesize(5)
##      enemy5.penup()
##      enemy5.speed(0)
##      enemy5.setposition(0,600)
##
##      enemy6 = turtle.Turtle()
##      enemy6.hideturtle()
##      enemy6.shape("Skeleton.gif")
##      enemy6.turtlesize(5)
##      enemy6.penup()
##      enemy6.speed(0)
##      enemy6.setposition(270,225)
##
##      enemy7 = turtle.Turtle()
##      enemy7.hideturtle()
##      enemy7.shape("Skeleton.gif")
##      enemy7.turtlesize(5)
##      enemy7.penup()
##      enemy7.speed(0)
##      enemy7.setposition(270,0)
##
##      enemy8 = turtle.Turtle()
##      enemy8.hideturtle()
##      enemy8.shape("Skeleton.gif")
##      enemy8.turtlesize(5)
##      enemy8.penup()
##      enemy8.speed(0)
##      enemy8.setposition(270,-225)
##
##      enemy9 = turtle.Turtle()
##      enemy9.hideturtle()
##      enemy9.shape("SkeletonStrong.gif")
##      enemy9.turtlesize(5)
##      enemy9.penup()
##      enemy9.speed(0)
##      enemy9.setposition(1500,1500)
##
##      enemy10 = turtle.Turtle()
##      enemy10.hideturtle()
##      enemy10.shape("SkeletonStrong.gif")
##      enemy10.turtlesize(5)
##      enemy10.penup()
##      enemy10.speed(0)
##      enemy10.setposition(1500,1500)
##
##      enemy11 = turtle.Turtle()
##      enemy11.hideturtle()
##      enemy11.shape("SkeletonStrong.gif")
##      enemy11.turtlesize(5)
##      enemy11.penup()
##      enemy11.speed(0)
##      enemy11.setposition(1500, 1500)
##
##      #Creating Boss
##      boss = turtle.Turtle()
##      boss.hideturtle()
##      boss.shape("Boss.gif")
##      boss.turtlesize(8)
##      boss.penup()
##      boss.speed(0)
##      boss.setposition(1500, 1500)
##
##      ###################################################################################################
##
##      ###################################################################################################
##      #Create Hero
##      Create the hero that will be playing the game 
##      hero = turtle.Turtle()
##      hero.shape("Back.gif")
##      hero.turtlesize(5)
##      hero.speed(0)
##      hero.penup()
##      hero.left(90)
##      hero.setposition(0,-50)
##      ###################################################################################################
##
##      ###################################################################################################
##      #Creating Hearts
##      Create the hearts that will be displayed in the top left hand corner so that the player can always see his remaining health 
##      heart1 = turtle.Turtle()
##      heart1.shape("Heart.gif")
##      heart1.penup()
##      heart1.speed(0)
##      heart1.setposition(-325, 300)
##
##      heart2 = turtle.Turtle()
##      heart2.shape("Heart.gif")
##      heart2.penup()
##      heart2.speed(0)
##      heart2.setposition(-275, 300)
##
##      heart3 = turtle.Turtle()
##      heart3.shape("Heart.gif")
##      heart3.penup()
##      heart3.speed(0)
##      heart3.setposition(-225, 300)
##
##      heart4 = turtle.Turtle()
##      heart4.shape("Heart.gif")
##      heart4.penup()
##      heart4.speed(0)
##      heart4.setposition(-175, 300)
##
##      heart5 = turtle.Turtle()
##      heart5.shape("Heart.gif")
##      heart5.penup()
##      heart5.speed(0)
##      heart5.setposition(-125, 300)
##      ###################################################################################################
##
##      ###################################################################################################
##      #Set up variables that will change based on the hero's movements and actions of the player
##      speed = .0001
##      move_speed = 20
##      count    = 0
##      offense  = 0
##      defense  = 0
##      chs      = 0    #(C.H.S acronym for "Change Hero Shape")
##      enemyvariable = 0
##      enemyhealth  = 5
##      enemy2health = 5
##      enemy3health = 5
##      enemy4health = 5
##      enemy5health = 5
##      enemy6health = 5
##      enemy7health = 5
##      enemy8health = 5
##      enemy9health = 10
##      enemy10health = 10
##      enemy11health = 10
##      enemyspeed = 5
##      health = 10
##      bowstatus = 0
##      herograbbedsword = 0
##      bowheading = 0
##      arrowheading = 0
##      roomboundaries = 1
##      bosshealth = 15
##      blockstatus = 0
##      ###################################################################################################
##
##      ###################################################################################################
##      #Define Functions
##      def heromovement():
##      The player will not be alowwed to move out side of the boundary that was set earlier and if he/she does then the funcitions that move the player with
##      the arrow keys will perforn and place beack within the borders, for the third room however then player will not be able to move past the cavern
##      unless her/she defeats all of the enemies
##
##        global roomboundaries
##          #Boundary Checking
##        if hero.xcor() >  300:
##           turnleft()
##
##        if hero.xcor() < -300:
##           turnright()
##
##        if hero.ycor() >  300:
##           downbackward()
##
##        if hero.ycor() < -300:
##           upforward()
##
##        if enemyvariable == 2 and enemy6health > 0 and enemy7health > 0 and enemy8health > 0:
##          if hero.xcor() > -150:
##            turnleft()
##
##          if hero.xcor() < -300:
##            turnright()
##
##          if hero.ycor() >  300:
##            downbackward()
##
##          if hero.ycor() < -300:
##            upforward()
##
##          
##      def grabsword():
##      The player will be able to pull the sword from the stone and when he/she does it will change the appearence for the turtle
##        global chs
##        global herograbbedsword
##        chs = 1
##        herograbbedsword = 1
##        swordinstone.shape("Stone.gif")
##        hero.shape("Back Stand.gif")
##
##      def upforward():
##      Fucntions for player to move upward
##        if chs == 1:
##          global offense
##          global defense
##          global bowheading
##          global arrowheading
##          offense = 1
##          defense = 1
##          bowheading = 1
##          arrowheaeding = 1
##          hero.shape("Back Stand.gif")
##          hero.setheading(90)
##          hero.forward(move_speed)
##        else:
##          hero.shape("Back.gif")
##          hero.setheading(90)
##          hero.forward(move_speed)
##
##      def downbackward():
##      Function for player to move downward
##        if chs == 1:
##          global offense
##          global defense
##          global bowheading
##          global arrowheading
##          offense = 2
##          defense = 2
##          bowheading = 2
##          arrowheaeding = 2
##          hero.shape("Front Stand.gif")
##          hero.setheading(270)
##          hero.forward(move_speed)
##        else:
##          hero.shape("Front.gif")
##          hero.setheading(270)
##          hero.forward(move_speed)
##
##      def turnleft():
##      Function for player to move left
##        if chs == 1:
##          global offense
##          global defense
##          global bowheading
##          global arrowheading    
##          offense = 3
##          defense = 3
##          bowheading = 3
##          arrowheaeding = 3
##          hero.shape("Left Stand.gif")
##          hero.setheading(180)
##          hero.forward(move_speed)
##        else:
##          hero.shape("Left.gif")
##          hero.setheading(180)
##          hero.forward(move_speed)
##          
##      def turnright():
##      Function for player to move right
##        if chs == 1:
##          global offense
##          global defense
##          global bowheading
##          global arrowheading    
##          offense = 4
##          defense = 4
##          bowheading = 4
##          arrowheaeding = 4    
##          hero.shape("Right Stand.gif")
##          hero.setheading(0)
##          hero.forward(move_speed)
##        else:
##          hero.shape("Right.gif")
##          hero.setheading(0)
##          hero.forward(move_speed)
##
##      ###################################################################################################
##
##      ###################################################################################################
##      These are the functions that will show the doors when the player has cleared the room and each perfomr specific tasks of
##      subratcing and adding variables once the hero passes a certain threshold  it will place him/her in a certain position
##      def opendoor():
##        global enemyvariable
##        f = math.sqrt(math.pow(hero.xcor()-door_open.xcor(),2) + math.pow(hero.ycor()-door_open.ycor(),2))
##        if f < 50:
##          enemyvariable = 1
##          hero.setposition(0,-260)
##          door_open.forward(300)
##          door.hideturtle()
##          swordinstone.hideturtle()
##          enemy.showturtle()
##          enemy2.showturtle()
##          enemy3.showturtle()
##          enemy4.showturtle()
##          enemy5.showturtle()
##          enemy.setposition(random.randint(-280, 280), random.randint(-200, 200))
##          enemy2.setposition(random.randint(-280, 280), random.randint(-200, 200))
##          enemy3.setposition(random.randint(-280, 280), random.randint(-200, 200))
##          enemy4.setposition(random.randint(-280, 280), random.randint(-200, 200))
##          enemy5.setposition(random.randint(-280, 280), random.randint(-200, 200)) 
##         
##      def opendoor2():
##        global enemyvariable
##        global bowstatus
##        global roomboundaries
##        if enemyhealth <= 0 and enemy2health <= 0 and enemy3health <= 0 and enemy4health <= 0 and enemy5health <= 0: 
##          bowandarrow.showturtle()
##          a = math.sqrt(math.pow(hero.xcor()-bowandarrow.xcor(),2) + math.pow(hero.ycor()-bowandarrow.ycor(),2))
##          if a < 50:
##            bowstatus = bowstatus + 1
##            bowandarrow.hideturtle()
##            bowandarrow.setposition(0,800)
##
##          door2.showturtle()
##          d = math.sqrt(math.pow(hero.xcor()-door2_open.xcor(),2) + math.pow(hero.ycor()-door2_open.ycor(),2))
##          if d < 50:
##            enemyvariable = 2
##            hero.setposition(-260, 0)
##            roomboundaries == 0
##            door2_open.forward(300)
##            door2.forward(800)
##            enemy6.showturtle()
##            enemy7.showturtle()
##            enemy8.showturtle()
##            black.showturtle()
##
##      def opendoor3():
##        global enemyvariable 
##        if enemy6health <= 0 and enemy7health <= 0 and enemy8health <= 0: 
##          bridge.showturtle()
##          door3.showturtle()
##          a = math.sqrt(math.pow(hero.xcor()-door3_open.xcor(),2) + math.pow(hero.ycor()-door3_open.ycor(),2))
##          if a < 50:
##            enemyvariable = 3
##            hero.setposition(-260, 0)
##            door3_open.setposition(1500,1500)
##            door3.setposition(1500,1500)
##            black.setposition(1500,1500)
##            bridge.setposition(1500,1500)
##            enemy9.setposition(random.randint(-250, 250), random.randint(-200, 200))
##            enemy10.setposition(random.randint(-250, 250), random.randint(-200, 200))
##            enemy11.setposition(random.randint(-250, 250), random.randint(-200, 200))
##            enemy9.right(random.randint(0,360))
##            enemy10.right(random.randint(0,360))
##            enemy11.right(random.randint(0,360))
##            enemy9.showturtle()
##            enemy10.showturtle()
##            enemy11.showturtle()
##
##      def opendoor4():
##        global enemyvariable 
##        if  enemy9health <= 0 and enemy10health <= 0 and enemy11health <= 0:
##          door4.showturtle()
##          a = math.sqrt(math.pow(hero.xcor()-door4_open.xcor(),2) + math.pow(hero.ycor()-door4_open.ycor(),2))    
##          if a < 50:
##            door4.setposition(1500,1500)
##            enemyvariable = 4
##            hero.setposition(0,-260)
##            door4_open.forward(300)
##            door4.setposition(0, 900)
##            boss.showturtle()
##            boss.setposition(0,0)  
##            boss.right(random.randint(0,360))
##      ###################################################################################################
##
##      ###################################################################################################
##      The enemies will attack once the x and y coordinates for an enemy and the hero are within a certain range and once that happens a radom number from
##      0 - 250 will generate and if the number becomes a specific integer the enemy will change shape, knockback the hero and subtract from his health
##      changing the appearence of the hearts with  every attack
##      def enemyattack():
##        global health
##        global blockstatus
##        if enemyvariable == 1:
##          a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
##          b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
##          c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
##          d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
##          e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))
##
##          num1 = random.randint(1,250)
##
##          if a < 100:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 1
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy.shape("Skeleton Attack.gif")
##              enemy.shape("Skeleton.gif")
##
##          if b < 100:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 1
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy2.shape("Skeleton Attack.gif")
##              enemy2.shape("Skeleton.gif")
##
##          if c < 100:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 1
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy3.shape("Skeleton Attack.gif")
##              enemy3.shape("Skeleton.gif")
##
##          if d < 100:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 1
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy4.shape("Skeleton Attack.gif")
##              enemy4.shape("Skeleton.gif")
##
##          if e < 100:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 1
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy5.shape("Skeleton Attack.gif")
##              enemy5.shape("Skeleton.gif")
##
##      def enemyattack2():
##        global enemyvariable
##        global health
##        global blockstatus
##        if enemyvariable == 3:
##          a = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
##          b = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
##          c = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))
##         measure the distacne between each enemy and the hero and set to multiple varialbes, once this happens a random number from 0-250 will
##         generate and is the distance between a enemy and player is less than 175 pixels it will attack if the variable lands on specific numbers
##         and subtracts health from theh hero
##          num1 = random.randint(1,250)
##
##          if a < 175:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 2
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy9.shape("SkeletonStrong Attack.gif")
##              enemy9.shape("SkeletonStrong.gif")
##
##          if b < 175:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 2
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy10.shape("SkeletonStrong Attack.gif")
##              enemy10.shape("SkeletonStrong.gif")
##
##          if c < 175:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
##              health = health - 2
##              blockstatus = blockstatus - 1
##              hero.backward(50)
##              for q in range(10):
##                enemy11.shape("SkeletonStrong Attack.gif")
##              enemy11.shape("SkeletonStrong.gif")
##
##      This is similar to the enemy attack functions just that is the hero and enemy are too close the hero will be knocked back and take damage
##      def enemycollision():
##        global enemyvariable
##        global health
##        if enemyvariable == 1:
##          a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
##          b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
##          c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
##          d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
##          e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))
##
##          if a < 50:
##            for q in range(10):
##              enemy.shape("Skeleton Attack.gif")
##            enemy.shape("Skeleton.gif")
##            hero.backward(50)
##            health = health - 1
##            enemy.right(random.randint(0,360))
##
##          if b < 50:
##            for q in range(10):
##              enemy2.shape("Skeleton Attack.gif")
##            enemy2.shape("Skeleton.gif")
##            hero.backward(50)
##            health = health - 1
##            enemy2.right(random.randint(0,360))
##            
##          if c < 50:
##            for q in range(10):
##              enemy3.shape("Skeleton Attack.gif")
##            enemy3.shape("Skeleton.gif")
##            hero.backward(50)
##            health = health - 1
##            enemy3.right(random.randint(0,360))
##            
##          if d < 50:
##            for q in range(10):
##              enemy4.shape("Skeleton Attack.gif")
##            enemy4.shape("Skeleton.gif")
##            hero.backward(50)
##            health = health - 1
##            enemy4.right(random.randint(0,360))
##            
##          if e < 50:
##            for q in range(10):
##              enemy5.shape("Skeleton Attack.gif")
##            enemy5.shape("Skeleton.gif")
##            hero.backward(50)
##            health = health - 1
##            enemy5.right(random.randint(0,360))
##
##
##      def enemycollision2():
##        global health
##        if enemyvariable == 3:
##          a = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
##          b = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
##          c = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))
##
##          if a < 75:
##            for q in range(10):
##              enemy9.shape("SkeletonStrong Attack.gif")
##            enemy9.shape("SkeletonStrong.gif")
##            hero.backward(50)
##            health = health - 2
##            enemy9.right(random.randint(0,360))
##
##          if b < 75:
##            for q in range(10):
##              enemy10.shape("SkeletonStrong Attack.gif")
##            enemy10.shape("SkeletonStrong.gif")
##            hero.backward(50)
##            health = health - 2
##            enemy10.right(random.randint(0,360))
##            
##          if c < 75:
##            for q in range(10):
##              enemy11.shape("SkeletonStrong Attack.gif")
##            enemy11.shape("SkeletonStrong.gif")
##            hero.backward(50)
##            health = health - 2
##            enemy11.right(random.randint(0,360))
##
##      These functions dictate the enemy movement and how they can move within the space of the borders, this also dictates theri speed and when they
##      they are allowed to move at all depending on the enemyvariable 
##      def enemymovement():
##        global doorstatus
##        if enemyvariable == 1:    
##          #Enemy Movement
##           enemy.forward(15)
##           enemy2.forward(15)
##           enemy3.forward(15)
##           enemy4.forward(15)
##           enemy5.forward(15)
##             
##           #Enemy Boundary Checking (X-cor)
##           if enemy.xcor() > 290 or enemy.xcor() < -290:
##             enemy.backward(50)
##             enemy.right(random.randint(0,180))
##
##           if enemy2.xcor() > 290 or enemy2.xcor() < -290:
##             enemy2.backward(50)
##             enemy2.right(random.randint(0,180))
##
##           if enemy3.xcor() > 290 or enemy3.xcor() < -290:
##             enemy3.backward(50)
##             enemy3.right(random.randint(0,180))
##
##           if enemy4.xcor() > 290 or enemy4.xcor() < -290:
##             enemy4.backward(50)
##             enemy4.right(random.randint(0,180))
##
##           if enemy5.xcor() > 290 or enemy5.xcor() < -290:
##             enemy5.backward(50)
##             enemy.right(random.randint(0,180))
##            
##          #Enemy Boundary Checking (Y-cor)
##           if enemy.ycor() > 250 or enemy.ycor() < -250:
##             enemy.backward(50)
##             enemy.right(random.randint(0, 180))
##
##           if enemy2.ycor() > 250 or enemy2.ycor() < -250:
##             enemy2.backward(50)
##             enemy2.right(random.randint(0, 180))
##
##           if enemy3.ycor() > 250 or enemy3.ycor() < -250:
##             enemy3.backward(50)
##             enemy3.right(random.randint(0, 180))
##
##           if enemy4.ycor() > 250 or enemy4.ycor() < -250:
##             enemy4.backward(50)
##             enemy4.right(random.randint(0, 180))
##
##           if enemy5.ycor() > 250 or enemy5.ycor() < -250:
##             enemy5.backward(50)
##             enemy5.right(random.randint(0, 180))
##
##
##      def enemymovement2():
##        global enemyvariable
##        if enemyvariable == 2:
##          enemy6.forward(15)
##          enemy7.forward(15)
##          enemy8.forward(15)
##          #Second Room Enemies
##          if enemy6.xcor() > 290 or enemy6.xcor() < 200:
##              enemy6.backward(25)
##              enemy6.right(random.randint(0, 180))
##
##          if enemy7.xcor() > 290 or enemy7.xcor() < 200:
##              enemy7.backward(25)
##              enemy7.right(random.randint(0, 180))
##
##          if enemy8.xcor() > 290 or enemy8.xcor() < 200:
##              enemy8.backward(25)
##              enemy8.right(random.randint(0, 180))
##
##          if enemy6.ycor() > 250 or enemy6.ycor() < -250:
##              enemy6.backward(25)
##              enemy6.right(random.randint(0, 180))
##
##          if enemy7.ycor() > 250 or enemy7.ycor() < -250:
##              enemy7.backward(25)
##              enemy7.right(random.randint(0, 180))
##
##          if enemy8.ycor() > 250 or enemy8.ycor() < -250:
##              enemy8.backward(25)
##              enemy8.right(random.randint(0, 180))
##
##      def enemymovement3():
##        global enemyvariable
##        if enemyvariable == 3:
##          
##            #Enemy Movement
##            enemy9.forward(20)
##            enemy10.forward(20)
##            enemy11.forward(20)
##
##            #Enemy Boundary Checking (X-cor)
##            if enemy9.xcor() > 280 or enemy9.xcor() < -280:
##              enemy9.backward(50)
##              enemy9.right(random.randint(0,180))
##
##            if enemy10.xcor() > 280 or enemy10.xcor() < -280:
##              enemy10.backward(50)
##              enemy10.right(random.randint(0,180))
##
##            if enemy11.xcor() > 280 or enemy11.xcor() < -280:
##              enemy11.backward(50)
##              enemy11.right(random.randint(0,180))
##            
##           #Enemy Boundary Checking (Y-cor)
##            if enemy9.ycor() > 210 or enemy9.ycor() < -210:
##              enemy9.backward(50)
##              enemy9.right(random.randint(0, 180))
##
##            if enemy10.ycor() > 210 or enemy10.ycor() < -210:
##              enemy10.backward(50)
##              enemy10.right(random.randint(0, 180))
##
##            if enemy11.ycor() > 210 or enemy11.ycor() < -210:
##              enemy11.backward(50)
##              enemy11.right(random.randint(0, 180))
##
##
##      #Boss Everything
##      def bossattack():
##        global newroom
##        global health
##        global blockstatus
##        if enemyvariable == 4:
##          a = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))
##          num1 = random.randint(1,250)
##          if a < 140:
##            if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21 or num1 == 24 or num1 == 25 or num1 == 28:
##              health = health - 2
##              blockstatus = blockstatus - 1
##              hero.backward(150)
##              for q in range(10):
##                boss.shape("Boss Attack.gif")
##              boss.shape("Boss.gif")
##
##      def bosscollision():
##        global enemyvariable
##        global health
##        if enemyvariable == 4:
##          a = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))
##          if a < 175:
##            for q in range(10):
##              boss.shape("Boss Attack.gif")
##            boss.shape("Boss.gif")
##            hero.backward(50)
##            health = health - 1
##            boss.right(random.randint(0,360))
##            
##      def bossmoves():
##        global enemyvariable
##        if enemyvariable == 4:
##          boss.forward(75)
##          if boss.xcor() > 280 or boss.xcor() < -280:
##              boss.backward(50)
##              boss.right(random.randint(0,180))
##          if boss.ycor() > 210 or boss.ycor() < -210:
##              boss.backward(50)
##              boss.right(random.randint(0, 180))
##      ###################################################################################################
##
##      ###################################################################################################
##      If the heros health is subtracted by any enemy through any means it will change the appearence of the hearts by hiding them or changing their shape
##      def healthstatus():
##        if blockstatus <= 0:
##          if health is 9:
##            heart5.shape("Half Heart.gif")
##
##          if health is 8:
##            heart5.hideturtle()
##
##          if health is 7:
##            heart5.hideturtle()
##            heart4.shape("Half Heart.gif")
##
##          if health is 6:
##            heart5.hideturtle()
##            heart4.hideturtle()
##
##          if health is 5:
##            heart5.hideturtle()
##            heart4.hideturtle()
##            heart3.shape("Half Heart.gif")
##
##          if health is 4:
##            heart5.hideturtle()
##            heart4.hideturtle()
##            heart3.hideturtle()
##
##          if health is 3:
##            heart5.hideturtle()
##            heart4.hideturtle()
##            heart3.hideturtle()
##            heart2.shape("Half Heart.gif")
##
##          if health is 2:
##            heart5.hideturtle()
##            heart4.hideturtle()
##            heart3.hideturtle()
##            heart2.hideturtle()
##
##          if health is 1:
##            heart5.hideturtle()
##            heart4.hideturtle()
##            heart3.hideturtle()
##            heart2.hideturtle()
##            heart1.shape("Half Heart.gif")
##
##          if health <=  0:
##            dead = turtle.Turtle()
##            dead.speed(0)
##            dead.color("red")
##            dead.setposition(0,0)
##            deadstring = ("YOU DIED")
##            dead.write(deadstring, False, align="center", font=("Arial", 145, "normal"))
##            dead.hideturtle()
##            hero.hideturtle()
##      ###################################################################################################
##
##      ###################################################################################################
##      #Attack-Block-Bow
##      These functions are going to be tied to the keys "a", "s", "d" and will didctate when the player decideds to attack, block or shoot an arrow.
##      If the enemy and hero are close enough to each other then when the okayer decides to attack the enemy will take damage and change shape for a fraction of a second.
##      If the player decides to block the blockstatus vaariable will equal 1 meaning the enemy can not do damgage the the health points.
##      If the user decieds to shoot an arrow when the bow is equiped then when pressing the "d" key and arrow will travel and if the arrow and enemy x and y coordinates
##      are close to each other the enemy will take damage and change its shape momentarily.
##
##      def attack():
##        global enemyvariable
##        global enemyhealth  
##        global enemy2health  
##        global enemy3health  
##        global enemy4health
##        global enemy5health
##        global enemy9health
##        global enemy10health
##        global enemy11health
##        global bosshealth
##
##        if offense is 1:
##          for x in range(5):
##            hero.shape("Back Attack.gif")
##          hero.shape("Back Stand.gif")
##
##        if offense is 2:
##          for x in range(5):
##            hero.shape("Front Attack.gif")
##          hero.shape("Front Stand.gif")
##
##        if offense is 3:
##          for x in range(5):
##            hero.shape("Left Attack.gif")
##          hero.shape("Left Stand.gif") 
##
##        if offense is 4:
##          for x in range(5):
##            hero.shape("Right Attack.gif")
##          hero.shape("Right Stand.gif")
##
##        a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
##        b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
##        c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
##        d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
##        e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))
##        f = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
##        g = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
##        h = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))
##        z = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))
##
##        if a < 150:
##          enemyhealth = enemyhealth - 1
##          for x in range(5):
##            enemy.shape("Damage Skeleton.gif")
##          enemy.shape("Skeleton.gif")
##        if enemyhealth == 0:
##          enemy.hideturtle()
##          enemy.setposition(0,1500)
##
##        if b < 150:
##          enemy2health = enemy2health - 1
##          for x in range(5):
##            enemy2.shape("Damage Skeleton.gif")
##          enemy2.shape("Skeleton.gif")
##        if enemy2health == 0:
##          enemy2.hideturtle()
##          enemy2.setposition(0,1500)
##          
##        if c < 150:
##          enemy3health = enemy3health - 1
##          for x in range(5):
##            enemy3.shape("Damage Skeleton.gif")
##          enemy3.shape("Skeleton.gif")
##        if enemy3health == 0:
##          enemy3.hideturtle()
##          enemy3.setposition(0,1500)
##
##        if d < 150:
##          enemy4health = enemy4health - 1
##          for x in range(5):
##            enemy4.shape("Damage Skeleton.gif")
##          enemy4.shape("Skeleton.gif")
##        if enemy4health == 0:
##          enemy4.hideturtle()
##          enemy4.setposition(0,1500)
##          
##        if e < 150:
##          enemy5health = enemy5health - 1
##          for x in range(5):
##            enemy5.shape("Damage Skeleton.gif")
##          enemy5.shape("Skeleton.gif")
##        if enemy5health == 0:
##          enemy5.hideturtle()
##          enemy5.setposition(0,1500)
##
##
##        if f < 200:
##          enemy9health = enemy9health - 1
##          for x in range(5):
##            enemy9.shape("Damage SkeletonStrong.gif")
##          enemy9.shape("SkeletonStrong.gif")
##        if enemy9health == 0:
##          enemy9.hideturtle()
##          enemy9.setposition(0, 1500)
##          enemy9.speed(0)
##
##        if g < 200:
##          enemy10health = enemy10health - 1
##          for x in range(5):
##            enemy10.shape("Damage SkeletonStrong.gif")
##          enemy10.shape("SkeletonStrong.gif")
##        if enemy10health == 0:
##          enemy10.hideturtle()
##          enemy10.setposition(0,1500)
##          enemy10.speed(0)
##
##        if h < 200:
##          enemy11health = enemy11health - 1
##          for x in range(5):
##            enemy11.shape("Damage SkeletonStrong.gif")
##          enemy11.shape("SkeletonStrong.gif")
##        if enemy11health == 0:
##          enemy11.hideturtle()
##          enemy11.setposition(0, 1500)
##          enemy11.speed(0)
##
##
##        if z < 200:
##          bosshealth = bosshealth - 1
##          for x in range(5):
##            boss.shape("Damage Boss.gif")
##          boss.shape("Boss.gif")
##        if bosshealth == 0:
##          boss.hideturtle()
##          boss.setposition(0, 1500)
##          boss.speed(0)
##
##      def block():
##        global blockstatus
##        blockstatus = 1
##        if defense is 1:
##          hero.shape("Back Block.gif")
##
##        if defense is 2:
##          hero.shape("Front Block.gif")
##
##        if defense is 3:
##          hero.shape("Left Block.gif")
##                        
##        if defense is 4:
##          hero.shape("Right Block.gif")
##
##      The arrow state dictates whether the arrow is ready to be fired or not. Its state will change from ("Ready") to
##      ("Fire") depending on if it is travelling, hit an enemy, or passed the barriers
##      arrowstate = ("ready")   
##      def shootbowandarrow():
##        global bowstatus
##        global bowheading
##        global arrowheading
##        global roomboundaries
##        global enemy6health
##        global enemy7health
##        global enemy8health
##        global enemy9health
##        global enemy10health
##        global enemy11health
##        global bosshealth
##        global arrowstate
##        if bowstatus is 1:
##          if arrowstate == ("ready"):
##            arrowstate = ("fire")
##            
##            #move bow above hero
##            x = hero.xcor()
##            y = hero.ycor() 
##
##            if bowheading is 1:
##               bow.shape("Bow Up.gif")
##               arrow.shape("Arrow Up.gif")
##               arrow.setheading(90)
##               bow.setposition(x, y + 75)
##               bow.showturtle()
##               arrow.setposition(x, y + 75)
##               arrow.showturtle()
##               arrow.speed(0)
##               bow.hideturtle()
##
##            if bowheading is 2:
##               bow.shape("Bow Down.gif")
##               arrow.shape("Arrow Down.gif")
##               arrow.setheading(270)
##               bow.setposition(x, y-120)
##               bow.showturtle()
##               arrow.setposition(x, y-120)
##               arrow.showturtle()
##               arrow.speed(0)
##               bow.hideturtle()
##               
##            if bowheading is 3:
##               bow.shape("Bow Left.gif")
##               arrow.shape("Arrow Left.gif")
##               arrow.setheading(180)
##               bow.setposition(x-75, y)
##               bow.showturtle()
##               arrow.setposition(x-75, y)
##               arrow.showturtle()
##               arrow.speed(0)
##               bow.hideturtle()
##               
##            if bowheading is 4:
##               bow.shape("Bow Right.gif")
##               arrow.shape("Arrow Right.gif")
##               arrow.setheading(0)
##               bow.setposition(x + 75, y)
##               bow.showturtle()
##               arrow.setposition(x+75, y)
##               arrow.showturtle()
##               arrow.speed(0)
##               bow.hideturtle()
##
##      def arrowdamage():
##        global bowstatus
##        global bowheading
##        global arrowheading
##        global roomboundaries
##        global enemy6health
##        global enemy7health
##        global enemy8health
##        global enemy9health
##        global enemy10health
##        global enemy11health
##        global bosshealth
##        global arrowstate
##        a = math.sqrt(math.pow(arrow.xcor()-enemy6.xcor(),2) + math.pow(arrow.ycor()-enemy6.ycor(),2))
##        b = math.sqrt(math.pow(arrow.xcor()-enemy7.xcor(),2) + math.pow(arrow.ycor()-enemy7.ycor(),2))
##        c = math.sqrt(math.pow(arrow.xcor()-enemy8.xcor(),2) + math.pow(arrow.ycor()-enemy8.ycor(),2))
##        d = math.sqrt(math.pow(arrow.xcor()-enemy9.xcor(),2) + math.pow(arrow.ycor()-enemy9.ycor(),2))
##        e = math.sqrt(math.pow(arrow.xcor()-enemy10.xcor(),2) + math.pow(arrow.ycor()-enemy10.ycor(),2))
##        f = math.sqrt(math.pow(arrow.xcor()-enemy11.xcor(),2) + math.pow(arrow.ycor()-enemy11.ycor(),2))
##        z = math.sqrt(math.pow(arrow.xcor()-boss.xcor(),2) + math.pow(arrow.ycor()-boss.ycor(),2))
##        
##        if a < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy6health = enemy6health - 1
##          for x in range(5):
##            enemy6.shape("Damage Skeleton.gif")
##          enemy6.shape("Skeleton.gif")
##        if enemy6health == 0:
##          enemy6.hideturtle()
##          enemy6.setposition(1500, 1500)
##
##        if b < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy7health = enemy7health - 1
##          for x in range(5):
##            enemy7.shape("Damage Skeleton.gif")
##          enemy7.shape("Skeleton.gif")
##        if enemy7health == 0:
##          enemy7.hideturtle()
##          enemy7.setposition(1500, 1500)
##           
##        if c < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy8health = enemy8health - 1
##          for x in range(5):
##            enemy8.shape("Damage Skeleton.gif")
##          enemy8.shape("Skeleton.gif")
##        if enemy8health == 0:
##          enemy8.hideturtle()
##          enemy8.setposition(1500, 1500)
##
##        if d < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy9health = enemy9health - 1
##          for x in range(5):
##            enemy9.shape("Damage SkeletonStrong.gif")
##          enemy9.shape("SkeletonStrong.gif")
##        if enemy9health == 0:
##          enemy9.hideturtle()
##          enemy9.setposition(1500, 1500)
##
##        if e < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy10health = enemy10health - 1
##          for x in range(5):
##            enemy10.shape("Damage SkeletonStrong.gif")
##          enemy10.shape("SkeletonStrong.gif")
##        if enemy10health == 0:
##          enemy10.hideturtle()
##          enemy10.setposition(1500, 1500)
##           
##        if f < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          enemy11health = enemy11health - 1
##          for x in range(5):
##            enemy11.shape("Damage SkeletonStrong.gif")
##          enemy11.shape("SkeletonStrong.gif")
##        if enemy11health == 0:
##          enemy11.hideturtle()
##          enemy11.setposition(1500, 1500)
##
##        if z < 175:
##          arrow.hideturtle()
##          arrowstate == ("ready")
##          arrow.setposition(0,900)
##          bosshealth = bosshealth - 1
##          for x in range(5):
##            boss.shape("Damage Boss.gif")
##          boss.shape("Boss.gif")
##        if bosshealth == 0:
##           boss.hideturtle()
##           boss.setposition(0, 800)
##
##      If the arrow passes a certain threshold then it will change its arrowstate to be fired again
##      def arrowchecking():
##        global arrowstate
##        if arrow.xcor() > 320 or arrow.xcor() < -320:
##          arrow.hideturtle()
##          arrow.setposition(0,900)
##          arrowstate = ("ready")
##
##        if arrow.ycor() > 320 or arrow.ycor() < -320:
##          arrow.hideturtle()
##          arrow.setposition(0,900)
##          arrowstate = ("ready")
##      ###################################################################################################
##
##      ###################################################################################################
##      These keys determine if the user will move up, down, left, right, attack ,block, or shoot an arrow
##      #Set keyboard bindings
##      turtle.listen()       
##      turtle.onkey(upforward, "Up")
##      turtle.onkey(downbackward, "Down")
##      turtle.onkey(turnleft, "Left")
##      turtle.onkey(turnright, "Right")
##      turtle.onkey(grabsword, "space")
##      turtle.onkey(attack, "a")
##      turtle.onkey(block, "s")
##      turtle.onkey(shootbowandarrow, "d")
##      ###################################################################################################
##
##      ###################################################################################################
##      The main game loop runs all of the functions depending if they are ready to be used. This is what runs the
##      entirety of the game.
##      #Main Game Loop 
##      while True:
##        
##        hero.forward(speed)
##        heromovement()
##        healthstatus()
##        enemymovement()
##        enemymovement2()
##        enemymovement3()
##        enemyattack()
##        enemyattack2()
##        enemycollision()
##        enemycollision2()
##        opendoor()
##        opendoor2()
##        opendoor3()
##        opendoor4()
##        arrowchecking()
##        bossattack()
##        bosscollision()
##        bossmoves()
##        arrowdamage()
##
##
##        This is to determing where the arrow will point depending which direction the hero is facing
##        and diplays the winning Statement once the game is beaten
##        if bowheading is 1:
##          if arrowstate == ("fire"):
##            y = arrow.ycor()
##            y += 250
##            arrow.sety(y)
##            
##        if bowheading is 2:
##          if arrowstate == ("fire"):
##            y = arrow.ycor()
##            y += -250
##            arrow.sety(y)
##            
##        if bowheading is 3:
##          if arrowstate == ("fire"):
##            x = arrow.xcor()
##            x += -250
##            arrow.setx(x)    
##
##        if bowheading is 4:
##          if arrowstate == ("fire"):
##            x = arrow.xcor()
##            x += 250
##            arrow.setx(x)
##
##        if bosshealth <= 0:
##          congratulations = turtle.Turtle()
##          congratulations.speed(0)
##          congratulations.color("green")
##          congratulations.setposition(0,0)
##          congratulationsstring = ("CONGRATULATIONS YOU BEAT THE GAME!!!")
##          congratulations.write(congratulationsstring, False, align="center", font=("Arial", 40, "normal"))
##          congratulations.hideturtle()
##          boss.hideturtle()
##          hero.hideturtle()
#        End        
#      ...
#*********************************************************

import turtle
import random
import math
import os
###################################################################################################

###################################################################################################
#Set up Screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("The Map")
screen.bgpic("StonesHandDrawnAnti.gif")
screen.screensize(800, 800)


#Draw Border
mypen = turtle.Turtle()
mypen.speed(100)
mypen.penup()
mypen.setposition(-350,-350)
mypen.pendown()
mypen.pensize(5)
mypen.speed(15)
for side in range(4):
  mypen.forward(700)
  mypen.left(90) 
mypen.hideturtle()


#Sword in Stone
turtle.register_shape("Sword in Stone.gif")
swordinstone = turtle.Turtle()
swordinstone.penup()
swordinstone.shape("Sword in Stone.gif")
swordinstone.left(90)
swordinstone.forward(100)

#Cavern
turtle.register_shape("Black.gif")
black = turtle.Turtle()
black.hideturtle()
black.speed(0)
black.penup()
black.shape("Black.gif")

#Bow and Arrow
turtle.register_shape("Bow Up.gif")
turtle.register_shape("Bow Down.gif")
turtle.register_shape("Bow Left.gif")
turtle.register_shape("Bow Right.gif")
turtle.register_shape("Arrow Up.gif")
turtle.register_shape("Arrow Down.gif")
turtle.register_shape("Arrow Left.gif")
turtle.register_shape("Arrow Right.gif")
turtle.register_shape("Bow and Arrow Up.gif")
turtle.register_shape("Bow and Arrow Down.gif")
turtle.register_shape("Bow and Arrow Left.gif")
turtle.register_shape("Bow and Arrow Right.gif")
bowandarrow = turtle.Turtle()
bow = turtle.Turtle()
arrow = turtle.Turtle()
bowandarrow.hideturtle()
bow.hideturtle()
arrow.hideturtle()
bowandarrow.shape("Bow and Arrow Right.gif")
bow.shape("Bow Right.gif")
arrow.shape("Arrow Right.gif")
arrow.turtlesize(5)
bowandarrow.speed(0)
bow.speed(0)
arrow.speed(0)
bowandarrow.penup()
bow.penup()
arrow.penup()

#Bridge
turtle.register_shape("Bridge.gif")
bridge = turtle.Turtle()
bridge.penup()
bridge.speed(0)
bridge.shape("Bridge.gif")
bridge.hideturtle()
###################################################################################################

###################################################################################################
#Register Shapes
turtle.register_shape("Front.gif")
turtle.register_shape("Back.gif")
turtle.register_shape("Left.gif")
turtle.register_shape("Right.gif")
turtle.register_shape("Stone.gif")
turtle.register_shape("Back Stand.gif")
turtle.register_shape("Back Block.gif")
turtle.register_shape("Back Attack.gif")
turtle.register_shape("Front Stand.gif")
turtle.register_shape("Front Block.gif")
turtle.register_shape("Front Attack.gif")
turtle.register_shape("Right Stand.gif")
turtle.register_shape("Right Block.gif")
turtle.register_shape("Right Attack.gif")
turtle.register_shape("Left Stand.gif")
turtle.register_shape("Left Block.gif")
turtle.register_shape("Left Attack.gif")
turtle.register_shape("Heart.gif")
turtle.register_shape("Half Heart.gif")
turtle.register_shape("Door.gif")
turtle.register_shape("Skeleton.gif")
turtle.register_shape("Skeleton Attack.gif")
turtle.register_shape("Damage Skeleton.gif")
turtle.register_shape("Door2.gif")
turtle.register_shape("SkeletonStrong.gif")
turtle.register_shape("SkeletonStrong Attack.gif")
turtle.register_shape("Damage SkeletonStrong.gif")
turtle.register_shape("Boss.gif")
turtle.register_shape("Boss Attack.gif")
turtle.register_shape("Damage Boss.gif")
###################################################################################################

###################################################################################################
#Door
door = turtle.Turtle()
door.shape("Door.gif")
door.penup()
door.speed(0)
door.setposition(-3, 305)

#Room 1
door_open = turtle.Turtle()
door_open.hideturtle()
door_open.penup()
door_open.turtlesize(5)
door_open.left(90)
door_open.setposition(0,265)

#Door 2
door2 = turtle.Turtle()
door2.hideturtle()
door2.shape("Door2.gif")
door2.turtlesize(5)
door2.penup()
door2.speed(0)
door2.setposition(305, 3)

#Room 2
door2_open = turtle.Turtle()
door2_open.hideturtle()
door2_open.penup()
door2_open.turtlesize(5)
door2_open.setposition(310,0)

#Door 3
door3 = turtle.Turtle()
door3.hideturtle()
door3.shape("Door2.gif")
door3.turtlesize(5)
door3.penup()
door3.speed(0)
door3.setposition(305, 3)

#Room 3
door3_open = turtle.Turtle()
door3_open.hideturtle()
door3_open.penup()
door3_open.turtlesize(5)
door3_open.setposition(310,0)

#Door 4
door4 = turtle.Turtle()
door4.hideturtle()
door4.left(90)
door4.shape("Door.gif")
door4.turtlesize(5)
door4.penup()
door4.speed(0)
door4.setposition(-3, 305)

#Room 4
door4_open = turtle.Turtle()
door4_open.left(90)
door4_open.hideturtle()
door4_open.penup()
door4_open.turtlesize(5)
door4_open.setposition(0,265)

###################################################################################################

###################################################################################################
#Create Enemies
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.shape("Skeleton.gif")
enemy.turtlesize(5)
enemy.penup()
enemy.speed(0)
enemy.setposition(0,600)

enemy2 = turtle.Turtle()
enemy2.hideturtle()
enemy2.shape("Skeleton.gif")
enemy2.turtlesize(5)
enemy2.penup()
enemy2.speed(0)
enemy2.setposition(0,600)

enemy3 = turtle.Turtle()
enemy3.hideturtle()
enemy3.shape("Skeleton.gif")
enemy3.turtlesize(5)
enemy3.penup()
enemy3.speed(0)
enemy3.setposition(0,600)

enemy4 = turtle.Turtle()
enemy4.hideturtle()
enemy4.shape("Skeleton.gif")
enemy4.turtlesize(5)
enemy4.penup()
enemy4.speed(0)
enemy4.setposition(0,600)

enemy5 = turtle.Turtle()
enemy5.hideturtle()
enemy5.shape("Skeleton.gif")
enemy5.turtlesize(5)
enemy5.penup()
enemy5.speed(0)
enemy5.setposition(0,600)

enemy6 = turtle.Turtle()
enemy6.hideturtle()
enemy6.shape("Skeleton.gif")
enemy6.turtlesize(5)
enemy6.penup()
enemy6.speed(0)
enemy6.setposition(270,225)

enemy7 = turtle.Turtle()
enemy7.hideturtle()
enemy7.shape("Skeleton.gif")
enemy7.turtlesize(5)
enemy7.penup()
enemy7.speed(0)
enemy7.setposition(270,0)

enemy8 = turtle.Turtle()
enemy8.hideturtle()
enemy8.shape("Skeleton.gif")
enemy8.turtlesize(5)
enemy8.penup()
enemy8.speed(0)
enemy8.setposition(270,-225)

enemy9 = turtle.Turtle()
enemy9.hideturtle()
enemy9.shape("SkeletonStrong.gif")
enemy9.turtlesize(5)
enemy9.penup()
enemy9.speed(0)
enemy9.setposition(1500,1500)

enemy10 = turtle.Turtle()
enemy10.hideturtle()
enemy10.shape("SkeletonStrong.gif")
enemy10.turtlesize(5)
enemy10.penup()
enemy10.speed(0)
enemy10.setposition(1500,1500)

enemy11 = turtle.Turtle()
enemy11.hideturtle()
enemy11.shape("SkeletonStrong.gif")
enemy11.turtlesize(5)
enemy11.penup()
enemy11.speed(0)
enemy11.setposition(1500, 1500)

#Creating Boss
boss = turtle.Turtle()
boss.hideturtle()
boss.shape("Boss.gif")
boss.turtlesize(8)
boss.penup()
boss.speed(0)
boss.setposition(1500, 1500)

###################################################################################################

###################################################################################################
#Create Hero
hero = turtle.Turtle()
hero.shape("Back.gif")
hero.turtlesize(5)
hero.speed(0)
hero.penup()
hero.left(90)
hero.setposition(0,-50)
###################################################################################################

###################################################################################################
#Creating Hearts
heart1 = turtle.Turtle()
heart1.shape("Heart.gif")
heart1.penup()
heart1.speed(0)
heart1.setposition(-325, 300)

heart2 = turtle.Turtle()
heart2.shape("Heart.gif")
heart2.penup()
heart2.speed(0)
heart2.setposition(-275, 300)

heart3 = turtle.Turtle()
heart3.shape("Heart.gif")
heart3.penup()
heart3.speed(0)
heart3.setposition(-225, 300)

heart4 = turtle.Turtle()
heart4.shape("Heart.gif")
heart4.penup()
heart4.speed(0)
heart4.setposition(-175, 300)

heart5 = turtle.Turtle()
heart5.shape("Heart.gif")
heart5.penup()
heart5.speed(0)
heart5.setposition(-125, 300)
###################################################################################################

###################################################################################################
#Set up variables
speed = .0001
move_speed = 20
count    = 0
offense  = 0
defense  = 0
chs      = 0    #(C.H.S acronym for "Change Hero Shape")
enemyvariable = 0
enemyhealth  = 5
enemy2health = 5
enemy3health = 5
enemy4health = 5
enemy5health = 5
enemy6health = 5
enemy7health = 5
enemy8health = 5
enemy9health = 10
enemy10health = 10
enemy11health = 10
enemyspeed = 5
health = 10
bowstatus = 0
herograbbedsword = 0
bowheading = 0
arrowheading = 0
bosshealth = 15
blockstatus = 0
###################################################################################################

###################################################################################################
#Define Functions
def heromovement():
    #Boundary Checking
  if hero.xcor() >  300:
     turnleft()

  if hero.xcor() < -300:
     turnright()

  if hero.ycor() >  300:
     downbackward()

  if hero.ycor() < -300:
     upforward()

  if enemyvariable == 2 and enemy6health > 0 and enemy7health > 0 and enemy8health > 0:
    if hero.xcor() > -150:
      turnleft()

    if hero.xcor() < -300:
      turnright()

    if hero.ycor() >  300:
      downbackward()

    if hero.ycor() < -300:
      upforward()

    
def grabsword():
  global chs
  global herograbbedsword
  chs = 1
  herograbbedsword = 1
  swordinstone.shape("Stone.gif")
  hero.shape("Back Stand.gif")

    
def upforward():
  if chs == 1:
    global offense
    global defense
    global bowheading
    global arrowheading
    offense = 1
    defense = 1
    bowheading = 1
    arrowheaeding = 1
    hero.shape("Back Stand.gif")
    hero.setheading(90)
    hero.forward(move_speed)
  else:
    hero.shape("Back.gif")
    hero.setheading(90)
    hero.forward(move_speed)


def downbackward():
  if chs == 1:
    global offense
    global defense
    global bowheading
    global arrowheading
    offense = 2
    defense = 2
    bowheading = 2
    arrowheaeding = 2
    hero.shape("Front Stand.gif")
    hero.setheading(270)
    hero.forward(move_speed)
  else:
    hero.shape("Front.gif")
    hero.setheading(270)
    hero.forward(move_speed)

  
def turnleft():
  if chs == 1:
    global offense
    global defense
    global bowheading
    global arrowheading    
    offense = 3
    defense = 3
    bowheading = 3
    arrowheaeding = 3
    hero.shape("Left Stand.gif")
    hero.setheading(180)
    hero.forward(move_speed)
  else:
    hero.shape("Left.gif")
    hero.setheading(180)
    hero.forward(move_speed)
    

def turnright():
  if chs == 1:
    global offense
    global defense
    global bowheading
    global arrowheading    
    offense = 4
    defense = 4
    bowheading = 4
    arrowheaeding = 4    
    hero.shape("Right Stand.gif")
    hero.setheading(0)
    hero.forward(move_speed)
  else:
    hero.shape("Right.gif")
    hero.setheading(0)
    hero.forward(move_speed)

###################################################################################################

###################################################################################################
def opendoor():
  global enemyvariable
  f = math.sqrt(math.pow(hero.xcor()-door_open.xcor(),2) + math.pow(hero.ycor()-door_open.ycor(),2))
  if f < 50:
    enemyvariable = 1
    hero.setposition(0,-260)
    door_open.forward(300)
    door.hideturtle()
    swordinstone.hideturtle()
    enemy.showturtle()
    enemy2.showturtle()
    enemy3.showturtle()
    enemy4.showturtle()
    enemy5.showturtle()
    enemy.setposition(random.randint(-280, 280), random.randint(-200, 200))
    enemy2.setposition(random.randint(-280, 280), random.randint(-200, 200))
    enemy3.setposition(random.randint(-280, 280), random.randint(-200, 200))
    enemy4.setposition(random.randint(-280, 280), random.randint(-200, 200))
    enemy5.setposition(random.randint(-280, 280), random.randint(-200, 200)) 

    
def opendoor2():
  global enemyvariable
  global bowstatus
  if enemyhealth <= 0 and enemy2health <= 0 and enemy3health <= 0 and enemy4health <= 0 and enemy5health <= 0: 
    bowandarrow.showturtle()
    a = math.sqrt(math.pow(hero.xcor()-bowandarrow.xcor(),2) + math.pow(hero.ycor()-bowandarrow.ycor(),2))
    if a < 50:
      bowstatus = bowstatus + 1
      bowandarrow.hideturtle()
      bowandarrow.setposition(0,800)

    door2.showturtle()
    d = math.sqrt(math.pow(hero.xcor()-door2_open.xcor(),2) + math.pow(hero.ycor()-door2_open.ycor(),2))
    if d < 50:
      enemyvariable = 2
      hero.setposition(-260, 0)
      door2_open.forward(300)
      door2.forward(800)
      enemy6.showturtle()
      enemy7.showturtle()
      enemy8.showturtle()
      black.showturtle()


def opendoor3():
  global enemyvariable 
  if enemy6health <= 0 and enemy7health <= 0 and enemy8health <= 0: 
    bridge.showturtle()
    door3.showturtle()
    a = math.sqrt(math.pow(hero.xcor()-door3_open.xcor(),2) + math.pow(hero.ycor()-door3_open.ycor(),2))
    if a < 50:
      enemyvariable = 3
      hero.setposition(-260, 0)
      door3_open.setposition(1500,1500)
      door3.setposition(1500,1500)
      black.setposition(1500,1500)
      bridge.setposition(1500,1500)
      enemy9.setposition(random.randint(-250, 250), random.randint(-200, 200))
      enemy10.setposition(random.randint(-250, 250), random.randint(-200, 200))
      enemy11.setposition(random.randint(-250, 250), random.randint(-200, 200))
      enemy9.right(random.randint(0,360))
      enemy10.right(random.randint(0,360))
      enemy11.right(random.randint(0,360))
      enemy9.showturtle()
      enemy10.showturtle()
      enemy11.showturtle()


def opendoor4():
  global enemyvariable 
  if  enemy9health <= 0 and enemy10health <= 0 and enemy11health <= 0:
    door4.showturtle()
    a = math.sqrt(math.pow(hero.xcor()-door4_open.xcor(),2) + math.pow(hero.ycor()-door4_open.ycor(),2))    
    if a < 50:
      door4.setposition(1500,1500)
      enemyvariable = 4
      hero.setposition(0,-260)
      door4_open.forward(300)
      door4.setposition(0, 900)
      boss.showturtle()
      boss.setposition(0,0)  
      boss.right(random.randint(0,360))
###################################################################################################

###################################################################################################
def enemyattack():
  global health
  global blockstatus
  if enemyvariable == 1:
    a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
    b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
    c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
    d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
    e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))

    num1 = random.randint(1,250)

    if a < 100:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 1
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy.shape("Skeleton Attack.gif")
        enemy.shape("Skeleton.gif")

    if b < 100:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 1
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy2.shape("Skeleton Attack.gif")
        enemy2.shape("Skeleton.gif")

    if c < 100:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 1
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy3.shape("Skeleton Attack.gif")
        enemy3.shape("Skeleton.gif")

    if d < 100:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 1
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy4.shape("Skeleton Attack.gif")
        enemy4.shape("Skeleton.gif")

    if e < 100:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 1
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy5.shape("Skeleton Attack.gif")
        enemy5.shape("Skeleton.gif")

def enemyattack2():
  global enemyvariable
  global health
  global blockstatus
  if enemyvariable == 3:
    a = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
    b = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
    c = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))
   
    num1 = random.randint(1,250)

    if a < 175:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 2
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy9.shape("SkeletonStrong Attack.gif")
        enemy9.shape("SkeletonStrong.gif")

    if b < 175:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 2
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy10.shape("SkeletonStrong Attack.gif")
        enemy10.shape("SkeletonStrong.gif")

    if c < 175:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21:
        health = health - 2
        blockstatus = blockstatus - 1
        hero.backward(50)
        for q in range(10):
          enemy11.shape("SkeletonStrong Attack.gif")
        enemy11.shape("SkeletonStrong.gif")


def enemycollision():
  global enemyvariable
  global health
  if enemyvariable == 1:
    a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
    b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
    c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
    d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
    e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))

    if a < 50:
      for q in range(10):
        enemy.shape("Skeleton Attack.gif")
      enemy.shape("Skeleton.gif")
      hero.backward(50)
      health = health - 1
      enemy.right(random.randint(0,360))

    if b < 50:
      for q in range(10):
        enemy2.shape("Skeleton Attack.gif")
      enemy2.shape("Skeleton.gif")
      hero.backward(50)
      health = health - 1
      enemy2.right(random.randint(0,360))
      
    if c < 50:
      for q in range(10):
        enemy3.shape("Skeleton Attack.gif")
      enemy3.shape("Skeleton.gif")
      hero.backward(50)
      health = health - 1
      enemy3.right(random.randint(0,360))
      
    if d < 50:
      for q in range(10):
        enemy4.shape("Skeleton Attack.gif")
      enemy4.shape("Skeleton.gif")
      hero.backward(50)
      health = health - 1
      enemy4.right(random.randint(0,360))
      
    if e < 50:
      for q in range(10):
        enemy5.shape("Skeleton Attack.gif")
      enemy5.shape("Skeleton.gif")
      hero.backward(50)
      health = health - 1
      enemy5.right(random.randint(0,360))


def enemycollision2():
  global health
  if enemyvariable == 3:
    a = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
    b = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
    c = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))

    if a < 75:
      for q in range(10):
        enemy9.shape("SkeletonStrong Attack.gif")
      enemy9.shape("SkeletonStrong.gif")
      hero.backward(50)
      health = health - 2
      enemy9.right(random.randint(0,360))

    if b < 75:
      for q in range(10):
        enemy10.shape("SkeletonStrong Attack.gif")
      enemy10.shape("SkeletonStrong.gif")
      hero.backward(50)
      health = health - 2
      enemy10.right(random.randint(0,360))
      
    if c < 75:
      for q in range(10):
        enemy11.shape("SkeletonStrong Attack.gif")
      enemy11.shape("SkeletonStrong.gif")
      hero.backward(50)
      health = health - 2
      enemy11.right(random.randint(0,360))
      
def enemymovement():
  global doorstatus
  if enemyvariable == 1:    
    #Enemy Movement
     enemy.forward(15)
     enemy2.forward(15)
     enemy3.forward(15)
     enemy4.forward(15)
     enemy5.forward(15)
       
     #Enemy Boundary Checking (X-cor)
     if enemy.xcor() > 290 or enemy.xcor() < -290:
       enemy.backward(50)
       enemy.right(random.randint(0,180))

     if enemy2.xcor() > 290 or enemy2.xcor() < -290:
       enemy2.backward(50)
       enemy2.right(random.randint(0,180))

     if enemy3.xcor() > 290 or enemy3.xcor() < -290:
       enemy3.backward(50)
       enemy3.right(random.randint(0,180))

     if enemy4.xcor() > 290 or enemy4.xcor() < -290:
       enemy4.backward(50)
       enemy4.right(random.randint(0,180))

     if enemy5.xcor() > 290 or enemy5.xcor() < -290:
       enemy5.backward(50)
       enemy.right(random.randint(0,180))
      
    #Enemy Boundary Checking (Y-cor)
     if enemy.ycor() > 250 or enemy.ycor() < -250:
       enemy.backward(50)
       enemy.right(random.randint(0, 180))

     if enemy2.ycor() > 250 or enemy2.ycor() < -250:
       enemy2.backward(50)
       enemy2.right(random.randint(0, 180))

     if enemy3.ycor() > 250 or enemy3.ycor() < -250:
       enemy3.backward(50)
       enemy3.right(random.randint(0, 180))

     if enemy4.ycor() > 250 or enemy4.ycor() < -250:
       enemy4.backward(50)
       enemy4.right(random.randint(0, 180))

     if enemy5.ycor() > 250 or enemy5.ycor() < -250:
       enemy5.backward(50)
       enemy5.right(random.randint(0, 180))


def enemymovement2():
  global enemyvariable
  if enemyvariable == 2:
    enemy6.forward(15)
    enemy7.forward(15)
    enemy8.forward(15)
    #Second Room Enemies
    if enemy6.xcor() > 290 or enemy6.xcor() < 200:
        enemy6.backward(25)
        enemy6.right(random.randint(0, 180))

    if enemy7.xcor() > 290 or enemy7.xcor() < 200:
        enemy7.backward(25)
        enemy7.right(random.randint(0, 180))

    if enemy8.xcor() > 290 or enemy8.xcor() < 200:
        enemy8.backward(25)
        enemy8.right(random.randint(0, 180))

    if enemy6.ycor() > 250 or enemy6.ycor() < -250:
        enemy6.backward(25)
        enemy6.right(random.randint(0, 180))

    if enemy7.ycor() > 250 or enemy7.ycor() < -250:
        enemy7.backward(25)
        enemy7.right(random.randint(0, 180))

    if enemy8.ycor() > 250 or enemy8.ycor() < -250:
        enemy8.backward(25)
        enemy8.right(random.randint(0, 180))

def enemymovement3():
  global enemyvariable
  if enemyvariable == 3:
    
      #Enemy Movement
      enemy9.forward(20)
      enemy10.forward(20)
      enemy11.forward(20)

      #Enemy Boundary Checking (X-cor)
      if enemy9.xcor() > 280 or enemy9.xcor() < -280:
        enemy9.backward(50)
        enemy9.right(random.randint(0,180))

      if enemy10.xcor() > 280 or enemy10.xcor() < -280:
        enemy10.backward(50)
        enemy10.right(random.randint(0,180))

      if enemy11.xcor() > 280 or enemy11.xcor() < -280:
        enemy11.backward(50)
        enemy11.right(random.randint(0,180))
      
     #Enemy Boundary Checking (Y-cor)
      if enemy9.ycor() > 210 or enemy9.ycor() < -210:
        enemy9.backward(50)
        enemy9.right(random.randint(0, 180))

      if enemy10.ycor() > 210 or enemy10.ycor() < -210:
        enemy10.backward(50)
        enemy10.right(random.randint(0, 180))

      if enemy11.ycor() > 210 or enemy11.ycor() < -210:
        enemy11.backward(50)
        enemy11.right(random.randint(0, 180))


#Boss Everything
def bossattack():
  global newroom
  global health
  global blockstatus
  if enemyvariable == 4:
    a = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))
    num1 = random.randint(1,250)
    if a < 140:
      if num1 == 3 or num1 == 6 or num1 == 9 or num1 == 12 or num1 == 15 or num1 == 18 or num1 == 21 or num1 == 24 or num1 == 25 or num1 == 28:
        health = health - 2
        blockstatus = blockstatus - 1
        hero.backward(150)
        for q in range(10):
          boss.shape("Boss Attack.gif")
        boss.shape("Boss.gif")

def bosscollision():
  global enemyvariable
  global health
  if enemyvariable == 4:
    a = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))
    if a < 175:
      for q in range(10):
        boss.shape("Boss Attack.gif")
      boss.shape("Boss.gif")
      hero.backward(50)
      health = health - 1
      boss.right(random.randint(0,360))
      
def bossmoves():
  global enemyvariable
  if enemyvariable == 4:
    boss.forward(75)
    if boss.xcor() > 280 or boss.xcor() < -280:
        boss.backward(50)
        boss.right(random.randint(0,180))
    if boss.ycor() > 210 or boss.ycor() < -210:
        boss.backward(50)
        boss.right(random.randint(0, 180))
###################################################################################################

###################################################################################################                    
def healthstatus():
  if blockstatus <= 0:
    if health is 9:
      heart5.shape("Half Heart.gif")

    if health is 8:
      heart5.hideturtle()

    if health is 7:
      heart5.hideturtle()
      heart4.shape("Half Heart.gif")

    if health is 6:
      heart5.hideturtle()
      heart4.hideturtle()

    if health is 5:
      heart5.hideturtle()
      heart4.hideturtle()
      heart3.shape("Half Heart.gif")

    if health is 4:
      heart5.hideturtle()
      heart4.hideturtle()
      heart3.hideturtle()

    if health is 3:
      heart5.hideturtle()
      heart4.hideturtle()
      heart3.hideturtle()
      heart2.shape("Half Heart.gif")

    if health is 2:
      heart5.hideturtle()
      heart4.hideturtle()
      heart3.hideturtle()
      heart2.hideturtle()

    if health is 1:
      heart5.hideturtle()
      heart4.hideturtle()
      heart3.hideturtle()
      heart2.hideturtle()
      heart1.shape("Half Heart.gif")

    if health <=  0:
      dead = turtle.Turtle()
      dead.speed(0)
      dead.color("red")
      dead.setposition(0,0)
      deadstring = ("YOU DIED")
      dead.write(deadstring, False, align="center", font=("Arial", 145, "normal"))
      dead.hideturtle()
      hero.hideturtle()
###################################################################################################

###################################################################################################

###################################################################################################

################################################################################################### 
#Attack-Block-Bow

def attack():
  global enemyvariable
  global enemyhealth  
  global enemy2health  
  global enemy3health  
  global enemy4health
  global enemy5health
  global enemy9health
  global enemy10health
  global enemy11health
  global bosshealth

  if offense is 1:
    for x in range(5):
      hero.shape("Back Attack.gif")
    hero.shape("Back Stand.gif")

  if offense is 2:
    for x in range(5):
      hero.shape("Front Attack.gif")
    hero.shape("Front Stand.gif")

  if offense is 3:
    for x in range(5):
      hero.shape("Left Attack.gif")
    hero.shape("Left Stand.gif") 

  if offense is 4:
    for x in range(5):
      hero.shape("Right Attack.gif")
    hero.shape("Right Stand.gif")

  a = math.sqrt(math.pow(hero.xcor()-enemy.xcor(),2) + math.pow(hero.ycor()-enemy.ycor(),2))
  b = math.sqrt(math.pow(hero.xcor()-enemy2.xcor(),2) + math.pow(hero.ycor()-enemy2.ycor(),2))
  c = math.sqrt(math.pow(hero.xcor()-enemy3.xcor(),2) + math.pow(hero.ycor()-enemy3.ycor(),2))
  d = math.sqrt(math.pow(hero.xcor()-enemy4.xcor(),2) + math.pow(hero.ycor()-enemy4.ycor(),2))
  e = math.sqrt(math.pow(hero.xcor()-enemy5.xcor(),2) + math.pow(hero.ycor()-enemy5.ycor(),2))
  f = math.sqrt(math.pow(hero.xcor()-enemy9.xcor(),2) + math.pow(hero.ycor()-enemy9.ycor(),2))
  g = math.sqrt(math.pow(hero.xcor()-enemy10.xcor(),2) + math.pow(hero.ycor()-enemy10.ycor(),2))
  h = math.sqrt(math.pow(hero.xcor()-enemy11.xcor(),2) + math.pow(hero.ycor()-enemy11.ycor(),2))
  z = math.sqrt(math.pow(hero.xcor()-boss.xcor(),2) + math.pow(hero.ycor()-boss.ycor(),2))

  if a < 150:
    enemyhealth = enemyhealth - 1
    for x in range(5):
      enemy.shape("Damage Skeleton.gif")
    enemy.shape("Skeleton.gif")
  if enemyhealth == 0:
    enemy.hideturtle()
    enemy.setposition(0,1500)

  if b < 150:
    enemy2health = enemy2health - 1
    for x in range(5):
      enemy2.shape("Damage Skeleton.gif")
    enemy2.shape("Skeleton.gif")
  if enemy2health == 0:
    enemy2.hideturtle()
    enemy2.setposition(0,1500)
    
  if c < 150:
    enemy3health = enemy3health - 1
    for x in range(5):
      enemy3.shape("Damage Skeleton.gif")
    enemy3.shape("Skeleton.gif")
  if enemy3health == 0:
    enemy3.hideturtle()
    enemy3.setposition(0,1500)

  if d < 150:
    enemy4health = enemy4health - 1
    for x in range(5):
      enemy4.shape("Damage Skeleton.gif")
    enemy4.shape("Skeleton.gif")
  if enemy4health == 0:
    enemy4.hideturtle()
    enemy4.setposition(0,1500)
    
  if e < 150:
    enemy5health = enemy5health - 1
    for x in range(5):
      enemy5.shape("Damage Skeleton.gif")
    enemy5.shape("Skeleton.gif")
  if enemy5health == 0:
    enemy5.hideturtle()
    enemy5.setposition(0,1500)


  if f < 200:
    enemy9health = enemy9health - 1
    for x in range(5):
      enemy9.shape("Damage SkeletonStrong.gif")
    enemy9.shape("SkeletonStrong.gif")
  if enemy9health == 0:
    enemy9.hideturtle()
    enemy9.setposition(0, 1500)
    enemy9.speed(0)

  if g < 200:
    enemy10health = enemy10health - 1
    for x in range(5):
      enemy10.shape("Damage SkeletonStrong.gif")
    enemy10.shape("SkeletonStrong.gif")
  if enemy10health == 0:
    enemy10.hideturtle()
    enemy10.setposition(0,1500)
    enemy10.speed(0)

  if h < 200:
    enemy11health = enemy11health - 1
    for x in range(5):
      enemy11.shape("Damage SkeletonStrong.gif")
    enemy11.shape("SkeletonStrong.gif")
  if enemy11health == 0:
    enemy11.hideturtle()
    enemy11.setposition(0, 1500)
    enemy11.speed(0)


  if z < 200:
    bosshealth = bosshealth - 1
    for x in range(5):
      boss.shape("Damage Boss.gif")
    boss.shape("Boss.gif")
  if bosshealth == 0:
    boss.hideturtle()
    boss.setposition(0, 1500)
    boss.speed(0)

def block():
  global blockstatus
  blockstatus = 1
  if defense is 1:
    hero.shape("Back Block.gif")

  if defense is 2:
    hero.shape("Front Block.gif")

  if defense is 3:
    hero.shape("Left Block.gif")
                  
  if defense is 4:
    hero.shape("Right Block.gif")


arrowstate = ("ready")   
def shootbowandarrow():
  global bowstatus
  global bowheading
  global arrowheading
  global roomboundaries
  global enemy6health
  global enemy7health
  global enemy8health
  global enemy9health
  global enemy10health
  global enemy11health
  global bosshealth
  global arrowstate
  if bowstatus is 1:
    if arrowstate == ("ready"):
      arrowstate = ("fire")
      
      #move bow above hero
      x = hero.xcor()
      y = hero.ycor() 

      if bowheading is 1:
         bow.shape("Bow Up.gif")
         arrow.shape("Arrow Up.gif")
         arrow.setheading(90)
         bow.setposition(x, y + 75)
         bow.showturtle()
         arrow.setposition(x, y + 75)
         arrow.showturtle()
         arrow.speed(0)
         bow.hideturtle()

      if bowheading is 2:
         bow.shape("Bow Down.gif")
         arrow.shape("Arrow Down.gif")
         arrow.setheading(270)
         bow.setposition(x, y-120)
         bow.showturtle()
         arrow.setposition(x, y-120)
         arrow.showturtle()
         arrow.speed(0)
         bow.hideturtle()
         
      if bowheading is 3:
         bow.shape("Bow Left.gif")
         arrow.shape("Arrow Left.gif")
         arrow.setheading(180)
         bow.setposition(x-75, y)
         bow.showturtle()
         arrow.setposition(x-75, y)
         arrow.showturtle()
         arrow.speed(0)
         bow.hideturtle()
         
      if bowheading is 4:
         bow.shape("Bow Right.gif")
         arrow.shape("Arrow Right.gif")
         arrow.setheading(0)
         bow.setposition(x + 75, y)
         bow.showturtle()
         arrow.setposition(x+75, y)
         arrow.showturtle()
         arrow.speed(0)
         bow.hideturtle()

def arrowdamage():
  global bowstatus
  global bowheading
  global arrowheading
  global roomboundaries
  global enemy6health
  global enemy7health
  global enemy8health
  global enemy9health
  global enemy10health
  global enemy11health
  global bosshealth
  global arrowstate
  a = math.sqrt(math.pow(arrow.xcor()-enemy6.xcor(),2) + math.pow(arrow.ycor()-enemy6.ycor(),2))
  b = math.sqrt(math.pow(arrow.xcor()-enemy7.xcor(),2) + math.pow(arrow.ycor()-enemy7.ycor(),2))
  c = math.sqrt(math.pow(arrow.xcor()-enemy8.xcor(),2) + math.pow(arrow.ycor()-enemy8.ycor(),2))
  d = math.sqrt(math.pow(arrow.xcor()-enemy9.xcor(),2) + math.pow(arrow.ycor()-enemy9.ycor(),2))
  e = math.sqrt(math.pow(arrow.xcor()-enemy10.xcor(),2) + math.pow(arrow.ycor()-enemy10.ycor(),2))
  f = math.sqrt(math.pow(arrow.xcor()-enemy11.xcor(),2) + math.pow(arrow.ycor()-enemy11.ycor(),2))
  z = math.sqrt(math.pow(arrow.xcor()-boss.xcor(),2) + math.pow(arrow.ycor()-boss.ycor(),2))
  
  if a < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy6health = enemy6health - 1
    for x in range(5):
      enemy6.shape("Damage Skeleton.gif")
    enemy6.shape("Skeleton.gif")
  if enemy6health == 0:
    enemy6.hideturtle()
    enemy6.setposition(1500, 1500)

  if b < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy7health = enemy7health - 1
    for x in range(5):
      enemy7.shape("Damage Skeleton.gif")
    enemy7.shape("Skeleton.gif")
  if enemy7health == 0:
    enemy7.hideturtle()
    enemy7.setposition(1500, 1500)
     
  if c < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy8health = enemy8health - 1
    for x in range(5):
      enemy8.shape("Damage Skeleton.gif")
    enemy8.shape("Skeleton.gif")
  if enemy8health == 0:
    enemy8.hideturtle()
    enemy8.setposition(1500, 1500)

  if d < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy9health = enemy9health - 1
    for x in range(5):
      enemy9.shape("Damage SkeletonStrong.gif")
    enemy9.shape("SkeletonStrong.gif")
  if enemy9health == 0:
    enemy9.hideturtle()
    enemy9.setposition(1500, 1500)

  if e < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy10health = enemy10health - 1
    for x in range(5):
      enemy10.shape("Damage SkeletonStrong.gif")
    enemy10.shape("SkeletonStrong.gif")
  if enemy10health == 0:
    enemy10.hideturtle()
    enemy10.setposition(1500, 1500)
     
  if f < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    enemy11health = enemy11health - 1
    for x in range(5):
      enemy11.shape("Damage SkeletonStrong.gif")
    enemy11.shape("SkeletonStrong.gif")
  if enemy11health == 0:
    enemy11.hideturtle()
    enemy11.setposition(1500, 1500)

  if z < 175:
    arrow.hideturtle()
    arrowstate == ("ready")
    arrow.setposition(0,900)
    bosshealth = bosshealth - 1
    for x in range(5):
      boss.shape("Damage Boss.gif")
    boss.shape("Boss.gif")
  if bosshealth == 0:
     boss.hideturtle()
     boss.setposition(0, 800)
           
def arrowchecking():
  global arrowstate
  if arrow.xcor() > 320 or arrow.xcor() < -320:
    arrow.hideturtle()
    arrow.setposition(0,900)
    arrowstate = ("ready")

  if arrow.ycor() > 320 or arrow.ycor() < -320:
    arrow.hideturtle()
    arrow.setposition(0,900)
    arrowstate = ("ready")
###################################################################################################

###################################################################################################  
#Set keyboard bindings
turtle.listen()       
turtle.onkey(upforward, "Up")
turtle.onkey(downbackward, "Down")
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(grabsword, "space")
turtle.onkey(attack, "a")
turtle.onkey(block, "s")
turtle.onkey(shootbowandarrow, "d")
###################################################################################################

###################################################################################################
#Main Game Loop 
while True:
  
  hero.forward(speed)
  heromovement()
  healthstatus()
  enemymovement()
  enemymovement2()
  enemymovement3()
  enemyattack()
  enemyattack2()
  enemycollision()
  enemycollision2()
  opendoor()
  opendoor2()
  opendoor3()
  opendoor4()
  arrowchecking()
  bossattack()
  bosscollision()
  bossmoves()
  arrowdamage()


    
  if bowheading is 1:
    if arrowstate == ("fire"):
      y = arrow.ycor()
      y += 250
      arrow.sety(y)
      
  if bowheading is 2:
    if arrowstate == ("fire"):
      y = arrow.ycor()
      y += -250
      arrow.sety(y)
      
  if bowheading is 3:
    if arrowstate == ("fire"):
      x = arrow.xcor()
      x += -250
      arrow.setx(x)    

  if bowheading is 4:
    if arrowstate == ("fire"):
      x = arrow.xcor()
      x += 250
      arrow.setx(x)

  if bosshealth <= 0:
    congratulations = turtle.Turtle()
    congratulations.speed(0)
    congratulations.color("green")
    congratulations.setposition(0,0)
    congratulationsstring = ("CONGRATULATIONS YOU BEAT THE GAME!!!")
    congratulations.write(congratulationsstring, False, align="center", font=("Arial", 40, "normal"))
    congratulations.hideturtle()
    boss.hideturtle()
    hero.hideturtle()
    



  



    

