from app.calculator import add,sub

'''
  from app -> folder
  calculator -> filename
  import add, substract (functions)
'''

def test_add():
  assert add(3,2) == 5

def test_sub():
  assert sub(5,2) == 3 
