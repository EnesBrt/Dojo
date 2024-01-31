# Aplatir un Tableau de Tableaux (Tableau Plat)

arr = [[1, 2, 3], [4, 5], [6]]

flatten_arr = []

def flat_arr(arr):
  for x in arr:
    for y in x:
      flatten_arr.append(y)

  return flatten_arr


print(flat_arr(arr))
