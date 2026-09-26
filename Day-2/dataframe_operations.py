import pandas

dataset={
    'subject':['Maths',"NULL",'Science','History'],
    'score':[90,80,70,60]
}

my_data_frame=pandas.DataFrame(dataset)
print(my_data_frame)

print(my_data_frame.info())