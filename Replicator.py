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
def Replicator(key):                    # Тело скрипта
    past = values['TAG']                # Запись первого заменяемого тега
    way = ("C:/Replicator/damp.txt")    # Путь к файлу
    with open(way, 'r') as file:        # Чтение файла с тегами
        buff = file.read()          
    with open(way, "w") as file:        # Запись в файл с тегами
        file.writelines(past+'\n')      # Запись первого тега
        file.write(buff)                # Запись старого файла
    file = open(way, "r")               # Открытие файла
    
    pastc = values['TAGС']              # Запись первого заменяемого комментария
    way2 = ("C:/Replicator/damp2.txt")  # Путь к файлу
    with open(way2, 'r') as filec:      # Чтение файла с комментариями
        buff1 = filec.read()          
    with open(way2, "w") as filec:      # Запись файла с комментариями
        filec.writelines(pastc+'\n')    # Запись первого комментария
        filec.write(buff1)              # Запись старого файла
    filec = open(way2, "r")             # Открытие файла  
    j = 0       # Счетчик цикла
    
    while True:                     # Цикл строчек
        if j == 0:
            linePast = file.readline()  # Перекладка строчки с первым тегом из dump в переменную linePast
            linePastC = filec.readline()  # Перекладка строчки с комментарием из dump в переменную linePastC
        else:
            linePast = lineFuture  # Перекладка строчки с тегом из прошлого цикла 
            linePastC = lineFutureC  # Перекладка строчки с комментарием из прошлого цикла
        lineFuture = file.readline()  # Перекладка строчки новго тега из файла
        lineFutureC = filec.readline()  # Перекладка строчки c новым комментарием из файла
        if not lineFuture:        
            print('Обработанны все строки в файле damp, рапликатор остановлен')
            window['out'].update(f'Status: Обработанны все строчки, репликатор остановлен')
        if not lineFuture or not thread2.is_alive(): # Остановка цикла, если строчка окажется пустой или поток два окажется остановленным
            break
        j = j + 1
        mouse.position = (718, 167) # Выбор буфферного окна
        mouse.click(Button.left)    # Клик

        time.sleep(0.2)
        keyb.press(keyboard.Key.ctrl_l)      # Вызов окна атозамены Ctrl_H
        time.sleep(0.1)         #
        keyb.press('р')         #
        time.sleep(0.3)        #
        keyb.release(keyboard.Key.ctrl_l)    #
        time.sleep(0.1)         #
        keyb.release('р')       #
        time.sleep(0.1)     
        
        ###########################!!!!!!!!!!!ЗАМЕНА!!!!!!!!!!!!!!!!!!!########################
        mouse.position = (680, 372)     # Верхняя строка в окне замены
        mouse.click(Button.left,2)   # Правый клик 
        time.sleep(0.1)
 
            ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(linePast)    # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if linePast[i] == (' '):    # Замена пробелов на "_"
                keyflow = '_'
            else:
                keyflow = linePast[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
       
        mouse.position = (680, 402) # Нижнеяя строка в окне замены
        mouse.click(Button.left, 2)  # Двойной клик
        time.sleep(0.1)                 # Пауза
        
                    ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(lineFuture)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if lineFuture[i] == (' '):   # Замена пробелов на "_"
                keyflow = '_'
            else:
                keyflow = lineFuture[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # Счетчик cPantyukhin
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
        
        time.sleep(0.1)      # Пауза
        mouse.position = (895, 427) # Кнопка "заменить все" в окне замены
        mouse.click(Button.left)    # Клик
  
        mouse.position = (680, 372) # Верхняя строка в окне замены
        mouse.click(Button.left, 2)   # Правый клик 
        time.sleep(0.1)     # Пауза

            ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(linePastC)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if linePastC[i] == (' '):    # Замена пробелов на "_"
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
        time.sleep(0.1)     # Пауза
        
                    ######## ЗАПИСЬ СЛОВА ИЗ СТРОЧКИ ФАЙЛА ##########
        long = len(lineFutureC)        # Определение длинны строчки
        i = 0                   # Внутренний цикловый счетчик
        while i < long:         # Цикл символов
            if lineFutureC[i] == (' '):    # Замена пробелов на "_"
                keyflow = '_'
            else:
                keyflow = lineFutureC[i]       # Присваивание символа переменной key
            keyb.press(keyflow)     # Нажимаем key
            keyb.release(keyflow)   # Отпускаем key
            i = i + 1           # Счетчик cPantyukhin
            if keyflow == ('\n'):    # Проверка символа на равенство "ПРБЕЛУ"
                break           # Останавливаем запись слова, если текущий смвол"ПРОБЕЛ"
        
        time.sleep(0.1)         # Пауза
        mouse.position = (895, 427) # Кнопка "заменить все" в окне замены
        mouse.click(Button.left)    # Клик

        time.sleep(0.1)         # Пауза
        mouse.position = (926, 341) # Кнопка "закрыть" в окне замены
        mouse.click(Button.left)    # Клик
        
        time.sleep(0.2)         # Пауза
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

def Listener():         # Слушатель
    def stop(key):                                                                       # Условие для остановки второго потока
        if key == keyboard.Key.shift_r:                                                  # Когда слушатель услышат правый шифт
            print('Нажат RShift репликатор остановлен')                                  # Он напишет сообщение в консоль
            window['out'].update(f'Status: был нажат RShift, репликатор остановлен')     # обновит вывод статуса в интерфейса
            return False                                                                 # Вернет команду остановки слушателю
            thread2.join()                                                               # Рипнет второй поток
    with keyboard.Listener(on_press=stop) as listener:     # Инициализация слушателя
        listener.join()

thread1 = Thread(target=Replicator, args=('Y')) #Инициализация первого потока
thread2 = Thread(target=Listener, args=())      #Инициализация второго потока

while True: # Основной цикл
    event, values = window.read()   # Чтение интерфейса
    if values['simple'] == True:    # Данные из чекбоксов в однозначный вид
        values['double'] = False
    if values['double'] == True:
        values['simple'] = False
    if event is None or event == sg.WIN_CLOSED:  # Остановка
        break
    if event == '!!GO!!':   # Событие нажатия кнопки
        thread1.start()     # Запуск первого потока
        thread2.start()     # Запуск второго потока
        window['out'].update(f'Status: Репликатор запущен')     # Обновление выхода 
        window['!!GO!!'].update(f'CLOSE')                       # Обновить кнопку запуска в кнопку закрытия
