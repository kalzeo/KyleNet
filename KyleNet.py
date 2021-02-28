import math
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.utils import shuffle
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam


class KyleNet:
    def __init__(self,
                 metadata_location,
                 experiment_title,
                 epochs=20,
                 batch_size=128,
                 learning_rate=0.0001,
                 balance_dataset=False,
                 do_augmentation=False):
        self.df = pd.read_csv(metadata_location)

        if balance_dataset:
            self.__Balancer()

        self.experiment_title = experiment_title
        self.labels = ["COVID-19", "NON-COVID"]

        # Model properties
        self.batchSize = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.imageSize = (224, 224)

        # Image generator and iterators
        if do_augmentation:
            self.training = self.__FlowFromDF(self.__AugmentationGenerator(), "training")
        else:
            self.training = self.__FlowFromDF(self.__ImageGenerator(), "training")

        self.testing = self.__FlowFromDF(self.__ImageGenerator(), "validation")

        # Number of samples to take in one epoch
        self.trainingSteps = (self.training.samples // self.training.batch_size)
        self.testingSteps = (self.testing.samples // self.testing.batch_size)

        self.model = self.Create()
        self.history = None
        self.predictions = None

    def Summary(self):
        return self.model.summary()

    def __AugmentationGenerator(self):
        return image.ImageDataGenerator(rescale=1. / 255,
                                        horizontal_flip=True,
                                        validation_split=0.25)

    def __ImageGenerator(self):
        return image.ImageDataGenerator(rescale=1. / 255, validation_split=0.25)

    def __FlowFromDF(self, generator, subset):
        return generator.flow_from_dataframe(self.df,
                                             x_col="filename",
                                             y_col="finding",
                                             target_size=self.imageSize,
                                             batch_size=self.batchSize,
                                             class_mode="binary",
                                             shuffle=True if subset == "training" else False,
                                             subset=subset)

    def __Balancer(self):
        # Undersample the majority class
        g = self.df.groupby("finding")
        self.df = shuffle(g.apply(lambda x: x.sample(g.size().min())).reset_index(drop=True))

    def Create(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation="relu", input_shape=self.imageSize + (3,)))
        model.add(Conv2D(32, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(64, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(128, (3, 3), activation="relu"))
        model.add(Conv2D(128, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Conv2D(256, (3, 3), activation="relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D())
        model.add(Flatten())
        model.add(Dense(32, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dense(1, activation="sigmoid"))
        model.compile(optimizer=Adam(learning_rate=self.learning_rate), loss="binary_crossentropy", metrics=["accuracy"])

        return model

    def Train(self):
        self.history = self.model.fit(self.training,
                              steps_per_epoch=self.trainingSteps,
                              epochs=self.epochs,
                              batch_size=self.batchSize,
                              validation_data=self.testing,
                              validation_steps=self.testingSteps)

    def PlotHistory(self, acc_title="Model Accuracy", loss_title="Model Loss"):
        fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(20, 5))

        ax.plot(self.history.history["accuracy"])
        ax.plot(self.history.history["val_accuracy"])
        ax.set_title(acc_title)
        ax.set(xlabel="# of Epochs", ylabel="Accuracy")
        ax.legend(["train", "val"], loc="upper left")

        ax2.plot(self.history.history["loss"])
        ax2.plot(self.history.history["val_loss"])
        ax2.set_title(loss_title)
        ax2.set(xlabel="# of Epochs", ylabel="Loss")
        ax2.legend(["train", "val"], loc="upper left")

        plt.grid(False)

    def Evaluate(self):
        self.model.evaluate(self.testing)

    def Predict(self):
        # The number of testing steps must be ceiled to use a confusion matrix otherwise the number of
        # samples will be inconsistent.
        # Predictions > 0.5 are NON-COVID (1), < 0.5 are COVID (0)
        predictions = self.model.predict(self.testing, math.ceil(self.testingSteps), verbose=1)
        self.predictions = np.where(predictions > 0.5, 1, 0)

    def MetricReport(self):
        # Build a report to show the main classification metrics
        print(classification_report(self.testing.classes, self.predictions, target_names=self.labels))

    def ConfusionMatrix(self):
        # Plots a confusion matrix to evaluate the accuracy of the classification
        cm = confusion_matrix(self.testing.classes, self.predictions)

        f = sns.heatmap(cm,
                        annot=True,
                        fmt="g",
                        linewidths=2,
                        xticklabels=self.labels,
                        yticklabels=self.labels,
                        cmap="Reds")

        f.set_title("Confusion Matrix\n")
        f.set_ylabel("True Class")
        f.set_xlabel("Predicted Class")
        f.xaxis.tick_top()

    def ROC(self):
        # Plots a ROC curve to show the performance of the classification at different thresholds
        fpr, tpr, thresholds = roc_curve(self.testing.classes, self.predictions)
        auc = roc_auc_score(self.testing.classes, self.predictions)

        plt.title("Receiver Operating Characteristic")
        plt.plot(fpr, tpr, "b", label=f"Area Under Curve: {round(auc * 100, 1)}%")
        plt.legend(loc="lower right")
        plt.plot([0, 1], [0, 1], "r--")
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel("True Positive Rate")
        plt.xlabel("False Positive Rate")
        plt.show()

    def Save(self):
        self.model.save(f"../models/{self.experiment_title}.h5")
