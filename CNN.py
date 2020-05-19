from keras.layers import Convolution2D, MaxPooling2D, Dense, Flatten
from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator

model = Sequential()

model.add(Convolution2D(filters = 32,
                        kernel_size = (3, 3),
                        activation = 'relu',
                        input_shape = (64, 64 ,3)))

model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())

model.add(Dense(units = 128,
                activation = 'relu'))

model.add(Dense(units = 64,
                activation = 'relu'))

model.add(Dense(units = 1,
                activation = 'sigmoid'))

model.compile(optimizer = 'adam',
             loss = 'binary_crossentropy',
             metrics = ['accuracy'])

train_datagen = ImageDataGenerator(
                rescale = 1./255,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(
               '/root/training_set',
                target_size = (64, 64),
                batch_size = 32,
                class_mode = 'binary')

testing_set = test_datagen.flow_from_directory(
                '/root/test_set',
                target_size = (64, 64),
                batch_size = 32,
                class_mode = 'binary')

his = model.fit(training_set,
               steps_per_epoch = 250,
               epochs = 2,
               validation_data = testing_set,
               validation_steps = 800)

#model.save('cats-dogs.h5')

#training_set.class_indices

final_acc = his.history['accuracy'][(len(his.history['accuracy'])-1)] * 100

#print(final_acc)

f = open("/root/output.txt", "w")
f.write("%d" % int(final_acc))
f.close()
