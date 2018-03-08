# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .audio_analyzer_preset import AudioAnalyzerPreset


class VideoAnalyzerPreset(AudioAnalyzerPreset):
    """A video analyzer preset that analyzes both audio and video.

    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param audio_language: Gets or sets the audio language for the video.
     Typically in the format of "language code-country/region" (e.g: en-US)
    :type audio_language: str
    :param audio_insights_only: Gets or sets whether to get insights for audio
     only.
    :type audio_insights_only: bool
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'audio_language': {'key': 'audioLanguage', 'type': 'str'},
        'audio_insights_only': {'key': 'audioInsightsOnly', 'type': 'bool'},
    }

    def __init__(self, audio_language=None, audio_insights_only=None):
        super(VideoAnalyzerPreset, self).__init__(audio_language=audio_language)
        self.audio_insights_only = audio_insights_only
        self.odatatype = '#Microsoft.Media.VideoAnalyzerPreset'
