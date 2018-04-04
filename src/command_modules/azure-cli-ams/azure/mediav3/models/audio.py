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

from .codec import Codec


class Audio(Codec):
    """Default base class for all Audio codecs.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AacAudio, DDPlusAudio

    :param label: Gets or sets the codec label.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param channels: Gets or sets number of channels in the Audio.
    :type channels: int
    :param sampling_rate: Gets or sets the sampling rate to use for encoding.
    :type sampling_rate: int
    :param bitrate: Gets or sets the bitrate of the encoded audio.
    :type bitrate: int
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'channels': {'key': 'channels', 'type': 'int'},
        'sampling_rate': {'key': 'samplingRate', 'type': 'int'},
        'bitrate': {'key': 'bitrate', 'type': 'int'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.AacAudio': 'AacAudio', '#Microsoft.Media.DDPlusAudio': 'DDPlusAudio'}
    }

    def __init__(self, label=None, channels=None, sampling_rate=None, bitrate=None):
        super(Audio, self).__init__(label=label)
        self.channels = channels
        self.sampling_rate = sampling_rate
        self.bitrate = bitrate
        self.odatatype = '#Microsoft.Media.Audio'
