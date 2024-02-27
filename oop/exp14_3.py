class Degree:
    def getDegree(self):
        print("I got a degree")
class UnderGraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")
class PostGraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")
d=Degree()
d.getDegree()
d=UnderGraduate()
d.getDegree()
d=PostGraduate()
d.getDegree()
        
