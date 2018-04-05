# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AkamaiSignatureHeaderAuthenticationKey(Model):
    """Akamai Signature Header authentication key.

    :param identifier: identifier of the key
    :type identifier: str
    :param base64_key: authentication key
    :type base64_key: str
    :param expiration: The exact time the authentication key.
    :type expiration: datetime
    """

    _attribute_map = {
        'identifier': {'key': 'identifier', 'type': 'str'},
        'base64_key': {'key': 'base64Key', 'type': 'str'},
        'expiration': {'key': 'expiration', 'type': 'iso-8601'},
    }

    def __init__(self, identifier=None, base64_key=None, expiration=None):
        super(AkamaiSignatureHeaderAuthenticationKey, self).__init__()
        self.identifier = identifier
        self.base64_key = base64_key
        self.expiration = expiration