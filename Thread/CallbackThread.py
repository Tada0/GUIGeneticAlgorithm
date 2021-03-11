from threading import Thread


class CallbackThread(Thread):
    def __init__(self, callback, daemon, callback_args=None, add_result_to_callback=False, *args, **kwargs):
        target = kwargs.pop('target')
        super(CallbackThread, self).__init__(target=self.__target, daemon=daemon, *args, **kwargs)
        self.__callback = callback
        self.__method = target
        self.__callback_args = callback_args
        self.__add_result_to_callback = add_result_to_callback

    def __target(self):
        result = self.__method()
        callback_data = (self.__callback_args + (result,)) if self.__add_result_to_callback else self.__callback_args
        self.__callback(*callback_data)
