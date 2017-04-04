from __future__ import  print_function


def fibs():
    a = 0
    b = 1
    while 1:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    f = fibs()
    for x in xrange(100):
        print(f.next())
