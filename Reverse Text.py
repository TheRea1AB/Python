""" This code will output a word in reverse """
""" Example: abcd will return dcba """ 


def reverse(text):
  word = ""
  length = len(text) - 1
  while length >= 0:
    word += text[length]
    length -= 1
  return word
