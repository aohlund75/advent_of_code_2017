
def read_file_as_int_matrix(file):
    matrix = []
    text_file = open(file, "r")
    for t in text_file.read().split('\n'):
        matrix.append(list(map(int, t.split())))
    return matrix     


def dif_max_min(list):
    return (max(list) - min(list))
    

def main():  
    print("Day 2:1")

    list_of_lists = read_file_as_int_matrix('../input/2_1.txt')
  
    diffs=[]
    for l in list_of_lists:
        diffs.append(dif_max_min(l))
    
    answer = sum(diffs)

    print("Svar: " + str(answer))

if __name__== "__main__":
  main()