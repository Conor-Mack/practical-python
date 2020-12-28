from timethis import timethis
import time

@timethis
def countdown(n):
    while n > 0:
        n -= 1

