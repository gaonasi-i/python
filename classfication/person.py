# Person 클래스

class Person:
    def __init__(self, name, age):
        self.name = name # 생성자 (함수)
        self.age = age

    #멤버의 정보
    def __str__(self):
        return f'이름 : {self.name}, 나이 : {self.age}'

# 클래스 상속 - 클래스이름(부모클래스)
class Employee(Person):
    def __init__(self, name, age, id): # 클래스 상속후 자식클래스에 생성자를 추가할때
        super().__init__(name, age)    # super().__init__(부모클래스 생성자)함수를 사용
        self.id = id # 자식클래스 사번 초기화

    #메서드 재정의(오버라이딩)
    def __str__(self):
        #return f'이름 : {self.name}, 나이 : {self.age}, 사번 : {self.id}'
        return f'{super().__str__()}, 사번 : {self.id}'

    def work(self):
        print("회사에 다닙니다.")

e1 = Employee("이하니", 25, 'a1001')
print(e1)
e1.work()

"""
# 클래스를 사용하려면 객체를 생성해야함 (메모리 실행)
# p1 = 객체(인스턴스, 오브젝트)
p1 = Person("김산", 21)
#print(p1.name)
#print(p1.age)
print(p1)

p2 = Person("이정", 30)
#print(p2.name)
#print(p2.age)
print(p2)
"""