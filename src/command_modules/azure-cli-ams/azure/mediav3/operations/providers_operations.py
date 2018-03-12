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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ProvidersOperations(object):
    """ProvidersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: The API version. Constant value: "2018-02-01-privatepreview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-02-01-privatepreview"

        self.config = config

    def check_name_availability(
            self, name=None, type=None, custom_headers=None, raw=False, **operation_config):
        """Check Name Availability.

        Checks whether the Media Service resource name is available.

        :param name: The account name.
        :type name: str
        :param type: The account type. For a Media Services account, this
         should be 'MediaServices'.
        :type type: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EntityNameAvailabilityCheckOutput or ClientRawResponse if
         raw=true
        :rtype: ~encoding.models.EntityNameAvailabilityCheckOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ApiErrorException<encoding.models.ApiErrorException>`
        """
        parameters = models.CheckNameAvailabilityInput(name=name, type=type)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/providers/Microsoft.Media/checkNameAvailability'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('EntityNameAvailabilityCheckOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
