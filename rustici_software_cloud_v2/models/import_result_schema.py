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


class ImportResultSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, web_path_to_course=None, parser_warnings=None, course_languages=None, course=None):
        """
        ImportResultSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'web_path_to_course': 'str',
            'parser_warnings': 'list[str]',
            'course_languages': 'list[str]',
            'course': 'CourseSchema'
        }

        self.attribute_map = {
            'web_path_to_course': 'webPathToCourse',
            'parser_warnings': 'parserWarnings',
            'course_languages': 'courseLanguages',
            'course': 'course'
        }

        self._web_path_to_course = web_path_to_course
        self._parser_warnings = parser_warnings
        self._course_languages = course_languages
        self._course = course

    @property
    def web_path_to_course(self):
        """
        Gets the web_path_to_course of this ImportResultSchema.
        web path to this course

        :return: The web_path_to_course of this ImportResultSchema.
        :rtype: str
        """
        return self._web_path_to_course

    @web_path_to_course.setter
    def web_path_to_course(self, web_path_to_course):
        """
        Sets the web_path_to_course of this ImportResultSchema.
        web path to this course

        :param web_path_to_course: The web_path_to_course of this ImportResultSchema.
        :type: str
        """

        self._web_path_to_course = web_path_to_course

    @property
    def parser_warnings(self):
        """
        Gets the parser_warnings of this ImportResultSchema.

        :return: The parser_warnings of this ImportResultSchema.
        :rtype: list[str]
        """
        return self._parser_warnings

    @parser_warnings.setter
    def parser_warnings(self, parser_warnings):
        """
        Sets the parser_warnings of this ImportResultSchema.

        :param parser_warnings: The parser_warnings of this ImportResultSchema.
        :type: list[str]
        """

        self._parser_warnings = parser_warnings

    @property
    def course_languages(self):
        """
        Gets the course_languages of this ImportResultSchema.

        :return: The course_languages of this ImportResultSchema.
        :rtype: list[str]
        """
        return self._course_languages

    @course_languages.setter
    def course_languages(self, course_languages):
        """
        Sets the course_languages of this ImportResultSchema.

        :param course_languages: The course_languages of this ImportResultSchema.
        :type: list[str]
        """

        self._course_languages = course_languages

    @property
    def course(self):
        """
        Gets the course of this ImportResultSchema.

        :return: The course of this ImportResultSchema.
        :rtype: CourseSchema
        """
        return self._course

    @course.setter
    def course(self, course):
        """
        Sets the course of this ImportResultSchema.

        :param course: The course of this ImportResultSchema.
        :type: CourseSchema
        """

        self._course = course

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
        if not isinstance(other, ImportResultSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
