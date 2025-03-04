import pygame
import numpy as np
import random

pygame.init()

cage = np.array([[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]])

for i in range(0,random.randint(2,3)):
    cage[random.randint(0,3),random.randint(0,3)] = 1

key = pygame.key.get_pressed()
#視窗大小
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 750
#常用顏色
BROWN = (172,157,143)
LIGHT_BROWN = (192,179,164)
#建立視窗及頻率鐘
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('2048')
clock = pygame.time.Clock()

pygame.font.init()          # if you want to use this module.

def print_on_screen(text='',sizes=30,place=(450,90)):
    my_font = pygame.font.SysFont('clear-sans.bold', sizes)
    text_surface = my_font.render(text, False, (77,57,0))
    gameDisplay.blit(text_surface,place)

def block_place(b,a):

    '''
    a=(0,1,2,3)
    b=(0,1,2,3)
    從左到右，從上到下
    '''
    an=30+a*140
    bn=180+b*140
    return (an,bn)

def load(num):
    pygame.image.load('2048game_and_ai\image'+'\\'+str(2**num)+'.png')

for i in range(1,19): block = load(i)

def put_image(place,image,getting_big=0):

    '''
    place=(x,y)
    image=log(target_number)
    getting big=0(no) 1(yes)

    '''
    if getting_big == 1:
        for i in range(1,21):
            now_image=pygame.image.load('2048game_and_ai\image'+'\\'+str(2**image)+'.png')
            now_image=pygame.transform.scale(now_image, (6*i, 6*i))
            gameDisplay.blit( now_image ,(place[0]+60-3*i,place[1]+60-3*i))
            pygame.display.update()
    else:
        now_image=pygame.image.load('2048game_and_ai\image'+'\\'+str(2**image)+'.png')
        now_image=pygame.transform.scale(now_image, (120, 120))
        gameDisplay.blit( now_image , place)

def detecting (cage):
    emptyplace = np.where( cage== 0)

    x=emptyplace[0]
    y=emptyplace[1]
    return x,y 

def move_direcrion(behave_input=0,cage_def=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])):

    moving = 0
    point = 0
    ram_change_def = 0

    if random.randint(0,9)==0:
        new_block = 2
    else:
        new_block = 1

    for plc_x in [0,1,2]:
        for plc_y in [0,1,2,3]:
            if cage_def[plc_x,plc_y]==cage_def[plc_x+1,plc_y]:moving=1
    for plc_x in [0,1,2,3]:
        for plc_y in [0,1,2]:
            if cage_def[plc_x,plc_y]==cage_def[plc_x,plc_y+1]:moving=1

    empty_x,empty_y = detecting(cage_def)

    if moving == 0 and len(empty_x) == 0:
        text = 'unmoving'
        return cage_def,point,text
    
    if behave_input == 1 :             #right move
        for i in range(0,4):
            ram = cage_def[i,0:4]
            ram_b = cage_def[i,0:4]
            for j in [3,3,2,3,2,1,3,2,1,0]: 
                if ram[j] == 0:
                    ram=np.delete(ram,j)
                    ram=np.insert(ram,0,0)
            for k in [3,2,1]:
                if ram[k] == ram[k-1] and ram[k] !=0 :
                    point = point+(2**(ram[k-1]+1))
                    ram[k-1]=ram[k]+1
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,0,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[i,0:4] = ram
        display_all(cage_def)


        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text='moving rignt'
            put_image(block_place(empty_x[ran],empty_y[ran]),new_block,1)

        else:
            text='didnt move'

    if behave_input == 2 :             #down move
        for i in range(0,4):
            ram = cage_def[0:4,i]
            ram_b = cage_def[0:4,i]
            for j in [3,3,2,3,2,1,3,2,1,0]: 
                if ram[j] == 0:
                    ram=np.delete(ram,j)
                    ram=np.insert(ram,0,0)
            for k in [3,2,1]:
                if ram[k] == ram[k-1] and ram[k] !=0 :
                    point = point+(2**(ram[k-1]+1))
                    ram[k-1]=ram[k]+1
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,0,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[0:4,i] = ram
        display_all(cage_def)


        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text='moving down'
            put_image(block_place(empty_x[ran],empty_y[ran]),new_block,1)

        else:
            text='didnt move'

    if behave_input == 3 :             #left move
        for i in range(0,4):
            ram = cage_def[i,0:4]
            ram_b = cage_def[i,0:4]
            for j in [0,0,1,0,1,2,0,1,2,3]: 
                if ram[j] == 0:
                    ram=np.delete(ram,j)
                    ram=np.insert(ram,3,0)
            for k in [0,1,2]:
                if ram[k] == ram[k+1] and ram[k] !=0 :
                    point = point+(2**(ram[k]+1))
                    ram[k+1]=ram[k]+1
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,3,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[i,0:4] = ram
        display_all(cage_def)


        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text='moving left'
            put_image(block_place(empty_x[ran],empty_y[ran]),new_block,1)

        else:
            text='didnt move'

    if behave_input == 4 :             #up move
        for i in range(0,4):
            ram = cage_def[0:4,i]
            ram_b = cage_def[0:4,i]
            for j in [0,0,1,0,1,2,0,1,2,3]: 
                if ram[j] == 0:
                    ram=np.delete(ram,j)
                    ram=np.insert(ram,3,0)
            for k in [0,1,2]:
                if ram[k] == ram[k+1] and ram[k] !=0 :
                    point = point+(2**(ram[k]+1))
                    ram[k+1]=ram[k]+1
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,3,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[0:4,i] = ram
        display_all(cage_def)


        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text = 'moving up'
            put_image(block_place(empty_x[ran],empty_y[ran]),new_block,1)

        else:
            text = 'didnt move'


    return cage_def,point,text

