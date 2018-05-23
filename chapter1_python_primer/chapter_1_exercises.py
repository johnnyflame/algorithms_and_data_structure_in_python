



"""

"""


def is_multiple(n,m):
    """
    R-1.1

    Write a short Python function, is multiple(n, m),
    that takes two integer values and returns True if n is a multiple of m,
    that is, n = mi for some integer i, and False otherwise.

    :param n:
    :param m:
    :return:
    """
    return n % m == 0



def is_even(k):
    """
    R-1.2

    Write a short Python function, is even(k), that takes an integer value and returns
    True if k is even, and False otherwise. However, your function cannot use the multiplication,
    modulo, or division operators.

    :param k:
    :return:
    """
    return k % 2 == 0


def minmax(data):
    """
    R-1.3

    Write a short Python function, minmax(data),
    that takes a sequence of one or more numbers, and returns the smallest and largest numbers,
    in the form of a tuple of length two.
    Do not use the built-in functions min or max in implementing your solution.
    :param data:
    :return:
    """
    smallest = data[0]
    largest = data[0]

    for i in range(0,len(data)):
        if data[i] < smallest:
            smallest = data[i]
        elif data[i] > largest:
            largest = data[i]

    return(smallest,largest)

def sum_of_squares(n):
    """
    R-1.4

    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.
    :param n:
    :return:
    """
    sum = 0

    for i in range(0,n):
        sum += i*i

    return sum



def sum_of_squares_built_in(n):

    """

    R-1.5

    Give a single command that computes the sum from Exercise R-1.4,
    rely- ing on Python’s comprehension syntax and the built-in sum function.

    """


    return sum(i*i for i in n)


def sum_of_squared_odd_integers(n):
    """
    R-1.6

    Write a short Python function that takes a positive integer n and returns the sum
    of the squares of all the odd positive integers smaller than n.
    :param n:
    :return:
    """

    sum = 0

    for i in range(0,n):
        if not is_even(i):
            sum += i*i

    return sum


def sum_of_squared_odd_integer_built_int(n):
    """
    R-1.7

    Give a single command that computes the sum from Exercise R-1.6, rely- ing on Python’s comprehension syntax
    and the built-in sum function.
    :param n:
    :return:
    """
    return sum(i*i for i in n if not is_even(i))


"""
    R-1.8

    Python allows negative integers to be used as indices into a sequence, such as a          string. If string s has length n, and expression s[k] is used for in- dex −n ≤ k < 0,     what is the equivalent index j ≥ 0 such that s[j] references the same element?
"""

