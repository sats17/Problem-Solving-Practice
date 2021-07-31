class Response:
    __response = None

    def __init__(self):
        self.__response = dict()

    def is_valid_value(self, answer: bool, reason: str):
        if reason is None:
            self.__response['isValidValue'] = {
                'answer': answer
            }
        else:
            self.__response['isValidValue'] = {
                'answer': answer,
                'reason': reason
            }
        return self

    def is_valid_index(self, answer: bool, reason: str):
        if reason is None:
            self.__response['isValidIndex'] = {
                'answer': answer
            }
        else:
            self.__response['isValidIndex'] = {
                'answer': answer,
                'reason': reason
            }
        return self

    def build(self):
        return self.__response
