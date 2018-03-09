# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .format import Format


class ImageFormat(Format):
    """Generates image file output.

    :param filename_pattern: Gets or sets the pattern of the filename to use
     excluding the extension. REVIEW: List "macros" that can be used and give
     examples.
    :type filename_pattern: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    def __init__(self, filename_pattern=None):
        super(ImageFormat, self).__init__(filename_pattern=filename_pattern)
        self.odatatype = '#Microsoft.Media.ImageFormat'