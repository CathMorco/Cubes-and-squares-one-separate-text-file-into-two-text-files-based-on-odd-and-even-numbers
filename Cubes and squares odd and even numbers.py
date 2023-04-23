#Imports the necessary modules
import pygame

#Sets the value for the width and height of the display screen
W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
clock = pygame.time.Clock()

#RGB example values
black = (0,0,0)
white = (255,255,255)

#The rate of change in colors
col_spd = 1

#The color directory & its values
col_dir =[[-1,1,1]]
def_col = [[120,120,240]]

#Opens and reads each individual line in the text file
with open("myfile.txt") as file:
    lines = [line.rstrip() for line in file]

#Divides the list into even and odd numbers
evens = []
odds = []
for i in lines:
    i=int(i)
    if i % 2 == 0:
        i *= i
        evens.append(i)
    else:
        i *= i*i
        odds.append(i)

#Tranfers the even and odd list of numbers into 2 separate text files
with open("even numbers.txt", "w") as even:
    even.write("\n".join(str(i) for i in evens))

with open("even numbers.txt", "r") as even:    
    evenlines = [line.rstrip() for line in even]

with open("odd numbers.txt", "w") as odd:
    odd.write("\n".join(str(i) for i in odds))

with open("odd numbers.txt", "r") as odd:    
    oddlines = [line.rstrip() for line in odd]


#Creates the main program


    #Sets the title for the screen display
    

    #Multiplies the color directory and its values in accordance to the number of items in its list
    

    #Initialized values for functions
    

    #Draws the text
    

    #Creates the color change
    

    #Combines the color change and draw text into one function
    
    # Initialising pygame
    

    #Creates the properties of the background screen so it can scroll
    

    #Runs the program
    

#Runs the program for the 2 text files
