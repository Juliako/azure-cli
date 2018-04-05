# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .job_output import JobOutput


class JobOutputAsset(JobOutput):
    """Represents an Asset used as a JobOutput.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar error: If the JobOutput is in the error state, it contains the
     details of the error.
    :vartype error: ~encoding.models.JobError
    :ivar state: State of the JobOutput. Possible values include: 'Canceled',
     'Canceling', 'Error', 'Finished', 'Processing', 'Queued', 'Scheduled'
    :vartype state: str or ~encoding.models.JobState
    :ivar progress: If the JobOutput is in the processing state, it contains
     the percentage of the job completed from 0 to 100 percent.
    :vartype progress: int
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param asset_name: The name of the output Asset.
    :type asset_name: str
    """

    _validation = {
        'error': {'readonly': True},
        'state': {'readonly': True},
        'progress': {'readonly': True},
        'odatatype': {'required': True},
        'asset_name': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'JobError'},
        'state': {'key': 'state', 'type': 'JobState'},
        'progress': {'key': 'progress', 'type': 'int'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'asset_name': {'key': 'assetName', 'type': 'str'},
    }

    def __init__(self, asset_name):
        super(JobOutputAsset, self).__init__()
        self.asset_name = asset_name
        self.odatatype = '#Microsoft.Media.JobOutputAsset'
