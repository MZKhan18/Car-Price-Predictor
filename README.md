# Car Price Estimation

This is a web application that estimates the price of a car based on various features. It uses a machine learning model trained on a dataset of car listings. The model predicts the price based on factors such as the car's company, model, variant, kilometers driven, transmission type, manufacture year, engine specifications, number of seats, fuel type, and previous ownership.

## Demo

To try out the car price estimation, you can visit https://car-price-predictor-l4dx.onrender.com

## How it Works

1. **Car Selection**: You can choose the car's company, model, and variant from the available options.
2. **Kilometers Driven**: Enter the number of kilometers driven by the car.
3. **Transmission**: Select the transmission type (Automatic or Manual) of the car.
4. **Manufacture Year**: Enter the year in which the car was manufactured.
5. **Engine Specifications**: Provide details about the car's engine.
6. **Number of Seats**: Select the number of seats in the car.
7. **Fuel Type**: Choose the fuel type used by the car.
8. **Previous Ownership**: Select the number of previous owners the car has had.

After entering all the necessary information, click the "Predict Price" button to get the estimated price of the car.

## Technologies Used

The following technologies were used to develop this car price estimation application:

- Streamlit: A Python library for building interactive web applications.
- Python: The programming language used for the application's backend.
- Pandas: A data manipulation library used for data analysis and cleaning.
- Scikit-learn: A machine learning library used for training the model.
- Random Forest Algorithm: The machine learning algorithm used to make price predictions.

## Dataset

The car price estimation model was trained on a carefully curated dataset of car listings. The dataset includes information about various car features, such as the company, model, variant, kilometers driven, transmission type, manufacture year, engine specifications, number of seats, fuel type, and previous ownership. The dataset was thoroughly analyzed and cleaned before training the model to ensure accurate predictions.

## Model Training

The Random Forest algorithm was chosen for training the car price estimation model. This algorithm is well-suited for regression tasks and can handle both numerical and categorical features effectively. The model was trained on the cleaned dataset, taking into account various car features as input and the corresponding price as the output. After training, the model was serialized and saved for future use.

## How to Run the Application Locally

To run the car price estimation application on your local machine, follow these steps:

1. Clone the GitHub repository: [link_to_github_repo].
2. Install the required dependencies listed in the `requirements.txt` file.
3. Ensure that you have the necessary data files, including `pipe.pkl` and `df.pkl`.
4. Run the Streamlit application by executing the command: `streamlit run app.py`.
5. Access the application in your web browser at `http://localhost:8501`.

Feel free to explore the code and make any necessary modifications to suit your needs.

## Future Improvements

Here are some potential improvements that can be made to enhance the car price estimation application:

1. Include more advanced machine learning algorithms and compare their performance.
2. Allow users to upload images of the car for more accurate price predictions.
3. Implement a feature to compare estimated prices across different car models and variants.
4. Provide additional insights and visualizations based on the dataset analysis.

Contributions and feedback are welcome!
