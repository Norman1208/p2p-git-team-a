from math_function import add, exp


def main():
    operator = input("masukkan operator :")
    data_1 = int(input("masukkan input 1 :"))
    if operator == "**":
        pass
    else:
        data_2 = int(input("masukkan input 2 :"))
    

    if operator == "+":
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
    
    if operator == "**":
        result = exp(data_1)
        print("exp({})  = {} ".format(data_1, result))

if __name__ == "__main__":
    print("Hello Main !")
    main()