
def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    
     num = input("ingresa un número:")
     assert num.isnumeric(), "debes ingresar un número"
     print(divisors(int(num)))
     print("terminó mi programa")
    





if __name__ == "__main__":
    run()