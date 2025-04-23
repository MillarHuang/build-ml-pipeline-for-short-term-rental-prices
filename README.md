# Background of project:
## Build an ML Pipeline for Short-Term Rental Prices in NYC
The dataset is from a property management company renting rooms and properties for short periods of 
time on various rental platforms. This project is to build an end-to-end pipeline to estimate the typical price for a given property based 
on the price of similar properties, and enable retraining easily.

### Supported Operating Systems

This project is compatible with the following operating systems:

- **Ubuntu 22.04** (Jammy Jellyfish) - both Ubuntu installation and WSL (Windows Subsystem for Linux)
- **Ubuntu 24.04** - both Ubuntu installation and WSL (Windows Subsystem for Linux)
- **macOS** - compatible with recent macOS versions

### Python Requirement

This project requires **Python 3.10**. Please ensure that you have Python 3.10 installed and set as the default version in your environment to avoid any runtime issues.

### Get API key for Weights and Biases
Make sure to be logged in to Weights & Biases. Get your API key from W&B by going to 
[https://wandb.ai/authorize](https://wandb.ai/authorize) and click on the + icon (copy to clipboard), 
then paste your key into this command:

```bash
> wandb login [your API key]
```

You should see a message similar to:
```
wandb: Appending key for api.wandb.ai to your netrc file: /home/[your username]/.netrc
```

## Instruction:

### Set up environment:
Make sure to have conda installed and ready, then create a new environment using the ``environment.yml``
file provided in the root of the repository and activate it:

```bash
> conda env create -f environment.yml
> conda activate nyc_airbnb_dev
```

### 1.Download data: download data and upload it to W&B
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=download
```
### 2.Basic Cleaning: clean the dataset and load the cleaned dataset to W&B
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=basic_cleaning
```
### 3.Data checking: perform tests on the cleaned dataset to validate it
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=data_check
```
### 4.Data split: split dataset into training_validation set and test set, and upload them to W&B
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=data_split \
```
### 5.Training: train a random forest model and upload the inference artifact and its performance metrics to W&B
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=train_random_forest
```
### 6.Optimize model performance by performing grid search(on parameters: max_tfidf_features, random_forest.max_features)
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=train_random_forest \
             -P hydra_options="modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m"
```
### 7.Testing: test the optimized well-trained model performance on test set and upload the performance metric to W&B
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P steps=test_regression_model
```
## Implement the whole MLpipeline
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1
```
## Train the model on a new data sample
```
mlflow run https://github.com/MillarHuang/build-ml-pipeline-for-short-term-rental-prices.git \
             -v 1.0.1 \
             -P hydra_options="etl.sample='sample2.csv'"
```

# Weights&Bias link (results of pre-built pipeline):
https://wandb.ai/zhiconghuang-non/nyc_airbnb?nw=nwuserzhiconghuang
