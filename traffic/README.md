# My experimentation process for CS50 AI traffic assignment

## Initial setup
- Convolutional Layer -> Pooling Layer -> Flatten -> Hidden Layer -> Output
- For the convolutional layer, I chose 32 filters and kernel size of 3x3 for the filter
- For the pooling layer, I chose 2x2 max pooling 
- For the hidden layer, I chose 128 neurons as the size using the rule 2/3 * (input + output) units

### Results
- The accuracy was pretty terrible
```sh
Epoch 1/10
2022-01-06 16:00:29.566693: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8202
500/500 [==============================] - 3s 3ms/step - loss: 4.7086 - accuracy: 0.0534
Epoch 2/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5885 - accuracy: 0.0566
Epoch 3/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5402 - accuracy: 0.0572
Epoch 4/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5180 - accuracy: 0.0572
Epoch 5/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5078 - accuracy: 0.0572
Epoch 6/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5031 - accuracy: 0.0567
Epoch 7/10
500/500 [==============================] - 1s 3ms/step - loss: 3.5008 - accuracy: 0.0572
Epoch 8/10
500/500 [==============================] - 1s 3ms/step - loss: 3.4997 - accuracy: 0.0572
Epoch 9/10
500/500 [==============================] - 1s 3ms/step - loss: 3.4991 - accuracy: 0.0561
Epoch 10/10
500/500 [==============================] - 1s 3ms/step - loss: 3.4988 - accuracy: 0.0572
333/333 - 0s - loss: 3.4980 - accuracy: 0.0549 - 487ms/epoch - 1ms/step
```

## Increasing the number of convolutional layers
- I tried to play around with different number of convolutional layers as well as the parameters for the pooling

### Results
- I found that 2 convolutional layers and pooling seems to be the sweet spot, after which , the accuracy would start to decline
- I also found out that average pooling seems to work significantly better than max pooling (97% compared to 92% for 2 CNN layers)
```sh
Epoch 1/10
2022-01-06 16:04:25.117657: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8202
500/500 [==============================] - 4s 3ms/step - loss: 3.3509 - accuracy: 0.3677
Epoch 2/10
500/500 [==============================] - 2s 3ms/step - loss: 1.1399 - accuracy: 0.6678
Epoch 3/10
500/500 [==============================] - 2s 3ms/step - loss: 0.7057 - accuracy: 0.7915
Epoch 4/10
500/500 [==============================] - 2s 3ms/step - loss: 0.5031 - accuracy: 0.8524
Epoch 5/10
500/500 [==============================] - 2s 3ms/step - loss: 0.4110 - accuracy: 0.8788
Epoch 6/10
500/500 [==============================] - 2s 3ms/step - loss: 0.3312 - accuracy: 0.9010
Epoch 7/10
500/500 [==============================] - 2s 3ms/step - loss: 0.3004 - accuracy: 0.9108
Epoch 8/10
500/500 [==============================] - 2s 3ms/step - loss: 0.2640 - accuracy: 0.9228
Epoch 9/10
500/500 [==============================] - 2s 3ms/step - loss: 0.2403 - accuracy: 0.9295
Epoch 10/10
500/500 [==============================] - 2s 3ms/step - loss: 0.2328 - accuracy: 0.9331
333/333 - 1s - loss: 0.1199 - accuracy: 0.9702 - 579ms/epoch - 2ms/step
```

## Increasing the number of hidden layers
- Finally I tried to increase the number of hidden layers in the model

### Results
- I found that having 2 hidden layers increased the accuracy slightly but after which, any increase in hidden layers yielded little to no improvements
```sh
Epoch 1/10
2022-01-06 16:06:26.507140: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8202
500/500 [==============================] - 4s 4ms/step - loss: 2.4173 - accuracy: 0.4032
Epoch 2/10
500/500 [==============================] - 2s 3ms/step - loss: 0.8662 - accuracy: 0.7433
Epoch 3/10
500/500 [==============================] - 2s 3ms/step - loss: 0.4760 - accuracy: 0.8591
Epoch 4/10
500/500 [==============================] - 2s 3ms/step - loss: 0.3269 - accuracy: 0.9046
Epoch 5/10
500/500 [==============================] - 2s 3ms/step - loss: 0.2344 - accuracy: 0.9298
Epoch 6/10
500/500 [==============================] - 2s 3ms/step - loss: 0.2024 - accuracy: 0.9426
Epoch 7/10
500/500 [==============================] - 2s 3ms/step - loss: 0.1721 - accuracy: 0.9493
Epoch 8/10
500/500 [==============================] - 2s 3ms/step - loss: 0.1459 - accuracy: 0.9595
Epoch 9/10
500/500 [==============================] - 2s 3ms/step - loss: 0.1129 - accuracy: 0.9661
Epoch 10/10
500/500 [==============================] - 2s 3ms/step - loss: 0.1036 - accuracy: 0.9713
333/333 - 1s - loss: 0.0914 - accuracy: 0.9778 - 596ms/epoch - 2ms/step
```

## Conclusion
- Having more layers in the neural network does not necessarily yield better results as it would run into the risk of overfitting