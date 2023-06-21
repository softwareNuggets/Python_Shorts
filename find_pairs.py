def find_sums(numbers, find_added_value):
    result = []

    for i in range(len(numbers) - 1):
        n1 = numbers[i]
        index = i + 1

        while index < len(numbers):
            n2 = numbers[index]
            if n1 + n2 == find_added_value:
                result.append([i, index])
            index += 1

    return result



def find_pairs(numbers, find_added_value):
    
    indexes = find_sums(numbers, find_added_value)
    if indexes:
       for pair in indexes:
            index1, index2 = pair
            n1,n2 = numbers[index1], numbers[index2]
            print(f'Found this: {n1} + {n2} = {find_added_value}')
    else:
        print('No pairs were found')



if __name__ == '__main__':

    numbers             =   [1, 5, 4, 2]
    find_added_value    =   6

    find_pairs(numbers,find_added_value)
