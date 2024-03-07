# coding: utf-8

"""
    IoT Device Pins Management API

    This API allows for managing the pin configurations of an IoT device.  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Pin(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, id=None, type=None, status=None):  # noqa: E501
        """Pin - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._status = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.status = status

    @property
    def id(self):
        """Gets the id of this Pin.  # noqa: E501

        The unique identifier of the pin.  # noqa: E501

        :return: The id of this Pin.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pin.

        The unique identifier of the pin.  # noqa: E501

        :param id: The id of this Pin.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Pin.  # noqa: E501

        The type of the pin (e.g., digital, analog).  # noqa: E501

        :return: The type of this Pin.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Pin.

        The type of the pin (e.g., digital, analog).  # noqa: E501

        :param type: The type of this Pin.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this Pin.  # noqa: E501

        The current status of the pin (e.g., on, off).  # noqa: E501

        :return: The status of this Pin.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pin.

        The current status of the pin (e.g., on, off).  # noqa: E501

        :param status: The status of this Pin.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Pin, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
