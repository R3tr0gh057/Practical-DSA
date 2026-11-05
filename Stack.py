# Initializing class for encapsulation of stack operations, also allows for the creation of multiple stack objects if required
class Stack:
    def __init__(self, size):
        self.size = size  # size of the stack
        self.items = []   # list to store stack items

    # Push operation to add an item to the top of the stack
    def push(self, item):
        if len(self.items) == self.size:
            return False
        else:
            self.items.append(item)
            return True

    # Pop operation to remove an item from the top of the stack
    def pop(self):
        if not self.items:
            print("Stack is empty.")
        else:
            return self.items.pop()

    # Peek operation to return the top item of the stack without popping it
    def peek(self):
        if not self.items:
            print("Stack is empty.")
        else:
            return self.items[-1]

    # Display operation to print the entire stack
    def display(self):
        if self.isempty():
            return "Empty Stack."
        else:
            for item in reversed(self.items):
                print(item)

    # isfull operation to check if the stack is full
    def isfull(self):
        return len(self.items) == self.size

    # isempty operation to check if the stack is empty
    def isempty(self):
        return not self.items

def main():
    # Validate the input to ensure it's positive
    while True:
        # Try catch block to handle non integer inputs
        try:
            # Create a Stack object and ask for input to define the stack size
            stack_size = int(input("Enter the stack size: "))
            # Break the loop if the input is a positive integer
            if stack_size > 0:
                break
            else:
                print("Stack size must be a positive integer, please re-enter.")
        except ValueError:
            print("Enter a valid integer for the stack size.")

    # Create a stack object with the validated stack size
    my_stack = Stack(stack_size)

    # Define a dictionary to map method names to their respective methods
    # Used dictionary dispather instead of switch case to avoid repetitive and rigid implementation
    dispatcher = {
        'push': my_stack.push,
        'pop': my_stack.pop,
        'peek': my_stack.peek,
        'display': my_stack.display,
        'isfull': my_stack.isfull,
        'isempty': my_stack.isempty
    }

    while True:
        # Ask the user to enter a method name to perform an operation on the stack
        operation = input("Enter an operation (push/pop/peek/display/isfull/isempty): ")

        # Exit operation to break the loop and exit the program
        if operation == 'exit':
            print("Exiting program.")
            break

        # Dispatch the chosen operation
        if operation in dispatcher:
            # Handle push operation seperately since it has a parameter to be passed
            if operation == 'push':
                item = input("Enter the item to be pushed: ")
                if dispatcher[operation](item):
                    print(f"Pushed {item} to the stack.")
                else:
                    # Handle overflow
                    print("Stack is full. Cannot push:", item)
                continue

            # Execute the selected operation other than push and print the result accordingly
            result = dispatcher[operation]()
            if result is not None: 
                print("Result:", result)

        else:
            # Print error for any invalid operations
            print("Invalid operation.")

# So that lib import does not include main function
if __name__ == "__main__":
    main()