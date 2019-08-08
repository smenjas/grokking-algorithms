def look_for_key_nonrecursively(main_box):
  pile = main_box.make_a_pile_to_look_through()
  while pile is not empty:
    box = pile.grab_a_box()
    for item in box:
      if item.is_a_box():
        pile.append(item)
      elif item.is_a_key():
        print "I found the key!"

def look_for_key(box):
  for item in box:
    if item.is_a_box():
      look_for_key(item)
    elif item.is_a_key():
      print "I found the key!"

def countdown(i):
  print i
  if i <= 1:
    return
  else:
    countdown(i-1)

def greet(name):
  print "Hello, " + name + "!"
  greet2(name)
  print "Getting ready to say goodbye..."
  bye()

def greet2(name):
  print "How are you, " + name + "?"

def bye():
  print "OK bye!"

def fact(x):
  if x == 1:
    return 1
  else:
    result = fact(x-1)
    print result
    return x * result

print fact(10)
