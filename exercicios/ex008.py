import math
# co=float(input('Comprimento do cateto oposto: '))
# ca=float(input('Comprimento do cateto adjacente: '))
# hi = math.hypot(co,ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

ang = float (input('Digite o angulo que você deseja: '))
print ('O angulo de {} tem o seno de {:.2f}'.format(ang,math.sin(math.radians(ang))))
print ('O angulo de {} tem o cosseno de {:.2f}'.format(ang,math.cos(math.radians(ang))))
print ('O angulo de {} tem o Tangente de {:.2f}'.format(ang,math.tan(math.radians(ang))))
