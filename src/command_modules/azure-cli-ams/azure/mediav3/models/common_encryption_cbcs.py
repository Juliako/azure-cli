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


class CommonEncryptionCbcs(Model):
    """Class for CommonEncryptionCbcs encryption scheme.

    :param enabled_protocols: Representing supported protocols
    :type enabled_protocols: ~encoding.models.EnabledProtocols
    :param clear_tracks: Representing which tracks should not be encrypted
    :type clear_tracks: list[~encoding.models.TrackSelection]
    :param content_keys: Representing default content key for each encryption
     scheme and separate content keys for specific tracks
    :type content_keys: ~encoding.models.StreamingPolicyContentKeys
    :param drm: Configuration of DRMs for current encryption scheme
    :type drm: ~encoding.models.CbcsDrmConfiguration
    """

    _attribute_map = {
        'enabled_protocols': {'key': 'enabledProtocols', 'type': 'EnabledProtocols'},
        'clear_tracks': {'key': 'clearTracks', 'type': '[TrackSelection]'},
        'content_keys': {'key': 'contentKeys', 'type': 'StreamingPolicyContentKeys'},
        'drm': {'key': 'drm', 'type': 'CbcsDrmConfiguration'},
    }

    def __init__(self, enabled_protocols=None, clear_tracks=None, content_keys=None, drm=None):
        super(CommonEncryptionCbcs, self).__init__()
        self.enabled_protocols = enabled_protocols
        self.clear_tracks = clear_tracks
        self.content_keys = content_keys
        self.drm = drm
