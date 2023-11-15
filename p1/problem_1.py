#Algorithm using recursions to find the longest contiguous subpart consisting 
#   of identical digits that is present in both sequences (given in input.txt) 
#   and write it to output.txt.
#The algorithm is inspired in the approach used in the algorithm to find the 
#   maximum subarray described in Chapter 4.1 of the book "Introduction to Algorithm" 
#   by Thomas H. Cormen.
#Made by Amon Vanderlei
#Email: amon.chalegre@gmail.com

from typing import Tuple

def find_longest_contiguous_subpart(A: list[int], 
                                    low: int, 
                                    high: int) -> Tuple[int, int, int, int]:
    """Find the longest contiguous subpart of a given array.

    Args:
        A (list[int]): Array of integers.
        low (int): First index of array.
        high (int): Last index of array.

    Returns:
        Tuple[int, int, int, int]: (
            index where subpart begins, 
            index where subpart ends, 
            length of subpart, 
            digit in subpart).
    """
    if low > high:
        return (0, 0, 0, 0)
    
    #Middle index of array.
    mid = (low + high)//2
    
    #Find how many digits in left side of mid are equal to it.
    #max_left is the index where this sequence starts.  
    max_left = mid
    for i in range(mid, low-1, -1):
        if A[mid] == A[i]:
            max_left = i
        else:
            break
    
    #Find how many digits in right side of mid are equal to it.
    #max_right is the index where this sequence ends.  
    max_right = mid
    for j in range(mid+1, high+1):
        if A[mid] == A[j]:
            max_right = j
        else:
            break
    
    #Longest subpart containg the middle element.
    longest_subpart = (max_left, max_right, max_right-max_left+1, A[max_left])
    
    #Longest subpart in left of the middle element (Resolved recursively).
    left_longest_subpart = find_longest_contiguous_subpart(A, low, max_left-1)
    #Longest subpart in right of the middle element (Resolved recursively).
    right_longest_subpart = find_longest_contiguous_subpart(A, max_right+1, high)
    
    #Returns the longest sequece.
    if longest_subpart[2] >= left_longest_subpart[2] and longest_subpart[2] >= right_longest_subpart[2]:
        return longest_subpart
    elif left_longest_subpart[2] >= right_longest_subpart[2] and left_longest_subpart[2] >= longest_subpart[2]:
        return left_longest_subpart
    else:
        return right_longest_subpart

def find_longest_identical_subpart(A: list[int], 
                                   B: list[int], 
                                   A_array: list[Tuple[int, int, int, int]] = [],
                                   B_array: list[Tuple[int, int, int, int]] = []) -> Tuple[int, int, int, int]:
    """Find the longest contiguous subpart consisting of identical digits
        that is present in both sequences.

    Args:
        A (list[int]): Array of integers.
        B (list[int]): Array of integers.
        A_array (list[Tuple[int, int, int, int]]): Array of the different 
            Tuples returned by find_longest_identical_subpart. Default: [].
        B_array (list[Tuple[int, int, int, int]]): Array of the different 
            Tuples returned by find_longest_identical_subpart. Default: [].

    Returns:
        Tuple[int, int, int, int]: See find_longest_contiguous_subpart.
    """
    #Gets the longest contiguous subpart for A and for B.
    A_longest = find_longest_contiguous_subpart(A, 0, len(A)-1)
    B_longest = find_longest_contiguous_subpart(B, 0, len(B)-1)
    
    #Put these longest contiguous subpart in the correspondent array.
    A_array.append(A_longest)
    B_array.append(B_longest)
    
    #Verify if there is an equal subpart in both lists.
    for A_subpart in A_array:
        for B_subpart in B_array:
            if A_subpart[2] == B_subpart[2] and A_subpart[3] == B_subpart[3]:
                return A_subpart
                
    #Creates new A and new B without the longest contiguous subpart.
    new_A = A[:A_longest[0]] + [A_longest[3]] + A[A_longest[1] + 1:]
    new_B = B[:B_longest[0]] + [B_longest[3]] + B[B_longest[1] + 1:]
    
    #Recursively returns the longest contiguous subpart present in both arrays
    return find_longest_identical_subpart(new_A, new_B, A_array, B_array)

#Gets the sequences present in input.txt
with open("input.txt", "r") as f:
    sequences = []
    for sequence in f:
        sequences.append(sequence.split("\n")[0])

#Transform these sequences in arrays of integers.
A, B = sequences
A = [int(n) for n in A]
B = [int(n) for n in B]

#Gets the longest identical subpart of the sequences.
longest_subpart = find_longest_identical_subpart(A, B)

#Transform the Tuple in a list of strings.
output = [str(longest_subpart[3]) for _ in range(longest_subpart[2])]

#Writes a string in output.txt
with open('output.txt', 'w') as f:
    f.write(''.join(output))