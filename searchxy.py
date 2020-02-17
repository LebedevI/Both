import pygame
import sys
import pyperclip


from tkinter import *

size_window = (WIDTH, HEIGHT) = (300, 90)

# Определяем цвета
color_background = (44,49,51)  # серый

pygame.init() #Инициализируем pygame
pygame.display.set_caption('Cursor coordinates') #выводим заголовок окна окна

screen = pygame.display.set_mode(size_window) # Закидываем всю структуру в переменную
window = Tk() # присваиваем класс ткинтера в переменную
text = Text()
clock = pygame.time.Clock() # создаем таймер


while True: #запускаем основной цикл и обрабатываем в нем же корректный выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(color_background) #устанавливаем фон
    font = pygame.font.Font(None, 25 ) #шрифт
    xy = str(window.winfo_pointerxy())# получаем координаты x y
    text = font.render('Координаты равны: ' + str(xy), True, (113, 150, 167))# форматируем и пихаем в text
    screen.blit(text, [20, 30]) #выводим на экран в определенном месте

    # Рисунок появится после обновления экрана
    pygame.display.flip()
    clock.tick(30)

    keys = pygame.key.get_pressed() # обработчик нажатых клавиш

    if keys[pygame.K_SPACE]:
        pyperclip.copy(xy[1:-1]) #заносим в буфер обмена значения координат 

