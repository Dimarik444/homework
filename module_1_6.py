my_dict = {"Denis": 2001 ,"Alex": 2004, "Vlad": 2021, "Dima": 2017, "Vova": 1991}
print(my_dict)
print(my_dict["Vlad"])
print(my_dict.get("Victor", "Нет такого"))
my_dict.update({"Anton": 1978,
                "Vasya": 1985})
print(my_dict)
a = my_dict.pop("Alex")
print(a)
print(my_dict)

my_set = {1, 2, 3, 4, 1, 4, 3 ,5, "Вадим", "Андрей", "Питон", "Вадим"}
print(my_set)
my_set.update({10, "Виктор"})
my_set.discard(4)
print(my_set)