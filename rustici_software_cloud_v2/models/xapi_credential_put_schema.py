# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class XapiCredentialPutSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, info=None, secret=None, is_enabled=None, auth=None, permissions_level=None):
        """
        XapiCredentialPutSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'info': 'str',
            'secret': 'str',
            'is_enabled': 'bool',
            'auth': 'XapiCredentialAuthTypeSchema',
            'permissions_level': 'XapiCredentialPermissionsLevelSchema'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'info': 'info',
            'secret': 'secret',
            'is_enabled': 'isEnabled',
            'auth': 'auth',
            'permissions_level': 'permissionsLevel'
        }

        self._id = id
        self._name = name
        self._info = info
        self._secret = secret
        self._is_enabled = is_enabled
        self._auth = auth
        self._permissions_level = permissions_level

    @property
    def id(self):
        """
        Gets the id of this XapiCredentialPutSchema.

        :return: The id of this XapiCredentialPutSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this XapiCredentialPutSchema.

        :param id: The id of this XapiCredentialPutSchema.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this XapiCredentialPutSchema.

        :return: The name of this XapiCredentialPutSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this XapiCredentialPutSchema.

        :param name: The name of this XapiCredentialPutSchema.
        :type: str
        """

        self._name = name

    @property
    def info(self):
        """
        Gets the info of this XapiCredentialPutSchema.

        :return: The info of this XapiCredentialPutSchema.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this XapiCredentialPutSchema.

        :param info: The info of this XapiCredentialPutSchema.
        :type: str
        """

        self._info = info

    @property
    def secret(self):
        """
        Gets the secret of this XapiCredentialPutSchema.

        :return: The secret of this XapiCredentialPutSchema.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this XapiCredentialPutSchema.

        :param secret: The secret of this XapiCredentialPutSchema.
        :type: str
        """

        self._secret = secret

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this XapiCredentialPutSchema.

        :return: The is_enabled of this XapiCredentialPutSchema.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this XapiCredentialPutSchema.

        :param is_enabled: The is_enabled of this XapiCredentialPutSchema.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def auth(self):
        """
        Gets the auth of this XapiCredentialPutSchema.

        :return: The auth of this XapiCredentialPutSchema.
        :rtype: XapiCredentialAuthTypeSchema
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """
        Sets the auth of this XapiCredentialPutSchema.

        :param auth: The auth of this XapiCredentialPutSchema.
        :type: XapiCredentialAuthTypeSchema
        """

        self._auth = auth

    @property
    def permissions_level(self):
        """
        Gets the permissions_level of this XapiCredentialPutSchema.

        :return: The permissions_level of this XapiCredentialPutSchema.
        :rtype: XapiCredentialPermissionsLevelSchema
        """
        return self._permissions_level

    @permissions_level.setter
    def permissions_level(self, permissions_level):
        """
        Sets the permissions_level of this XapiCredentialPutSchema.

        :param permissions_level: The permissions_level of this XapiCredentialPutSchema.
        :type: XapiCredentialPermissionsLevelSchema
        """

        self._permissions_level = permissions_level

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, XapiCredentialPutSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
