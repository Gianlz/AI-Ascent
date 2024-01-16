class Testing:

    def __init__(self) -> None:
        pass

    def __connect(self):
        pass

    def __structEmail(self):
        return f"""
Hello this is my test to learn OOP - email sended
                """
    
    def __send(self):
        return None
    
    def sendEmail(self):
        self.__connect()
        self.__send()
        return self.__structEmail()
        
        

testing = Testing()

print(testing.sendEmail())
