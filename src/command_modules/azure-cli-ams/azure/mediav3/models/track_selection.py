# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TrackSelection(Model):
    """Class to select a track.

    :param track_selections: TrackSelections is a track property condition
     list which can specify track(s)
    :type track_selections: list[~encoding.models.TrackPropertyCondition]
    """

    _attribute_map = {
        'track_selections': {'key': 'trackSelections', 'type': '[TrackPropertyCondition]'},
    }

    def __init__(self, track_selections=None):
        super(TrackSelection, self).__init__()
        self.track_selections = track_selections
