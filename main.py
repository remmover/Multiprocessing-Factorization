from time import time
from multiprocessing import Pool, cpu_count


def factorize(*number):
    # timer = time()
    result = []
    for num in number:
        fact = []
        for i in range(1, num + 1):
            if num % i == 0:
                fact.append(i)
        result.append(fact)
    # result.append(time() - timer)
    print(result)
    # raise NotImplementedError()  # Remove after implementation

    # Time - 0.3799419403076172
    # Time - 0.535747766494751

# def callback(result):
#     print(f"Result in callback: {result}")


if __name__ == '__main__':
    timer = time()
    with Pool(cpu_count()) as pool:
        r = pool.map(factorize, [128, 255, 99999, 10651060])
        print(r, f'timer - {time() - timer}')

    # print(factorize(128, 255, 99999, 10651060), f'timer - {time() - timer}')
    # a, b, c, d = factorize(128, 255, 99999, 10651060)
    #
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    #              1521580, 2130212, 2662765, 5325530, 10651060]
