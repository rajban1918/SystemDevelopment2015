
<<<<<<< HEAD
class YourExceptionHandler(object):

    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, type, value, tb):
        return True
=======

class YourExceptionHandler(object):
    def __enter__(self):
        pass

    def __exit__(self, ex_type, value, traceback):
        print "there was a %s error" % ex_type
        if ex_type is ZeroDivisionError:
            return True
        else:
            return False

>>>>>>> 24857aee40187b54c23b754026c68169b01decd1

with YourExceptionHandler():
    print "do some stuff here"
    1 / 0

print "should still reach this point"

with YourExceptionHandler():
    print "do more"
    fasldkj

print "you should not get here"

