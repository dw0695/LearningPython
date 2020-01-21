class MethodDemo:
    a = 1

    @classmethod
    def classM(cls):
        print("Class Methofd cls.a = ",cls.a)

    @staticmethod
    def staticM():
        print("Static method")
        
