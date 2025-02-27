from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *

from area_assesment.neural_networks.metrics import *


def cnn_v1():
    """
    Definition of cnn architecture from
    Article: "Multiple Object Extraction from Aerial Imagery with Convolutional Neural Networks" by
    Authors: Saito, Shunta; Yamashita, Takayoshi; Aoki, Yoshimitsu
    Source: http://www.ingentaconnect.com/content/ist/jist/2016/00000060/00000001/art00003

    The difference from the paper above is in tha last dense layer:
    1) shape
    2) activation function is sigmoid instead of softmax (due to binary class problem specification)

    :return: keras model
    """

    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=16, strides=4, activation='relu', input_shape=(64, 64, 3)))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=112, kernel_size=4, strides=1, activation='relu'))
    model.add(Conv2D(filters=80, kernel_size=3, strides=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dense(64 ** 2, activation='sigmoid'))
    model.add(Reshape((64, 64)))
    # print(model.output_shape)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def cnn_v3():
    """
    cnn architecture from
    Article: "Multiple Object Extraction from Aerial Imagery with Convolutional Neural Networks" by
    Authors: Saito, Shunta; Yamashita, Takayoshi; Aoki, Yoshimitsu
    Source: http://www.ingentaconnect.com/content/ist/jist/2016/00000060/00000001/art00003

    :return: keras model
    """

    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=16, strides=4, activation='relu', input_shape=(64, 64, 3)))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=112, kernel_size=4, strides=1, activation='relu'))
    model.add(Conv2D(filters=80, kernel_size=3, strides=1, activation='relu'))

    model.add(Flatten())
    model.add(Dense(64 ** 2, activation='relu'))
    model.add(Dense(16 ** 2, activation='sigmoid'))
    model.add(Reshape((16, 16)))
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
    return model


def cnn_v4():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 3)))
    model.add(Conv2D(filters=64, kernel_size=5, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    # model.add(BatchNormalization())
    model.add(Conv2D(filters=128, kernel_size=5, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    # model.add(BatchNormalization())
    model.add(Conv2D(filters=256, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    # model.add(BatchNormalization())
    model.add(Conv2D(filters=128, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Flatten())
    model.add(Dense(16 ** 2, activation='sigmoid'))
    model.add(Reshape((16, 16)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', jaccard_coef])
    return model


def cnn_v4_cont():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 1)))
    model.add(Conv2D(filters=64, kernel_size=4, strides=4, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=128, kernel_size=4, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=256, kernel_size=2, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=128, kernel_size=2, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Flatten())
    model.add(Dense(16 ** 2, activation='sigmoid'))
    model.add(Reshape((16, 16)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', jaccard_coef])
    return model


def cnn_v5():
    """
    input shape: (64, 64, 32)
    output shape: (48, 48)
    :return:
    """
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 3)))

    model.add(Conv2D(filters=32, kernel_size=5, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Conv2D(filters=64, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Conv2D(filters=128, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Conv2D(filters=256, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Conv2D(filters=1, kernel_size=3, strides=1, activation='sigmoid'))

    model.add(Reshape((48, 48)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', jaccard_coef])
    return model


def cnn_v7():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 3)))
    model.add(Conv2D(filters=32, kernel_size=9, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=64, kernel_size=7, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=128, kernel_size=5, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=256, kernel_size=5, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=128, kernel_size=3, strides=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1))
    model.add(Conv2D(filters=1, kernel_size=3, strides=1, activation='sigmoid'))
    model.add(MaxPooling2D(pool_size=2, strides=1))

    model.add(Reshape((32, 32)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', precision, recall,
                                                                         fmeasure, jaccard_coef])
    return model


def cnn_v7_jb_rural():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 3)))
    model.add(Conv2D(filters=32, kernel_size=9, strides=1, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1, padding='same'))
    model.add(Conv2D(filters=1, kernel_size=1, strides=1, activation='sigmoid'))
    model.add(Reshape((64, 64)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', jaccard_coef])
    return model


def cnn_v7_jb_city():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(64, 64, 3)))
    model.add(Conv2D(filters=32, kernel_size=9, strides=1, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1, padding='same'))
    model.add(Conv2D(filters=64, kernel_size=7, strides=1, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=1, padding='same'))
    model.add(Conv2D(filters=1, kernel_size=1, strides=1, activation='sigmoid'))
    model.add(Reshape((64, 64)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', jaccard_coef])
    return model


def baseline_model():
    model = Sequential()
    model.add(Flatten(input_shape=(64, 64, 3), activation='relu'))
    model.add(Dense(16**2, activation='sigmoid'))
    model.add(Reshape((16, 16)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
