# Duplicate Encoder

string = "Success"


def duplicate_encode(word):
  word = word.lower()
  count_character = {}

  # Count the frequency of each character
  for letter in word:
      count_character[letter] = count_character.get(letter, 0) + 1

  # Create a new string for the result
  encoded_string = ""

  # Append '(' or ')' based on character frequency
  for letter in word:
      if count_character[letter] == 1:
          encoded_string += "("
      else:
          encoded_string += ")"

  return encoded_string


if __name__ == "__main__":
  print(duplicate_encode(string))
