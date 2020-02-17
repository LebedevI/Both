import pyautogui
import time
from settings import *
from class_ofbot import create

      
#функция, которая дает возможно заказать нужное кол-во рабочих в здании
def double_production(variable):
    count = 0
    while count < variable:
        pyautogui.press('z')
        count += 1

#выбор первого всадника и отправка на добычу еды
def first_horseman():
    pyautogui.moveTo(740, 487, duration = speed)
    pyautogui.click()
    pyautogui.rightClick(461, 375, duration = speed)

#Запуск игры 
def start_game(): 
    pyautogui.moveTo(101, 440, duration = 1)
    pyautogui.doubleClick()
    pyautogui.moveTo(1430, 173, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(176, 228, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(420, 230, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1820, 999, duration = 1)
    pyautogui.click()
    time.sleep(5)


#Main
start_game()

#Биндим главное здание
pyautogui.click(953, 571, duration = speed)
pyautogui.hotkey('ctrl', '0')

#Заказ 4 рабочих
pyautogui.press('0')
variable = 4
double_production(variable)




first_horseman()

pyautogui.moveTo(735, 632, duration = speed)
pyautogui.click()
pyautogui.hotkey('ctrl', '1')

#постройка первого дома c помощью созданного объекта класса create()
#mycreate ('юнит, кем будем строить','координаты где будем строить','что будем строить')
build = create()
build.mycreate('1',(134, 828), home)
build.get_create()# метод строительства

#отправка крестьян на ягоды
pyautogui.moveTo(778, 652, duration = speed)
pyautogui.click()
pyautogui.hotkey('ctrl', '2')
pyautogui.rightClick(120, 705, duration = speed)

pyautogui.moveTo(815, 682, duration = speed)
pyautogui.click()
pyautogui.hotkey('ctrl', '3')
pyautogui.rightClick(56, 732, duration = speed)

pyautogui.moveTo(852, 715, duration = speed)
pyautogui.click()
pyautogui.rightClick(145, 616, duration = speed)

#Биндим двух солдат на 4-ку
pyautogui.moveTo(1126, 514, duration = speed)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', '4')

#Строительство 1-ой лесопилки
build.mycreate('4',(1120, 455), stock)
build.get_create()

pyautogui.moveTo(1101, 709, duration = speed)
pyautogui.doubleClick()
pyautogui.rightClick(1120, 455, duration = speed)

#ставим точку сбора главцентра на лесопилку
pyautogui.press('0')
pyautogui.rightClick(1235, 402, duration = speed)

#заказываем еще 3-ех рабочих на лес
pyautogui.press('0')
variable = 2
double_production(variable)

#пока ждем 40 сек и строим поле рабочим с леса
time.sleep(35)
pyautogui.click(1232, 428, duration = speed)
pyautogui.hotkey('ctrl', '5')

#строим этим рабочим поле
build.mycreate('5', (1208, 751), field)
build.get_create()

#заказываем на это поле одного рабочего
pyautogui.press('0')
variable = 1
double_production(variable)
pyautogui.rightClick(1208, 751, duration = speed)

#ждем 11 секунда и заказываем на это поле одного рабочего
time.sleep(11)
pyautogui.press('0')
pyautogui.press('z')

#выбираем строителя дома и строим самболин
build.mycreate('1', (925, 820), symbolion)
time.sleep(12)
build.get_create()

time.sleep(14)

#отправляем рабочего на лес
pyautogui.press('0')
pyautogui.press('z')
pyautogui.rightClick(1346, 434, duration = speed)

time.sleep(5)

#строим второе поле
build.mycreate('2', (756, 714), field)
build.get_create()

time.sleep(10)

#отправляем первого рабочего на поле
pyautogui.press('0')
pyautogui.rightClick(756, 714, duration = speed)
pyautogui.press('z')

time.sleep(9)

#отправляем второго рабочего на второе поле
pyautogui.press('z')

time.sleep(17)

#отправляем третьего рабочего на второе поле
pyautogui.press('z')

#выбираем рабочего для постройки загона и строим его
build.mycreate('3', (310, 736), paddok)
build.get_create()

time.sleep(1)

#освободившимя рабочим помогаем строить загон
pyautogui.press('1')
pyautogui.rightClick(310, 736, duration = speed) 

#биндим загон на цифру 9
pyautogui.click(310, 736, duration = speed)
pyautogui.hotkey('ctrl', '9')

#выбираем главное здание и строим четвертого рабочего на поле
pyautogui.press('0')
pyautogui.press('z')

#устанавливаем точку сбору загона
pyautogui.press('9')
pyautogui.rightClick(362, 815, duration = speed) 

time.sleep(12.5)

#строим баррак
build.mycreate('4', (1307, 586), barracs)
build.get_create()

time.sleep(2)

#строим крестьянина на дерево
pyautogui.press('0')
pyautogui.press('z')
pyautogui.rightClick(1260, 351, duration = speed) 


