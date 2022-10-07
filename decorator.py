from datetime import datetime

def timeit(input_func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = input_func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

# Синтаксический сахар
#l1 = timeit(get_list_of_even_numbers)(100)
@timeit
def get_list_of_even_numbers(num):
    l = [x for x in range(num) if x % 2 == 0]
    return l

get_list_of_even_numbers(num=1000001)



# def timeit(arg):
#     """
#     ToDo: Прочитать про замыкание
#     """
#     def outer(input_func):
#         def wrapper(*args, **kwargs):
#             start = datetime.now()
#             result = input_func(*args, **kwargs)
#             print(arg, datetime.now() - start)
#             return result
#         return wrapper
#     return outer
#
# @timeit('list_of_even_numbers')
# def get_list_of_even_numbers(num):
#     l = [x for x in range(num) if x % 2 == 0]
#     return l
#
#
# #get_list_of_even_numbers(150000)
# # Синтаксический сахар
# l1 = timeit("list_of_even_numbers")(get_list_of_even_numbers)(100)
