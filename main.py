import threading
from timerit import Timerit
import math
import time


class Thread(threading.Thread):
    def __init__(self, parts, step, items):
        self.items = items
        self.size = len(items)
        self.parts = parts
        self.step = step
        self.begin = int(((self.size/self.parts)*(self.step-1)))
        self.end = int((self.size/self.parts)*self.step)
        super(Thread, self).__init__()

    def run(self):
        for t in range(self.begin, self.end):
            # item = self.items[t]
            # Cálculo para simular situalção de processamento de dados
            # result = math.sqrt(item)
            # Delay para simular situação de resposta de requisicao
            time.sleep(1)
            # print("Running: {}, Thread: {}, Result: {}".format(self.items[t], self.step, math.sqrt(cont)))


def main():
    items = range(200)
    parts = 20
    thread_list = []
    for i in range(1, parts+1):
        thread = Thread(parts, i, items)
        thread_list.append(thread)
        thread.start()
        # print('Start thread: {}'.format(i))
    for th in thread_list:
        th.join()


if __name__ == "__main__":
    for _ in Timerit(num=1, verbose=2):
        print("=============================================================================================")
        print("||=======================.Script para processo paralelizado em lote.=======================||")
        print("=============================================================================================")
        main()
