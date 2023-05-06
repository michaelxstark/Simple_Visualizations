randlist = [int(random(30) + 5) for i in range(10)]

def setup():
    size(400, 400)
    background(255)
    frameRate(6)

def draw():
    global randlist
    background(255)
    counter = 0
    for i in range(len(randlist) - 1):
        if randlist[i] < randlist[i+1]:
            randlist[i], randlist[i+1] = randlist[i+1], randlist[i]
            counter += 1
    for x, y in enumerate(randlist):
        circle(x * 40 + 50, height/2, y)
    print(randlist)
    if counter < 1:
        noLoop()
