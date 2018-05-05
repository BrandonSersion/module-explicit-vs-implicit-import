def test_function():
    print('got test_function')

class TestClass:
    def test_class_function(self):
        print('got test_class_function')


# This module can be executed as a package.
def main():
    test_function()
    test_class_instance = TestClass()
    test_class_instance.test_class_function()

if __name__=="__main__":
    main()