# MAP project 
Student performance prediction:

**Introduction**

Problem: Identifying students who are at risk of failing based on factors such as extracurricular activities and family income


Based on the student performance and behavior dataset from Kaggle, we can predict that a student's attendance percentage, participation score, study hours, stress level, family income, extracurricular activities and daily sleep hours contribute to the student's overall ability to pass the class. Many studies try to unravel different factors that shapes academic success, including examining the effects of diversity and immigration status or if self-interest affects academic achievement more than environmental influences. Both psychological and environmental factors should be considered for an individuals results.


This project analyzes factors influencing a student's academic performance using:
- K-Nearest Neighbors (KNN) for classification
- Neural Networks for deep learning
- Validation Set Approach for resampling


**Data documentation/processing** 


Dataset is from Kaggle called the student and behavior dataset. To clean the data, any rows with null values were removed and a new data frame was created to include only the input variables that will be used. The columns with object variables are also changed to classification variables. For example, "No" and "Yes" for extracurricular activities were changed to 0 and 1 and for family income levels, low=0, medium=1 and high=2. The target value is the grade variable but instead of using the letter grades directly, their results is determined through pass/fail. The letter grades D/F is a 0 which means fail while A/B/C is a 1 meaning pass.

**code instructions**

1. Importing and Cleaning the Data

After importing the Kaggle dataset, the data is preprocessed to retain only the relevant variables needed for analysis.
Any missing or irrelevant data points are removed to ensure a clean dataset.
Variables used include: student's attendance percentage, participation score, study hours, stress level, family income, extracurricular activities and daily sleep hours.

2. Resampling Method: Validation Set Approach

The dataset is split into training and validation sets using the validation set approach, ensuring that the model is evaluated on unseen data.
The data is then standardized (normalized) to improve model performance, particularly for distance-based algorithms like K-Nearest Neighbors (KNN).

3. K-Nearest Neighbors (KNN) Classification

A loop is implemented to test different values of K (number of neighbors).
The model is trained and tested on the validation set for each K value.
Accuracy is recorded for each iteration to determine the optimal K value.
The results indicate that K = 9 provides the best accuracy for this dataset.

4. Artificial Neural Network (ANN) Model

A neural network is constructed and trained using different hyperparameters.
Multiple architectures are tested by adjusting the number of layers, number of neurons per layer, activation functions, and optimization methods.
The goal is to find the optimal network configuration that yields the best predictive performance.


**Analysis of results and discussion**

Justification of using the modeling approaches for the type of data: 


Validation set approach: This method is a simple and effective way to compare models without excessive retraining.
KNN: This method is good for datasets consisting of numerical and categorical features as KNN can handle it when combined with appropriate distance metrics. If the data is standardized, it ensures that all features contribute equally to the classification process. The most accurate k-value is shown to be 9. The accuracy of 0.69 shows better than random guessing, but could be better. 
ANN: This is suitable for large datasets, allowing the model to learn meaningful patterns without overfitting. The model's best parameters indicate that a neural network with three hidden layers (256, 128, 64 neurons) using the logistic activation function and Adam optimizer with an alpha (regularization term) of 0.001 achieved the best performance. The f1_score for the model is 0.733 showing a fairly balanced tradeoff between precision and recall. One downside to this model is that you could not explain how the output is formed. One issue with this is that there is no way to explain how the output is reached. This may create issues if individuals claim one demographic is being targeted unproportionally.






