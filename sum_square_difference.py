def list_natural_numbers(value):
    """Lists all natural numbers less than or equal to 100 """

    number_list = []

    for val in range(value):
        number_list.append(val)
    return number_list


def sum_square_difference(func, value):
    """
    Calculates the difference between the sum of the squares of the 
    first one hundred natural numbers and the square of the sum.
    """

    number_list = func(value)
    square_of_sum_number_list = sum(number_list) ** 2
    sum_of_squares_number_list = sum(list(map(lambda x: x ** 2 , number_list)))
    
    sum_difference = square_of_sum_number_list - sum_of_squares_number_list
    return sum_difference

if __name__ == "__main__":
    print(sum_square_difference(list_natural_numbers,101))