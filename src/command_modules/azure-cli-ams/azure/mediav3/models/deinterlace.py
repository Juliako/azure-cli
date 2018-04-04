# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Deinterlace(Model):
    """A class to define de-interlacing settings.

    :param parity: Gets or sets the parity to use. Possible values include:
     'Auto', 'TopFieldFirst', 'BottomFieldFirst'
    :type parity: str or ~encoding.models.DeinterlaceParity
    :param mode: Gets or sets the deinterlace Mode. Possible values include:
     'Off', 'AutoPixelAdaptive'
    :type mode: str or ~encoding.models.DeinterlaceMode
    """

    _attribute_map = {
        'parity': {'key': 'parity', 'type': 'DeinterlaceParity'},
        'mode': {'key': 'mode', 'type': 'DeinterlaceMode'},
    }

    def __init__(self, parity=None, mode=None):
        super(Deinterlace, self).__init__()
        self.parity = parity
        self.mode = mode
