"""
Write two functions to find the minimum number in a list.
First function: O(n)
Second function: O(n**2)
"""


def search_minimum1(list1):
    """
    Complexity O(n)
    """
    temp = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < temp:
            temp = list1[i]
    return temp


def search_minimum2(list2: list):
    """
    Complexity O(n**2)
    """
    for i in range(len(list2)):
        temp = list2[i]
        for j in range(1, len(list2)):
            if temp > list2[j]:
                temp = list2[j]
        return temp


lista = [10, 30, 20, 5, 15, 3, 1, 0.2, 0.05]
print(search_minimum2(lista))
print(search_minimum1(lista))