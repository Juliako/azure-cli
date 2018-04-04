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

from .job_input import JobInput


class JobInputClip(JobInput):
    """Represents Job Inputs that can have a start or end time specified to take a
    subset of the specified media.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: JobInputAsset, JobInputHttp

    :param label: Customer provided label of the JobInput.
    :type label: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param files: List of files.  Required for JobInputAzureBlob. It
     optionally can be used for JobInputAsset to tell the service to only use
     the files specified from the Asset.
    :type files: list[str]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'files': {'key': 'files', 'type': '[str]'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.JobInputAsset': 'JobInputAsset', '#Microsoft.Media.JobInputHttp': 'JobInputHttp'}
    }

    def __init__(self, label=None, files=None):
        super(JobInputClip, self).__init__(label=label)
        self.files = files
        self.odatatype = '#Microsoft.Media.JobInputClip'
