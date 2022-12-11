import pygame


screen = pygame.display.set_mode((500,500))   # длина и ширина экрана(можно вынести в одтельную переменную)
#экран будет сразу исчезать, если не создать ЦИКЛ ОБРАБОТКИ СОБЫТИЙ(игровой цикл)
pygame.display.set_caption("крестики-нолики")  # заголовок окна программы
width_square = heigth_square = 160 # ширина и высота квадратика
margin = 10                       # отступ, иначе будет просто полоска склееных квадратов
red = (255, 0, 0)               # RGB!
white = (255, 255, 255)        
lst = [[0] * 10 for i in range(10)]                  
while True:                                  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        # выход из программы через нажатие на крестик
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()   # получение координат при нажатии мышки
            print(x_mouse,y_mouse)
            column = x_mouse // (margin + width_square)
            row = y_mouse // (margin + heigth_square)
            lst[row][column] = 1
    for row in range(10): 
        for col in range(10):
            if lst[row][col] == 1:
                color = red
            else:
                color = white    
            x = col * width_square + (col + 1) * margin
            y = row * heigth_square + (row + 1) * margin                         
            pygame.draw.rect(screen,color, (x, y, width_square, heigth_square))   
    pygame.display.update()                                            
    
#img = pygame.image.load("путь к файлу с картинкой") иконка окна программы
#pygame.display.set_icon(img)