#!/usr/bin/env python3


class Machine():
    def increment(self):
        plus_one = self._increment()
        plus_one()
        plus_one()

    def _increment(self):
        x = 0

        def plus_one():
            nonlocal x
            print(x)
            x += 1

        return plus_one


def main():
    machine = Machine()
    machine.increment()


if __name__ == '__main__':
    main()
