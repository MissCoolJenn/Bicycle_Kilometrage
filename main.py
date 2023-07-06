from datetime import datetime, timedelta
import time
import json

def open_file():  # открыть файл, и вернуть словарь 
    try:
        file = open('history.txt', 'r')
        file_readed = file.read()
        main_hash = eval(file_readed)
        return main_hash
    except:
        file = open('history.txt', 'w')
        www = {'01.01': 00}
        file.write(json.dumps(www))
        file.close()
        return(open_file())

def save_file(main_hash):
    file = open('history.txt', 'w')
    file.write(json.dumps(main_hash))
    file.close()

def last_value(main_hash, first = None, second = None):  # возвращает из словаря последние дата/значение (по желанию можно выбрать что то одно или и то и то)
    key, value = main_hash.popitem()  # получить значения
    main_hash[key] = value            # и вернуть их обратно в словарь

    if first != None and second != None:
        return key, value
    elif first != None:
        return key
    elif second != None:
        return value
    
def kilometers_sum(main_hash):
    time.sleep(0.5)
    value_list = list(main_hash.values())

    sum_all = 0
    for i in value_list:
        time.sleep(0.03)
        try:
            s = int(i)
            if int(s):
                print(sum_all) # остановился тут
                sum_all += s
        except:
            pass
    return sum_all
    
def writing_data(main_hash):
    time.sleep(0.5)

    # получение даты с коротой будет начата запись
    print(f'**********\nLast date was: {last_value(main_hash, "key")}\ni think you need to know this\n')
    date_str_to_write = input('Print begin date like "24.01"\n')

    # перевод даты из str в формат datetime
    try:
        date_to_write = datetime.strptime(date_str_to_write, '%d.%m')
    except:
        time.sleep(1)
        print('... error\n')
        time.sleep(0.5)
        return
    
    tomorrow = datetime.today() + timedelta(days=1)
    key = date_to_write.strftime("%d:%m")
    
    # цикл записи значений в дату (дата каждый раз изменяется на +1 день)
    while True: 
        time.sleep(0.5)

        if date_to_write < tomorrow: #  and date_str_to_write > last_value(main_hash, 'first')
            # получение значения сколько км пройдено за день
            print(f'/______/\n... Day:{key[:2]}, Month:{key[3:]}')
            print('(press Enter to skip this day or "stop" to stop)')
            value = input('Print how many kilometers is was:\n')
        
            # проверка значния, это 'int' или '' или 'stop' или всё остальное
            try:
                if int(value):
                    pass
            except:
                if value == '':
                    pass
                if value == 'stop':
                    break
                else:
                    print('\nit is not a fucking int')
                    continue
            
            # сохранение значения даты и значение в словарь
            main_hash[key] = value
            print(main_hash)

            # замена текущей даты в ключе на дату следующую
            key_date = datetime.strptime(key, '%d:%m')
            key = key_date + timedelta(days=1)
            key = key.strftime("%d:%m")

            # вызов функции сохранения словаря в файл
            save_file(main_hash)

        elif date_to_write >= tomorrow:
            print('\nTo late for that')
            time.sleep(1)
            break

        else:
            print('\nNow its good time to stop')
            time.sleep(1)
            break

def loop(main_hash):
    help_me = lambda: print('**********\n"start" - начало записи данных километража начиная с последнего дня и до сейчас\n"last" - дата последнего дня записи\n"all" - total amount km')
    
    while True:
        help_me()
        q = input()

        if q == 'last':       # последняя дата и значение из хєша
            time.sleep(0.5)
            print(f'**********\nDay {last_value(main_hash, "key")[:2]}, Month {last_value(main_hash, "key")[3:]}')
            time.sleep(0.5)
        
        elif q == 'start':    # начало записи
            writing_data(main_hash)
                
        elif q == 'all':     # подсчет общего количества км
            print(f'Всего было пройдено {kilometers_sum(main_hash)} km')

        elif q == 'test':     # запуск части кода для теста
            pass

if __name__ == '__main__':
    loop(open_file())