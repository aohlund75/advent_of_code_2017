
def read_file_as_int_matrix(file):
    matrix = []
    text_file = open(file, "r")
    for t in text_file.read().split('\n'):
        matrix.append(list(map(int, t.split())))
    return matrix     


def product_of_dividers(in_list):
    in_list.sort(reverse=True)

    max = in_list.pop(0)

    while len(in_list) > 0:
        divider = divider_in_list(max, in_list)
        if divider > 0:
            return max / divider
        max = in_list.pop(0)

    print("Did not find any divisor!")


def even_divideble(numerator, denominator):
    return (numerator % denominator) == 0


def divider_in_list(numerator, list_of_denominators):
    for d in list_of_denominators:
        if even_divideble(numerator, d):
            return d

    return 0 


def sum_all_divisions(list_of_lists):
    diffs=[]
    for l in list_of_lists:
        diffs.append(product_of_dividers(l))
    
    return int(sum(diffs))


def main():  
    print("Day 2:2")

    list_of_lists = read_file_as_int_matrix('../input/2_1.txt')
  
    print("Svar: {}".format(sum_all_divisions(list_of_lists)))

if __name__== "__main__":
  main()