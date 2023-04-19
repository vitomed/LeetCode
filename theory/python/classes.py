class A:
    print("cls A")

    def __call__(self):
        print("call cls A")


if __name__ == '__main__':
    A()()
