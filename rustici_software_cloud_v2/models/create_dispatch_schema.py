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


class CreateDispatchSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, destination_id=None, course_id=None, allow_new_registrations=True, instanced=True, registration_cap=0, expiration_date=None, enabled=True, tags=None, email=None, notes=None, post_back=None):
        """
        CreateDispatchSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'destination_id': 'str',
            'course_id': 'str',
            'allow_new_registrations': 'bool',
            'instanced': 'bool',
            'registration_cap': 'int',
            'expiration_date': 'datetime',
            'enabled': 'bool',
            'tags': 'list[str]',
            'email': 'str',
            'notes': 'str',
            'post_back': 'PostBackSchema'
        }

        self.attribute_map = {
            'destination_id': 'destinationId',
            'course_id': 'courseId',
            'allow_new_registrations': 'allowNewRegistrations',
            'instanced': 'instanced',
            'registration_cap': 'registrationCap',
            'expiration_date': 'expirationDate',
            'enabled': 'enabled',
            'tags': 'tags',
            'email': 'email',
            'notes': 'notes',
            'post_back': 'postBack'
        }

        self._destination_id = destination_id
        self._course_id = course_id
        self._allow_new_registrations = allow_new_registrations
        self._instanced = instanced
        self._registration_cap = registration_cap
        self._expiration_date = expiration_date
        self._enabled = enabled
        self._tags = tags
        self._email = email
        self._notes = notes
        self._post_back = post_back

    @property
    def destination_id(self):
        """
        Gets the destination_id of this CreateDispatchSchema.
        Id of the destination this dispatch will belong to.

        :return: The destination_id of this CreateDispatchSchema.
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """
        Sets the destination_id of this CreateDispatchSchema.
        Id of the destination this dispatch will belong to.

        :param destination_id: The destination_id of this CreateDispatchSchema.
        :type: str
        """
        if destination_id is None:
            raise ValueError("Invalid value for `destination_id`, must not be `None`")

        self._destination_id = destination_id

    @property
    def course_id(self):
        """
        Gets the course_id of this CreateDispatchSchema.
        Id of the course to be dispatched.

        :return: The course_id of this CreateDispatchSchema.
        :rtype: str
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """
        Sets the course_id of this CreateDispatchSchema.
        Id of the course to be dispatched.

        :param course_id: The course_id of this CreateDispatchSchema.
        :type: str
        """
        if course_id is None:
            raise ValueError("Invalid value for `course_id`, must not be `None`")

        self._course_id = course_id

    @property
    def allow_new_registrations(self):
        """
        Gets the allow_new_registrations of this CreateDispatchSchema.
        If true, then new registrations can be created for this dispatch.

        :return: The allow_new_registrations of this CreateDispatchSchema.
        :rtype: bool
        """
        return self._allow_new_registrations

    @allow_new_registrations.setter
    def allow_new_registrations(self, allow_new_registrations):
        """
        Sets the allow_new_registrations of this CreateDispatchSchema.
        If true, then new registrations can be created for this dispatch.

        :param allow_new_registrations: The allow_new_registrations of this CreateDispatchSchema.
        :type: bool
        """

        self._allow_new_registrations = allow_new_registrations

    @property
    def instanced(self):
        """
        Gets the instanced of this CreateDispatchSchema.
        If true, then a new registration instance will be created if the client LMS doesn't provide launch data for an existing one. Otherwise, the same instance will always be used for the given cmi.learner_id. 

        :return: The instanced of this CreateDispatchSchema.
        :rtype: bool
        """
        return self._instanced

    @instanced.setter
    def instanced(self, instanced):
        """
        Sets the instanced of this CreateDispatchSchema.
        If true, then a new registration instance will be created if the client LMS doesn't provide launch data for an existing one. Otherwise, the same instance will always be used for the given cmi.learner_id. 

        :param instanced: The instanced of this CreateDispatchSchema.
        :type: bool
        """

        self._instanced = instanced

    @property
    def registration_cap(self):
        """
        Gets the registration_cap of this CreateDispatchSchema.
        The maximum number of registrations that can be created for this dispatch, where '0' means 'unlimited registrations'. 

        :return: The registration_cap of this CreateDispatchSchema.
        :rtype: int
        """
        return self._registration_cap

    @registration_cap.setter
    def registration_cap(self, registration_cap):
        """
        Sets the registration_cap of this CreateDispatchSchema.
        The maximum number of registrations that can be created for this dispatch, where '0' means 'unlimited registrations'. 

        :param registration_cap: The registration_cap of this CreateDispatchSchema.
        :type: int
        """

        self._registration_cap = registration_cap

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this CreateDispatchSchema.
        The date after which this dispatch will be disabled as an ISO 8601 string, or not present for no expiration date. 

        :return: The expiration_date of this CreateDispatchSchema.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this CreateDispatchSchema.
        The date after which this dispatch will be disabled as an ISO 8601 string, or not present for no expiration date. 

        :param expiration_date: The expiration_date of this CreateDispatchSchema.
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def enabled(self):
        """
        Gets the enabled of this CreateDispatchSchema.
        If true, then this dispatch can be launched.

        :return: The enabled of this CreateDispatchSchema.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CreateDispatchSchema.
        If true, then this dispatch can be launched.

        :param enabled: The enabled of this CreateDispatchSchema.
        :type: bool
        """

        self._enabled = enabled

    @property
    def tags(self):
        """
        Gets the tags of this CreateDispatchSchema.
        The tags to associate with this Dispatch.

        :return: The tags of this CreateDispatchSchema.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CreateDispatchSchema.
        The tags to associate with this Dispatch.

        :param tags: The tags of this CreateDispatchSchema.
        :type: list[str]
        """

        self._tags = tags

    @property
    def email(self):
        """
        Gets the email of this CreateDispatchSchema.
        SCORM Cloud user e-mail associated with this dispatch. If this is not provided, it will default to the owner of the Realm. 

        :return: The email of this CreateDispatchSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateDispatchSchema.
        SCORM Cloud user e-mail associated with this dispatch. If this is not provided, it will default to the owner of the Realm. 

        :param email: The email of this CreateDispatchSchema.
        :type: str
        """

        self._email = email

    @property
    def notes(self):
        """
        Gets the notes of this CreateDispatchSchema.
        Any provided notes about this dispatch.

        :return: The notes of this CreateDispatchSchema.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this CreateDispatchSchema.
        Any provided notes about this dispatch.

        :param notes: The notes of this CreateDispatchSchema.
        :type: str
        """

        self._notes = notes

    @property
    def post_back(self):
        """
        Gets the post_back of this CreateDispatchSchema.
        The postback information for this Dispatch.

        :return: The post_back of this CreateDispatchSchema.
        :rtype: PostBackSchema
        """
        return self._post_back

    @post_back.setter
    def post_back(self, post_back):
        """
        Sets the post_back of this CreateDispatchSchema.
        The postback information for this Dispatch.

        :param post_back: The post_back of this CreateDispatchSchema.
        :type: PostBackSchema
        """

        self._post_back = post_back

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
        if not isinstance(other, CreateDispatchSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
