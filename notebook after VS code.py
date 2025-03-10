{
    "metadata": {
        "kernelspec": {
            "language": "python",
            "display_name": "Python 3",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.10.12",
            "mimetype": "text/x-python",
            "codemirror_mode": {"name": "ipython", "version": 3},
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py",
        },
        "kaggle": {
            "accelerator": "none",
            "dataSources": [
                {
                    "sourceId": 10776076,
                    "sourceType": "datasetVersion",
                    "datasetId": 6685670,
                }
            ],
            "dockerImageVersionId": 30918,
            "isInternetEnabled": false,
            "language": "python",
            "sourceType": "script",
            "isGpuEnabled": false,
        },
    },
    "nbformat_minor": 4,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "code",
            "source": "# %% [code]\n# This Python 3 environment comes with many helpful analytics libraries installed\n# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n# For example, here's several helpful packages to load\n\nimport numpy as np\nimport pandas as pd \nimport matplotlib.pyplot as plt\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split, GridSearchCV\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Input data files are available in the read-only \"../input/\" directory\n# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n\nimport os\nfor dirname, _, filenames in os.walk('/kaggle/input'):\n    for filename in filenames:\n        print(os.path.join(dirname, filename))\n\n# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session\n\n# %% [code]\ndf = pd.read_csv(\"/kaggle/input/students-grading-dataset/Students_Grading_Dataset.csv\")\ndf.head()\ndf.dtypes\n\n# %% [code]\ndata = df[['Attendance (%)', 'Midterm_Score', 'Participation_Score', 'Study_Hours_per_Week', 'Extracurricular_Activities', 'Family_Income_Level', 'Stress_Level (1-10)', 'Sleep_Hours_per_Night', 'Grade']]\ndata.head()\n\n# %% [code]\ndata.isnull().sum()\n\n# %% [code]\ndataCleaned = data.dropna()\n\n# %% [code]\ndataCleaned['Extracurricular_Activities'] = dataCleaned['Extracurricular_Activities'].replace({'No': 0, 'Yes': 1})\ndataCleaned['Family_Income_Level'] = dataCleaned['Family_Income_Level'].replace({'Low': 0, 'Medium': 1, 'High': 2})\ndataCleaned['Pass_Fail'] = dataCleaned['Grade'].map(lambda x: 0 if x in ['F', 'D'] else 1)\ndataCleaned.head()\n\n# %% [code]\n# Split the data into train and test\nX = dataCleaned.drop(['Grade', 'Pass_Fail'], axis=1)\ny = dataCleaned['Pass_Fail']\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n\n# %% [code]\n# Standardize the data\nscaler = StandardScaler()\nX_train = scaler.fit_transform(X_train)\nX_test = scaler.transform(X_test)\n\n# %% [code]\n# Create a KNN classifier by looping through and testing k values from 1 to 10. We will use accuracy as the metric we are trying to optimize for.\nk_values = range(1, 11)\n\nfor k in k_values:\n    knn = KNeighborsClassifier(n_neighbors=k)\n    knn.fit(X_train, y_train)\n    y_pred = knn.predict(X_test)\n    print(f'k = {k}  Accuracy: {accuracy_score(y_test, y_pred)}')\n\n\n# %% [code]\n# evaluate the model with k value = 9 using the test data\nknn = KNeighborsClassifier(n_neighbors=9)\nknn.fit(X_train, y_train)\ny_pred = knn.predict(X_test)\n\n# calculate the accuracy of the model using the test data\naccuracy = accuracy_score(y_test, y_pred)\n\n\nprint(f\"The accuracy of the model is: {accuracy:.2f}\")\n\n# %% [code]\n# Empty dataframe for storing results\nresults = pd.DataFrame(columns=['model', 'parameters', 'f1_weighted_score', 'duration'])\n\n# Get current time\nstart = time.time()\n\n# Instantiate the model\nmlp = MLPClassifier(max_iter=1000)\n\n# Create a parameter grid for GridSearchCV\nparam_grid = {'hidden_layer_sizes': [(512,256,128), (256,128,64), (128,64,32), (128,), (64,), (32,), (16,)],\n              'activation': ['identity', 'logistic', 'tanh', 'relu'],\n              'solver': ['lbfgs', 'sgd', 'adam'],\n              'alpha': np.arange(0.001, 0.01, 0.1)}\n\n# Instantiate the GridSearchCV object\nmlp_cv = GridSearchCV(mlp, param_grid, cv=5, scoring='f1_weighted', verbose=1, n_jobs=-1)\n\n# Fit the model\nmlp_cv.fit(X_train, y_train)\n\n# Get the end time\nend = time.time()\n\n# Print the best parameters found\nprint(f'The best parameters are: {mlp_cv.best_params_}')\n\n# Print the f1_score for the the model\nprint(f'The f1_score for the model is: {mlp_cv.best_score_}')\n\n# Add the results to the results data frame\nresults = results._append({'model': 'mlp', 'parameters': mlp_cv.best_params_, 'f1_weighted_score': mlp_cv.best_score_, 'duration':end-start}, ignore_index=True)\n\nresults",
            "metadata": {
                "_uuid": "5b09cb14-64af-4fb7-a040-e2603d45d391",
                "_cell_guid": "2609f7b9-3848-42b8-928a-eab8426cfe66",
                "trusted": true,
                "collapsed": false,
                "jupyter": {"outputs_hidden": false},
            },
            "outputs": [],
            "execution_count": null,
        }
    ],
}
