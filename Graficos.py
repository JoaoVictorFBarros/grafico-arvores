import matplotlib.pyplot as plt

Figure , Axes=plt.subplots (2,3,figsize=(24,9), dpi = 70)
Figure.suptitle('Estruturas de Árvores', fontsize=26)

plt.subplot (231)

plt.bar('Binária',0.0006666667, color = '#C2CEF2')
plt.bar('Rubro Negra',0.0009, color = '#D9946C')
plt.bar('AVL',0.00106667, color = '#D5D9B8')

plt.ylabel ('Segundos',fontsize=14)
plt.title('Inserção - Mil entradas',fontsize = 16)


plt.subplot(232)

plt.bar('Binária',0.00763333, color = '#C2CEF2')
plt.bar('Rubro Negra',0.0108667, color = '#D9946C')
plt.bar('AVL',0.0144, color = '#D5D9B8')

plt.ylabel('Segundos',fontsize = 14)
plt.title('Inserção - 10 Mil entradas',fontsize = 16)

plt.subplot(233)

plt.bar('Binária',0.1822, color = '#C2CEF2')
plt.bar('Rubro Negra',0.280667, color = '#D9946C')
plt.bar('AVL',0.382467, color = '#D5D9B8')

plt.ylabel('Segundos',fontsize = 14)
plt.title('Inserção - 1 Milhão de entradas',fontsize = 16)

plt.subplot(234)

plt.bar('Binária',0.00396667, color = '#C2CEF2')
plt.bar('Rubro Negra',0.0026, color = '#D9946C')
plt.bar('AVL',0.00256667, color = '#D5D9B8')

plt.ylabel('Segundos',fontsize = 14)
plt.title('Busca - 5 Mil entradas',fontsize = 16)

plt.subplot(235)

plt.bar('Binária',0.00813333, color = '#C2CEF2')
plt.bar('Rubro Negra',0.0051, color = '#D9946C')
plt.bar('AVL',0.00513333, color = '#D5D9B8')

plt.ylabel('Segundos',fontsize = 14)
plt.title('Busca - 10 Mil entradas',fontsize = 16)

plt.subplot(236)

plt.bar('Binária',0.1035, color = '#C2CEF2')
plt.bar('Rubro Negra',0.0553333, color = '#D9946C')
plt.bar('AVL',0.0509, color = '#D5D9B8')

plt.ylabel('Segundos',fontsize = 14)
plt.title('Busca - 100 Mil entradas',fontsize = 16)

Figure.tight_layout(pad = 2.8)
plt.show()
