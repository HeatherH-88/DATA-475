#%%

import csv
with open('C:/Users/hkste/OneDrive/Documents/SAIT/DATA-475/1 - AI-Driven Data Analytics/DATA475_lab_rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    area_list = []
    for row in reader:
    #    print(row)
       width = float(row[1])
       height = float(row[2])
       area = width*height
       area_list.append(area)

print(area_list)


# %%

count = len(area_list)
min = min(area_list)
max = max(area_list)
sum = sum(area_list)

import statistics as st
avg = st.mean(area_list)

print(f'Total Count: {count}')
print(f'Total Area: {sum}')
print(f'Average Area: {avg}')
print(f'Minimum Area: {min}')
print(f'Maximum Area: {max}')


# %%

import csv

stats = [
    ('Total Count', count),
    ('Total Area', sum),
    ('Average Area', avg),
    ('Minimum Area', min),
    ('Maximum Area', max)    
]

# for r in stats:
#     print (r)

with open ('C:/Users/hkste/OneDrive/Documents/SAIT/DATA-475/Lab1/summary.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow([r[0] for r in stats])
    writer.writerow([r[1] for r in stats])


# %%
