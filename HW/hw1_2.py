class Human: 
    def __init__ (self, s): 
        self.__Height = 0;
        self.__Weight = 0;
        self.__name = s;

    def setHeight (self, a): 
        self.__Height = a;

    def setWeight (self, a): 
        self.__Weight = a;

    def getHeight (self): 
        return self.__Height;

    def getWeight (self): 
        return self.__Weight;

    def getName (self) -> str: 
        return self.__name;

class Student (Human): 
    def __init__ (self, s, a): 
        Human.__init__(self, s);
        self.__ID = a;

    def getID (self) -> str: 
        return self.__ID;

    def BMI (self) -> str: 
        h = float(self.getHeight()) / 100;
        w = self.getWeight();
        bmi = w / (h * h);
        return f"{self.getName()}，學號為{self.getID()}，BMI 為 {bmi}";

if __name__ == "__main__": 
    a = Student("Apple", "48763");
    a.setHeight(181);
    a.setWeight(72);
    print(a.BMI());