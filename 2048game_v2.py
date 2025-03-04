import numpy as np
import random

cage = np.array([[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]])

for i in range(0,random.randint(1,2)):
    cage[random.randint(0,3),random.randint(0,3)] = 2

def detecting (cage):
    emptyplace = np.where( cage== 0)

    x=emptyplace[0]
    y=emptyplace[1]
    return x,y 

def move_direcrion(behave_input=0,cage_def=np.array([[0,0,0,0],
                                                     [0,0,0,0],
                                                     [0,0,0,0],
                                                     [0,0,0,0]])):

    point = 0
    ram_change_def = 0

    if random.randint(0,9)==0:
        new_block = 4
    else:
        new_block = 2

    for plc_x in [0,1,2]:
        for plc_y in [0,1,2,3]:
            if cage_def[plc_x,plc_y]==cage_def[plc_x+1,plc_y]:moveable=1
    for plc_x in [0,1,2,3]:
        for plc_y in [0,1,2]:
            if cage_def[plc_x,plc_y]==cage_def[plc_x,plc_y+1]:moveable=1

    empty_x,empty_y = detecting(cage_def)

    if moveable and len(empty_x) == 0:
        text = 'unmoveable'
        return cage_def,point,text
    
    if behave_input == 1 :             #right move
        for i in range(0,4):
            ram = cage_def[i,0:4]
            ram_b = cage_def[i,0:4]
            for j in [3,3,2,3,2,1,3,2,1,0]: 
                if ram[j] == 0:
                    ram = np.delete(ram,j)
                    ram = np.insert(ram,0,0)
            for k in [3,2,1]:
                if ram[k] == ram[k-1] and ram[k] != 0 :
                    ram[k-1] = ram[k]*2
                    point = point+ram[k-1]
                    ram = np.delete(ram,k)
                    ram = np.insert(ram,0,0)
            if np.array_equal(ram,ram_b) == 0:
                ram_change_def += 1
            cage_def[i,0:4] = ram

        if ram_change_def != 0:
            empty_x,empty_y = detecting(cage_def)
            ran = random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text = 'moving rignt'
        else:
            text = 'didnt move'

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
                    ram[k-1]=ram[k]*2
                    point = point+ram[k-1]
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,0,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[0:4,i] = ram

        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text='moving down'
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
                    ram[k+1]=ram[k]*2
                    point = point+ram[k+1]
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,3,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[i,0:4] = ram

        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text='moving left'
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
                    ram[k+1]=ram[k]*2
                    point = point+ram[k+1]
                    ram=np.delete(ram,k)
                    ram=np.insert(ram,3,0)
            if np.array_equal(ram,ram_b)==0:
                ram_change_def+=1
            cage_def[0:4,i] = ram

        if ram_change_def!=0:
            empty_x,empty_y = detecting(cage_def)
            ran=random.randint(0,len(empty_x)-1)
            cage_def[empty_x[ran],empty_y[ran]] = new_block
            text = 'moving up'
        else:
            text = 'didnt move'


    return cage_def,point,text
    
out_put = ''
now_point=0
print(cage)

while out_put != 'unmoveable':
    behave=int(input('1=right,2=down,3=left,4=up:'))
    cage,ram_point,out_put=move_direcrion(behave,cage)
    now_point = now_point+ram_point
    print(out_put)
    print(cage)
    print('now point:',now_point)

print('game over')
print(cage)
print('final point:',now_point)