# Bagel-Sales-Predictive-Analytics

### Description

The objective of this project was to illustrate to a bagel shop business owner the strategic advantages of leveraging data for enhanced productivity. Given the absence of existing data collection methods, I created a simulated dataset reflecting perceived trends observed by the owner over the past two years of operation. Initially, the owner highlighted significant variations in sales corresponding to seasonal changes. To address this, I incorporated average monthly high and low temperatures for Nederland, Colorado, randomly selecting temperatures within that range, with a slight chance of deviation. Furthermore, recognizing the importance of holiday rushes, I integrated holiday data into the dataset. The owner also provided monthly sales range estimates, from which I randomly selected figures for each month. Notably, the owner emphasized that weekend traffic was twice as high as on weekdays. Additionally, the owner requested the inclusion of daily sales figures for each type/flavor of bagel sold. This particular data point enabled the manager to identify popular flavors and adjust production accordingly to prevent stock shortages. Subsequently, within the "Data Investigator" Python notebook file, I demonstrated to the owner methods for charting the data and making predictions on the best ways to forecast the dataset.

During my analysis of the bagel sales, I found several significant trends. Notably, over 36% of all bagels sold were Everything, followed by 24% Salt, and approximately 16-17% for Plain and Sesame, with Cinnamon accounting for 5%. Temperature exhibited a strong correlation with bagel sales, with coefficients of 0.72 for weekends and 0.70 for weekdays. Additionally, the previous day's sales showed robust correlations, with coefficients of 0.74 for weekends and 0.72 for weekdays. Regarding predictive modeling, the best linear regression model, leveraging features such as temperature, previous day's sales, and weekend indicators, yielded an MSE of 638.18 and an R-squared (R2) score of 0.67. The top-performing KNN model, utilizing the same features, resulted in an MSE of 1067.89 and an R2 score of 0.51, while the best decision tree model achieved an MSE of 675.12 and an R2 score of 0.65. These findings underscore the significance of temperature, previous sales, and weekend patterns in accurately predicting bagel sales, providing valuable insights for business optimization.

### Installations and Dependencies

#### Data Creator (Python File - Visual Studio Code):
- **Libraries Used:**
  - `csv`: Used for reading and writing CSV files.
  - `random`: Utilized for generating random numbers.
  - `datetime`: Imported for working with dates and times.
  - `holidays`: Used to determine holiday dates.

#### Data Investigator (Python Notebook - Jupyter Notebook):
- **Libraries Used:**
  - `pandas`: Required for data manipulation and analysis.
  - `matplotlib.pyplot`: Utilized for creating visualizations such as plots and charts.
  - `seaborn`: Used for enhancing the aesthetics of statistical graphics.
  - `numpy`: Essential for numerical computing and working with arrays.
  - `scipy.stats`: Utilized for statistical analysis, including the calculation of Pearson correlation coefficients.
  - `sklearn.model_selection`: Required for splitting the dataset into training and testing sets.
  - `sklearn.linear_model`: Necessary for implementing linear regression models.
  - `sklearn.metrics`: Utilized for evaluating the performance of machine learning models using metrics such as mean squared error and R-squared.
  - `sklearn.neighbors`: Required for implementing K-nearest neighbors regression.
  - `sklearn.tree`: Utilized for constructing decision tree-based regression models.
  
#### Additional Notes:
- Ensure that you have Python installed on your system.
- Some libraries, such as `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`, may require additional dependencies to be installed. You can install them using Python package managers like `pip`.
- It's recommended to set up a virtual environment to manage dependencies and avoid conflicts with other projects.
- Refer to the documentation of each library for installation instructions and additional information on usage.
