
sentence = "j'aime  les framboises et le chocolat"

# supprimer les espaces doubles sans utiliser replace
def delete_double_space(strings):
  new_string = ""
  for i in range(len(strings)):
    if strings[i] == " " and strings[i+1] == " ":
      new_string += ""
    else:
      new_string += strings[i]

  return new_string
    
  

print(delete_double_space(sentence))
