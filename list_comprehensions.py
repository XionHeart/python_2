
def run():
    # new_list= []

    # for i in range(1, 99999):
    #     if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:   
    #         new_list.append(i)
    # print(new_list)

    new_list = [i for i in range(1, 9999) if i % 4 == 0
                    and i % 6 == 0 and i % 9 == 0] 
    print(new_list)


if __name__== "__main__":
    run()