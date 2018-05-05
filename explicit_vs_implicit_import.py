# two identical modules

# implicit import
import module1
# explicit import
from module2 import test_function, TestClass

# module1
def run_module_function():
    module1.test_function()
        
def run_module_class_function():
    example = module1.TestClass()
    example.test_class_function()

# module2
def run_module2_function():
    test_function()

def run_module2_class_function():
    example = TestClass()
    example.test_class_function()


def main():
    print('module1 - implicit import')
    run_module_function()
    run_module_class_function()
    print()
    print('module2 - explicit import')
    run_module2_function()
    run_module2_class_function()

if __name__ == '__main__':
    main()