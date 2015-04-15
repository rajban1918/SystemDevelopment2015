
class YourExceptionHandler(object):

    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, type, value, tb):
        return True

with YourExceptionHandler():
    print "do some stuff here"
    1/0

print "should still reach this point"
