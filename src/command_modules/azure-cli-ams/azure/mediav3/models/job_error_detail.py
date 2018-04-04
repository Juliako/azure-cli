# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobErrorDetail(Model):
    """Details of JobOutput errors.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Code describing the error detail.
    :vartype code: str
    :ivar message: A human-readable representation of the error.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        super(JobErrorDetail, self).__init__()
        self.code = None
        self.message = None
