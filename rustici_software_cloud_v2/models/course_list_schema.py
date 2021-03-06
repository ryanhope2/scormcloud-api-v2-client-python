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


class CourseListSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, courses=None, more=None):
        """
        CourseListSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'courses': 'list[CourseSchema]',
            'more': 'str'
        }

        self.attribute_map = {
            'courses': 'courses',
            'more': 'more'
        }

        self._courses = courses
        self._more = more

    @property
    def courses(self):
        """
        Gets the courses of this CourseListSchema.

        :return: The courses of this CourseListSchema.
        :rtype: list[CourseSchema]
        """
        return self._courses

    @courses.setter
    def courses(self, courses):
        """
        Sets the courses of this CourseListSchema.

        :param courses: The courses of this CourseListSchema.
        :type: list[CourseSchema]
        """

        self._courses = courses

    @property
    def more(self):
        """
        Gets the more of this CourseListSchema.

        :return: The more of this CourseListSchema.
        :rtype: str
        """
        return self._more

    @more.setter
    def more(self, more):
        """
        Sets the more of this CourseListSchema.

        :param more: The more of this CourseListSchema.
        :type: str
        """

        self._more = more

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
        if not isinstance(other, CourseListSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
