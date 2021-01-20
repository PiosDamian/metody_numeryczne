# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sqrt(a, e=0.01):
    result = 1.0
    if a != 0:
        while abs(result ** 2 - a) > e:
            result = 0.5 * (result + a / result)
    return result;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sqrt(25, 0.1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
