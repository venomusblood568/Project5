# Linear Regression

Linear regression is a fundamental statistical technique used for modeling the relationship between a dependent variable (target) and one or more independent variables (features). It assumes a linear relationship between the variables and is widely used for predicting numerical values based on historical data.

## How It Works

In a simple linear regression, the relationship between the dependent variable \( y \) and the independent variable \( x \) is represented by the equation:

\[ y = mx + b \]

Where:
- \( y \) is the dependent variable (target).
- \( x \) is the independent variable (feature).
- \( m \) is the slope of the line (coefficient) representing the relationship between \( x \) and \( y \).
- \( b \) is the y-intercept, indicating the value of \( y \) when \( x \) is 0.

Multiple linear regression extends this concept to more than one independent variable, creating a linear equation in multiple dimensions.

## Usage

Linear regression is commonly used in various fields for tasks such as:
- **Predictive Analysis:** Predicting numerical values based on historical data.
- **Economics:** Modeling economic trends and forecasting.
- **Finance:** Predicting stock prices, currency exchange rates, etc.
- **Biology:** Modeling biological processes based on experimental data.

## Example Code

Here's an example of how you can perform linear regression in Python using the popular scikit-learn library:

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 8])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict values
predicted_values = model.predict([[5]])

print("Predicted value for x=5:", predicted_values[0])
