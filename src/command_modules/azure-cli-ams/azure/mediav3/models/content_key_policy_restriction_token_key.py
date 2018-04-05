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


class ContentKeyPolicyRestrictionTokenKey(Model):
    """Base class for Content Key Policy key for token validation. A derived class
    must be used to create a token key.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ContentKeyPolicySymmetricTokenKey,
    ContentKeyPolicyRsaTokenKey, ContentKeyPolicyX509CertificateTokenKey

    :param odatatype: Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.ContentKeyPolicySymmetricTokenKey': 'ContentKeyPolicySymmetricTokenKey', '#Microsoft.Media.ContentKeyPolicyRsaTokenKey': 'ContentKeyPolicyRsaTokenKey', '#Microsoft.Media.ContentKeyPolicyX509CertificateTokenKey': 'ContentKeyPolicyX509CertificateTokenKey'}
    }

    def __init__(self):
        super(ContentKeyPolicyRestrictionTokenKey, self).__init__()
        self.odatatype = None
