# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input('Digite a medida em metros: '))

vkm = v / 1000
vhm = v / 100
vdam = v / 10
vdm = v * 10
vcm = v * 100
vmm = v * 1000
print('A medida fornecida vale: {:.6f}km / {:.5f}hm / {:.4f}dam / {:.3f}m / {:.2f}dm / {:.1f}cm / {:.0f}mm.'.format(vkm,vhm,vdam,v,vdm,vcm,vmm))
print('A medida fornecida vale: {:.6f}km / {:.5f}hm / {:.4f}dam / {:.3f}m / {:.2f}dm / {:.1f}cm / {:.0f}mm.'.format(v/1000,v/100,v/10,v,v*10,v*100,v*1000))
