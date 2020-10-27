import pygame


pygame.init()


''' rgb value of general colours that we can use (have to add more colours) '''
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


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
def drawrect(heights):
    for i in range(len(heights)):
        pygame.draw.rect(window, white, (x + 30*i, y, 20, heights[i]- h + 150 ))


''' game fps '''
FPS = 120
clock = pygame.time.Clock()

run = True
sort = False

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


    ''' Only display the bars till the spacebar is pressed to sort '''
    if sort == False:
        ''' filling the background with black colour'''
        window.fill(black)

        ''' drawing the rectangles '''
        drawrect(heights)

        ''' updating the game window at every iteration of the loop '''
        pygame.display.update()
    
    
    elif sort == True :

        ''' Bubble Sort algo '''
        for i in range(len(heights)):
            for j in range(len(heights)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                
                ''' filling the screen black before updating the position of bars'''
                window.fill(black)

                drawrect(heights)

                ''' adding delay to properly visualize '''
                pygame.time.delay(100)

                ''' update the game window after every swap '''
                pygame.display.update()

        sort = False

    clock.tick(FPS)

