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


class InvitationSummarySchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, course_id=None, is_public=None, create_date=None, updated=None):
        """
        InvitationSummarySchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'course_id': 'str',
            'is_public': 'bool',
            'create_date': 'datetime',
            'updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'course_id': 'courseId',
            'is_public': 'isPublic',
            'create_date': 'createDate',
            'updated': 'updated'
        }

        self._id = id
        self._course_id = course_id
        self._is_public = is_public
        self._create_date = create_date
        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this InvitationSummarySchema.
        The invitationId for this invitation.

        :return: The id of this InvitationSummarySchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InvitationSummarySchema.
        The invitationId for this invitation.

        :param id: The id of this InvitationSummarySchema.
        :type: str
        """

        self._id = id

    @property
    def course_id(self):
        """
        Gets the course_id of this InvitationSummarySchema.
        Course Id for this Invitation.

        :return: The course_id of this InvitationSummarySchema.
        :rtype: str
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """
        Sets the course_id of this InvitationSummarySchema.
        Course Id for this Invitation.

        :param course_id: The course_id of this InvitationSummarySchema.
        :type: str
        """

        self._course_id = course_id

    @property
    def is_public(self):
        """
        Gets the is_public of this InvitationSummarySchema.
        Is the invitation Public or Private

        :return: The is_public of this InvitationSummarySchema.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this InvitationSummarySchema.
        Is the invitation Public or Private

        :param is_public: The is_public of this InvitationSummarySchema.
        :type: bool
        """

        self._is_public = is_public

    @property
    def create_date(self):
        """
        Gets the create_date of this InvitationSummarySchema.
        The create date for the invitation

        :return: The create_date of this InvitationSummarySchema.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this InvitationSummarySchema.
        The create date for the invitation

        :param create_date: The create_date of this InvitationSummarySchema.
        :type: datetime
        """

        self._create_date = create_date

    @property
    def updated(self):
        """
        Gets the updated of this InvitationSummarySchema.

        :return: The updated of this InvitationSummarySchema.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this InvitationSummarySchema.

        :param updated: The updated of this InvitationSummarySchema.
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, InvitationSummarySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other