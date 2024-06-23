'''
Use this as a reference and continue on last week's notebook.
Use separate cells as per your requirement. Do this wisely!
'''

# Training the model with LSTMs

from keras.layers import LSTM

# TODO 1: Create a model. How many layers to use? What all layers to use? Try figuring out!

# TODO 2: Compile the model with the appropriate loss function and optimizer. 
# You may use the 'adam' optimizer and 'binary_crossentropy' as the loss function. Use metrics=['acc'].
# (Optional) Try printing the model summary to see the model 

# TODO 3: Train the model with the training data. 
# Try using different batch sizes and number of epochs to see how the model performs.

# TODO 4: Evaluate the model with the test data.

# TODO 5: Print the accuracy of the model.

# (Optional) Try plotting the training and validation accuracy and loss to see how the model performs. 
# Given below is a sample code for this, but the variables are not defined for your undersatnding. Use it as a reference.
'''
import matplotlib.pyplot as plt

plt.plot(history.history['acc'])    # history is the variable that stores the training history of the model
plt.plot(history.history['val_acc'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
'''

# TODO 6: Save the model so that it can be used later for prediction.

# (Optional) Try tuning different hyperparameters to see how the model performs, and try to reach a higher accuracy. 
# You can also try using different layers and units to see how the model performs.
# Your model will be graded based on the accuracy of the model.