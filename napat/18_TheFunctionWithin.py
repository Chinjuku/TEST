"""TheFunctionWithin"""
def func_f(math_a):
    """function_f"""
    return math_a*2

def func_g(math_a):
    """function_g"""
    ans = 3*(math_a**4) - math_a**3 + 2*(math_a**2) + 10
    return ans

def func_h(math_a, math_b, math_c):
    """function_h"""
    ans = (math_c + math_a)**2 - (math_a*math_b) + math_b**2
    return ans

def func_i(math_a, math_b, math_c, math_d):
    """function_h"""
    ans = (math_a**2 + math_b**2 - math_c**2)/(math_d**2 - 2*(math_a*math_d) + math_a*2)
    return ans

def main():
    """main"""
    math_a = float(input())
    math_b = float(input())
    math_c = float(input())
    math_d = float(input())
    print((func_f(func_f(math_a))))
    print(func_g(func_f(math_a - math_b)))
    print(func_h(func_f(math_a + math_b), func_f(math_a + math_c), func_g(func_f(math_d**2))))
    print(func_i(func_h(func_f(math_a + math_b), func_f(math_a - math_c),\
        func_g(func_f(math_d**2))), func_g(func_f(math_a - math_b)),\
        func_f(func_f(func_f(func_f(func_f(math_c))))), math_d**8))
main()
