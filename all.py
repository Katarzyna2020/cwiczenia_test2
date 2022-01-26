import wczytaj as w
import ploty as p
import matplotlib.pyplot as plt
import dopasowania as d
import teoria as t

# To jest główny program"

# To jest nazwa pliku

nazwa=input("Podaj nazwę pliku bez rozszerzenia .txt \n")

print(nazwa)

dane=w.wczytaj(nazwa+'ala.txt')

f=dane[:,0]
uwe=dane[:,1]
uwy=dane[:,2]
r=uwy/uwe
dr=0.02*r
deltafi=dane[:,3]

print("Liczba pomiarów w pliku = ", w.ilepom(dane))

plt.figure()
p.plot_noerr(f,r)
plt.show()

plt.figure()
p.plot_err(f,r,dr)

par=d.dopasuj(f,r,dr,t.tlumienie_fit)

p.plot_tlumienie_after_fit(par)

plt.show()


