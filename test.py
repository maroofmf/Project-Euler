import multiprocessing
import time

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

def mp_worker((inputs, the_time)):
    # print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
    if the_time == '3':
        return('cant')
    time.sleep(int(the_time))
    return('adfa')
    # print " Process %s\tDONE" % inputs


def mp_handler():
    p = multiprocessing.Pool(8)
    a = (p.map_async(mp_worker, data))
    print(a)

if __name__ == '__main__':
    mp_handler()