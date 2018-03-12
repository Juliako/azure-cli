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

from .preset import Preset


class BuiltInStandardEncoderPreset(Preset):
    """Preset to use Media Encoder Standard (MES) with a built in named preset.

    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param preset_name: Gets or sets the built in preset to use. Possible
     values include: 'AdaptiveStreaming', 'ContentAdaptiveMultipleBitrateMP4',
     'AACGoodQualityAudio', 'H264MultipleBitrate1080p',
     'H264MultipleBitrate720p'
    :type preset_name: str or ~encoding.models.EncoderNamedPreset
    """

    _validation = {
        'odatatype': {'required': True},
        'preset_name': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'preset_name': {'key': 'presetName', 'type': 'EncoderNamedPreset'},
    }

    def __init__(self, preset_name):
        super(BuiltInStandardEncoderPreset, self).__init__()
        self.preset_name = preset_name
        self.odatatype = '#Microsoft.Media.BuiltInStandardEncoderPreset'
