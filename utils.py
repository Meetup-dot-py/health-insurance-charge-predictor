import pickle


def model_predictor(model_input: list) -> float:
    """
    This function is used to predict the insurance charge
    """
    with open("trained_model/regression.pkl", 'rb') as predictor_model:
        # Load the model
        model = pickle.load(predictor_model)
        charge = model.predict([model_input])
        return charge