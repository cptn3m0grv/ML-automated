import fileinput

file_name = '/root/workshop-ml/CNN.py'

for line in fileinput.FileInput(file_name, inplace = 1):
    if "model.add(MaxPooling2D(pool_size = (2, 2))" in line:
        line = line.replace(line, line + '''model.add(Convolution2D(filters = 64,
                        kernel_size = (3, 3),
                        activation = 'relu'))

model.add(MaxPooling2D(pool_size = (2, 2))
''' + '\n')
    print(line)

