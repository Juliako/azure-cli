# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .job_input import JobInput


class JobInputs(JobInput):
    """Supports list of inputs to a Job.

    :param label: Label of the JobInput.  Used to match JobInputs to
     TransformInputs.  If no Label is given then the JobInputs are matched by
     index.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param inputs: List of Job inputs.
    :type inputs: list[~encoding.models.JobInput]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[JobInput]'},
    }

    def __init__(self, label=None, inputs=None):
        super(JobInputs, self).__init__(label=label)
        self.inputs = inputs
        self.odatatype = '#Microsoft.Media.JobInputs'
