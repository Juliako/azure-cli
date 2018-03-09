# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AvailablePresets(Model):
    """The response message for available presets.

    :param presets: Lists the available presets
    :type presets: list[str]
    """

    _attribute_map = {
        'presets': {'key': 'presets', 'type': '[str]'},
    }

    def __init__(self, presets=None):
        super(AvailablePresets, self).__init__()
        self.presets = presets