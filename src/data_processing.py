import pandas as pd

def load_clean_data(path: str) -> pd.DataFrame:
    # Load the dataset
    df = pd.read_csv(path)

    # Example cleaning steps
    df.dropna(inplace=True)  # Remove missing values
    df.drop_duplicates(inplace=True)  # Remove duplicate rows

    # Additional cleaning steps can be added here
    # Encoding categorical Values 
    # Nominal: Gender, Workout_type, meal_type, diet_type, cooking_method
    # Ordinal: Difficulty Level, Burns_Calories_Bin

    nominal_cols = ['Gender', 'Workout_Type', 'meal_type', 'diet_type', 'cooking_method']
    ordinal_difficulty = ['Difficulty Level']
    ordinal_burns = ['Burns_Calories_Bin']

    order_difficulty = [['Beginner', 'Intermediate', 'Advanced']]
    order_burns_cal = [['Low', 'Medium', 'High', 'Very High']]

    preprocessor = ColumnTransformer(
        transformers=[
            ('nominal', OneHotEncoder(drop='first'), nominal_cols),
            ('ordinal_difficulty', OrdinalEncoder(categories=order_difficulty), ordinal_difficulty),
            ('ordinal_burns', OrdinalEncoder(categories=order_burns_cal), ordinal_burns)
        ],
        remainder='passthrough'
    )

    df_encoded = pd.DataFrame(
        preprocessor.fit_transform(df_raw),
        columns=preprocessor.get_feature_names_out()
    )
    return df_encoded

