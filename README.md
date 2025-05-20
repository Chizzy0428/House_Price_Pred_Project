# House_Price_Pred_Project
Predicting the price of house based on different inputs

Here's a beginner-friendly `README.md` file for your **House Price Prediction with Streamlit** project:


#  House Price Prediction App

This is a beginner-friendly end-to-end machine learning project that predicts house prices based on various features such as area, number of bedrooms, presence of a basement, guestroom, and more. It includes:

- Data preprocessing in Jupyter Notebook  
- A linear regression model using scikit-learn  
- A deployed interactive web app using **Streamlit**



##  Project Structure

```
house_pred/
│
├── app.py                 # Streamlit app
├── model.pkl              # Trained linear regression model
├── Housing.csv               # Dataset 
├── house_price_mini_project.ipynb      # Jupyter notebook for EDA & training
├── requirements.txt       # List of dependencies
└── README.md              # Project info


##  Features Used in Model

* `price`: Target variable (what we're predicting)
* `area`: Square feet
* `bedrooms`: Number of bedrooms
* `bathrooms`: Number of bathrooms
* `stories`: Number of stories
* `mainroad`: Is the house on a main road? (yes/no)
* `guestroom`: Has a guestroom? (yes/no)
* `basement`: Has a basement? (yes/no)
* `hotwaterheating`: Has hot water heating? (yes/no)
* `airconditioning`: Has air conditioning? (yes/no)
* `parking`: Number of parking spaces
* `prefarea`: Located in a preferred area? (yes/no)

All categorical variables were converted to binary using `yes → 1` and `no → 0`.



##  ML Model

* **Model Used**: Linear Regression
* **Library**: `scikit-learn`
* The model was trained in `house_price_mini_project.ipynb` and saved as `model.pkl` using `pickle`.



## ⚙Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/house_pred.git
cd house_pred
```

### 2. Create virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can manually install:

```bash
pip install numpy pandas scikit-learn streamlit
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


