import pygame
import time
import random
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
exit12ic = (22,70,70)
exit12ac = (40,90,90)


score = 0
ammo = 0
money = 0
kids = 0
HP = 100
sentence = 0
fsr = 1
timerFS = 0
timerColBikeL = 0
timerColBikeR = 0
ksispeed = 1
bulletL = False
#food stamp rate

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Wakanda simulator')
clock = pygame.time.Clock()

ksiImg = pygame.image.load('ksibaldre.jpg')
(ksi_width,ksi_height) = ksiImg.get_rect().size

wmImg = pygame.image.load('wm.png')
(wm_width, wm_height) = wmImg.get_rect().size

kfcImg = pygame.image.load('kfc.png')
(kfc_width,kfc_height) = kfcImg.get_rect().size

koolaidImg = pygame.image.load('koolaid.png')
(koolaid_width,koolaid_height) = koolaidImg.get_rect().size

foodstampImg = pygame.image.load('foodstamp.png')
(foodstamp_width,foodstamp_height) = foodstampImg.get_rect().size

deImg = pygame.image.load('de.png')
(de_width,de_height) = deImg.get_rect().size

tyraLImg = pygame.image.load('tyraL.png')
(tyraL_width,tyraL_height) = tyraLImg.get_rect().size

tyraRImg = pygame.image.load('tyraR.png')
(tyraR_width,tyraR_height) = tyraRImg.get_rect().size

bikeLImg = pygame.image.load('bikeL.png')
(bikeL_width, bikeL_height) = bikeLImg.get_rect().size

bikeRImg = pygame.image.load('bikeR.png')
(bikeR_width, bikeR_height) = bikeRImg.get_rect().size

exit12Img = pygame.image.load('exit12.png')
(exit12_width, exit12_height) = exit12Img.get_rect().size

welfareImg = pygame.image.load('welfare.png')
(welfare_width, welfare_height) = welfareImg.get_rect().size

debulletLImg = pygame.image.load('debulletL.png')
(debulletL_width,debulletL_height) = debulletLImg.get_rect().size

debulletRImg = pygame.image.load('debulletR.png')
(debulletR_width,debulletR_height) = debulletRImg.get_rect().size

neiltysonImg = pygame.image.load('neiltyson.png')

sheeeitImg = pygame.image.load('sheeeit.png')


pygame.mixer.music.load('wdtbs.wav')
pygame.mixer.music.play(-1)


print(deImg.get_rect())


def ksi(x,y):
    gameDisplay.blit(ksiImg,(x,y))

def wm(wm_x,wm_y):
    gameDisplay.blit(wmImg, (wm_x,wm_y))

def kfc(kfc_x,kfc_y):
    gameDisplay.blit(kfcImg, (kfc_x,kfc_y))
def koolaid(koolaid_x,koolaid_y):
    gameDisplay.blit(koolaidImg, (koolaid_x,koolaid_y))
def de(de_x,de_y):
    gameDisplay.blit(deImg, (de_x,de_y))
def tyraL(tyraL_x,tyraL_y):
    gameDisplay.blit(tyraLImg, (tyraL_x,tyraL_y))
def tyraR(tyraR_x,tyraR_y):
    gameDisplay.blit(tyraRImg, (tyraR_x,tyraR_y))
def foodstamp(foodstamp_x,foodstamp_y):
    gameDisplay.blit(foodstampImg, (foodstamp_x,foodstamp_y))
def bikeL(bikeL_x,bikeL_y):
    gameDisplay.blit(bikeLImg, (bikeL_x, bikeL_y))
def bikeR(bikeR_x,bikeR_y):
    gameDisplay.blit(bikeRImg, (bikeR_x, bikeR_y))
def exit12():
    gameDisplay.blit(exit12Img,(0,0))
def welfare(welfare_x,welfare_y):
    gameDisplay.blit(welfareImg,(welfare_x, welfare_y))
def debulletL(debulletL_x,debulletL_y):
    gameDisplay.blit(debulletLImg, (debulletL_x,debulletL_y))
def debulletR(debulletR_x,debulletR_y):
    gameDisplay.blit(debulletRImg, (debulletR_x,debulletR_y))





def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    textSurf,textRect = text_objects(text,largeText,red)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(1.5)



def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect( )

