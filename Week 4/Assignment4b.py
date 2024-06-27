# Making Live predictions on IMDB reviews using LSTM
# Continue this assignment in the same notebook.

from keras.models import load_model

# TODO 7: Load the model that you saved in the previous cell using load_model() function.

# TODO 8: Load the IMDB Dataset using pandas

# TODO 9: Preprocess the data as you did in the previous assignment.

from keras_preprocessing.text import tokenizer_from_json

# TODO 10: Tokenize the data using the tokenizer_from_json() function. You may use another tokenizer if you wish.

# TODO 11: Pad the data using the pad_sequences() function.

# TODO 12: Make predictions on the data using the model.predict() function.

# TODO 13: For each review, if the prediction is stored in variable, 'prediction', then np.round(prediction*10,1) will give you the predicted rating
# Store this back to csv and compare the predicted ratings with the actual ratings.