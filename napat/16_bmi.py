"""bmi"""
def main():
    """bmi"""
    name_1 = input()
    weight_1 = float(input())
    high_1 = float(input())
    bmi_1 = weight_1/(high_1/100)**2
    name_2 = input()
    weight_2 = float(input())
    high_2 = float(input())
    bmi_2 = weight_2/(high_2/100)**2
    name_3 = input()
    weight_3 = float(input())
    high_3 = float(input())
    bmi_3 = weight_3/(high_3/100)**2
    name_4 = input()
    weight_4 = float(input())
    high_4 = float(input())
    bmi_4 = weight_4/(high_4/100)**2
    name_5 = input()
    weight_5 = float(input())
    high_5 = float(input())
    bmi_5 = weight_5/(high_5/100)**2
    print(name_1+"'s", " "+"BMI = %0.2f" %bmi_1)
    print(name_2+"'s", " "+"BMI = %0.2f" %bmi_2)
    print(name_3+"'s", " "+"BMI = %0.2f" %bmi_3)
    print(name_4+"'s", " "+"BMI = %0.2f" %bmi_4)
    print(name_5+"'s", " "+"BMI = %0.2f" %bmi_5)
main()
