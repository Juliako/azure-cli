# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationDisplay(Model):
    """Operation display properties.

    :param provider: The service provider.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: The operation type.
    :type operation: str
    :param description: The operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, provider=None, resource=None, operation=None, description=None):
        super(OperationDisplay, self).__init__()
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description
