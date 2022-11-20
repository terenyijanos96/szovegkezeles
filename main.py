from fuggvenyek import *

nagybetu = nagybetus()
print(f"Adott szöveg nagybetűsen: {nagybetu}\n")
hosszabb = hosszabb_mint10()
print(f"Hosszabb-e mint 10 karakter? {hosszabb}\n")

betu3()
print()

elso, hany_a = elso_a()
print(f'\nAz első "a"-betű indexe: {elso}')
print(f'Összesen ennyi "a" betű van a szövegben: {hany_a}\n')

nehez = feketeoves()
print(nehez)

# nev, kor = nevbekero(), kor_ado()
# print(nev)
# print(kor)

nev, kor = legidosebb_ember_kereso()
print(f"A legidősebb: {nev}, aki {kor} éves")
