def capitals(word):
  up = []
  
  for i in range(len(word)):   # so as not to repeat first instance of cap
      if word[i].isupper():
          up.append(i)
  return up