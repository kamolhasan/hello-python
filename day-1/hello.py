print(2+3)
print(3-2)
print(3**3)
print(13/5)
print(13//5)

# single line comment
"""
multiline comment I guess.
"""

st = 'single line string'
print(st)
st = '''multi line string 
so far
I guess'''
print(st)


# Checking data type

print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary, like map of CPP, also unlike map :P 
print(type({9.8, 3.14, 2.7}))    # Set, like set of CPP, unique, but could be mixed of data type
print(type((9.8, 3.14, 2.7)))    # Tuple, immutable they said :D Thanos will be proud :::D