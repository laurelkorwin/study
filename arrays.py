from collections import defaultdict, OrderedDict

# QUESTION 1
# Is unique: implement an algorithm to determine if a string has all unique characters.

def is_unique(strng):

    my_set = set()

    for i in strng:
        if i in my_set:
            return False
        else:
            my_set.add(i)

    return True

# if you can't use additional data structures
def is_unique_2(strng):

    lower_strng = ''.join([s.lower() for s in strng])

    for i in range(len(lower_strng) - 1):
        if lower_strng[i] in lower_strng[i + 1:]:
            return False

    return True

# QUESTION 2
# Check permutation: given two strings, write a method to decide if one is a permutation
# of the other

def check_permutation(strng1, strng2):

    if len(strng1) != len(strng2):
        return False

    # below assumes that both strings are all lowercase - otherwise, would use list comprehension similar to above to make them lowercase
    sorted_strng1 = sorted(strng1)
    sorted_strng2 = sorted(strng2)

    if sorted_strng1 == sorted_strng2:
        return True

    return False

def check_permutation_2(strng1, strng2):
# NOT SURE IF THIS WOULD ALWAYS WORK...
    if len(strng1) != len(strng2):
        return False

    letters = defaultdict(int)

    for s in strng1:
        letters[s] += 1

    for s in strng2:
        letters[s] -= 1

    for value in letters.values():
        if value != 0:
            return False

    return True

# QUESTION 3
# Replace all spaces in a string with '%20'

def urlify(strng):

    strng_lst = [s for s in strng]

    for index, item in enumerate(strng_lst):
        if item.isspace():
            strng_lst[index] = '%20'

    return ''.join(strng_lst)

# QUESTION 4
# Palindrome permutation - given a string, write a function to check if it is a permutation
# of a palindrome

def palindrome_permutation(strng):

    my_dict = defaultdict(int)
    s_lst = [s for s in strng if not s.isspace()]

    for s in s_lst:
        my_dict[s] += 1

    if len(s_lst) % 2 == 0:
        for value in my_dict.values():
            if value % 2 != 0:
                return False

    elif len(s_lst) % 2 != 0:
        odds = 0
        for key, value in my_dict.items():
            if value % 2 != 0 and not key.isspace():
                odds += 1
        if odds > 1:
            return False

    return True

# QUESTION 5
# One away - write a function to see if two string are 'one edit' away from being 
# the same. Edits can be insert a character, remove a character, replace a character

def one_away(strng1, strng2):

    s1len = len(strng1)
    s2len = len(strng2)

    if (abs(s1len - s2len) > 1):
        return False

    editcount = 0

    i = 0
    j = 0

    while i < s1len and j < s2len:
        if strng1[i] != strng2[j]:
            if editcount == 1:
                return False

            if s1len > s2len:
                i += 1

            elif s2len > s1len:
                j += 1

            else:
                i += 1
                j += 1

            editcount += 1

        else:
            i += 1
            j += 1

    # if last character is extra in any string
    if i < s1len or j < s2len:
        editcount += 1

    return editcount == 1

# QUESTION 6
# String compression - use counts of repeated characters.
# if compressed string would not become smaller than original, return original
# assume string only has upper and lowercase letters a-z

# Below only gives totals - doesn't sum each group of letters in place
# for letters duplicated across the entire word
def compress_string(strng):

    my_dict = OrderedDict()
    new_strng = ''

    for s in strng:
        my_dict[s] = my_dict.get(s, 0)
        my_dict[s] += 1


    for key, value in my_dict.items():
        if value > 1:
            new_strng += key + str(value)
        else:
            new_strng += key

    return new_strng

def compress_string2(strng):

    new_strng = ''
    current_count = 1

    my_set = set(strng)

    if len(my_set) == len(strng):
        return strng

    for i in range(0, len(strng)):
        if i != len(strng) - 1 and strng[i] == strng[i + 1]:
            current_count += 1
        else:
            if current_count > 1:
                new_strng += strng[i] + str(current_count)
                current_count = 1
            else:
                new_strng += strng[i]

    return new_strng

# QUESTION 7
# Rotate matrix - given an image represented by an NxN matrix, where each pixel is 4 bytes
# write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix):

    n = len(matrix)

    for layer in range(n // 2):
        # saves the indices you need to switch
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # saves top
            top = matrix[layer][i]
            # left to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
             # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top

    return matrix

# QUESTION 8
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to zero
def zero_matrix(matrix):

    num_rows = len(matrix)
    num_columns = len(matrix[0])

    column_zeros = []
    row_zeros = []

    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] == 0:
                row_zeros.append(i)
                column_zeros.append(j)

    for i in range(num_rows):
        if i in row_zeros:
            for j in range(num_columns):
                matrix[i][j] = 0

    for i in range(num_columns):
        if i in column_zeros:
            for j in range(num_rows):
                matrix[j][i] = 0

    return matrix

# QUESTION 9
# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, write code to check if one string is a rotation of s1 using only one
# call to isSubstring (e.g. "waterbottle" is a rotation of 'erbottlewat')

def string_rotation(strng1, strng2):

    if len(strng1) != len(strng2):
        return False

    else:
        our_range = len(strng1)
        for i in range(our_range):
            for j in range(our_range):
                if strng1[i] == strng2[j]:
                    if strng1[:our_range - j] == strng2[j:] and strng1[our_range - j:] == strng2[:j]:
                        return True

    return False
