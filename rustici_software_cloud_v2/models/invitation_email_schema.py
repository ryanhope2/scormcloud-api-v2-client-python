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


class InvitationEmailSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, subject=None, body=None, addresses=None):
        """
        InvitationEmailSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'subject': 'str',
            'body': 'str',
            'addresses': 'list[str]'
        }

        self.attribute_map = {
            'subject': 'subject',
            'body': 'body',
            'addresses': 'addresses'
        }

        self._subject = subject
        self._body = body
        self._addresses = addresses

    @property
    def subject(self):
        """
        Gets the subject of this InvitationEmailSchema.
        The subject line for the email.

        :return: The subject of this InvitationEmailSchema.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this InvitationEmailSchema.
        The subject line for the email.

        :param subject: The subject of this InvitationEmailSchema.
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """
        Gets the body of this InvitationEmailSchema.
        The body of the email.

        :return: The body of this InvitationEmailSchema.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this InvitationEmailSchema.
        The body of the email.

        :param body: The body of this InvitationEmailSchema.
        :type: str
        """

        self._body = body

    @property
    def addresses(self):
        """
        Gets the addresses of this InvitationEmailSchema.
        A comma separated list of email addresses to which this invitation will be sent.  NOTE: registrations with automatically be create for each of these e-mail addresses.

        :return: The addresses of this InvitationEmailSchema.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this InvitationEmailSchema.
        A comma separated list of email addresses to which this invitation will be sent.  NOTE: registrations with automatically be create for each of these e-mail addresses.

        :param addresses: The addresses of this InvitationEmailSchema.
        :type: list[str]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")

        self._addresses = addresses

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
        if not isinstance(other, InvitationEmailSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
