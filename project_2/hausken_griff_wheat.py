squares = 64
rice = 1
total = 0

for i in range(0,squares): # 63 doublings
    total += rice  
    rice *=2 

print('Grains of rice: ', total)


weight = rice * .000000055116 # 50mg= .000000055116 tons
print('Total weight: ', weight, 'tons')

depth_over_oregon = total / (10 * 1E10 * 254806) # 10 grains of rice/cm^2,  10^10 cm^2/km^2, divided by SA of ORegon
print("Oregon would be covered in a layer of rice ", depth_over_oregon, "grains of rice tall")