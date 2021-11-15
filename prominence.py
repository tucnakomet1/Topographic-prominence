#!/usr/bin/env python3

def find_prominance(values, top):
    miss = False
    vrcholy = []
    result = []

    for i in range(0, len(values)):
        plus_i = 0                  # get value on index i + 1
        if i == len(values) - 1:
            plus_i = 0
        elif i < len(values) - 1:
            plus_i = values[i+1]

        minus_i = 0                 # get value on index i - 1
        if i > 0:
            minus_i = values[i-1]

        i_value = values[i]         # value of index i

        if i_value == top and i_value == plus_i:
            miss = True
        else:
            miss = False
        
        if not miss:
            if i_value == top:
                vrcholy.append(i_value)
                result.append(i_value)
                print(i_value)
            else:
                if plus_i < i_value and minus_i < i_value:
                    vrcholy.append(i_value)

                    if i_value == top:
                        result.append(i_value)
                        print(i_value)
                    else:
                        left_list = []
                        right_list = []
                        res_right = 0
                        res_left = 0
                        res = 0

                        indx = i

                        if indx == 0:
                            right_list = right(i_value, indx, values)
                            res_right = min(right_list)
                            res = i_value - res_right
                        elif indx == len(values) - 1:
                            left_list = left(i_value, indx, values)
                            res_left = min(left_list)
                            res = i_value - res_left
                        else:
                            left_list = left(i_value, indx, values)
                            right_list = right(i_value, indx, values)

                            res_left = min(left_list)
                            res_right = min(right_list)

                            l = i_value - res_left
                            r = i_value - res_right
                            if (l > r):
                                res = r
                            else:
                                res = l
                        result.append(res)
                        
                        print(res)
    return result

def right(vrchol, indx, listak):
    res_list = []

    for r in range(indx + 1, len(listak)):
        r_value = listak[r]

        if vrchol > r_value:
            res_list.append(r_value)
            if r == len(listak) -1:
                res_list = [0]
        elif vrchol == r_value:
            pass
        else:
            break
    return res_list

def left(vrchol, indx, listak):
    res_list = []

    for l in range(indx - 1, -1, -1):
        l_value = listak[l]

        if vrchol >= l_value:
            res_list.append(l_value)
            if l == 0:
                res_list = [0]
        elif vrchol == l_value:
            pass
        else:
            break

    return res_list


### basic methods ###

def numOfValues(values):
    list_of_all_values = []

    for i in values:
        if (i not in list_of_all_values):
            list_of_all_values.append(i)
    return len(list_of_all_values)      # return number of types of values

def run_it(values):
    num_of_values = numOfValues(values) # find number of values

    if num_of_values <= 1:
        print(values[0])                # if number of values is 0/1, result is number on any position
    elif num_of_values >= 2:
        topH = max(values)

        find_prominance(values, topH)      


### main ###

if __name__ == '__main__':
    values = [ int(_) for _ in input().split() ]
    valuesN = []

    for i in range(0, len(values)):
        if (values[i] < 1):
            break

        if i == 0 or (values[i] != values[i-1] and i > 0):
            valuesN.append(values[i])   # remove duplicates

    run_it(valuesN)
