# Richter's Predictor: Modeling Earthquake Damage

## Overview

This repository hosts the code and resources for the Nepal 2015 Earthquake building damage predictor, a part of the DrivenData Competitions. The project aims to predict the level of damage to buildings caused by the 2015 Gorkha earthquake in Nepal based on aspects like building structure and location. This model is an essential tool for disaster management and helps in prioritizing aid and reconstruction efforts.

[Here's a link to the "Richter's Predictor: Modeling Earthquake Damage" competition](https://www.drivendata.org/competitions/57/nepal-earthquake/)

## Repository Structure

- **Jupyter Notebooks:** Each notebook (`Nepal-Earthquake-predictor-*.ipynb`) corresponds to a specific machine learning model, detailing the data processing, model training, evaluation, and prediction stages.
- **Feature Importance Visuals:** Visual representations (`Feature_importance_Pictures/`) of feature importance derived from different models.
- **Hyperparameters:** JSON files (`Hyperparameters/`) containing the hyperparameters used for tuning each model.
- **Model Summaries:** Text summaries (`Model_Summary/`) describing the configuration and performance of each model.
- **Model Visuals:** Images (`Model_Visuals/`) showcasing model architectures and performances.
- **Optuna Logs:** Log files (`Optuna_Logs/`) documenting the hyperparameter tuning process using Optuna.
- **Saved Models:** Serialized models (`Saved_Models/`) that can be loaded for prediction or further training.
- **Submissions:** Submission files (`Submissions/`) containing the predicted damage levels for the competition.
- **Utility Scripts:** Additional scripts like `label_analysis.py` for data analysis and preprocessing.

## Models

- **Light Gradient Boosting Machine (LGBM):** Utilizes gradient boosting frameworks for efficient and accurate predictions.
- **Neural Networks:** Harnesses TensorFlow to build and train deep learning models.
- **TensorFlow Decision Forests (TFDF):** A novel approach using decision forests with TensorFlow.
- **XGBoost:** Implements an optimized distributed gradient boosting library.

## Getting Started

1. **Clone the Repository:** `git clone https://github.com/23yem/Richter-s-Predictor-Modeling-Earthquake-Damage.git`
2. **Install Dependencies:** Ensure you have Python and necessary libraries (pandas, numpy, scikit-learn, TensorFlow, etc.) installed.
3. **Explore Notebooks:** Start with the Jupyter notebooks to understand the workflow for each model.
4. **Load Models:** Use the saved models for quick evaluations or predictions.
5. **Experiment and Extend:** Modify the models, tune hyperparameters, or use different datasets for further exploration.

## Contributing

Contributions to improve the models or extend the functionality of this repository are welcome. Please adhere to the following steps for contributions:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear, descriptive messages.
4. Push to the branch and open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to DrivenData for hosting the competition and providing the dataset. Appreciation goes to all contributors and researchers in the field of disaster management and machine learning.
