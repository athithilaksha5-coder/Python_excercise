class college:
    dep="computer science"
    def __init__(self,name):
        self.name=name
        self.clg2=self.college2()

    def dept(self):
        print("my college name:", self.name)
        print("my depart is:",college.dep)
    class college2:
        def __init__(self):
            pass
        def teach(self):
            print("teaching")
madurai=college("NGK")
madurai.dept()
madurai.clg2.teach() 