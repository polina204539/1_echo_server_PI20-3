import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    name = input ('Пожалуйста, введите личный ник (1<длина<10): ')
    if 1<len(name)<10:
        break

host = 'localhost'
port = 9093

client.connect((host, port))
print ('установлено подключение к серверу')
print ('введите "exit", чтобы закрыть соединение с сервером')

def vvod():
    while True:
        outdata = input('')
        print()
        if outdata=='exit' or outdata=='Exit':
            break
                  # Отправить на сервер
        client.send(f'{name}: {outdata}'.encode('utf-8'))
        print('%s:%s'% (name, outdata))


def priem():
    while True:
        try:
            indata = client.recv(1024)
            print(indata.decode('utf-8')) #Закодировать полученную информацию
        except:
            print('--Отключение--')
            break


 #Создание многопоточности
t1 = threading.Thread(target=priem, name='input')#Установить получение информации, объект потока
t2 = threading.Thread(target=vvod, name='out') #Создание выходной информации, объект потока

 #Начать многопоточность
t1.start()
t2.start()

t2.join()

 #Закрыть соединение
print ('Сервер отключен')
client.close()
