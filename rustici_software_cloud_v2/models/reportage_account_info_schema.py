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


class ReportageAccountInfoSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email=None, first_name=None, last_name=None, company=None, account_type=None, reg_limit=None, strict_limit=None, create_date=None, usage=None):
        """
        ReportageAccountInfoSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'company': 'str',
            'account_type': 'str',
            'reg_limit': 'int',
            'strict_limit': 'bool',
            'create_date': 'datetime',
            'usage': 'ReportageAccountInfoUsageSchema'
        }

        self.attribute_map = {
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'company': 'company',
            'account_type': 'accountType',
            'reg_limit': 'regLimit',
            'strict_limit': 'strictLimit',
            'create_date': 'createDate',
            'usage': 'usage'
        }

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._company = company
        self._account_type = account_type
        self._reg_limit = reg_limit
        self._strict_limit = strict_limit
        self._create_date = create_date
        self._usage = usage

    @property
    def email(self):
        """
        Gets the email of this ReportageAccountInfoSchema.

        :return: The email of this ReportageAccountInfoSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ReportageAccountInfoSchema.

        :param email: The email of this ReportageAccountInfoSchema.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this ReportageAccountInfoSchema.

        :return: The first_name of this ReportageAccountInfoSchema.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this ReportageAccountInfoSchema.

        :param first_name: The first_name of this ReportageAccountInfoSchema.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this ReportageAccountInfoSchema.

        :return: The last_name of this ReportageAccountInfoSchema.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this ReportageAccountInfoSchema.

        :param last_name: The last_name of this ReportageAccountInfoSchema.
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """
        Gets the company of this ReportageAccountInfoSchema.

        :return: The company of this ReportageAccountInfoSchema.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this ReportageAccountInfoSchema.

        :param company: The company of this ReportageAccountInfoSchema.
        :type: str
        """

        self._company = company

    @property
    def account_type(self):
        """
        Gets the account_type of this ReportageAccountInfoSchema.

        :return: The account_type of this ReportageAccountInfoSchema.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this ReportageAccountInfoSchema.

        :param account_type: The account_type of this ReportageAccountInfoSchema.
        :type: str
        """

        self._account_type = account_type

    @property
    def reg_limit(self):
        """
        Gets the reg_limit of this ReportageAccountInfoSchema.

        :return: The reg_limit of this ReportageAccountInfoSchema.
        :rtype: int
        """
        return self._reg_limit

    @reg_limit.setter
    def reg_limit(self, reg_limit):
        """
        Sets the reg_limit of this ReportageAccountInfoSchema.

        :param reg_limit: The reg_limit of this ReportageAccountInfoSchema.
        :type: int
        """

        self._reg_limit = reg_limit

    @property
    def strict_limit(self):
        """
        Gets the strict_limit of this ReportageAccountInfoSchema.

        :return: The strict_limit of this ReportageAccountInfoSchema.
        :rtype: bool
        """
        return self._strict_limit

    @strict_limit.setter
    def strict_limit(self, strict_limit):
        """
        Sets the strict_limit of this ReportageAccountInfoSchema.

        :param strict_limit: The strict_limit of this ReportageAccountInfoSchema.
        :type: bool
        """

        self._strict_limit = strict_limit

    @property
    def create_date(self):
        """
        Gets the create_date of this ReportageAccountInfoSchema.

        :return: The create_date of this ReportageAccountInfoSchema.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this ReportageAccountInfoSchema.

        :param create_date: The create_date of this ReportageAccountInfoSchema.
        :type: datetime
        """

        self._create_date = create_date

    @property
    def usage(self):
        """
        Gets the usage of this ReportageAccountInfoSchema.

        :return: The usage of this ReportageAccountInfoSchema.
        :rtype: ReportageAccountInfoUsageSchema
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this ReportageAccountInfoSchema.

        :param usage: The usage of this ReportageAccountInfoSchema.
        :type: ReportageAccountInfoUsageSchema
        """

        self._usage = usage

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
        if not isinstance(other, ReportageAccountInfoSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other