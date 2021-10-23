import sys
import itertools
import time

def spin(msg,cond):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + '  ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        # if not cond:
        #     break
    write('' * len(status) + '\x08' * len(status))


if __name__ == '__main__':
    spin('Loading ...', 1)