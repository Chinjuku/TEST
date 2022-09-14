"""CompositeFunction"""
def func_f(mathx):
    """ function_f"""
    return mathx*2

def func_g(mathx):
    """ function_g"""
    return mathx/2+1

def main():
    """CompositeFunction"""
    mathx = float(input())
    print("%0.2f" %(func_f(func_g(mathx))))
    print("%0.2f" %(func_g(func_f(mathx))))
main()
