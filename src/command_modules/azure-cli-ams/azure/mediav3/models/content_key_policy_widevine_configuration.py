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

from .content_key_policy_configuration import ContentKeyPolicyConfiguration


class ContentKeyPolicyWidevineConfiguration(ContentKeyPolicyConfiguration):
    """Specifies a configuration for Widevine licenses.

    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param widevine_template: The Widevine template.
    :type widevine_template: str
    """

    _validation = {
        'odatatype': {'required': True},
        'widevine_template': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'widevine_template': {'key': 'widevineTemplate', 'type': 'str'},
    }

    def __init__(self, widevine_template):
        super(ContentKeyPolicyWidevineConfiguration, self).__init__()
        self.widevine_template = widevine_template
        self.odatatype = '#Microsoft.Media.ContentKeyPolicyWidevineConfiguration'
