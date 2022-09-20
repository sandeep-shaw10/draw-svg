import random


KEY = ['*','&','#','\\','\/','!','@','#','$','%']


def randomKey(size=10):
    if(size > 0):
        string = ''
        for i in range(size):
            string += random.choice(KEY)
        return string
    else:
        return random.choice(KEY)*10
