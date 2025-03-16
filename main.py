import pygame as pg, math, numpy as np, random as r

pg.font.init()

###VARIABLES###

FOV = 70
WIDTH, HEIGHT = RES = (1280, 720)
DIST = 10
LINES_WIDTH = 3

FPS = 60
font = pg.font.SysFont('calibri', 36)
clock = pg.time.Clock()


###CUBE###

FACES = [
    #Bottom
    [
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5]
    ],

    #Top
    [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, -0.5, 0.5],
        [-0.5, -0.5, 0.5]
    ],

    #Front
    [
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5]
    ],

    #Back
    [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5]
    ]
]

TRIANGLE = [
    #Bottom
    [
        [-0.5, 0.5, -0.5],
        [0, -1, 0],
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5],
        [0, -1, 0],
        [0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
        [0, -1, 0],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [0, -1, 0],
        [-0.5, 0.5, 0.5],
        [-0.5, 0.5, -0.5],
        [0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
    ],
]

SEXAGON = [
    [
        [0, 0.5, 0],
        [0, 0, -0.3],
        [0, 0.5, 0],
        [0.3, 0.3, 0],
        [0, 0, -0.3],
        [0.3, 0.3, 0],
        [0.5, 0, 0],
        [0, 0, -0.3],
        [0.5, 0, 0],
        [0.3, -0.3, 0],
        [0, 0, -0.3],
        [0.3, -0.3, 0],
        [0, -0.5, 0],
        [0, 0, -0.3],
        [0, -0.5, 0],
        [-0.3, -0.3, 0],
        [0, 0, -0.3],
        [-0.3, -0.3, 0],
        [-0.5, 0, 0],
        [0, 0, -0.3],
        [-0.5, 0, 0],
        [-0.3, 0.3, 0],
        [0, 0, -0.3],
        [-0.3, 0.3, 0]
    ],
    [
        [0, 0.3, 0],
        [0.3, 0.3, 0],
        [0.5, 0, 0],
        [0.3, -0.3, 0],
        [0, -0.5, 0],
        [-0.3, -0.3, 0],
        [-0.5, 0, 0],
        [-0.3, 0.3, 0],
    ],
    [
        [0, 0.5, 0.3],
        [0, 0.5, 0],
        [0, 0.5, 0.3],
        [0.3, 0.3, 0.3],
        [0.3, 0.3, 0],
        [0.3, 0.3, 0.3],
        [0.5, 0, 0.3],
        [0.5, 0, 0],
        [0.5, 0, 0.3],
        [0.3, -0.3, 0.3],
        [0.3, -0.3, 0],
        [0.3, -0.3, 0.3],
        [0, -0.5, 0.3],
        [0, -0.5, 0],
        [0, -0.5, 0.3],
        [-0.3, -0.3, 0.3],
        [-0.3, -0.3, 0],
        [-0.3, -0.3, 0.3],
        [-0.5, 0, 0.3],
        [-0.5, 0, 0],
        [-0.5, 0, 0.3],
        [-0.3, 0.3, 0.3],
        [-0.3, 0.3, 0],
        [-0.3, 0.3, 0.3]
    ],

    [
        [0, 0.5, 0.3],
        [0, 0, 0.3],
        [0, 0.5, 0.3],
        [0.3, 0.3, 0.3],
        [0, 0, 0.5],
        [0.3, 0.3, 0.3],
        [0.5, 0, 0.3],
        [0, 0, 0.5],
        [0.5, 0, 0.3],
        [0.3, -0.3, 0.3],
        [0, 0, 0.5],
        [0.3, -0.3, 0.3],
        [0, -0.5, 0.3],
        [0, 0, 0.5],
        [0, -0.5, 0.3],
        [-0.3, -0.3, 0.3],
        [0, 0, 0.5],
        [-0.3, -0.3, 0.3],
        [-0.5, 0, 0.3],
        [0, 0, 0.5],
        [-0.5, 0, 0.3],
        [-0.3, 0.3, 0.3],
        [0, 0, 0.5],
        [-0.3, 0.3, 0.3]
    ],

]

IDEAL_FIGURE = [
    [
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],

        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1],

        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],

        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1],
    ]
]

def transformTo2D(xory, z):
    angleR = (FOV / 180) * math.pi
    return xory / (z * math.tan(angleR / 2))

