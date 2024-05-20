mylist = [1,2,3,3,4,4,5]
def uniqueList(my_list):
  my_list = set(my_list)
  my_list = list(my_list)
  print(my_list)
  return len(my_list)
print(uniqueList(mylist))