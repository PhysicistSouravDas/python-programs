def calculate_exponent(num, exp):
  """
  num: int or float
  exp: int
  various methods to find num^exp, contrary to the standard method num**exp
  """
#By iterative loops
  final = 1
  for i in range(1, exp + 1):
    final = final * num
  return final
    
"""
OR    
  i = 1
  answer = num
  while i < exp:
    answer = answer * num 
    i = i + 1
  return answer

#By recursion
  if exp == 0:
		num = 1
	else:
		num *= calculate_exponent(num, exp - 1)
	return num
"""