def draw(faces, x, y, z):
    for i in faces:
        for j in range(len(i)):
            # if pg.key.get_pressed()[pg.K_w]:
            #     i[j][1]-=0.1
            # if pg.key.get_pressed()[pg.K_d]:
            #     i[j][0]+=0.1
            # if pg.key.get_pressed()[pg.K_s]:
            #     i[j][1]+=0.1
            # if pg.key.get_pressed()[pg.K_a]:
            #     i[j][0]-=0.1
            if pg.key.get_pressed()[pg.K_RIGHT]:
                i[j][0], i[j][1], i[j][2] = rotateY(i[j][0], i[j][1], i[j][2], 0.1)
            if pg.key.get_pressed()[pg.K_LEFT]:
                i[j][0], i[j][1], i[j][2] = rotateY(i[j][0], i[j][1], i[j][2], -0.1)
            if pg.key.get_pressed()[pg.K_UP]:
                i[j][0], i[j][1], i[j][2] = rotateX(i[j][0], i[j][1], i[j][2], 0.1)
            if pg.key.get_pressed()[pg.K_DOWN]:
                i[j][0], i[j][1], i[j][2] = rotateX(i[j][0], i[j][1], i[j][2], -0.1)
            if pg.key.get_pressed()[pg.K_n]:
                i[j][0], i[j][1], i[j][2] = rotateZ(i[j][0], i[j][1], i[j][2], 0.1)
            if pg.key.get_pressed()[pg.K_m]:
                i[j][0], i[j][1], i[j][2] = rotateZ(i[j][0], i[j][1], i[j][2], -0.1)
            if pg.key.get_pressed()[pg.K_q]:
                i[j][0], i[j][1], i[j][2] = rotateX(i[j][0], i[j][1], i[j][2], -0.01)
                i[j][0], i[j][1], i[j][2] = rotateY(i[j][0], i[j][1], i[j][2], -0.01)
                i[j][0], i[j][1], i[j][2] = rotateZ(i[j][0], i[j][1], i[j][2], -0.01)
            

            pg.draw.circle(sc, (255, 255, 255), (transformTo2D(i[j][0]*WIDTH+WIDTH/2, i[j][2]+z)+x, transformTo2D(i[j][1]*HEIGHT+HEIGHT/2, i[j][2]+z)+y), 2)
            pg.draw.line(sc, (150, 60, 30), (transformTo2D(i[j][0]*WIDTH+WIDTH/2, i[j][2]+z)+x, transformTo2D(i[j][1]*HEIGHT+HEIGHT/2, i[j][2]+z)+y), (transformTo2D(i[j-1][0]*WIDTH+WIDTH/2, i[j-1][2]+z)+x, transformTo2D(i[j-1][1]*HEIGHT+HEIGHT/2, i[j-1][2]+z)+y), 2)
            # pg.draw.polygon(sc, (0, 255, 0), ((transformTo2D(i[j][0]*WIDTH+WIDTH/2, i[j][2]+z)+x, transformTo2D(i[j][1]*HEIGHT+HEIGHT/2, i[j][2]+z)+y), (transformTo2D(i[j-1][0]*WIDTH+WIDTH/2, i[j-1][2]+z)+x, transformTo2D(i[j-1][1]*HEIGHT+HEIGHT/2, i[j-1][2]+z)+y), 
            #                                   (transformTo2D(i[j-2][0]*WIDTH+WIDTH/2, i[j-2][2]+z)+x, transformTo2D(i[j-2][1]*HEIGHT+HEIGHT/2, i[j-2][2]+z)+y)))
def rotateX(x, y, z, angle):
    cord = np.array([x, y, z])
    rotateXm = np.array([[1, 0, 0],
                        [0, math.cos(angle), -math.sin(angle)],
                        [0, math.sin(angle), math.cos(angle)]])
    
    return np.matmul(cord, rotateXm)
    
def rotateY(x, y, z, angle):
    cord = np.array([x, y, z])
    rotateYm = np.array([[math.cos(angle), 0, math.sin(angle)],
                        [0, 1, 0],
                        [-math.sin(angle), 0, math.cos(angle)]])
    
    return np.matmul(cord, rotateYm)

def rotateZ(x, y, z, angle):
    cord = np.array([x, y, z])
    rotateZm = np.array([[math.cos(angle), -math.sin(angle), 0],
                        [math.sin(angle), math.cos(angle), 0],
                        [0, 0, 1]])
    
    return np.matmul(cord, rotateZm)

pg.init()

sc = pg.display.set_mode(RES)
pg.display.set_caption("3D projection")

run = True
while run:
    clock.tick(FPS)
    text = font.render(str(clock.get_fps), (255, 255, 255), False, False)

    sc.fill((0, 10, 50))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    draw(SEXAGON, WIDTH/2-WIDTH/2.5, HEIGHT/2-HEIGHT/6, 10)
    draw(FACES, WIDTH/2-WIDTH/8, HEIGHT/2-HEIGHT/6, 10)
    draw(TRIANGLE, WIDTH/2+WIDTH/6, HEIGHT/2-HEIGHT/6, 10)
    sc.blit(text, (50, 50))
    pg.display.flip()