
def sum_two(a: int, b: int)->int:
    def func2(c: int, d: int)->int:
        return c+d
    return func2(a,b)
print(sum_two(1, 2))
string= 'слово слово'
print(string.capitalize())