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


class PostBackSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, auth_type='UNDEFINED', user_name=None, password=None, results_format='UNDEFINED', legacy=None):
        """
        PostBackSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'auth_type': 'str',
            'user_name': 'str',
            'password': 'str',
            'results_format': 'str',
            'legacy': 'bool'
        }

        self.attribute_map = {
            'url': 'url',
            'auth_type': 'authType',
            'user_name': 'userName',
            'password': 'password',
            'results_format': 'resultsFormat',
            'legacy': 'legacy'
        }

        self._url = url
        self._auth_type = auth_type
        self._user_name = user_name
        self._password = password
        self._results_format = results_format
        self._legacy = legacy

    @property
    def url(self):
        """
        Gets the url of this PostBackSchema.

        :return: The url of this PostBackSchema.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PostBackSchema.

        :param url: The url of this PostBackSchema.
        :type: str
        """

        self._url = url

    @property
    def auth_type(self):
        """
        Gets the auth_type of this PostBackSchema.
        Optional parameter to specify how to authorize against the given postbackurl, can be 'form' or 'httpbasic'. If form authentication, the username and password for authentication are submitted as form fields 'username' and 'password', and the registration data as the form field 'data'. If httpbasic authentication is used, the username and password are placed in the standard Authorization HTTP header, and the registration data is the body of the message (sent as text/xml content type). This field is set to 'form' by default.

        :return: The auth_type of this PostBackSchema.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this PostBackSchema.
        Optional parameter to specify how to authorize against the given postbackurl, can be 'form' or 'httpbasic'. If form authentication, the username and password for authentication are submitted as form fields 'username' and 'password', and the registration data as the form field 'data'. If httpbasic authentication is used, the username and password are placed in the standard Authorization HTTP header, and the registration data is the body of the message (sent as text/xml content type). This field is set to 'form' by default.

        :param auth_type: The auth_type of this PostBackSchema.
        :type: str
        """
        allowed_values = ["UNDEFINED", "FORM", "HTTPBASIC"]
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def user_name(self):
        """
        Gets the user_name of this PostBackSchema.
        The user name to be used in authorizing the postback of data to the URL specified by postback url.

        :return: The user_name of this PostBackSchema.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this PostBackSchema.
        The user name to be used in authorizing the postback of data to the URL specified by postback url.

        :param user_name: The user_name of this PostBackSchema.
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this PostBackSchema.
        The password to be used in authorizing the postback of data to the URL specified by postback url.

        :return: The password of this PostBackSchema.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this PostBackSchema.
        The password to be used in authorizing the postback of data to the URL specified by postback url.

        :param password: The password of this PostBackSchema.
        :type: str
        """

        self._password = password

    @property
    def results_format(self):
        """
        Gets the results_format of this PostBackSchema.
        This parameter allows you to specify a level of detail in the information that is posted back while the course is being taken. It may be one of three values: 'course' (course summary), 'activity' (activity summary, or 'full' (full detail), and is set to 'course' by default. The information will be posted as xml, and the format of that xml is specified below under the method 'getRegistrationResult'

        :return: The results_format of this PostBackSchema.
        :rtype: str
        """
        return self._results_format

    @results_format.setter
    def results_format(self, results_format):
        """
        Sets the results_format of this PostBackSchema.
        This parameter allows you to specify a level of detail in the information that is posted back while the course is being taken. It may be one of three values: 'course' (course summary), 'activity' (activity summary, or 'full' (full detail), and is set to 'course' by default. The information will be posted as xml, and the format of that xml is specified below under the method 'getRegistrationResult'

        :param results_format: The results_format of this PostBackSchema.
        :type: str
        """
        allowed_values = ["UNDEFINED", "COURSE", "ACTIVITY", "FULL"]
        if results_format not in allowed_values:
            raise ValueError(
                "Invalid value for `results_format` ({0}), must be one of {1}"
                .format(results_format, allowed_values)
            )

        self._results_format = results_format

    @property
    def legacy(self):
        """
        Gets the legacy of this PostBackSchema.
        This paramenter is ONLY used for backwards compatibility with XML postback implementations.  You probably shouldn't need to use this unless you're currently transitioning from the V1 api to the V2 api and already have existing XML postback logic in your application, but have not yet built out JSON postback logic.  If a registration is created with the V2 api we will assume that you're expecting JSON results unless otherwise specified. 

        :return: The legacy of this PostBackSchema.
        :rtype: bool
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy):
        """
        Sets the legacy of this PostBackSchema.
        This paramenter is ONLY used for backwards compatibility with XML postback implementations.  You probably shouldn't need to use this unless you're currently transitioning from the V1 api to the V2 api and already have existing XML postback logic in your application, but have not yet built out JSON postback logic.  If a registration is created with the V2 api we will assume that you're expecting JSON results unless otherwise specified. 

        :param legacy: The legacy of this PostBackSchema.
        :type: bool
        """

        self._legacy = legacy

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
        if not isinstance(other, PostBackSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
