# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .stream_selection import StreamSelection


class AudioStream(StreamSelection):
    """Object to represent audio stream selection.

    :param file_index: Gets the file index where the stream is present.
    :type file_index: int
    :param stream_index: Gets the stream index.
    :type stream_index: int
    :param is_absolute_stream_index: Gets a value indicating whether the
     stream index is absolute or relative to the stream type.
    :type is_absolute_stream_index: bool
    :param stream_selection_mode: Gets the stream selection mode. Possible
     values include: 'SelectionNotSet', 'SelectHighestBitrateStream',
     'SelectLowestBitrateStream', 'SelectAllStreams'
    :type stream_selection_mode: str or ~encoding.models.StreamSelectionMode
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param language_tag: Gets or sets the Audio Language Tag.
    :type language_tag: str
    :param audio_channel_mapping: Gets or sets the Audio channel mapping
     string.
    :type audio_channel_mapping: str
    """

    _validation = {
        'file_index': {'required': True},
        'stream_index': {'required': True},
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'file_index': {'key': 'fileIndex', 'type': 'int'},
        'stream_index': {'key': 'streamIndex', 'type': 'int'},
        'is_absolute_stream_index': {'key': 'isAbsoluteStreamIndex', 'type': 'bool'},
        'stream_selection_mode': {'key': 'streamSelectionMode', 'type': 'StreamSelectionMode'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'language_tag': {'key': 'languageTag', 'type': 'str'},
        'audio_channel_mapping': {'key': 'audioChannelMapping', 'type': 'str'},
    }

    def __init__(self, file_index, stream_index, is_absolute_stream_index=None, stream_selection_mode=None, language_tag=None, audio_channel_mapping=None):
        super(AudioStream, self).__init__(file_index=file_index, stream_index=stream_index, is_absolute_stream_index=is_absolute_stream_index, stream_selection_mode=stream_selection_mode)
        self.language_tag = language_tag
        self.audio_channel_mapping = audio_channel_mapping
        self.odatatype = '#Microsoft.Media.AudioStream'
