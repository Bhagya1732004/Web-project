
with open ("C:\\Users\\HP\\Downloads\\tp\A.txt","w") as f2:
  with open ("C:\\Users\\HP\\Downloads\\tp\B.txt","r") as f3:
    for i in f3:
      f2.write(i)