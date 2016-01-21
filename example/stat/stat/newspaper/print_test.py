import os
from fython import *

os.system('rm *.out') # cleaning any previous run

m = load('.print', force=1)

print('\nfinal x')
print(open('./x_final.out', 'r').read())

print('\nx transformed')
print(open('./x_transformed.out', 'r').read())