#un comentario

def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firtname": "facundo", "lastname": "garcía"}

    super_list = [
        {"firstname":"facundo", "lastname": "garcía"},
        {"firstname":"miguel", "lastname": "torres"},
        {"firstname":"pepe", "lastname": "rodelo"},
        {"firstname":"susana", "lastname": "martinez"},
        {"firstname":"josé", "lastname": "garcía"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }    

    for key, value in super_dict.items():
        print(key, "-",value)

    for i in super_list:
        print(i["firstname"] , "-", i["lastname"])


if __name__ == "__main__":
    run()

    