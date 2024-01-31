# Filtrage de Tableau

arr = [1, 2, 3, 4, 5, 6]


def odd(array):
  return array % 2 != 0


def even(array):
  return array % 2 == 0


def is_prime(array):
  if array <= 1:
    return False
  for i in range(2, int(array**0.5) + 1):
    if array % i == 0:
      return False
  return True


def greater(threshold):
  return lambda n: n > threshold


def smaller(threshold):
  return lambda n: n < threshold


predicats = input(
    "You can choose those predicats:\n1. odd\n2. even\n3. is_prime\n6. greater\n7. smaller\n"
)

if predicats == "odd":
  predicats = odd
elif predicats == "even":
  predicats = even
elif predicats == "is_prime":
  predicats = is_prime
elif predicats == "greater":
  threshold = int(input("Enter the threshold for 'greater than': "))
  predicats = greater(threshold)
elif predicats == "smaller":
  threshold = int(input("Enter the threshold for 'smaller than': "))
  predicats = smaller(threshold)
else:
  print("Error")
  exit()


def filter_array(array, predicats):
  result = []
  for n in array:
    if predicats(n):
      result.append(n)

  return result


print(filter_array(arr, predicats))
