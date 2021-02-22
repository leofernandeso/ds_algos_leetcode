from typing import List

def can_form_array(arr: List[int], pieces: List[List[int]]) -> bool:
    
    def find_subpiece(arr: List[int], subpiece: List[int]) -> bool:
        piece_size = len(subpiece)
        for i in range(len(arr)):
            if piece == arr[i:i+piece_size]:
                return True
        return False

    for piece in pieces:
        piece_size = len(piece)
        if find_subpiece(arr, piece) == False:
            return False
    return True



        

    
