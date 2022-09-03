class Animals:
    def __init__(self):
        self.eyes = 2
    def breath(self):
        print("enhale, exhale")
class fish(Animals):
    def __init__(self):
        super(fish, self).__init__()
    def swim(self):
        print("move in water.")
    def breath(self):
        super().breath()
        print("doing this under water.")

nemo = fish()
nemo.swim()
nemo.breath()
print(nemo.eyes)
