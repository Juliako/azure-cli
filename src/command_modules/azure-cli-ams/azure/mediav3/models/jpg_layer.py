# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .layer import Layer


class JpgLayer(Layer):
    """This represents a layer in the JpgImage class.

    :param width: Gets or sets width of video in pixels for this layer.
    :type width: str
    :param height: Gets or sets height of video in pixels for this layer.
    :type height: str
    :param condition: Gets or sets the predicate to be evaluated before
     encoding this layer.
    :type condition: str
    :param label: Gets or sets the label for this layer.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param quality: Gets or sets the compression quality of the JPEG output.
     Range is from 0-100 and the default is 70.
    :type quality: int
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'width': {'key': 'width', 'type': 'str'},
        'height': {'key': 'height', 'type': 'str'},
        'condition': {'key': 'condition', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'quality': {'key': 'quality', 'type': 'int'},
    }

    def __init__(self, width=None, height=None, condition=None, label=None, quality=None):
        super(JpgLayer, self).__init__(width=width, height=height, condition=condition, label=label)
        self.quality = quality
        self.odatatype = '#Microsoft.Media.JpgLayer'