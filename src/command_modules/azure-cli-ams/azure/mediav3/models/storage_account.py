# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageAccount(Model):
    """Storage account properties.

    :param id: The ID of the storage account resource. Media Services relies
     on tables and queues as well as blobs, so the primary storage account must
     be a Standard Storage account (either Microsoft.ClassicStorage or
     Microsoft.Storage). Blob only storage accounts can be added as secondary
     storage accounts.
    :type id: str
    :param type: The type of the storage account. Possible values include:
     'Primary', 'Secondary'
    :type type: str or ~encoding.models.StorageAccountType
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'StorageAccountType'},
    }

    def __init__(self, type, id=None):
        super(StorageAccount, self).__init__()
        self.id = id
        self.type = type
