import pandas as pd
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam

class CovidCNN():
    def __init__(self, metadata_location):
        self.df = pd.read_csv(metadata_location)

        # Model properties
        self.batchSize = 128
        self.epochs = 20
        self.imageSize = (224, 224)

        # Image generator and iterators
        self.generator = self.ImageGenerator()
        self.training = self.FlowFromDF("training")
        self.testing = self.FlowFromDF("validation")

        # Number of samples to take in one epoch
        self.trainingSteps = (self.training.samples // self.training.batch_size)
        self.testingSteps = (self.testing.samples // self.testing.batch_size)
        
        self.model = self.Create()

    def Summary(self):
        return self.model.summary()

    def ImageGenerator(self):
        return image.ImageDataGenerator(validation_split=0.2)

    def FlowFromDF(self, subset):
        return self.generator.flow_from_dataframe(self.df,
                                                  x_col="filename",
                                                  y_col="finding",
                                                  target_size=self.imageSize,
                                                  batch_size=self.batchSize,
                                                  class_mode="binary",
                                                  shuffle=True if subset == "training" else False,
                                                  subset=subset)

    def Create(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation="relu", input_shape=self.imageSize + (3,)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(64, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(128, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(256, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(512, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Flatten())
        model.add(Dense(64, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dense(1, activation="sigmoid"))
        model.compile(optimizer=Adam(learning_rate=0.0005), loss="binary_crossentropy", metrics=["accuracy"])

        return model

    def Train(self, model_name):
        return self.model.fit(self.training,
                              steps_per_epoch=self.trainingSteps,
                              epochs=self.epochs,
                              batch_size=self.batchSize,
                              validation_data=self.testing,
                              validation_steps=self.testingSteps)

    def Evaluate(self):
        self.model.evaluate(self.testing)