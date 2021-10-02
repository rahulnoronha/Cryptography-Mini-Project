def encrypt(plaintext,depth):
  matrix = [[] for i in range(depth)]
  rail  = 0
  var   = 1
  for char in plaintext:
    matrix[rail].append(char)
    rail += var
    if rail == depth-1 or rail == 0:
      var = -var
  res = ''
  for i in matrix:
    for j in i:
      res += j
  return res

def decrypt(ciphertext,depth):
    matrix = [[] for i in range(depth)]
    rail  = 0
    var   = 1
    for char in ciphertext:
        matrix[rail].append(char)
        rail += var
        if rail == depth-1 or rail == 0:
            var = -var
    rFence = [[] for i in range(depth)]
    i = 0
    l = len(ciphertext)
    ciphertext = list(ciphertext)
    for r in matrix:
        for j in range(len(r)):
            rFence[i].append(ciphertext[0])
            ciphertext.remove(ciphertext[0])
        i += 1
    rail = 0
    var  = 1
    r = ''
    for i in range(l):
        r += rFence[rail][0]
        rFence[rail].remove(rFence[rail][0])
        rail += var
        if rail == depth-1 or rail == 0:
            var = -var
    return r
