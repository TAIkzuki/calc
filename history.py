import collections

class History:
    def __init__(self, hsize=10):

        self._history = collections.deque([], hsize)

    def push (self, item :str )->None:
        self._history.append(item)

    def show (self)->None:
        print(self._history)
    @staticmethod
    def run(self):
        print('hello')

def main():
    h = History(3)
    h.push('2+3')
    h.push('3+3')
    h.push('2+5')
    h.show()

if __name__ == '__main__':
    main()