# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0 beta
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SettingMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default=None, data_type=None, setting_description=None, level=None, learning_standards=None, learning_standard_variant='either', fallback=None, valid_values=None):
        """
        SettingMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default': 'str',
            'data_type': 'str',
            'setting_description': 'str',
            'level': 'str',
            'learning_standards': 'list[str]',
            'learning_standard_variant': 'str',
            'fallback': 'str',
            'valid_values': 'list[SettingValidValue]'
        }

        self.attribute_map = {
            'default': 'default',
            'data_type': 'dataType',
            'setting_description': 'settingDescription',
            'level': 'level',
            'learning_standards': 'learningStandards',
            'learning_standard_variant': 'learningStandardVariant',
            'fallback': 'fallback',
            'valid_values': 'validValues'
        }

        self._default = default
        self._data_type = data_type
        self._setting_description = setting_description
        self._level = level
        self._learning_standards = learning_standards
        self._learning_standard_variant = learning_standard_variant
        self._fallback = fallback
        self._valid_values = valid_values

    @property
    def default(self):
        """
        Gets the default of this SettingMetadata.
        Default value of this setting

        :return: The default of this SettingMetadata.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this SettingMetadata.
        Default value of this setting

        :param default: The default of this SettingMetadata.
        :type: str
        """

        self._default = default

    @property
    def data_type(self):
        """
        Gets the data_type of this SettingMetadata.
        The data type of this setting

        :return: The data_type of this SettingMetadata.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this SettingMetadata.
        The data type of this setting

        :param data_type: The data_type of this SettingMetadata.
        :type: str
        """

        self._data_type = data_type

    @property
    def setting_description(self):
        """
        Gets the setting_description of this SettingMetadata.
        description of this setting

        :return: The setting_description of this SettingMetadata.
        :rtype: str
        """
        return self._setting_description

    @setting_description.setter
    def setting_description(self, setting_description):
        """
        Sets the setting_description of this SettingMetadata.
        description of this setting

        :param setting_description: The setting_description of this SettingMetadata.
        :type: str
        """

        self._setting_description = setting_description

    @property
    def level(self):
        """
        Gets the level of this SettingMetadata.
        The level this setting will be applied at, which limits where it can be set. For example, WebPathToContentRoot is applied at the application level, so it's not valid to set it for a registration.

        :return: The level of this SettingMetadata.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this SettingMetadata.
        The level this setting will be applied at, which limits where it can be set. For example, WebPathToContentRoot is applied at the application level, so it's not valid to set it for a registration.

        :param level: The level of this SettingMetadata.
        :type: str
        """

        self._level = level

    @property
    def learning_standards(self):
        """
        Gets the learning_standards of this SettingMetadata.
        The list of learning standards this setting applies to. If not present, this setting is not limited to certain learning standards.

        :return: The learning_standards of this SettingMetadata.
        :rtype: list[str]
        """
        return self._learning_standards

    @learning_standards.setter
    def learning_standards(self, learning_standards):
        """
        Sets the learning_standards of this SettingMetadata.
        The list of learning standards this setting applies to. If not present, this setting is not limited to certain learning standards.

        :param learning_standards: The learning_standards of this SettingMetadata.
        :type: list[str]
        """

        self._learning_standards = learning_standards

    @property
    def learning_standard_variant(self):
        """
        Gets the learning_standard_variant of this SettingMetadata.
        Does this setting apply to only single-SCO packages, only multi-SCO, or either?

        :return: The learning_standard_variant of this SettingMetadata.
        :rtype: str
        """
        return self._learning_standard_variant

    @learning_standard_variant.setter
    def learning_standard_variant(self, learning_standard_variant):
        """
        Sets the learning_standard_variant of this SettingMetadata.
        Does this setting apply to only single-SCO packages, only multi-SCO, or either?

        :param learning_standard_variant: The learning_standard_variant of this SettingMetadata.
        :type: str
        """
        allowed_values = ["singleScoOnly", "multiScoOnly", "either"]
        if learning_standard_variant not in allowed_values:
            raise ValueError(
                "Invalid value for `learning_standard_variant` ({0}), must be one of {1}"
                .format(learning_standard_variant, allowed_values)
            )

        self._learning_standard_variant = learning_standard_variant

    @property
    def fallback(self):
        """
        Gets the fallback of this SettingMetadata.
        A setting that will be used instead of this setting if no value is provided for this setting (This is similar to a default, except that the the value of another setting is being used instead of a fixed default value).

        :return: The fallback of this SettingMetadata.
        :rtype: str
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """
        Sets the fallback of this SettingMetadata.
        A setting that will be used instead of this setting if no value is provided for this setting (This is similar to a default, except that the the value of another setting is being used instead of a fixed default value).

        :param fallback: The fallback of this SettingMetadata.
        :type: str
        """

        self._fallback = fallback

    @property
    def valid_values(self):
        """
        Gets the valid_values of this SettingMetadata.
        For settings with a fixed list of valid values, the list of those values

        :return: The valid_values of this SettingMetadata.
        :rtype: list[SettingValidValue]
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        """
        Sets the valid_values of this SettingMetadata.
        For settings with a fixed list of valid values, the list of those values

        :param valid_values: The valid_values of this SettingMetadata.
        :type: list[SettingValidValue]
        """

        self._valid_values = valid_values

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
        if not isinstance(other, SettingMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
