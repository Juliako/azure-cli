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


class ContentKeyPolicyProperties(Model):
    """The properties of the Content Key Policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar policy_id: The legacy Policy ID.
    :vartype policy_id: str
    :ivar created: The creation date of the Policy
    :vartype created: datetime
    :ivar last_modified: The last modified date of the Policy
    :vartype last_modified: datetime
    :param description: A description for the Policy.
    :type description: str
    :param options: The Key Policy options.
    :type options: list[~encoding.models.ContentKeyPolicyOption]
    """

    _validation = {
        'policy_id': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
        'options': {'required': True},
    }

    _attribute_map = {
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'options': {'key': 'options', 'type': '[ContentKeyPolicyOption]'},
    }

    def __init__(self, options, description=None):
        super(ContentKeyPolicyProperties, self).__init__()
        self.policy_id = None
        self.created = None
        self.last_modified = None
        self.description = description
        self.options = options
