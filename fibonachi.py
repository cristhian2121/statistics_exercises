import time
import sys
from utils.time_mesure import measure_time

def fibonacci_recursive(n: int) -> int:

  if n == 0 or n == 1:
    return 1
  
  return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n: int, memo = {}) -> int:

  if n == 0 or n == 1:
    return 1
  
  try: 
    return memo[n]
  except KeyError:
    res = fibonacci_dynamic(n-1, memo) + fibonacci_dynamic(n-2, memo) 
    memo[n] = res
    return res

@measure_time
def run_recursive(n:int) -> int:
  res = fibonacci_recursive(n)
  return res

@measure_time
def run_dynamic(n:int) -> int:
  res = fibonacci_dynamic(n)
  return res

if __name__ == "__main__":

  # Config max recursive iteration
  sys.setrecursionlimit(100)

  entry = int(input("Text a number to calculate fibonacci serie: "))
  res = run_recursive(entry)  
  res2 = run_dynamic(entry)
  print(f'Are equal? {res == res2}')