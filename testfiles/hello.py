class Hello():
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def display_details(self):
        print(self.n, self.a)


class Bye(Hello):
    def __init__(self, name, age):
        super().__init__(name, age)


student = Hello("Akash ", 22)
student.display_details()
print("Wassup?")
RcbWinsIPL = int(input())
if(RcbWinsIPL):
    print("RCB is great, RCB is always great")
else:
    print("Eventhough RCB is the greatest team of all time.")
