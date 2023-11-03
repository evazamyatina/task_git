from math import sqrt
from random import randint
from typing import Tuple
def quadratic_equation(a: int, b: int, c:int):
    disc=b**2-4*a*c
    sq=sqrt(disc)
    fst_x= -b - sq/(2*a)
    snd_x=-b + sq/(2*a)
    return fst_x, snd_x
def rnd(start: int = -10, end: int = 10) ->int:
    return randint(start, end)
equations = [(rnd(), rnd(), rnd()) for _ in range(10)]
if __name__ =='__main__':
    for values in equations:
        print('Values\t a: {0} b: {1} c: {2}'.format(*values))
        print('Answers\tx1: {0} x2: {1} x3 {2}'.format(*quadratic_equation(*values)))