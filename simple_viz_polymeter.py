lens = [3, 9, 5, 11]
t_c = 0

def setup():
    size(500, 500)
    background(255)
    frameRate(6)
    noStroke()

def draw():
    global lens, t_c
    background(255)
    for i, x in enumerate(lens):
        fill(0)
        circle(width / 4 * i + 60, t_c % x * 40 + 20, 30)
    t_c += 1