def display_cage(cage_now):
    for i in [0,1,2,3]:
        for j in [0,1,2,3]:
            if cage_now[i,j]!=0:
                put_image(block_place(i,j),cage_now[i,j])

def display_all(cage):
    gameDisplay.fill(BROWN)
    for i in [30,170,310,450]:
        for j in [180,320,460,600]:pygame.draw.rect(gameDisplay,LIGHT_BROWN,(i,j,120,120),0,20) 
    display_cage(cage)
    pygame.draw.rect(gameDisplay,LIGHT_BROWN,(440,110,150,60),0,10)
    pygame.draw.rect(gameDisplay,LIGHT_BROWN,(440,40,150,60),0,10)
    print_on_screen('NOW POINT',30,(455,115))
    print_on_screen('BEST POINT',30,(453,45))
    print_on_screen('2 0 4 8',150,(45,30))
    print_on_screen('I dont wanna wait for my life to begin',30,(10,118))
    print_on_screen('I cant explain how',30,(10,136))
    print_on_screen('But I feel it in the eye as it touches my skin',30,(10,156))
    print_on_screen(str(best_point),50,(445,65))
    print_on_screen(str(now_point),50,(445,135))
    pygame.display.update()

ram_point=0
out_put = ''
now_point=0
best_point=0

playing = True

up_key_pressed = False
down_key_pressed = False
right_key_pressed = False
left_key_pressed = False
r_key_pressed = False

display_all(cage)

while playing:
    
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not up_key_pressed:
                up_key_pressed = True
                cage,ram_point,out_put=move_direcrion(4,cage)
            if event.key == pygame.K_DOWN and not down_key_pressed:
                down_key_pressed = True
                cage,ram_point,out_put=move_direcrion(2,cage)
            if event.key == pygame.K_RIGHT and not right_key_pressed:
                right_key_pressed = True
                cage,ram_point,out_put=move_direcrion(1,cage)
            if event.key == pygame.K_LEFT and not left_key_pressed:
                left_key_pressed = True
                cage,ram_point,out_put=move_direcrion(3,cage)

            now_point=now_point+ram_point
            
            
            if best_point <= now_point:
                best_point=now_point 
            display_all(cage)

            if out_put == 'unmoving':

                pygame.draw.rect(gameDisplay,LIGHT_BROWN,(150,350,330,50),0,10)
                print_on_screen('PRESS R TO RETRY',45,(170,355))
                pygame.display.update()

                if event.key == pygame.K_r and not r_key_pressed:
                    r_key_pressed = True
                    if best_point < now_point:
                        best_point,now_point=now_point,0
                    else:
                        now_point=0
                    cage,ram_point,out_put=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),0,''
                    for i in range(0,random.randint(2,3)):cage[random.randint(0,3),random.randint(0,3)] = 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_key_pressed = False
            if event.key == pygame.K_DOWN:
                down_key_pressed = False
            if event.key == pygame.K_LEFT:
                left_key_pressed = False
            if event.key == pygame.K_RIGHT:
                right_key_pressed = False
            if event.key == pygame.K_r:
                r_key_pressed = False


    clock.tick(60)
    
print('game over')
print(cage)
print('final point:',now_point)

pygame.quit()