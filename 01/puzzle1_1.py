
#1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
#1111 produces 4 because each digit (all 1) matches the next.
#1234 produces 0 because no digit matches the next.
#91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

import array

def calculate_sum(list_of_int):
  off_by_1 = list_off_by_one(list_of_int)
  pairs = zip(list_of_int, off_by_1)
  return sum_all_equals(pairs)


def sum_all_equals(pairs):
  sum = 0
  for tuple in pairs:
    if (tuple[0] == tuple[1]):
      sum = sum + tuple[0]
  return sum


def list_off_by_one(list_of_int):
  copy = list_of_int.copy()
  copy.append(copy.pop(0))
  return copy


def file_into_list_of_int(path):
  list = []
  with open(path) as f:
    for x in next(f):
      list.append(int(x))
  
  return list 

def main():  
  print("Day 1:1")

  svar = calculate_sum(file_into_list_of_int('../input/1_1.txt'))
  
  print("Svar: " + str(svar))
  
if __name__== "__main__":
  main()
