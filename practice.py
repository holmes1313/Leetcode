

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    import pdb;pdb.set_trace()
    string = list(string)
    new_index = len(string)
    
    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

def test1():
    output = urlify('Mr John Smith    ', 13)
    import pdb;pdb.set_trace()