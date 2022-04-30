
import tensorflow as tf


class ModelTrainer:


    def get_model(self,encoder):
        model = tf.keras.Sequential([
                encoder,
                tf.keras.layers.Embedding(len(encoder.get_vocabulary()), 64, mask_zero=True),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(1)    
                ])
        return model

        
