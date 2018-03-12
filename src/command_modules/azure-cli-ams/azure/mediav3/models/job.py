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

from msrest.serialization import Model


class Job(Model):
    """A Job resource type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The resource name.
    :vartype name: str
    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar created: The date and time when the Job was created.
    :vartype created: datetime
    :ivar state: The current state of the job. Possible values include:
     'Canceled', 'Canceling', 'Error', 'Finished', 'Processing', 'Queued',
     'Scheduled'
    :vartype state: str or ~encoding.models.JobState
    :param description: The customer supplied description of the Job.
    :type description: str
    :param input: The inputs for the Job.
    :type input: ~encoding.models.JobInput
    :ivar last_modified: The date and time when the Job was last updated.
    :vartype last_modified: datetime
    :param outputs: The outputs for the Job.
    :type outputs: list[~encoding.models.JobOutput]
    :param priority: Priority with which the job should be processed.  Higher
     priority jobs are processed before lower priority jobs if there is
     resource contention. If not set, the default is normal. Possible values
     include: 'Low', 'Normal', 'High'
    :type priority: str or ~encoding.models.Priority
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'created': {'readonly': True},
        'state': {'readonly': True},
        'input': {'required': True},
        'last_modified': {'readonly': True},
        'outputs': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'JobState'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'input': {'key': 'properties.input', 'type': 'JobInput'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
        'outputs': {'key': 'properties.outputs', 'type': '[JobOutput]'},
        'priority': {'key': 'properties.priority', 'type': 'Priority'},
    }

    def __init__(self, input, outputs, description=None, priority=None):
        super(Job, self).__init__()
        self.name = None
        self.id = None
        self.type = None
        self.created = None
        self.state = None
        self.description = description
        self.input = input
        self.last_modified = None
        self.outputs = outputs
        self.priority = priority
