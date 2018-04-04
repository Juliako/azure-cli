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


class LiveEventPreviewAccessControl(Model):
    """The IP access control for Live Event preview.

    :param ip: The IP access control properties.
    :type ip: ~encoding.models.IPAccessControl
    """

    _attribute_map = {
        'ip': {'key': 'ip', 'type': 'IPAccessControl'},
    }

    def __init__(self, ip=None):
        super(LiveEventPreviewAccessControl, self).__init__()
        self.ip = ip
