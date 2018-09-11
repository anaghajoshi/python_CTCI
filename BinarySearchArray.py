

def binary_search(in_array, target_value):
    min_i = 0
    max_i = len(in_array)
    print('in fn')
    while max_i >= min_i:
        guess = (max_i+min_i)//2
        print('Min ', min_i, 'Guess ', guess, 'Max ', max_i)
        print('value' , in_array[guess])

        if in_array[guess] == target_value:
            return guess
        elif in_array[guess] < target_value:
            min_i = guess+1
        else:
            max_i = guess -1
    return -1


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(binary_search(primes, 67))
    print(binary_search(primes, 65))





