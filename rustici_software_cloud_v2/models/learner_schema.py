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


class LearnerSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, email=None, first_name=None, last_name=None):
        """
        LearnerSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'email': 'str',
            'first_name': 'str',
            'last_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName'
        }

        self._id = id
        self._email = email
        self._first_name = first_name
        self._last_name = last_name

    @property
    def id(self):
        """
        Gets the id of this LearnerSchema.

        :return: The id of this LearnerSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LearnerSchema.

        :param id: The id of this LearnerSchema.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this LearnerSchema.
        Optional email address associated with the learner.

        :return: The email of this LearnerSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this LearnerSchema.
        Optional email address associated with the learner.

        :param email: The email of this LearnerSchema.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this LearnerSchema.

        :return: The first_name of this LearnerSchema.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this LearnerSchema.

        :param first_name: The first_name of this LearnerSchema.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this LearnerSchema.

        :return: The last_name of this LearnerSchema.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this LearnerSchema.

        :param last_name: The last_name of this LearnerSchema.
        :type: str
        """

        self._last_name = last_name

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
        if not isinstance(other, LearnerSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
