# Practical No. 14
# Exercise Q.3
class Degree:
    def getDegree(self):
        print("I got degree")
class UnderGraduate(Degree):
    def getDegree(self):
        print("I am an UnderGraduate")
class postGraduate(Degree):
    def getDegree(self):
        print("I am a postGraduate")

d=Degree()
d.getDegree()
d=UnderGraduate()
d.getDegree()
d=postGraduate()
d.getDegree()