def HUD():
    scoretext = "Score: " + str(score)
    scoreText = pygame.font.Font('freesansbold.ttf',30)
    scoreTextSurf, scoreTextRect = text_objects(scoretext,scoreText,white)
    score_width,score_height = scoreTextRect.size
    scoreTextRect = (display_width -score_width,0)
    gameDisplay.blit(scoreTextSurf,scoreTextRect)

    hptext = 'HP: '
    hpText = pygame.font.Font('freesansbold.ttf',25)
    hpTextSurf,hpTextRect = text_objects(hptext,hpText,white)
    hp_width,hp_height = hpTextRect.size
    hpTextRect = (0,0)
    gameDisplay.blit(hpTextSurf,hpTextRect)
    pygame.draw.rect(gameDisplay,green,(hp_width,hp_height/2-8, HP, 15))

    ammotext = 'Ammo: ' + str(ammo)
    ammoText = pygame.font.Font('freesansbold.ttf',25)
    ammoTextSurf,ammoTextRect = text_objects(ammotext,ammoText,white)
    ammo_width,ammo_height = ammoTextRect.size
    ammoTextRect = (0,hp_height)
    gameDisplay.blit(ammoTextSurf,ammoTextRect)

    kidstext = 'Kids: ' + str(kids)
    kidsText = pygame.font.Font('freesansbold.ttf', 18)
    kidsTextSurf, kidsTextRect = text_objects(kidstext, kidsText, white)
    kids_width, kids_height = kidsTextRect.size
    kidsTextRect = (0, hp_height+ammo_height)
    gameDisplay.blit(kidsTextSurf, kidsTextRect)

    if sentence <= 1:
        sentencetext = 'Sentence: ' + str(sentence) + ' year'
        sentenceText = pygame.font.Font('freesansbold.ttf', 18)
        sentenceTextSurf, sentenceTextRect = text_objects(sentencetext, sentenceText, white)
        sentence_width, sentence_height = sentenceTextRect.size
        sentenceTextRect = (0, hp_height + ammo_height + kids_height)
        gameDisplay.blit(sentenceTextSurf, sentenceTextRect)
    else:
        sentencetext = 'Sentence: ' + str(sentence) + ' years'
        sentenceText = pygame.font.Font('freesansbold.ttf', 18)
        sentenceTextSurf, sentenceTextRect = text_objects(sentencetext, sentenceText, white)
        sentence_width, sentence_height = sentenceTextRect.size
        sentenceTextRect = (0, hp_height + ammo_height + kids_height)
        gameDisplay.blit(sentenceTextSurf, sentenceTextRect)

    moneytext = 'Money: $' + str(money)
    moneyText = pygame.font.Font('freesansbold.ttf', 18)
    moneyTextSurf, moneyTextRect = text_objects(moneytext, moneyText, white)
    money_width, money_height = moneyTextRect.size
    moneyTextRect = (0, hp_height + ammo_height + kids_height + sentence_height)
    gameDisplay.blit(moneyTextSurf, moneyTextRect)

    pygame.display.update()

def crash():
    message_display('Thanks Obama')
    x_change = 0
    gameDisplay.blit(sheeeitImg, (0,0))
    pygame.display.update()
    time.sleep(1)
    gameloop()
