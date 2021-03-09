import math
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.utils import shuffle
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image


class KyleNet:

    def __init__(self,
                 metadata_location,
                 experiment_title,
                 epochs=20,
                 batch_size=128,
                 learning_rate=0.0001,
                 validation_split=0.25,
                 balance_dataset=False,
                 do_augmentation=False):
        self.df = pd.read_csv(metadata_location)

        if balance_dataset:
            self.__balancer()

        self.experiment_title = experiment_title
        self.labels = ["COVID-19", "NON-COVID"]

        # Model properties
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.validation_split = validation_split
        self.image_size = (224, 224)

        # Image generator and iterators
        if do_augmentation:
            self.training = self.__flow_from_df(self.__image_generator(True), "training")
        else:
            self.training = self.__flow_from_df(self.__image_generator(), "training")
        self.testing = self.__flow_from_df(self.__image_generator(), "validation")

        # Number of samples to take per epoch
        self.training_steps = (self.training.samples // self.training.batch_size)
        self.testing_steps = (self.testing.samples // self.testing.batch_size)

        # Create the model
        self.model = self.create_model()
        self.history = None
        self.predictions = None

    def summary(self):
        """Prints a string summary of the network."""
        return self.model.summary()

    def __image_generator(self, using_augmentation=False):
        """
        Generate batches of tensor image data with real-time data augmentation.
        The data will be looped over (in batches).

        :param using_augmentation: Bool value to determine whether or not to include augmentation parameters.
        :return: Returns a generator object that can be looped over.
        """
        return image.ImageDataGenerator(rescale=1. / 255,
                                        horizontal_flip=True if using_augmentation else False,
                                        validation_split=self.validation_split)

    def __flow_from_df(self, generator, subset):
        """
        Takes the dataframe and generates batches.
        The generated batches contain augmented/normalized data.

        :param generator: An ImageDataGenerator instance
        :param subset: Subset of data ('training' or 'validation') if 'validation_split' is set in 'ImageDataGenerator'.

        :return:
        A 'DataFrameIterator' yielding tuples of '(x, y)' where 'x' is a numpy array containing a batch
        of images with shape '(batch_size, *target_size, channels)' and 'y' is a numpy array of corresponding labels.
        """
        return generator.flow_from_dataframe(self.df,
                                             x_col="filename",
                                             y_col="finding",
                                             target_size=self.image_size,
                                             batch_size=self.batch_size,
                                             class_mode="binary",
                                             shuffle=True if subset == "training" else False,
                                             subset=subset)

    def __balancer(self):
        """Balance the dataset but under-sampling the majority class and then shuffles it."""
        g = self.df.groupby("finding")
        self.df = shuffle(g.apply(lambda x: x.sample(g.size().min())).reset_index(drop=True))

    def create_model(self):
        """
        Build the CNN model.
        :return: Returns a 'sequential' model.
        """
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation="relu", input_shape=self.image_size + (3,)))
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

        model.compile(optimizer=Adam(learning_rate=self.learning_rate),
                      loss="binary_crossentropy",
                      metrics=["accuracy"])

        return model

    def train(self):
        """
        Trains the model for a fixed number of epochs (iterations on a dataset).

        :return:
        A 'History' object. Its 'History.history' attribute is a record of training loss values and metrics values
        at successive epochs, as well as validation loss values and validation metrics values (if applicable).
        """
        self.history = self.model.fit(self.training,
                                      steps_per_epoch=self.training_steps,
                                      epochs=self.epochs,
                                      batch_size=self.batch_size,
                                      validation_data=self.testing,
                                      validation_steps=self.testing_steps)

    def plot_history(self, acc_title="Model Accuracy", loss_title="Model Loss"):
        """
        Uses the models 'History' object to plot the accuracy/loss graphs from the 'History.history' attribute to
        analyse how well the model performed during training.
        """
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

    def evaluate(self):
        """
        Returns the loss value & metrics values for the model in the validation set.

        :return:
        Scalar test loss (if the model has a single output and no metrics) or list of scalars (if the model has
        multiple outputs and/or metrics).
        """
        self.model.evaluate(self.testing)

    def predict(self):
        """
        Generates output predictions for the validation set.

        The number of testing steps MUST be ceiled for it to work with a confusion matrix otherwise the number of
        samples will be inconsistent.

        Any predictions > 0.5 are considered NON-COVID (1), < 0.5 are considered COVID-19 (0).

        :return: Numpy array of predictions.
        """
        predictions = self.model.predict(self.testing, math.ceil(self.testing_steps), verbose=1)
        self.predictions = np.where(predictions > 0.5, 1, 0)

    def metric_report(self):
        """Built a text report that shows the precision, recall, and F1-score of the model."""
        print(classification_report(self.testing.classes, self.predictions, target_names=self.labels))

    def confusion_matrix(self):
        """Plot a confusion matrix to evaluate the accuracy of the predictions."""
        cm = confusion_matrix(self.testing.classes, self.predictions)

        fig = sns.heatmap(cm,
                          annot=True,
                          fmt="g",
                          linewidths=2,
                          xticklabels=self.labels,
                          yticklabels=self.labels,
                          cmap="Reds")

        fig.set_title("Confusion Matrix\n")
        fig.set_ylabel("True Class")
        fig.set_xlabel("Predicted Class")
        fig.xaxis.tick_top()

    def roc(self):
        """Plot a ROC curve to show the performance of the classifications at all thresholds."""
        fpr, tpr, _ = roc_curve(self.testing.classes, self.predictions)
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

    def save(self):
        """
        Save the current model in HDF5 format.

        The saved model includes:
        - The model architecture, allowing to re-instantiate the model.
        - The model weights.
        - The state of the optimizer, allowing to resume training exactly where you left off.
        """
        self.model.save(f"../models/{self.experiment_title}.h5")
