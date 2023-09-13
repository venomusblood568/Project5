# Cancer Diagnosis Prediction using Neural Networks

This project aims to build a neural network model for predicting cancer diagnosis based on a dataset. The dataset contains features related to cancer diagnoses, and we will use a neural network to classify whether a diagnosis is malignant (1) or benign (0).

## Dataset
The dataset used in this project is `cancer.csv`, which contains the following columns:

- `diagnosis(1=m, 0=b)`: The target variable indicating whether the diagnosis is malignant (1) or benign (0).

## Usage
1. Clone the repository to your local machine.
2. Install the required libraries and dependencies using `pip` or `conda`. You can find the necessary packages in the project's `requirements.txt` file.
   

3. Run the `cancer_prediction.py` script to train and evaluate the neural network model.


4. The model will be trained and evaluated on the provided dataset. You can adjust hyperparameters and experiment with different configurations in the script.

## Model Details
- Neural Network Architecture: This project uses a simple feedforward neural network with two hidden layers, each consisting of 256 units and sigmoid activation functions.
- Loss Function: Binary Cross-Entropy
- Optimizer: Adam
- Training Epochs: 1500

## Results
After training, the model's performance can be evaluated using `model.evaluate(x_train, y_train)`.


## License
This project is licensed under the [MIT License](LICENSE).


Feel free to contribute or report issues!
