from itertools import count         # https://stackoverflow.com/questions/9884213/looping-from-1-to-infinity-in-python

for i in count():       # Will continue indefinetly 
    pbil_activator = input('Try alphabetical: ')    
    if pbil_activator == 'alphebetical':        # As long as alphebetical is input by user
        print('pbil')                           # Print pbil

# I decided to find a way to loop a for loop indefinitely
# since the prompt seemed to imply that it should continue
# and just print pbil when the input was alphebetical
