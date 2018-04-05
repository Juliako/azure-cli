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


class StreamingLocatorContentKey(Model):
    """Class for content key in Streaming Locator.

    :param label: Label of Content Key
    :type label: str
    :param type: Encryption type of Content Key. Possible values include:
     'CommonEncryptionCenc', 'CommonEncryptionCbcs', 'EnvelopeEncryption'
    :type type: str or ~encoding.models.StreamingLocatorContentKeyType
    :param id: ID of Content Key
    :type id: str
    :param value: Value of  of Content Key
    :type value: str
    :param policy_name: ContentKeyPolicy used by Content Key
    :type policy_name: str
    :param tracks: Tracks which use this Content Key
    :type tracks: list[~encoding.models.TrackSelection]
    """

    _validation = {
        'type': {'required': True},
        'id': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'type': {'key': 'type', 'type': 'StreamingLocatorContentKeyType'},
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
        'tracks': {'key': 'tracks', 'type': '[TrackSelection]'},
    }

    def __init__(self, type, id, label=None, value=None, policy_name=None, tracks=None):
        super(StreamingLocatorContentKey, self).__init__()
        self.label = label
        self.type = type
        self.id = id
        self.value = value
        self.policy_name = policy_name
        self.tracks = tracks