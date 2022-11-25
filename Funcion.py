#Función que permite sumar numeros
def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(1, 101))
    return sum(numbers)