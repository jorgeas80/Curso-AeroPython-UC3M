# Tu codigo aqui

import multiprocessing

def worker(num):
    return num*2

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    p = multiprocessing.Pool(2)
    values = p.map(worker,nums)

    p.close()
    p.join()

    print(values)
