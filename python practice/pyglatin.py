# 1
print("Pig Latin")

# 2
print('Welcome to the Pig Latin Translator!')

# PY2
# original = raw_input("Enter a word: ")
# PY3
original = input("Enter a word: ")

# 4
# original = raw_input("Enter a word: ")
original = input("Enter a word: ")
if len(original) > 0:
    print(original)
else:
    print("empty")

# 5
# original = raw_input("Enter a word: ")
original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")

# 11
pyg = 'ay'
original = input('Enter a word:')
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print('empty')