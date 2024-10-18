#%%

name = input("What is your name? ")

print(f'Hello, {name}!')

birthyear = input("What is your year of birth? ")

from datetime import datetime
this_year = datetime.now().year

print(f'You must be {int(this_year)-int(birthyear)}.')





# %%