# ic = inactive color, ac = active color
def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                gameloop()
            elif action == "quit":
                gameDisplay.blit(neiltysonImg, (0, 0))
                pygame.display.update()
                time.sleep(6)
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    textSurf, textRect = text_objects(msg, largeText, black)
    textRect.center = (x + w//2, y + h//2)
    gameDisplay.blit(textSurf, textRect)


def collision(ax,ay,aw,ah,bx,by,bw,bh,inc):
    if (by + bh > ay and ah + ay > by) and (ax + aw > bx and  bx + bw > ax):
        global score
        score += inc
        return True
# def addonVer(item_x,item_y,col,r1,r2):
#     global
#     if item_y > display_height or col == True:
#         item_x = random.randrange(0,display_width)
#         item_y = random.randrange(r1,r2)
#  global item_x
#     ^
# SyntaxError: name 'item_x' is parameter and global


def game_intro():
    exit12()

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = text_objects("Black People", largeText, white)
        textRect.center = (650, 550)
        gameDisplay.blit(textSurf, textRect)
        button("Education and civility",296,86,215,162,exit12ic,exit12ac,"quit")
        button("Gangsta and sheeit",626,86,311,162,exit12ic,exit12ac,"play")
        pygame.display.update()




def gameloop():
    pygame.event.clear()
    x = display_width*0.45
    y = display_height*0.8
    x_change = 0
    y_change = 0
    global bulletL
    global ammo


    wm_x = random.randrange(-wm_width,display_width)
    wm_y = -500
    wm_speed = 6
    kfc_x = random.randrange(-kfc_width,display_width)
    # change lower limit from 0 to -image_width so image can spawn partially on LHS
    kfc_y = random.randrange(-1500,-100)
    kfc_speed = 8
    koolaid_x = random.randrange(-koolaid_width,display_width)
    koolaid_y = random.randrange(-1200,-100)
    koolaid_speed = 7
    foodstamp_x = random.randrange(-foodstamp_width,display_width)
    foodstamp_y = random.randrange(-20000,-15000)
    foodstamp_speed = 5
    de_x = random.randrange(-de_width,display_width)
    de_y = random.randrange(-5000,-1000)
    de_speed = 7

    bikeL_x = random.randrange(1000,2000)
    bikeL_y = random.randrange(-bikeL_height,display_height)
    bikeL_speed = -9

    bikeR_x = random.randrange(-2000,-1000)
    bikeR_y = random.randrange(-bikeR_height, display_height)
    bikeR_speed = 9

    tyraL_x = random.randrange(2000,3000)
    tyraL_y = random.randrange(-tyraL_height,display_height)
    tyraL_speed = -7
    tyraR_x = random.randrange(-3000,-2000)
    tyraR_y = random.randrange(-tyraR_height, display_height)
    tyraR_speed = 7
    debulletLspeed = debulletRspeed = 15

    welfare_x = random.randrange(-welfare_width,display_width)
    welfare_y = random.randrange(-2000,-100)
    welfare_speed = 8
    debulletL_x = -100
    debulletL_y = -100

    gameExit = False
    key_left = False
    key_right = False
    while not gameExit:
        global ksispeed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change += -5

                if event.key == pygame.K_SPACE:
                    bulletL = True
                    debulletL_x = x
                    debulletL_y = y + ksi_height // 3


                if event.key == pygame.K_d:
                    x_change += 5
                if event.key == pygame.K_w:
                    y_change += -5
                if event.key == pygame.K_s:
                    y_change += 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change += 5
                if event.key == pygame.K_d:
                    x_change += -5
                if event.key == pygame.K_w:
                    y_change += 5
                if event.key == pygame.K_s:
                    y_change += -5

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change += -5 * ksispeed
            #     if event.key == pygame.K_RIGHT:
            #         x_change += 5 * ksispeed
            #     if event.key == pygame.K_UP:
            #         y_change += -5 * ksispeed
            #     if event.key == pygame.K_DOWN:
            #         y_change += 5 * ksispeed
            #
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         x_change += 5 * ksispeed
            #     if event.key == pygame.K_RIGHT:
            #         x_change += -5 * ksispeed
            #     if event.key == pygame.K_UP:
            #         y_change += 5 * ksispeed
            #     if event.key == pygame.K_DOWN:
            #         y_change += -5 * ksispeed

        x += x_change
        y += y_change
        gameDisplay.fill(black)

        wm(wm_x,wm_y)
        wm_y += wm_speed

        kfc(kfc_x,kfc_y)
        kfc_y += kfc_speed

        koolaid(koolaid_x,koolaid_y)
        koolaid_y += koolaid_speed

        foodstamp(foodstamp_x,foodstamp_y)
        foodstamp_y += foodstamp_speed

        de(de_x,de_y)
        de_y += de_speed

        tyraL(tyraL_x,tyraL_y)
        tyraL_x += tyraL_speed

        tyraR(tyraR_x, tyraR_y)
        tyraR_x += tyraR_speed

        bikeL(bikeL_x,bikeL_y)
        bikeL_x += bikeL_speed

        bikeR(bikeR_x,bikeR_y)
        bikeR_x += bikeR_speed

        welfare(welfare_x,welfare_y)
        welfare_y += welfare_speed
        print(bulletL,debulletL_x,debulletL_y,x,y)
        if bulletL == True:
            debulletL(debulletL_x,debulletL_y)
            debulletL_x -= debulletLspeed


        ksi(x,y)

        # defining crash after non positive HP here to prevent drawing HP on the -ve axis using pygame.draw in HUD()
        global HP
        global money
        if HP <= 0:
            HP = 100
            global score
            score = 0
            global kids
            kids = 0

            ammo = 0
            global sentence
            sentence = 0
            crash()
        HUD()
        colwm = collision(x,y,ksi_width,ksi_height,wm_x,wm_y,wm_width,wm_height,5)
        colkfc = collision(x,y,ksi_width,ksi_height,kfc_x,kfc_y,kfc_width,kfc_height,10)
        colkoolaid = collision(x,y,ksi_width,ksi_height,koolaid_x,koolaid_y,koolaid_width,koolaid_height,8)
        colde = collision(x,y,ksi_width,ksi_height,de_x,de_y,de_width,de_height,0)
        coltyraL = collision(x,y,ksi_width,ksi_height,tyraL_x,tyraL_y,tyraL_width,tyraL_height,0)
        coltyraR = collision(x, y, ksi_width, ksi_height, tyraR_x, tyraR_y, tyraR_width, tyraR_height, 0)
        colfoodstamp = collision(x,y,ksi_width,ksi_height,foodstamp_x,foodstamp_y,foodstamp_width,foodstamp_height,0)
        colbikeL = collision(x,y,ksi_width,ksi_height,bikeL_x,bikeL_y,bikeL_width,bikeL_height,0)
        colbikeR = collision(x, y, ksi_width, ksi_height,bikeR_x,bikeR_y,bikeR_width,bikeR_height,0)
        colwelfare = collision(x,y,ksi_width,ksi_height,welfare_x,welfare_y,welfare_width,welfare_height,0)
        # try adding score, ammo.. increase in collision as parameter




        if (x < 0 or x > display_width-ksi_width) or (y < 0 or y > display_height-ksi_height):
            score = 0
            HP = 100
            kids = 0
            ammo = 0
            sentence = 0
            crash()
        if (HP < 200):
            if colwm == True:
                HP += 5
                print(HP)
            if colkfc == True:
                HP += 10
                print(HP)
            if colkoolaid == True:
                HP += 7
                print(HP)
            if HP > 200:
                HP = 200

        global fsr
        # addonVer(wm_x,wm_y,colwm,-700,-100)
        # addonVer(kfc_x,kfc_y,colkfc,-1500,-200)
        if wm_y > display_height or colwm == True:
            wm_x = random.randrange(0,display_width)
            wm_y = random.randrange(-700//fsr,-100//fsr)
        if kfc_y > display_height or colkfc == True:
            kfc_x = random.randrange(0,display_width)
            kfc_y = random.randrange(-2000//fsr,-200//fsr)
        if koolaid_y > display_height or colkoolaid == True:
            koolaid_x = random.randrange(0,display_width)
            koolaid_y = random.randrange(-2000//fsr,-100//fsr)
        if de_y > display_height:
            de_x = random.randrange(0,display_width)
            de_y = random.randrange(-5000,-1000)
            print(ammo)
        if colde == True:
            ammo += 5
            de_x = random.randrange(0, display_width)
            de_y = random.randrange(-5000, -1000)
            print(ammo)
        if tyraL_x < -tyraL_width:
            tyraL_x = random.randrange(2000,3000)
            tyraL_y = random.randrange(-80,600)
            print('kids'+':'+str(kids))
        if coltyraL == True:
            kids += 1
            tyraL_x = random.randrange(2000, 3000)
            tyraL_y = random.randrange(-80, 600)
            print('kids'+':'+str(kids))
        if tyraR_x > display_width:
            tyraR_x = random.randrange(-3000,-2000)
            tyraR_y = random.randrange(-80, 600)
            print('kids' + ':' + str(kids))
        if coltyraR == True:
            kids += 1
            tyraR_x = random.randrange(2000, 3000)
            tyraR_y = random.randrange(-80, 600)
            print('kids' + ':' + str(kids))
        if foodstamp_y > display_height:
            foodstamp_x = random.randrange(-foodstamp_width,display_width)
            foodstamp_y = random.randrange(-20000,-15000)
        if welfare_y > display_height:
            welfare_x = random.randrange(-welfare_width, display_width)
            welfare_y = random.randrange(-2000, -100)
        if colwelfare == True:
            welfare_x = random.randrange(-welfare_width, display_width)
            welfare_y = random.randrange(-2000, -100)
            money += 300



        global timerFS
        if colfoodstamp == True:
            foodstamp_x = random.randrange(-foodstamp_width, display_width)
            foodstamp_y = random.randrange(-20000, -15000)
            fsr = 10
            timerFS = time.time()

        if bikeL_x < -display_width:
            bikeL_x = random.randrange(1000,2000)
            bikeL_y = random.randrange(-bikeL_height, display_height)
        if bikeR_x > display_width:
            bikeR_x = random.randrange(-2000,-1000)
            bikeR_y = random.randrange(-bikeR_height, display_height)
        global timerColBikeL
        global timerColBikeR

        if colbikeL == True:
            bikeL_x = random.randrange(1000, 2000)
            bikeL_y = random.randrange(-bikeL_height, display_height)
            ksispeed = 2
            timerColBikeL = time.time()
        if colbikeR == True:
            bikeR_x = random.randrange(-2000, -1000)
            bikeR_y = random.randrange(-bikeR_height, display_height)
            ksispeed = 2
            timerColBikeR = time.time()
        # takes two bikes to gain speed, goes off at top right angle

        if time.time() - timerFS > 15:
            fsr = 1
        if time.time() - timerColBikeL > 10:
            ksispeed = 1
        if time.time() - timerColBikeR > 10:
            ksispeed = 1










        pygame.display.update()
        clock.tick(60)
game_intro()
gameloop()
pygame.quit()
quit()