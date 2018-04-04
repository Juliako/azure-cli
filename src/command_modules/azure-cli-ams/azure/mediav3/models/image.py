# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .video import Video


class Image(Video):
    """Base class for all Image codecs.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: BmpImage, JpgImage, PngImage

    :param label: Gets or sets the codec label.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param preserve_resolution_after_rotation: Gets or sets a value indicating
     whether to disable resolution change rotation.
    :type preserve_resolution_after_rotation: bool
    :param key_frame_interval: Gets or sets the distance between two key
     frames.
    :type key_frame_interval: timedelta
    :param stretch_mode: Gets or sets the Resolution Mode. Possible values
     include: 'None', 'AutoSize', 'AutoFit'
    :type stretch_mode: str or ~encoding.models.StretchMode
    :param sync_mode: Gets or sets the Video Sync Mode. Possible values
     include: 'Auto', 'Passthrough', 'Cfr', 'Vfr', 'Drop'
    :type sync_mode: str or ~encoding.models.VideoSyncMode
    :param start: Gets or sets the start position in the input from where to
     generate the thumbnails. Can be either absolute duration (e.g: PT05S) or
     relative value (e.g: 100%) Can also be a value like {Best} to select the
     best thumbnail.
    :type start: str
    :param step: Gets or sets the step condition attribute for the thumbnails.
     Can be either absolute duration (e.g: PT05S) or relative value (e.g: 10%)
    :type step: str
    :param range: Gets or sets the Duration till which to generate the
     thumbnails. Can be either absolute duration (e.g: PT05S) or relative value
     (e.g: 100%)
    :type range: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'preserve_resolution_after_rotation': {'key': 'preserveResolutionAfterRotation', 'type': 'bool'},
        'key_frame_interval': {'key': 'keyFrameInterval', 'type': 'duration'},
        'stretch_mode': {'key': 'stretchMode', 'type': 'StretchMode'},
        'sync_mode': {'key': 'syncMode', 'type': 'VideoSyncMode'},
        'start': {'key': 'start', 'type': 'str'},
        'step': {'key': 'step', 'type': 'str'},
        'range': {'key': 'range', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.BmpImage': 'BmpImage', '#Microsoft.Media.JpgImage': 'JpgImage', '#Microsoft.Media.PngImage': 'PngImage'}
    }

    def __init__(self, label=None, preserve_resolution_after_rotation=None, key_frame_interval=None, stretch_mode=None, sync_mode=None, start=None, step=None, range=None):
        super(Image, self).__init__(label=label, preserve_resolution_after_rotation=preserve_resolution_after_rotation, key_frame_interval=key_frame_interval, stretch_mode=stretch_mode, sync_mode=sync_mode)
        self.start = start
        self.step = step
        self.range = range
        self.odatatype = '#Microsoft.Media.Image'
