
def positionBySalary(salary):
  if salary <= 2000:
    position = "estagiário"
  elif 2000 < salary <= 5800:
    position = "júnior"
  elif 5800 < salary <= 7500:
    position = "pleno"
  elif 7500 < salary <= 10500:
    position = "senior"
  else:
    position = "líder"
    
  return position  

print(positionBySalary(2000))
print(positionBySalary(5800))
print(positionBySalary(7500))
print(positionBySalary(10500))
