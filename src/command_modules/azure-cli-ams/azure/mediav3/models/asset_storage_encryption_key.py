# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AssetStorageEncryptionKey(Model):
    """The Asset storage encryption key.

    :param storage_encryption_key: The Asset storage encryption key.
    :type storage_encryption_key: str
    """

    _attribute_map = {
        'storage_encryption_key': {'key': 'storageEncryptionKey', 'type': 'str'},
    }

    def __init__(self, storage_encryption_key=None):
        super(AssetStorageEncryptionKey, self).__init__()
        self.storage_encryption_key = storage_encryption_key