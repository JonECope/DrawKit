"""
This code was written by JonECope
Using Python 3035 in Processing 3.3.7
"""
color_choice = color(0, 0, 0)
circ = True
instructions = "Press Mouse to draw, Right-click to erase, Q to exit, R, O, Y, G, B, V for colors. Press S for square brush or C for circle brush. Press Enter to save."
def setup():
    #size(800, 800)
    fullScreen()
    background(255)
    textSize(30)
    fill(0)
    text(instructions, 10, 100, width-20, 200)
    circ = True

def draw():
    global color_choice
    if mousePressed:
        if mouseButton == LEFT:
            fill(color_choice)
            stroke(color_choice)
        elif mouseButton == RIGHT:
            fill(255, 255, 255)
            stroke(255, 255, 255)
    else:
        fill(0, 0, 0, 0)
        stroke(0, 0, 0, 0)
        
    global circ
    if keyPressed:
        if key == "s" or key == "S":
            circ = False
        elif key == "c" or key == "C":
            circ = True
        if key == "q" or key == "Q":
            exit()
        elif key == ENTER:
            save("MyDrawing.png")
            background(255)
            fill(255, 0, 0)
            text("Your creation has been saved to the application's folder!", 10, 100, width-20, 200)
        elif keyCode == LEFT:
            color_choice = color(0)
        elif key == "r" or key == "R":
            color_choice = color(255, 0, 0)
        elif key == "o" or key == "O":
            color_choice = color(255, 156, 0)
        elif key == "y" or key == "Q":
            color_choice = color(255, 255, 0)
        elif key == "g" or key == "Q":
            color_choice = color(0, 255, 0)
        elif key == "b" or key == "Q":
            color_choice = color(0, 0, 255)
        elif key == "v" or key == "Q":
            color_choice = color(169, 0, 255)
            
    if circ:
        ellipse(mouseX, mouseY, 30, 30)
    else:
        rect(mouseX, mouseY, 30, 30)
