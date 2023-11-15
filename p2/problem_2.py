#Algorithm using recursions to find the longest contiguous subpart that is 
#   present in both sequences and write it to a file called output.txt
#Made by Amon Vanderlei
#Email: amon.chalegre@gmail.com

def longest_contiguous_subpart(A: str, B: str) -> str:
    """Find the longest contiguous subpart present in both strings.

    Args:
        A (str): String containing a sequence.
        B (str): String containing a sequence.

    Returns:
        str: Longest continguous subpart present in both strings.
    """
    for i in range(1, len(A)+1):
        #Verifies if A's first i numbers are in B.
        if A[0:i] not in B:
            #sub_A is a sequence present in both
            sub_A = A[0:i-1]
            #sub_A_2 is the rest of the sequence
            sub_A_2 = A[i:]
            
            #If it's True, sub_A is the longest sequence.
            if len(sub_A) >= len(sub_A_2):
                return sub_A
            #If it's False, the longest sequence can be in sub_A_2.
            else:
                longest_in_A_2 = longest_contiguous_subpart(sub_A_2, B)
                if len(longest_in_A_2) >= len(sub_A):
                    return longest_in_A_2
                else:
                    return sub_A

#Gets the sequences present in input.txt
with open("input.txt", "r") as f:
    sequences = []
    for sequence in f:
        sequences.append(sequence.split("\n")[0])
A, B = sequences

#Gets the longest contiguous subpart present in both sequences.
longest_subpart = longest_contiguous_subpart(A, B)

#Writes the output in output.txt
with open('output.txt', 'w') as f:
    f.write(longest_subpart)
