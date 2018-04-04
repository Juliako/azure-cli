# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .codec import Codec


class CopyAudio(Codec):
    """An object to represent an audio copy codec.

    :param label: Gets or sets the codec label.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    def __init__(self, label=None):
        super(CopyAudio, self).__init__(label=label)
        self.odatatype = '#Microsoft.Media.CopyAudio'
