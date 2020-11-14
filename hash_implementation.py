def sum_of_characters(data):
    sum = 0
    for character in data:
        sum += ord(character)
    return sum

def guess_position(data, array):
    sum = sum_of_characters(data)
    guessed_pos = sum % len(array)
    return guessed_pos


def insert_in_array(data, array):
    # TODO check, no more space
    if type(data) == str:
        pos = guess_position(data, array)
        # first, search from [pos..len(array)]
        inserted = False
        
        for j in range(pos, len(array)):
            if array[j] == None:
                array[j] = data
                return array, j

        for i in range(0, pos-1):
            if array[i] == None:
                array[i] = data
                return array, i
        
        return array, None
        
        
def search_in_hash_table(data, array):
    pos = guess_position(data, array)
    
    for j in range(pos, len(array)):
        if array[j] == data:
            return j

    for i in range(0, pos-1):
        if array[i] == data:
            return i
    
    return -1

array = [ None, None, None, None, None]
array, pos1 = insert_in_array('uno', array)
print(array)
array,pos2 = insert_in_array('dos', array)
print(array)
array,pos3 = insert_in_array('tres', array)
print(array)
print(array[search_in_hash_table('tres', array)])
array,pos4 = insert_in_array('cuatro', array)
print(array)
print(array[search_in_hash_table('cuatro', array)])
