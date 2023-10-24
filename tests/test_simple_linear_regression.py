import numpy as np
import tensorflow as tf
from src.simple_linear_regression import generate_data, build_model


def test_generate_data():
    X, Y = generate_data(100)

    # Assert that the generated data has the expected shape
    assert X.shape == (100,)
    assert Y.shape == (100,)

    # Assert that X is a linear space from -1 to 1
    assert np.array_equal(X, np.linspace(-1, 1, 100))

    # You can add more complex assertions about the nature of Y if needed.


def test_build_model():
    model = build_model()

    # Assert that the model has only one layer
    assert len(model.layers) == 1

    # Assert that the layer is a Dense layer
    assert isinstance(model.layers[0], tf.keras.layers.Dense)

    # Assert that the activation is linear
    assert model.layers[0].get_config()["activation"] == "linear"

    # Assert that the model's optimizer is sgd and the loss function is mse
    assert model.optimizer.get_config()["name"] == "SGD"
    assert model.loss == "mse"
