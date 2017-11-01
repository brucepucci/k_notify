from keras.callbacks import Callback


class BaseNotificationCallback(Callback):
    def __init__(self, epoch_freq=3):
        self.epoch_freq = epoch_freq

    def on_train_begin(self, logs=None):
        self.seen = 0

    def on_train_end(self, logs={}):
        self.send(f'Training completed for {self.model.name}')

    def on_epoch_end(self, epoch, logs={}):
        self.seen += 1
        if self.seen % self.epoch_freq == 0:
            self.send(self.epoch_message(logs))

    def send(self, logs):
        raise NotImplementedError

    def epoch_message(self, logs):
        message = [f'Training results for {self.model.name}',
                   f'    Epochs complete: {self.seen}']
        for k, v in logs.items():
            message.append(f'    {k}: {v:.5f}')
        return '\n'.join(message)
