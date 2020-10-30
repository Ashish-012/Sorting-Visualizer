import pygame
import random


pygame.init()


''' rgb value of general colours that we can use (have to add more colours) '''
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
purple = (128,0,128)

''' Dimension of the game window '''
w = 800
h = 600


''' Initial x and y coordinates of the rectangles '''
x = 80
y = 550


''' Drawing the game window and setting the caption '''
window = pygame.display.set_mode((w,h))
pygame.display.set_caption('Sorting Visualizer')


''' Heights of the bars we have to sort (should add a random function to generate this height) '''
heights = [185, 40, 190, 200, 130, 381, 150, 358, 21, 80, 77, 282, 180, 100, 252, 164, 196, 130, 145, 200, 300, 155]


''' Drawing the rectangles to visualize '''
# def drawrect(heights):
#     for i in range(len(heights)):
#         pygame.draw.rect(window, white, (x + 30*i, y, 20, heights[i]- h + 150 ))

''' Drawing and Updating the rectangles while sorting '''        
def update(swap1 = None, swap2 = None, window = window, s = None, first = False):
    window.fill(black)

    for i in range(len(heights)):
        ''' white means array is sorting, purple after sorting, red means those elements are active '''
        if first == False:
            color = white
        else: 
            color = purple

        if swap1 == i or swap2 == i:
            color = red
        
        elif s != None and i in s:
            color = purple
        ''' drawing the rectangles '''
        pygame.draw.rect(window, color, (x + 30*i, y, 20, heights[i]- h + 150 ))

    '''updating the window after every iteration '''
    pygame.display.update()

''' Randomise the array '''
def generate_height(heights):
    random.shuffle(heights)


''' game fps '''
FPS = 120
clock = pygame.time.Clock()

run = True
sort = False
''' List containing sorted elements '''
l = [] 

''' Main game loop (will run till the run is True) '''
while run:
    
    ''' Capturing all the events since the last game loop and checking if any useful key is pressed '''
    for event in pygame.event.get():

        ''' Quit if the user clicks quit button '''
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        ''' If a key is pressed and it is spacebar start the sorting (have to add more keys for different functionalities thats why we used seperate if statements intead of `and`) '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                sort = True
            ''' randomise the array if `r` is pressed '''
            if event.key == pygame.K_r:
                generate_height(heights)


    ''' Only display the bars till the spacebar is pressed to sort '''
    if sort == False:
        ''' filling the background with black colour'''
        window.fill(black)

        ''' drawing the rectangles '''
        update(first = True)

        ''' updating the game window at every iteration of the loop '''
        pygame.display.update()
    
    
    elif sort == True :

        ''' Bubble Sort algo '''
        for i in range(len(heights)):

            for j in range(len(heights)-i-1):
            
                ''' updating the display at every iteration to make the active rectangles of different colours '''
                update(swap1 = j, swap2 = j+1, s = l)

                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]

                ''' creating a delay so that we can see the list during the sorting process '''
                pygame.time.delay(50)
            
            l.append(len(heights)-i)
            update(s = l)

            ''' old code might need it later '''
                # ''' filling the screen black before updating the position of bars'''
                # window.fill(black)

                # drawrect(heights)

                # ''' adding delay to properly visualize '''
                # pygame.time.delay(100)

                # ''' update the game window after every swap '''
                # pygame.display.update()
        l.clear()
        sort = False

    clock.tick(FPS)

