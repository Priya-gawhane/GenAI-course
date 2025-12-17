chai_type = "plain"

def front():

    def kitchen():
        global chai_type
        chai_type = 'irani'
    kitchen()

front()
print("final global chai", chai_type)