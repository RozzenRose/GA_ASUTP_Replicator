print('Перед запуском рекомендуется прочесть инструкцию\nрепликатор будет невозможно остановить\nпока он не обработает весь damp\n\nby Пантюхин В.А. отдел АСУТП \n\n')

from pynput import keyboard, mouse          # Библиотеки для управления клавиатуры и мышки
from pynput.mouse import Controller, Button # Подтягивание контроллеров клавиатуры и мышки
import time                                 # Подтягивание библиотеки для переменных управления временем
from threading import Thread                # Библиотека для исползования нескольких потоков
import PySimpleGUI as sg                    # Библиотека для интерфейса

STOP = False
keyb = keyboard.Controller()    # Присвоение контроллера клавиатуры
mouse = mouse.Controller()      # Присвоение контроллера мыши
ctrl_l = keyboard.Key.ctrl_l    # Присвоение клавиши LCtrl в более удобную переменную

sg.theme('Default')             # Тема интерфейса
layout = [                      # Интерфейс
    [sg.Text('Перед началом работы рекомендуется прочесть инструкцию!')],
    [sg.Text('Для немедленной остановки репликатора нажмите RShift')],
    [sg.Text('Строчка для замены тега'), sg.Input(default_text='Введите заменяемый тег', key='TAG')],
    [sg.Text('Строчка для замены комментария'), sg.Input(default_text='Введите заменяемый комментарий', key='TAGС')], 
    [sg.Checkbox('Реплицировать в один столбец', key='simple', default=False), sg.Checkbox('Реплицировать в два столбца', key='double', default=True)], # Чекбоксы, галочки
    [sg.Text('Status: ready', key='out')],      #Вывод статуса
    [sg.Button('!!GO!!')]                       #Кнопка
]
window = sg.Window('Replicator', layout, icon=r'C:/Users/rozze/OneDrive/Рабочий стол/Feels/Replicator.ico') #Вызов ярлыка
def Replicator(key):                    #Тело 
    past = values['TAG']
    way = ("C:/Replicator/damp.txt")    # Путь к файлу
    with open(way, 'r') as file:
        buff = file.read()
    with open(way, "w") as file:              # Открытие файла
        file.writelines(past+'\n')
        file.write(buff)
    file = open(way, "r")            # Открытие файла
    
    pastc = values['TAGС']
    way2 = ("C:/Replicator/damp2.txt")    # Путь к файлу
    with open(way2, 'r') as filec:
        buff1 = filec.read()
    with open(way2, "w") as filec:              # Открытие файла
        filec.writelines(pastc+'\n')
        filec.write(buff1)
    filec = open(way2, "r")            # Открытие файла  
    j = 0
    
    while True:                     # Цикл строчек
        if j == 0:
            linePast = file.readline()  # Перекладка строчки из dump в переменную line
            linePastC = filec.readline()  # Перекладка строчки из dump в переменную line
        else:
            linePast = lineFuture  # Перекладка строчки из dump в переменную line
            linePastC = lineFutureC  # Перекладка строчки из dump в переменную line
        lineFuture = file.readline()  # Перекладка строчки из dump в переменную line
        lineFutureC = filec.readline()  # Перекладка строчки из dump в переменную line
        if not lineFuture:
            print('Обработанны все строки в файле damp, рапликатор остановлен')
            window['out'].update(f'Status: Обработанны все строчки, репликатор остановлен')
        if not lineFuture or not thread2.is_alive(): # Остановка цикла, если строчка окажется пустой
            break
        j = j + 1
        mouse.position = (718, 167) # Выбор буфферного окна
        mouse.click(Button.left)    # Клик

        time.sleep(0.2)
        keyb.press(keyboard.Key.ctrl_l)      #
        time.sleep(0.1)         #
        keyb.press('р')         #
        time.sleep(0.3)        #
        keyb.release(keyboard.Key.ctrl_l)    #
        time.sleep(0.1)         #
        keyb.release('р')       #
        time.sleep(0.1)     
        
        ###########################!!!!!!!!!!!ЗАМЕНА!!!!!!!!!!!!!!!!!!!########################
        mouse.position = (680, 372) # Верхняя строка в окне замены
        mouse.click(Button.left,2)   # Правый клик 
        time.sleep(0.1)
 
            ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(linePast)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if linePast[i] == (' '):
                keyflow = '_'
            else:
                keyflow = linePast[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # 
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
       
        mouse.position = (680, 402) # Нижнеяя строка в окне замены
        mouse.click(Button.left, 2)  # Двойной клик
        time.sleep(0.1) 
        
                    ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(lineFuture)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if lineFuture[i] == (' '):
                keyflow = '_'
            else:
                keyflow = lineFuture[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # Счетчик cPantyukhin
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
        
        time.sleep(0.1)
        mouse.position = (895, 427) # Кнопка "заменить все" в окне замены
        mouse.click(Button.left)    # Клик
  
        mouse.position = (680, 372) # Верхняя строка в окне замены
        mouse.click(Button.left, 2)   # Правый клик 
        time.sleep(0.1) 

            ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(linePastC)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if linePastC[i] == (' '):
                keyflow = '_'
            else:
                keyflow = linePastC[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # Счетчик cPantyukhin
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
       
        mouse.position = (680, 402) # Нижнеяя строка в окне замены
        mouse.click(Button.left, 2)  # Двойной клик
        time.sleep(0.1) 
        
                    ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(lineFutureC)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if lineFutureC[i] == (' '):
                keyflow = '_'
            else:
                keyflow = lineFutureC[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # Счетчик cPantyukhin
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
        
        time.sleep(0.1)
        mouse.position = (895, 427) # Кнопка "заменить все" в окне замены
        mouse.click(Button.left)    # Клик

        time.sleep(0.1)
        mouse.position = (926, 341) # Кнопка "закрыть" в окне замены
        mouse.click(Button.left)    # Клик
        
        time.sleep(0.2)
        keyb.press(keyboard.Key.ctrl_l)   #
        time.sleep(0.1)      #
        keyb.press('ф')      #
        time.sleep(0.1)      # Ctrl+A
        keyb.release(keyboard.Key.ctrl_l) #
        time.sleep(0.1)      #
        keyb.release('ф')    #

        keyb.press(keyboard.Key.ctrl_l)   # 
        time.sleep(0.1)      #
        keyb.press('с')      #
        time.sleep(0.1)      # Ctrl+C
        keyb.release(keyboard.Key.ctrl_l) #
        time.sleep(0.1)      #
        keyb.release('с')    #

        mouse.position = (620, 166) # Переключение в основную подпрограмму
        mouse.click(Button.left)    # Клик
        if values['double']:
            if j % 2 == 0:
                keyb.press(keyboard.Key.ctrl_l)   # 
                time.sleep(0.1)      #
                keyb.press('м')      #
                time.sleep(0.1)      # Ctrl+V
                keyb.release(keyboard.Key.ctrl_l) #
                time.sleep(0.1)      #
                keyb.release('м')    #
            else:
                mouse.position = (842, 218)
                mouse.click(Button.right)    # Клик
                time.sleep(0.2)
                mouse.position = (913, 352)
                mouse.click(Button.left)    # Клик
                time.sleep(0.2)            
        if values['simple']:
            keyb.press(keyboard.Key.ctrl_l)   # 
            time.sleep(0.1)      #
            keyb.press('м')      #
            time.sleep(0.1)      # Ctrl+V
            keyb.release(keyboard.Key.ctrl_l) #
            time.sleep(0.1)      #
            keyb.release('м')    #

    file.close()    # Закрытие файла
    filec.close()    # Закрытие файла

def Listener():
    def stop(key):
        if key == keyboard.Key.shift_r:
            print('Нажат RShift репликатор остановлен')
            window['out'].update(f'Status: был нажат RShift, репликатор остановлен')
            return False
            thread2.join()
    with keyboard.Listener(on_press=stop) as listener:     # Инициализация чтения клавиатуры
        listener.join()

thread1 = Thread(target=Replicator, args=('Y'))
thread2 = Thread(target=Listener, args=())

while True:
    event, values = window.read()
    if values['simple'] == True:
        values['double'] = False
    if values['double'] == True:
        values['simple'] = False
    if event is None or event == sg.WIN_CLOSED:
        break
    if event == '!!GO!!':
        thread1.start()
        thread2.start()
        window['out'].update(f'Status: Репликатор запущен')
        window['!!GO!!'].update(f'CLOSE')
