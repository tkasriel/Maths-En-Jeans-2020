import processing, math, time
step = 0
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20
states = ["F+"]
variables = ["+", "-", "F"]
constants = []
showString = False
rules = {"+":["-", "+"],
         "-":["+", "-"],
         "F":["F-F","F+F"]
         }
def setup():
    global WIDTH, HEIGHT
    size(WIDTH, HEIGHT)
    background(0)
    update()

def draw():
    pass

def update():
    global step, prevStr, GRID_SIZE, states
    
    #create new state from rules
    while step >= len(states):
        print ("Generating next step(s)...")
        newString = ""
        for i, char in enumerate(states[-1]):
            if char in constants:
                newString += char
                continue
            if not char in variables:
                raise ValueError("Incorrect character {} in string at position {}".format(char, i))
            temp = (i % 4) // 2
            newString += rules[char][temp]
        states.append(newString)
        print ("step finished")
    
    background (0)
    fill (255)
    textAlign(LEFT)
    text ("Step:{}".format(step), WIDTH - 70, 20)
    
    stroke (255, 0, 0)
    pos = [WIDTH // 2, HEIGHT // 2]
    dir = 0.0
    #draw current string
    for char in states[step]:
        if char == 'F':
            newPos = [pos[0] + 1,#(math.cos(dir / 2 * math.pi) * GRID_SIZE),
                      pos[1] + 1]#(math.sin(dir / 2 * math.pi) * GRID_SIZE)]
            
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
