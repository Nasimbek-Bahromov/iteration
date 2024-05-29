# 1) classlar yozing. va classlarga iter va next degan dunder method yozing va uni amalda skil ichida ishlatishni mashq qiling 

# class Meningclassim:
#     def __init__(self, boshlanish, tugash):
#         self.hozirgi = boshlanish
#         self.tugash = tugash
    
#     def __iter__(self):
#         ...
#         return self
    
#     def __next__(self):
#         if self.hozirgi < self.tugash:
#             hozirgi = self.hozirgi
#             self.hozirgi += 1
#             return hozirgi
#         else:
#             raise StopIteration
# mening_classim = Meningclassim(1, 5)
# for raqam in mening_classim:
#     print(raqam)

# 2) Shunday class yozingki u iteration bo`lganida o`sha class asosida yaratilingan barcha objectlar iteratsiyaga tushsin 
    
# class Student:
#     students = []

#     def __init__(self, name):
#         self.name = name
#         Student.students.append(self)

#     def __iter__(self):
#         self._iter = iter(Student.students)
#         return self

#     def __next__(self):
#         return next(self._iter)

# student1 = Student("Ali")
# student2 = Student("Vali")
# student3 = Student("G'ani")

# for student in student1:
#     print(student.name)

# 3) Shunday class yozingki u iteration bo`lganida o`sha class asosida yaratilingan barcha objectlar iteratsiyaga tushsin va
# filter yordamida classni xususiyatlariga ko`ra xoxishingizga ko`ra filterlar yozing


# class Talaba:
#     hammasi = []

#     def __init__(self, ism, yosh, bahosi):
#         self.ism = ism
#         self.yosh = yosh
#         self.bahosi = bahosi
#         Talaba.hammasi.append(self)

#     @classmethod
#     def filtr(cls, **kwargs):
#         def moslari(talaba):
#             return all(getattr(talaba, xususiya) == qiymat for xususiya, qiymat in kwargs.items())

#         return filter(moslari, cls.hammasi)

# talaba1 = Talaba("Ali", 20, 'A')
# talaba2 = Talaba("Vali", 21, 'B')
# talaba3 = Talaba("G`ani", 20, 'A')
# talaba4 = Talaba("Salim", 22, 'C')

# print("Barcha talabalar:")
# for talaba in Talaba.hammasi:
#     print(talaba.ism)
# print("Yoshi 20 ga teng bo'lgan talabalar:")
# for talaba in Talaba.filtr(yosh=20):
#     print(talaba.ism)

# 4) Shunday class yozingki u iteration bo`lganida o`sha class asosida yaratilingan barcha objectlarning idsi iteratsiyaga tushsin

# class Talaba:
#     hammasi = []

#     def __init__(self, ism, yosh, bahosi):
#         self.ism = ism
#         self.yosh = yosh
#         self.bahosi = bahosi
#         Talaba.hammasi.append(self)

#     @classmethod
#     def filtr(cls, **kwargs):
#         def mos_keladimi(talaba):
#             return all(getattr(talaba, xususiya) == qiymat for xususiya, qiymat in kwargs.items())

#         return filter(mos_keladimi, cls.hammasi)

#     def __iter__(self):
#         for talaba in self.hammasi:
#             yield talaba

# talaba1 = Talaba("Ali", 20, 'A')
# talaba2 = Talaba("Vali", 21, 'B')
# talaba3 = Talaba("Gulnor", 20, 'A')
# talaba4 = Talaba("Salim", 22, 'C')

# print("Barcha talabalar:")
# for talaba in Talaba.hammasi:
#     print(talaba.ism)

# print("IDlari:")
# for talaba in Talaba.hammasi:
#     print(id(talaba))






