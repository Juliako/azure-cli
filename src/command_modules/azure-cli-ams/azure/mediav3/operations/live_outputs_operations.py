# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import DeserializationError
from msrestazure.azure_operation import AzureOperationPoller

from .. import models


class LiveOutputsOperations(object):
    """LiveOutputsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The Version of the API to be used with the client request. Constant value: "2018-03-30-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-03-30-preview"

        self.config = config

    def list(
            self, resource_group_name, account_name, live_event_name, custom_headers=None, raw=False, **operation_config):
        """Lists the Live Outputs in the Live Event.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param live_event_name: The name of the Live Event.
        :type live_event_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LiveOutput
        :rtype: ~encoding.models.LiveOutputPaged[~encoding.models.LiveOutput]
        :raises: :class:`ApiErrorException<encoding.models.ApiErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str'),
                    'liveEventName': self._serialize.url("live_event_name", live_event_name, 'str', max_length=32, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ApiErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.LiveOutputPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LiveOutputPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs'}

    def get(
            self, resource_group_name, account_name, live_event_name, live_output_name, custom_headers=None, raw=False, **operation_config):
        """Gets a Live Output.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param live_event_name: The name of the Live Event.
        :type live_event_name: str
        :param live_output_name: The name of the Live Output.
        :type live_output_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LiveOutput or ClientRawResponse if raw=true
        :rtype: ~encoding.models.LiveOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ApiErrorException<encoding.models.ApiErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'liveEventName': self._serialize.url("live_event_name", live_event_name, 'str', max_length=32, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
            'liveOutputName': self._serialize.url("live_output_name", live_output_name, 'str', max_length=256, min_length=1, pattern=r'^([a-zA-Z0-9])+(-*[a-zA-Z0-9])*$')
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

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LiveOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName}'}


    def _create_initial(
            self, resource_group_name, account_name, live_event_name, live_output_name, parameters, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'liveEventName': self._serialize.url("live_event_name", live_event_name, 'str', max_length=32, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
            'liveOutputName': self._serialize.url("live_output_name", live_output_name, 'str', max_length=256, min_length=1, pattern=r'^([a-zA-Z0-9])+(-*[a-zA-Z0-9])*$')
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
        body_content = self._serialize.body(parameters, 'LiveOutput')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LiveOutput', response)
        if response.status_code == 202:
            deserialized = self._deserialize('LiveOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, resource_group_name, account_name, live_event_name, live_output_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates a Live Output.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param live_event_name: The name of the Live Event.
        :type live_event_name: str
        :param live_output_name: The name of the Live Output.
        :type live_output_name: str
        :param parameters: Live Output properties needed for creation.
        :type parameters: ~encoding.models.LiveOutput
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: An instance of AzureOperationPoller that returns LiveOutput
         or ClientRawResponse if raw=true
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~encoding.models.LiveOutput]
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ApiErrorException<encoding.models.ApiErrorException>`
        """
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            live_event_name=live_event_name,
            live_output_name=live_output_name,
            parameters=parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )
        if raw:
            return raw_result

        # Construct and send request
        def long_running_send():
            return raw_result.response

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            header_parameters = {}
            header_parameters['x-ms-client-request-id'] = raw_result.response.request.headers['x-ms-client-request-id']
            return self._client.send(
                request, header_parameters, stream=False, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ApiErrorException(self._deserialize, response)

            deserialized = self._deserialize('LiveOutput', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName}'}


    def _delete_initial(
            self, resource_group_name, account_name, live_event_name, live_output_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'liveEventName': self._serialize.url("live_event_name", live_event_name, 'str', max_length=32, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
            'liveOutputName': self._serialize.url("live_output_name", live_output_name, 'str', max_length=256, min_length=1, pattern=r'^([a-zA-Z0-9])+(-*[a-zA-Z0-9])*$')
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

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.ApiErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, resource_group_name, account_name, live_event_name, live_output_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a Live Output.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param live_event_name: The name of the Live Event.
        :type live_event_name: str
        :param live_output_name: The name of the Live Output.
        :type live_output_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: An instance of AzureOperationPoller that returns None or
         ClientRawResponse if raw=true
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ApiErrorException<encoding.models.ApiErrorException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            live_event_name=live_event_name,
            live_output_name=live_output_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )
        if raw:
            return raw_result

        # Construct and send request
        def long_running_send():
            return raw_result.response

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            header_parameters = {}
            header_parameters['x-ms-client-request-id'] = raw_result.response.request.headers['x-ms-client-request-id']
            return self._client.send(
                request, header_parameters, stream=False, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202, 204]:
                raise models.ApiErrorException(self._deserialize, response)

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName}'}
