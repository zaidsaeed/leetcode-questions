"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    encoded_str = ''
    for string in strs:
        encoded_str += (str(len(string)) + '/' + string)
    print(encoded_str)
    return encoded_str

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(string):
    ans = []
    i = 0
    while i < len(string):
        e = i
        while (string[e] != '/'):
            e += 1
        num = int(string[i:e])
        sub_str = string[e+1:e+num+1]
        i = e+num+1
        ans.append(sub_str)
        
    print(ans)
    return ans

input_str = ["lint","code","love","you"]
input_str = encode(input_str)
decode(input_str)
