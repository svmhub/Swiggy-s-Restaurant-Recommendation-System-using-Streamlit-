# Swiggy's-Restaurant-Recommendation-System-using-Streamlit-
The objective is to build a recommendation system based on restaurant data provided. The system should recommend restaurants to users based on input features such as city, rating, cost, and cuisine preferences. The application will utilize clustering or similarity measures to generate recommendations and display results in an Streamlit Application.

By the end of this project, you will:
* Perform data cleaning and preprocessing.
* Encode categorical features using One-Hot Encoding.
* Apply clustering or similarity-based methods for recommendations.
* Build a Streamlit application to showcase recommendations.

## Business Use Cases:
* Personalized Recommendations: Help users discover restaurants based on their preferences.
* Improved Customer Experience: Provide tailored suggestions to enhance decision-making.
* Market Insights: Understand customer preferences and behaviors for targeted marketing.
* Operational Efficiency: Enable businesses to optimize their offerings based on popular preferences.

## Approach:
The dataset is provided as a CSV file with the following columns:
['id', 'name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'lic_no', 'link', 'address', 'menu']   
***Categorical: name, city, cuisine   
Numerical: rating, rating_count, cost***
1. Data Understanding and Cleaning
  * Duplicate Removal: Identify and drop duplicate rows.
  * Handling Missing Values: Impute or drop rows with missing values.
  * Saved the cleaned data to a new CSV file (cleaned_data.csv).
2. Data Preprocessing
  * Encoding: Apply One-Hot Encoding to categorical features ( city, cuisine).
  * Save the encoder as a Pickle file (encoder.pkl) for the application and future use.
  * Ensure all features are numerical after encoding.
  * Created a preprocessed dataset in a file(encoded_data.csv).
  * Ensure the indices of cleaned_data.csv and encoded_data.csv match.
3. Recommendation Methodology
 * Used the Cosine Similarity to identify similar restaurants based on input features as the dataset contains the binary values more.
 * Use the encoded dataset for computations.
 * Result Mapping:
 * Map the recommendation results (indices) back to the non-encoded dataset (cleaned_data.csv).
4. Streamlit Application
 * Builded an interactive application(Swiggy_Restaurant_Recommandation_app.py with the following components:
 * User Input: Accept user preferences (e.g., city, cuisine, rating,price,etc).
 * Recommendation Engine: Process the input, query the encoded data, and generate recommendations.
 * Output: Displayed recommended restaurants using cleaned_data.csv.

***Note: I have a file(Model_Preparation_and_Building.ipynb) in the repository. Kindly go through that file to how I have addressed this recommendation model***
