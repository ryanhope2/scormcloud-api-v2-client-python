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


class SettingItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, effective_value=None, effective_value_source=None, explicit_value=None, metadata=None):
        """
        SettingItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'effective_value': 'str',
            'effective_value_source': 'str',
            'explicit_value': 'str',
            'metadata': 'SettingMetadata'
        }

        self.attribute_map = {
            'id': 'id',
            'effective_value': 'effectiveValue',
            'effective_value_source': 'effectiveValueSource',
            'explicit_value': 'explicitValue',
            'metadata': 'metadata'
        }

        self._id = id
        self._effective_value = effective_value
        self._effective_value_source = effective_value_source
        self._explicit_value = explicit_value
        self._metadata = metadata

    @property
    def id(self):
        """
        Gets the id of this SettingItem.

        :return: The id of this SettingItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SettingItem.

        :param id: The id of this SettingItem.
        :type: str
        """

        self._id = id

    @property
    def effective_value(self):
        """
        Gets the effective_value of this SettingItem.
        The value of this setting that would be used if read at this level, including defaults, fallback, and values set at less specific levels.

        :return: The effective_value of this SettingItem.
        :rtype: str
        """
        return self._effective_value

    @effective_value.setter
    def effective_value(self, effective_value):
        """
        Sets the effective_value of this SettingItem.
        The value of this setting that would be used if read at this level, including defaults, fallback, and values set at less specific levels.

        :param effective_value: The effective_value of this SettingItem.
        :type: str
        """

        self._effective_value = effective_value

    @property
    def effective_value_source(self):
        """
        Gets the effective_value_source of this SettingItem.
        The source of this effective value, default, fallback, or the level the value was set at.

        :return: The effective_value_source of this SettingItem.
        :rtype: str
        """
        return self._effective_value_source

    @effective_value_source.setter
    def effective_value_source(self, effective_value_source):
        """
        Sets the effective_value_source of this SettingItem.
        The source of this effective value, default, fallback, or the level the value was set at.

        :param effective_value_source: The effective_value_source of this SettingItem.
        :type: str
        """
        allowed_values = ["default", "fallback", "base", "system", "learningStandard", "application", "learningStandardForApplication", "dispatchDestination", "course", "dispatchDestinationForCourse", "registration"]
        if effective_value_source not in allowed_values:
            raise ValueError(
                "Invalid value for `effective_value_source` ({0}), must be one of {1}"
                .format(effective_value_source, allowed_values)
            )

        self._effective_value_source = effective_value_source

    @property
    def explicit_value(self):
        """
        Gets the explicit_value of this SettingItem.
        The value of this setting that is explicitly set at this level. If not present, the setting is not specified at this level.

        :return: The explicit_value of this SettingItem.
        :rtype: str
        """
        return self._explicit_value

    @explicit_value.setter
    def explicit_value(self, explicit_value):
        """
        Sets the explicit_value of this SettingItem.
        The value of this setting that is explicitly set at this level. If not present, the setting is not specified at this level.

        :param explicit_value: The explicit_value of this SettingItem.
        :type: str
        """

        self._explicit_value = explicit_value

    @property
    def metadata(self):
        """
        Gets the metadata of this SettingItem.

        :return: The metadata of this SettingItem.
        :rtype: SettingMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this SettingItem.

        :param metadata: The metadata of this SettingItem.
        :type: SettingMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, SettingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
