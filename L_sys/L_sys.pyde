import processing, math, time
step = 0
WIDTH = 1000
HEIGHT = 1000
GRID_SIZE = 20
allStates = [["F"]]#, ["-F"], ["--F"], ["+F"]]
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255)]
variables = ["F", "G"]
constants = ["+", "-"]
showString = False
rules = {
         "F":"F-G",
         "G":"F+G"
         }
def setup():
    global WIDTH, HEIGHT
    size(WIDTH, HEIGHT)
    background(255)
    update()

def draw():
    pass

def update():
    global step, prevStr, GRID_SIZE, states
    
    #create new state from rules
    for states in allStates:
        while step >= len(states):
            print ("Generating step {}...".format(step))
            newString = ""
            for i, char in enumerate(states[-1]):
                if char in constants:
                    newString += char
                    continue
                if not char in variables:
                    raise ValueError("Incorrect character {} in string at position {}".format(char, i))
                # temp = (i % 4) // 2
                newString += rules[char]
            states.append(newString)
            print ("step {} finished".format(step))
        
    background (255)
    fill (255)
    textAlign(LEFT)
    text ("Step:{}".format(step), WIDTH - 70, 20)
    
    #draw current string
    for i, states in enumerate(allStates):
        pos = [WIDTH // 2, HEIGHT // 2]
        dir = 0.0
        stroke (colors[i][0], colors[i][1], colors[i][2])
        for char in states[step]:
            if char == 'F' or char == 'G':
                newPos = [pos[0] + (math.cos(dir / 2 * math.pi) * GRID_SIZE),
                        pos[1] + (math.sin(dir / 2 * math.pi) * GRID_SIZE)]
                
                if (0 < pos[0] < WIDTH and 0 < pos[1] < HEIGHT) or (0 < newPos[0] < WIDTH and 0 < newPos[1] < HEIGHT):
                    line(pos[0], pos[1], newPos[0], newPos[1])
                pos = newPos[:]
            elif char == '+':
                dir += 1
            elif char == '-':
                dir -= 1
            dir = dir % 4
            ellipse(pos[0], pos[1], 2, 2)
        textSize (12)
        text (states[step], 10, HEIGHT - 50, WIDTH-20, 50)
        
def keyPressed():
    global step, GRID_SIZE
    if keyCode == RIGHT:
        step += 1
        update()
    elif keyCode == LEFT:
        if step > 0:
            step -= 1
            update()
    elif key == "h" or key == "H":
        showString = not showString
    elif key == "-":
        GRID_SIZE /= 2
        update()
    elif key == "+":
        GRID_SIZE *= 2
        update()
    elif key == "p":
        print ("Current state: {}".format(states[step]))
    elif key == "P":
        print ("List of states:")
        for i, state in enumerate (states):
            print ("State {} : {}".format(i, state))
