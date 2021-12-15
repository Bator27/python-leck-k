kutyanev = input('Hogyan hívják az ebet?')
print('Kutya neve:  ',  kutyanev)
kutyaeletkor = int(input('Hány éves a kutya?'))
print('Kutya életkora:', kutyaeletkor)
kutyafajta = input('Milyen fajta a kutya?')
print('Kutya fajtája:' ,kutyafajta)
veszetsegioltas = input('Rendelkezik a házi állatjuk veszetségi elleni oltással?')
print('Veszetségi oltása van-e?' ,veszetsegioltas)
fajtisztae = input( 'Fajtiszta? : igen/nem')
if fajtisztae == 'igen' :
    print('Fajtiszta : igen')
else:
    print('Keverék')

oltásszuri = {}
print(oltásszuri)

kutya = {
    'Neve' : kutyanev,
    'eletkor': kutyaeletkor,
    'fajtája': kutyafajta,
    'fajtiszta' : fajtisztae,
    'veszetség elleni oltás': True
}
print('kutya életkor:')
print(kutya['eletkor'])

print(kutya.get('eletkor'))
print(kutya.get('veszetség elleni oltás', 'nem'))
print('Neve' in kutya)
kutya['eletkor'] = kutyaeletkor
print(kutya['eletkor'])
kutya['Fajtiszta'] = fajtisztae
del kutya['fajtiszta']

for oltás in kutya:
    print(oltás, kutya[oltás])

for ertek in kutya.values():
    print(ertek)

for oltás, ertek in kutya.items():
    print(oltás , ertek)
