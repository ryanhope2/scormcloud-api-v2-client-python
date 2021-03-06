# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AuthenticationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_app_token(self, scope, **kwargs):
        """
        Authenticates for a oauth token
        Creates, signs and returns an OAuth2 token based on the provided permissions, if the credentials used to request the token have the permissions being requested.  >Note:  >The token is not stored and therefore can not be modified or deleted. The requested permissions are encoded in the token which is then signed. As long as the secret used to create it is not changed the token will be valid until it expires. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_token(scope, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scope: (required)
        :param int expiration:
        :return: ApplicationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_app_token_with_http_info(scope, **kwargs)
        else:
            (data) = self.get_app_token_with_http_info(scope, **kwargs)
            return data

    def get_app_token_with_http_info(self, scope, **kwargs):
        """
        Authenticates for a oauth token
        Creates, signs and returns an OAuth2 token based on the provided permissions, if the credentials used to request the token have the permissions being requested.  >Note:  >The token is not stored and therefore can not be modified or deleted. The requested permissions are encoded in the token which is then signed. As long as the secret used to create it is not changed the token will be valid until it expires. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_token_with_http_info(scope, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scope: (required)
        :param int expiration:
        :return: ApplicationToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope', 'expiration']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in params) or (params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `get_app_token`")

        if 'expiration' in params and params['expiration'] > 43200:
            raise ValueError("Invalid value for parameter `expiration` when calling `get_app_token`, must be a value less than or equal to `43200`")
        if 'expiration' in params and params['expiration'] < 60:
            raise ValueError("Invalid value for parameter `expiration` when calling `get_app_token`, must be a value greater than or equal to `60`")

        collection_formats = {}

        resource_path = '/oauth/authenticate/application/token'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'scope' in params:
            form_params.append(('scope', params['scope']))
        if 'expiration' in params:
            form_params.append(('expiration', params['expiration']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['APP_NORMAL']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApplicationToken',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
