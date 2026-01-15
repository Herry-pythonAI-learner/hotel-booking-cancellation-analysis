
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.compose import ColumnTransformer 
from sklearn.linear_model import LogisticRegression

def booking_predictor(numeric_features, categorical_features):
    """
    A model that can predict the cancellation status(Cancel or not)
     of hotel booking based on the various features of the booking.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), categorical_features)
                  ])

    model = Pipeline(steps=[
                 ('preprocessor', preprocessor),
                 ('classifier', LogisticRegression())
        ])
    
    return model