import random as r; c = 'abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)'; print(''.join([c[r.randint(0,len(c)-1)] for i in range(32)]))
