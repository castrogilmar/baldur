class MountingOrder(object):
    """
    Class for mouinting order that is used in the CMobile API.
    """
    def __init__(self, kwargs):
        self._kwargs = kwargs
        
    @property
    def request_data(self):
        """
        Returns the request data that is passed for api of control-mobile app.
        """
        return self._kwargs
    