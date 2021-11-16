#!/usr/bin/env python3

def find_prominance(values, top):
    miss = False

    for i in range(0, len(values)):
        plus_i = 0                  # get value on index 'i + 1'
        if (i == len(values) - 1):
            plus_i = 0
        elif (i < len(values) - 1):
            plus_i = values[i+1]


        minus_i = 0                 # get value on index 'i - 1'
        if (i > 0):
            minus_i = values[i-1]


        i_value = values[i]         # specify value of index 'i'


        if (i_value == top) and (i_value == plus_i):
            miss = True
        else:
            miss = False
        
        if not miss:                # if value is not repeating
            if (i_value == top):    # when value is the highest one, automatically print
                print(i_value)

            else:
                if (plus_i < i_value) and (minus_i < i_value):
                    prominance_value = calculate_prominance(i, i_value)                  

                    print(prominance_value)

def calculate_prominance(indx, i_value):
    left_list = []
    right_list = []
    p_right = 0
    p_left = 0
    prominance = 0

    if (indx == 0):                                 # - when index is 0, calculate only the right side
        right_list = right(i_value, indx, values)   # - logically, because there is no value on the left
        p_right = min(right_list)
        prominance = i_value - p_right                   # >>> calculating prominance

    elif (indx == len(values) - 1):                 # - when index is the last one, calculate only the left side
        left_list = left(i_value, indx, values)     # - logically, again, there is no value on the right side
        p_left = min(left_list)
        prominance = i_value - p_left                    # >>> calculating prominance

    else:                                           # - when index is somewhere in the between, calculating both sides
        left_list = left(i_value, indx, values)     # - at first calculates values on right side, than left side
        right_list = right(i_value, indx, values)   

        p_left = min(left_list)                     # now finding the minimum value in peak list
        p_right = min(right_list)

        l = i_value - p_left                             # >>> calculating prominence
        r = i_value - p_right
        if (l > r):
            prominance = r                          # choosing better (smaller) promimence as result
        else:
            prominance = l

    return prominance


#### finding values on rigt and left sides ####

def right(i_value, indx, values):
    right_list = []

    for r in range(indx + 1, len(values)):    # 'index + 1' -> we dont want to start at index position (i_value)
        r_value = values[r]

        if (i_value > r_value):               # adding to list while 'i_value' is bigger than 'r_value' (value somewhere right)
            right_list.append(r_value)
            if (r == len(values) -1):         # if we are at the and of the list and there was no higher peak... return 0
                right_list = [0]

        elif (i_value == r_value):
            pass

        else:
            break

    return right_list

def left(i_value, indx, values):
    left_list = []

    for l in range(indx - 1, -1, -1):       # reverse loop - we need to go left
        l_value = values[l]

        if (i_value >= l_value):            # adding to list while 'i_value' is bigger than 'l_value' (value somewhere left)
            left_list.append(l_value)
            if (l == 0):                    # if we are at the and of the list and there was no higher peak... return 0
                left_list = [0]

        elif (i_value == l_value):
            pass

        else:
            break

    return left_list


### basic methods ###

def numOfValues(values):
    list_of_all_values = []

    for i in values:
        if (i not in list_of_all_values):
            list_of_all_values.append(i)

    return len(list_of_all_values)      # return number of types of values

def run(values):
    num_of_values = numOfValues(values) # find number of values

    if (num_of_values <= 1):
        print(values[0])                # if number of values is 0/1, result is number on any position

    elif (num_of_values >= 2):
        topH = max(values)

        find_prominance(values, topH)      


### main ###

if __name__ == '__main__':
    values = [ int(_) for _ in input().split() ] # input - values separated by spaces
    valuesN = []

    for i in range(0, len(values)):
        if (values[i] < 1):
            exit(1)

        if i == 0 or (values[i] != values[i-1] and i > 0):
            valuesN.append(values[i])   # remove duplicates

    run(valuesN)
