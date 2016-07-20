from contextlib import closing
class RefrigeratorRaider:
    def open(self):
        print('open the fridge door')
    

    def take(self, food):
        print('Finding {}...'.format(food))
        if food == 'pizza':
            raise RuntimeError("too much pizza is not good for your health!")
        print("Taking {}...".format(food))
    

    def close(self): # this implements the closing protocol.
        print("Close the fridge door!")
    

    def raid(self, food):
        # this calls 'close()' automatically by the context manager!
        with closing(RefrigeratorRaider()) as r:
            r.open()
            r.take(food)
            
def main():
    r = RefrigeratorRaider()
    r.raid('two apples!')
    r.raid('pizza')


if __name__ == '__main__':
    main()
