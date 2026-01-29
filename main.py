"""
Мне просто вздумалось написать эту программу и я не знаю зачем
"""
def gen1(a=0,b=9):
    arr=[]
    for number in range(a,b+1):
        arr.append(str(number))
    return arr

def gen(a=0,b=9,l=3,arr=None):
    """
    this function generates by using recursion numbers.
    generation start from @parameter a
    and
    generation ends until @parameter b
    and
    this generation has length defined by @parameter l
    UPD: I certainly don't recommend to change @parameter arr
    """
    if l<=0:
        return []

    if arr is None:
        arr=[gen1(a,b)]
        gen(a,b,l-1,arr)
        return arr

    new_arr=[]

    for i in arr[-1]:
        for number in range(a,b+1):
            new_arr.append(i+str(number))

    arr.append(new_arr)

    gen(a,b,l-1,arr)

    return arr


def print_gen(gen_result):
    """
    default print
    """
    # цикл по разрядам
    for r in gen_result:
        # цикл по числам внутри разрядов
        for num in r:
            print(num)

def print_sorted(gen_result):
    if not gen_result:
        return
    digits=len(gen_result[0])
    new_arr=[]
    for arr_numbers in gen_result:
        del_counter=len(arr_numbers)
        counter=0
        for number in arr_numbers:
            print(number)
            counter+=1
            if del_counter/digits == counter:
                new_arr.append(arr_numbers[counter:])
                break
    print_sorted(new_arr)


def introduction():
    print("Hi! This program generates numbers from a to b and with certain len of numbers(called l).")
    print("Now let's start")

def ask_for_help_menu():
    print("\nCommands list:\n"
          "help - shows this text\n"
          "write - to set your own value for parameters (a,b,l)\n"
          "default - to use default values for parameters (a=0, b=9, l=3)\n"
          "off - to turn off program\n")

def ask_for_help_print():
    print("\nCommands list:\n"
          "exit - to level up on program\n"
          "off - to turn off program\n"
          "sorted - sorted print or just type 1\n"
          "unsorted - unsorted print or just type 0\n")

if __name__=="__main__":
    introduction()
    while True:
        gen_res=[]

        print("If you wanna get more info about commands on every stage of the program than just type command: help")
        prompt=input("Type word: ").strip().lower()
        if prompt=="write":
            start=int(input("Type a: "))
            end=int(input("Type b: "))
            length=int(input("Type l: "))
            gen_res=gen(a=start,b=end,l=length)
        elif prompt=="default" or prompt=="":
            gen_res=gen()
        elif prompt=="off":
            exit("Bye! Have a good time!")
        elif prompt=="help":
            ask_for_help_menu()
            continue
        else:
            print("Oops there is a mistake! Please try again!\n")
            continue

        while True:
            status_print=input("\nType command for print's mode: ").strip().lower()
            if status_print == "1" or status_print == "sorted":
                print_sorted(gen_res)
            elif status_print == "0" or status_print == "unsorted":
                print_gen(gen_res)
            elif status_print=="help":
                ask_for_help_print()
                continue
            elif status_print=="exit":
                print()
                break
            elif status_print=="off":
                exit("Bye bye! Have a nice day!")
            else:
                print("Oops there is a mistake. Please try again!")
