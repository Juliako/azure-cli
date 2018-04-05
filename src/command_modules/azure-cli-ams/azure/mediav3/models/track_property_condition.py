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


class TrackPropertyCondition(Model):
    """Class to specify one track property condition.

    :param property: Track property type. Possible values include: 'Unknown',
     'FourCC'
    :type property: str or ~encoding.models.TrackPropertyType
    :param operation: Track property condition operation. Possible values
     include: 'Unknown', 'Equal'
    :type operation: str or ~encoding.models.TrackPropertyCompareOperation
    :param value: Track proprty value
    :type value: str
    """

    _validation = {
        'property': {'required': True},
        'operation': {'required': True},
    }

    _attribute_map = {
        'property': {'key': 'property', 'type': 'TrackPropertyType'},
        'operation': {'key': 'operation', 'type': 'TrackPropertyCompareOperation'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, property, operation, value=None):
        super(TrackPropertyCondition, self).__init__()
        self.property = property
        self.operation = operation
        self.value = value