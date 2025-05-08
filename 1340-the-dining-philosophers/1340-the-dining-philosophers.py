import threading

class DiningPhilosophers:
    def __init__(self):
        self.locks = [threading.Lock() for x in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # if all want to eat, let philosopher pick their right and left for 0
        # otherwise pick their left and someone else right
        # avoids deadlock
        if philosopher == 0:
            right = philosopher
            left = (philosopher + 1) % 5
        else:
            left = philosopher
            right = (philosopher + 1) % 5

        with self.locks[left], self.locks[right]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()