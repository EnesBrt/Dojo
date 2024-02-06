import string

def alphabet_position(text):

  text =  text.lower()
  text = list(text)
  alphabet = list(string.ascii_lowercase)

  for letter in range(len(text)):
    for x in alphabet:
      if letter in alphabet:
        return text[letter]
    



if __name__ == "__main__":
  print(alphabet_position('lol'))