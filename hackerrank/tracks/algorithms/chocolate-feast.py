import sys

def parse_input():
    for line in sys.stdin.readlines()[1:]:
        yield map(int, line.split())

if __name__ == "__main__":
    for n,c,m in parse_input():
        bars = wrappers = n / c
        while wrappers/m:
            extra_bars, unused_wrappers = wrappers/m, wrappers%m
            bars += extra_bars
            wrappers = unused_wrappers + extra_bars
        print bars
