# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0 beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ActivityResultSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, attempts=None, activity_completion=None, activity_success=None, score=None, time_tracked=None, completion_amount=None, suspended=None, children=None, objectives=None, static_properties=None, runtime=None):
        """
        ActivityResultSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'attempts': 'int',
            'activity_completion': 'str',
            'activity_success': 'str',
            'score': 'ScoreSchema',
            'time_tracked': 'str',
            'completion_amount': 'CompletionAmountSchema',
            'suspended': 'bool',
            'children': 'list[ActivityResultSchema]',
            'objectives': 'list[ObjectiveSchema]',
            'static_properties': 'StaticPropertiesSchema',
            'runtime': 'RuntimeSchema'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'attempts': 'attempts',
            'activity_completion': 'activityCompletion',
            'activity_success': 'activitySuccess',
            'score': 'score',
            'time_tracked': 'timeTracked',
            'completion_amount': 'completionAmount',
            'suspended': 'suspended',
            'children': 'children',
            'objectives': 'objectives',
            'static_properties': 'staticProperties',
            'runtime': 'runtime'
        }

        self._id = id
        self._title = title
        self._attempts = attempts
        self._activity_completion = activity_completion
        self._activity_success = activity_success
        self._score = score
        self._time_tracked = time_tracked
        self._completion_amount = completion_amount
        self._suspended = suspended
        self._children = children
        self._objectives = objectives
        self._static_properties = static_properties
        self._runtime = runtime

    @property
    def id(self):
        """
        Gets the id of this ActivityResultSchema.


        :return: The id of this ActivityResultSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivityResultSchema.


        :param id: The id of this ActivityResultSchema.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this ActivityResultSchema.


        :return: The title of this ActivityResultSchema.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ActivityResultSchema.


        :param title: The title of this ActivityResultSchema.
        :type: str
        """

        self._title = title

    @property
    def attempts(self):
        """
        Gets the attempts of this ActivityResultSchema.


        :return: The attempts of this ActivityResultSchema.
        :rtype: int
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """
        Sets the attempts of this ActivityResultSchema.


        :param attempts: The attempts of this ActivityResultSchema.
        :type: int
        """

        self._attempts = attempts

    @property
    def activity_completion(self):
        """
        Gets the activity_completion of this ActivityResultSchema.


        :return: The activity_completion of this ActivityResultSchema.
        :rtype: str
        """
        return self._activity_completion

    @activity_completion.setter
    def activity_completion(self, activity_completion):
        """
        Sets the activity_completion of this ActivityResultSchema.


        :param activity_completion: The activity_completion of this ActivityResultSchema.
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLETED", "INCOMPLETE"]
        if activity_completion not in allowed_values:
            raise ValueError(
                "Invalid value for `activity_completion` ({0}), must be one of {1}"
                .format(activity_completion, allowed_values)
            )

        self._activity_completion = activity_completion

    @property
    def activity_success(self):
        """
        Gets the activity_success of this ActivityResultSchema.


        :return: The activity_success of this ActivityResultSchema.
        :rtype: str
        """
        return self._activity_success

    @activity_success.setter
    def activity_success(self, activity_success):
        """
        Sets the activity_success of this ActivityResultSchema.


        :param activity_success: The activity_success of this ActivityResultSchema.
        :type: str
        """
        allowed_values = ["UNKNOWN", "PASSED", "FAILED"]
        if activity_success not in allowed_values:
            raise ValueError(
                "Invalid value for `activity_success` ({0}), must be one of {1}"
                .format(activity_success, allowed_values)
            )

        self._activity_success = activity_success

    @property
    def score(self):
        """
        Gets the score of this ActivityResultSchema.


        :return: The score of this ActivityResultSchema.
        :rtype: ScoreSchema
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this ActivityResultSchema.


        :param score: The score of this ActivityResultSchema.
        :type: ScoreSchema
        """

        self._score = score

    @property
    def time_tracked(self):
        """
        Gets the time_tracked of this ActivityResultSchema.


        :return: The time_tracked of this ActivityResultSchema.
        :rtype: str
        """
        return self._time_tracked

    @time_tracked.setter
    def time_tracked(self, time_tracked):
        """
        Sets the time_tracked of this ActivityResultSchema.


        :param time_tracked: The time_tracked of this ActivityResultSchema.
        :type: str
        """

        self._time_tracked = time_tracked

    @property
    def completion_amount(self):
        """
        Gets the completion_amount of this ActivityResultSchema.


        :return: The completion_amount of this ActivityResultSchema.
        :rtype: CompletionAmountSchema
        """
        return self._completion_amount

    @completion_amount.setter
    def completion_amount(self, completion_amount):
        """
        Sets the completion_amount of this ActivityResultSchema.


        :param completion_amount: The completion_amount of this ActivityResultSchema.
        :type: CompletionAmountSchema
        """

        self._completion_amount = completion_amount

    @property
    def suspended(self):
        """
        Gets the suspended of this ActivityResultSchema.


        :return: The suspended of this ActivityResultSchema.
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """
        Sets the suspended of this ActivityResultSchema.


        :param suspended: The suspended of this ActivityResultSchema.
        :type: bool
        """

        self._suspended = suspended

    @property
    def children(self):
        """
        Gets the children of this ActivityResultSchema.


        :return: The children of this ActivityResultSchema.
        :rtype: list[ActivityResultSchema]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this ActivityResultSchema.


        :param children: The children of this ActivityResultSchema.
        :type: list[ActivityResultSchema]
        """

        self._children = children

    @property
    def objectives(self):
        """
        Gets the objectives of this ActivityResultSchema.


        :return: The objectives of this ActivityResultSchema.
        :rtype: list[ObjectiveSchema]
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives):
        """
        Sets the objectives of this ActivityResultSchema.


        :param objectives: The objectives of this ActivityResultSchema.
        :type: list[ObjectiveSchema]
        """

        self._objectives = objectives

    @property
    def static_properties(self):
        """
        Gets the static_properties of this ActivityResultSchema.


        :return: The static_properties of this ActivityResultSchema.
        :rtype: StaticPropertiesSchema
        """
        return self._static_properties

    @static_properties.setter
    def static_properties(self, static_properties):
        """
        Sets the static_properties of this ActivityResultSchema.


        :param static_properties: The static_properties of this ActivityResultSchema.
        :type: StaticPropertiesSchema
        """

        self._static_properties = static_properties

    @property
    def runtime(self):
        """
        Gets the runtime of this ActivityResultSchema.


        :return: The runtime of this ActivityResultSchema.
        :rtype: RuntimeSchema
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this ActivityResultSchema.


        :param runtime: The runtime of this ActivityResultSchema.
        :type: RuntimeSchema
        """

        self._runtime = runtime

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other