import random

import numpy as np
import matplotlib.pyplot as plt

time = 100000
#tao = 2
#p = 0.7

#p_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
tao_list = []
tao_list_sec = []
def with_return(tao, p):
    reciever = []               #модель получателя
    bool = False                #Было ли удаление
    k = 1
    tao_list.append(tao)
    for i in range(1, time):
        if bool == True:        #Если было удаление то чтобы получить сообщение нужно время пропускаем единицу времени
            tao = int(np.ceil(np.random.exponential(8)))
            tao_list.append(tao)
            bool = False
            continue
        reciever.append(len(reciever) + 1)    #Получение сообщения
        if k >= tao:
            if np.random.random() < p and reciever:
                k = 0
                bool = True
                for j in range(tao):
                    reciever.pop()              #удаление tao сообщений

        k += 1
    koef = len(reciever) / time
    return koef


def high_p_of_err(tao, p):
    reciever = []
    k = 0
    bool = False
    f = tao
    num = 1
    for i in range(1, time):

        if bool == True:  # Если было удаление то чтобы получить сообщение нужно время пропускаем единицу времени
            bool = False
            continue

        if k >= tao:
            if np.random.random() > p and reciever:
                k = 0
                bool = True
                num += 1
                for j in range(f - 1):
                    reciever.pop()  # удаление tao сообщений
                tao = int(np.ceil(np.random.exponential(8)))
                tao_list.append(tao)
                f = tao
            else:
                if reciever:
                    f += 1
        reciever.append(num)
        k += 1

    koef = len(reciever) / time
    return koef


def teoretical_with_return(tao, p):
    koef = (1 - p) / (1 + p * tao)
    return koef

def teoretical_high_p_of_err(tao,p):
    koef = (1 - p) / (1 + (1 - p) * tao)
    return  koef

wr = []
twr = []
h = []
th = []
p_list = []
for p in np.arange(0, 0.9, 0.1):
    p_list.append(p)
    tao = 5                     #int(np.ceil(np.random.exponential(5)))
    #print(tao)
    #print(f"exp {with_return(tao, p)}")
    #print(f"teo {teoretical_with_return(tao, p)}")
    wr.append(with_return(tao, p))
    twr.append(teoretical_with_return(np.mean(tao_list), p))
    h.append(high_p_of_err(tao, p))
    th.append(teoretical_high_p_of_err(np.mean(tao_list), p))   #np.mean(tao_list)

print(tao_list[:10])
plt.figure(figsize=(8,6))

plt.plot(p_list, wr, ms=5, label='коэф использования с возвратом')
plt.plot(p_list, twr, ms=5, linestyle='--', label='коэф использования с возвратом(теор)')
plt.plot(p_list, h, ms=5, label='коэф использования с выс вер ошибки')
plt.plot(p_list, th, ms=5, linestyle='--', label='коэф использования с выс вер ошибки(теор)')

plt.xlabel("Вероятность ошибки")
plt.ylabel("Коэффициент использования канала")
plt.ylim(0, 1)  # Диапазон значений по оси Y от 0 до 1
#plt.title("average waiting time")

# Добавление легенды и сетки
plt.legend()
plt.grid(True)
plt.show()