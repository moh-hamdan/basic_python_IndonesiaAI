import math

print('Program Menghitung Luas Lingkaran')
print('=================================================================================')

radius = int(input('Masukan jari-jari lingkaran: '))

circle_area = math.pi*radius**2

print('\nLuas lingkaran dengan jari-jari %d cm adalah %0.2f cm\u00b2.' %(radius, circle_area))