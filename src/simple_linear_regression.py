import numpy as np
import tensorflow as tf


# Generate some random data for training
def generate_data(points=100):
    X = np.linspace(-1, 1, points)
    Y = 2 * X + np.random.randn(*X.shape) * 0.33
    return X, Y


# Build a simple linear regression model using TensorFlow
def build_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, input_dim=1, activation="linear"))
    model.compile(optimizer="sgd", loss="mse", metrics=["mae"])
    return model


def main():
    X, Y = generate_data()

    model = build_model()
    model.fit(X, Y, epochs=20)

    # Test the model's prediction
    sample_input = np.array([0.5])
    predicted_output = model.predict(sample_input)

    print(f"Model prediction for input {sample_input[0]} is: {predicted_output[0][0]}")


if __name__ == "__main__":
    main()
