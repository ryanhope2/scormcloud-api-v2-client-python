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


class XapiCredentialSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, info=None, secret=None, is_enabled=None, auth=None, permissions_level=None):
        """
        XapiCredentialSchema - a model defined in Swagger

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
        Gets the id of this XapiCredentialSchema.

        :return: The id of this XapiCredentialSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this XapiCredentialSchema.

        :param id: The id of this XapiCredentialSchema.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this XapiCredentialSchema.

        :return: The name of this XapiCredentialSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this XapiCredentialSchema.

        :param name: The name of this XapiCredentialSchema.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def info(self):
        """
        Gets the info of this XapiCredentialSchema.

        :return: The info of this XapiCredentialSchema.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this XapiCredentialSchema.

        :param info: The info of this XapiCredentialSchema.
        :type: str
        """

        self._info = info

    @property
    def secret(self):
        """
        Gets the secret of this XapiCredentialSchema.

        :return: The secret of this XapiCredentialSchema.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this XapiCredentialSchema.

        :param secret: The secret of this XapiCredentialSchema.
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")

        self._secret = secret

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this XapiCredentialSchema.

        :return: The is_enabled of this XapiCredentialSchema.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this XapiCredentialSchema.

        :param is_enabled: The is_enabled of this XapiCredentialSchema.
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")

        self._is_enabled = is_enabled

    @property
    def auth(self):
        """
        Gets the auth of this XapiCredentialSchema.

        :return: The auth of this XapiCredentialSchema.
        :rtype: XapiCredentialAuthTypeSchema
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """
        Sets the auth of this XapiCredentialSchema.

        :param auth: The auth of this XapiCredentialSchema.
        :type: XapiCredentialAuthTypeSchema
        """
        if auth is None:
            raise ValueError("Invalid value for `auth`, must not be `None`")

        self._auth = auth

    @property
    def permissions_level(self):
        """
        Gets the permissions_level of this XapiCredentialSchema.

        :return: The permissions_level of this XapiCredentialSchema.
        :rtype: XapiCredentialPermissionsLevelSchema
        """
        return self._permissions_level

    @permissions_level.setter
    def permissions_level(self, permissions_level):
        """
        Sets the permissions_level of this XapiCredentialSchema.

        :param permissions_level: The permissions_level of this XapiCredentialSchema.
        :type: XapiCredentialPermissionsLevelSchema
        """
        if permissions_level is None:
            raise ValueError("Invalid value for `permissions_level`, must not be `None`")

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
        if not isinstance(other, XapiCredentialSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other