# simple calculator represented using regular expressions
import re


class Calculator:
    """Class to represent the calculator using regular expression"""
    def __init__(self, math_operation):
        """Init method"""
        self.math_operation = math_operation

        # this is the desired pattern we're looking for:
        # first number: must have at least 1 digit; it can be negative or not and also can have any number of decimals
        # operation sign: must be one of +, -, /, *, //, **, %
        # second number: must have at least 1 digit; it can be negative or not and also can have any number of decimals
        self.pattern = r'^([-])?(\d+)(\.\d+)?([+\-%])?([/]{1,2})?([\*]{1,2})?([-])?(\d+)(\.\d+)?$'

        # checking if our pattern matches the user's input
        self.data = re.match(self.pattern, self.math_operation)

    def check_match(self):
        """Method to check if the pattern matches the input"""
        if self.data:
            # if the pattern matches the input, the input is split in groups of characters and a list is created
            self.data = self.data.groups()
            return self.data
        else:
            return False

    def check_first_number(self):
        """Method to validate the first number"""
        self.data = Calculator.check_match(self)
        if self.data is False:
            return False
        else:
            if len(self.data) < 8:
                return False
            else:
                # validating the first number by checking its assigned groups from the list
                if self.data[0] is None and self.data[2] is None:
                    first_number = int(self.data[1])
                elif self.data[0] is None and self.data[2] is not None:
                    first_number = float(self.data[1] + self.data[2])
                elif self.data[0] is not None and self.data[2] is None:
                    first_number = -int(self.data[1])
                else:
                    first_number = -float(self.data[1] + self.data[2])
                return first_number, self.data

    def check_operation_sign(self):
        """Method to validate the operation sign"""
        data = Calculator.check_first_number(self)
        if data:
            first_number = data[0]
            self.data = data[1]

            # validating the operation sign by checking its assigned groups from the list
            if self.data[3] is None and self.data[4] is None:
                operation = self.data[5]
            elif self.data[3] is None and self.data[5] is None:
                operation = self.data[4]
            else:
                operation = self.data[3]
            return first_number, operation, self.data
        else:
            return False

    def check_second_number(self):
        """Method to validate the second number"""
        data = Calculator.check_operation_sign(self)
        if data:
            first_number = data[0]
            operation = data[1]
            self.data = data[2]

            # validating the second number by checking its assigned groups from the list
            if self.data[6] is None and self.data[8] is None:
                second_number = int(self.data[7])
            elif self.data[6] is None and self.data[8] is not None:
                second_number = float(self.data[7] + self.data[8])
            elif self.data[6] is not None and self.data[8] is None:
                second_number = -int(self.data[7])
            else:
                second_number = -float(self.data[7] + self.data[8])
            return first_number, operation, second_number
        else:
            return False

    def calculate_math_operation(self):
        data = Calculator.check_second_number(self)
        if data:
            # calculating the result if the first number, operation sign and second number are valid
            first_number = data[0]
            operation = data[1]
            second_number = data[2]
            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '/':
                result = first_number / second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '//':
                result = first_number // second_number
            elif operation == '**':
                result = first_number ** second_number
            else:
                result = first_number % second_number
            message = f'The result is {result}'
            return message
        else:
            message = 'Invalid format!'
            return message


user_math_operation = input('Supported math operations are-> +, -, /, *, //, **, % ;please type the math operation -> ')
if __name__ == '__main__':
    calculator = Calculator(user_math_operation)
    print(calculator.calculate_math_operation())
