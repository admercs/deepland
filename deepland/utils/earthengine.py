import os
import json
import ee
import tensorflow as tf
from tensorflow.python.keras import layers, losses, models, metrics, optimizers


def fcn():
    """."""

    print("Earth Engine version:", ee.__version__)
    print("TensorFlow version:", tf.__version__)

    ee.Authenticate()
    ee.Initialize()

    tf.enable_eager_execution()

    # FCN code here


