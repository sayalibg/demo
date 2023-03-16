# print("hi")

# print(__name__)   # __main__

def func():
    print("inside function")

# # define main method:

# if __name__ == "__main__":
#     func()

def main():
    print("hi")

    print(__name__)
    func()

def outer_func():
    print("inside outer function")

if __name__ == "__main__":
    main()







