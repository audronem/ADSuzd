grafas = {
  '1' : ['3','5', '6'],
  '2' : ['4', '3'],
  '3' : ['1', '2', '8'],
  '4' : ['2', '5', '6', '7'],
  '5' : ['1', '4', '6'],
  '6' : ['1', '4', '5'],
  '7' : ['4'],
  '8' : ['3']
}

aplankyti = []
eile = []

def bfs(aplankyti, grafas, taskas):
  aplankyti.append(taskas)
  eile.append(taskas)

  while eile:
    s = eile.pop(0)
    print (s, end = " ") 

    for kaimynas in grafas[s]:
      if kaimynas not in aplankyti:
        aplankyti.append(kaimynas)
        eile.append(kaimynas)

bfs(aplankyti, grafas, '1')
