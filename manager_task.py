# Decorating function
def count_call(func):
    def writer(self, *args, **Kwargs):
        self.call += 1
        return func(self, *args, **Kwargs)
    return writer


# Class that manages task
class Manager:
    # Initialize are call and email.
    def __init__(self):
        """Whenever you add new functions, you need to initialize them here"""
        self.call = 0
        self.email = None


    # Decorating function
    @count_call
    # Function that register email
    def register_email(self, email):
        self.email = email
        return f"{self.call} emails were called"
    

# protection so that code is executed only when it is directly
if __name__ == "__main__":
    # Instantiating the class
    manager = Manager()
    print(manager.register_email('testemailnotexist@gmail.com'))

      
