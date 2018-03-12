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


class Transform(Model):
    """A Media Transform that can be applied to an input by creating Jobs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The resource name.
    :vartype name: str
    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: Optional resource tags.
    :type tags: object
    :ivar created: The date and time when the Transform was created.
    :vartype created: datetime
    :param description: Customer supplied description of the transform.
    :type description: str
    :ivar last_modified: The date and time when the Transform was last
     updated.
    :vartype last_modified: datetime
    :param outputs: The outputs for the Transform.
    :type outputs: list[~encoding.models.TransformOutput]
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
        'outputs': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
        'outputs': {'key': 'properties.outputs', 'type': '[TransformOutput]'},
    }

    def __init__(self, outputs, location=None, tags=None, description=None):
        super(Transform, self).__init__()
        self.name = None
        self.id = None
        self.type = None
        self.location = location
        self.tags = tags
        self.created = None
        self.description = description
        self.last_modified = None
        self.outputs = outputs
