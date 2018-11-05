

#You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:
#
#Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.
#
#For example:

#1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
#1221 produces 0, because every comparison is between a 1 and a 2.
#123425 produces 4, because both 2s match each other, but no other digit has a match.
#123123 produces 12.
#12131415 produces 4.

import array

def calculate_sum(list):
  first_half =  list[:len(list)//2]
  second_half = list[len(list)//2:]
  pairs = zip(first_half, second_half)
  return sum_all_equals(pairs)


def sum_all_equals(pairs):
  sum = 0
  for tuple in pairs:
    if (tuple[0] == tuple[1]):
      sum = sum + tuple[0] + tuple[1]
  return sum

def file_into_list_of_int(path):
  list = []
  with open(path) as f:
    for x in next(f):
      list.append(int(x))
  
  return list 

def main():  
  print("Day 1:2")

  svar = calculate_sum(file_into_list_of_int('../input/1_1.txt'))
  
  print("Svar: " + str(svar))
  
if __name__== "__main__":
  main()
