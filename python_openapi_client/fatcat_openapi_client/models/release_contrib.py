# coding: utf-8

"""
    fatcat

    Fatcat is a scalable, versioned, API-oriented catalog of bibliographic entities and file metadata.   # noqa: E501

    OpenAPI spec version: 0.3.0
    Contact: webservices@archive.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from fatcat_openapi_client.models.creator_entity import CreatorEntity  # noqa: F401,E501


class ReleaseContrib(object):
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
        'index': 'int',
        'creator_id': 'str',
        'creator': 'CreatorEntity',
        'raw_name': 'str',
        'given_name': 'str',
        'surname': 'str',
        'role': 'str',
        'raw_affiliation': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'index': 'index',
        'creator_id': 'creator_id',
        'creator': 'creator',
        'raw_name': 'raw_name',
        'given_name': 'given_name',
        'surname': 'surname',
        'role': 'role',
        'raw_affiliation': 'raw_affiliation',
        'extra': 'extra'
    }

    def __init__(self, index=None, creator_id=None, creator=None, raw_name=None, given_name=None, surname=None, role=None, raw_affiliation=None, extra=None):  # noqa: E501
        """ReleaseContrib - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._creator_id = None
        self._creator = None
        self._raw_name = None
        self._given_name = None
        self._surname = None
        self._role = None
        self._raw_affiliation = None
        self._extra = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if creator_id is not None:
            self.creator_id = creator_id
        if creator is not None:
            self.creator = creator
        if raw_name is not None:
            self.raw_name = raw_name
        if given_name is not None:
            self.given_name = given_name
        if surname is not None:
            self.surname = surname
        if role is not None:
            self.role = role
        if raw_affiliation is not None:
            self.raw_affiliation = raw_affiliation
        if extra is not None:
            self.extra = extra

    @property
    def index(self):
        """Gets the index of this ReleaseContrib.  # noqa: E501

        Internally assigned zero-indexed sequence number of contribution. Authors should come first; this encodes the order of attriubtion.   # noqa: E501

        :return: The index of this ReleaseContrib.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ReleaseContrib.

        Internally assigned zero-indexed sequence number of contribution. Authors should come first; this encodes the order of attriubtion.   # noqa: E501

        :param index: The index of this ReleaseContrib.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def creator_id(self):
        """Gets the creator_id of this ReleaseContrib.  # noqa: E501

        If known, indicates the creator entity this contribution was made by.   # noqa: E501

        :return: The creator_id of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ReleaseContrib.

        If known, indicates the creator entity this contribution was made by.   # noqa: E501

        :param creator_id: The creator_id of this ReleaseContrib.  # noqa: E501
        :type: str
        """
        if creator_id is not None and len(creator_id) > 26:
            raise ValueError("Invalid value for `creator_id`, length must be less than or equal to `26`")  # noqa: E501
        if creator_id is not None and len(creator_id) < 26:
            raise ValueError("Invalid value for `creator_id`, length must be greater than or equal to `26`")  # noqa: E501
        if creator_id is not None and not re.search('[a-zA-Z2-7]{26}', creator_id):  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def creator(self):
        """Gets the creator of this ReleaseContrib.  # noqa: E501

        Complete creator entity. Only returned in GET responses, and only if `contribs` included in the `expand` query parameter.   # noqa: E501

        :return: The creator of this ReleaseContrib.  # noqa: E501
        :rtype: CreatorEntity
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ReleaseContrib.

        Complete creator entity. Only returned in GET responses, and only if `contribs` included in the `expand` query parameter.   # noqa: E501

        :param creator: The creator of this ReleaseContrib.  # noqa: E501
        :type: CreatorEntity
        """

        self._creator = creator

    @property
    def raw_name(self):
        """Gets the raw_name of this ReleaseContrib.  # noqa: E501

        Full name of the contributor as typeset in the release.   # noqa: E501

        :return: The raw_name of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._raw_name

    @raw_name.setter
    def raw_name(self, raw_name):
        """Sets the raw_name of this ReleaseContrib.

        Full name of the contributor as typeset in the release.   # noqa: E501

        :param raw_name: The raw_name of this ReleaseContrib.  # noqa: E501
        :type: str
        """

        self._raw_name = raw_name

    @property
    def given_name(self):
        """Gets the given_name of this ReleaseContrib.  # noqa: E501

        In English commonly the first name, but ordering is context and culture specific.   # noqa: E501

        :return: The given_name of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this ReleaseContrib.

        In English commonly the first name, but ordering is context and culture specific.   # noqa: E501

        :param given_name: The given_name of this ReleaseContrib.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """Gets the surname of this ReleaseContrib.  # noqa: E501

        In English commonly the last, or family name, but ordering is context and culture specific.   # noqa: E501

        :return: The surname of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this ReleaseContrib.

        In English commonly the last, or family name, but ordering is context and culture specific.   # noqa: E501

        :param surname: The surname of this ReleaseContrib.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def role(self):
        """Gets the role of this ReleaseContrib.  # noqa: E501

        Short string (slug) indicating type of contribution (eg, \"author\", \"translator\"). See guide for list of accpeted values.   # noqa: E501

        :return: The role of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ReleaseContrib.

        Short string (slug) indicating type of contribution (eg, \"author\", \"translator\"). See guide for list of accpeted values.   # noqa: E501

        :param role: The role of this ReleaseContrib.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def raw_affiliation(self):
        """Gets the raw_affiliation of this ReleaseContrib.  # noqa: E501

        Raw affiliation string as displayed in text  # noqa: E501

        :return: The raw_affiliation of this ReleaseContrib.  # noqa: E501
        :rtype: str
        """
        return self._raw_affiliation

    @raw_affiliation.setter
    def raw_affiliation(self, raw_affiliation):
        """Sets the raw_affiliation of this ReleaseContrib.

        Raw affiliation string as displayed in text  # noqa: E501

        :param raw_affiliation: The raw_affiliation of this ReleaseContrib.  # noqa: E501
        :type: str
        """

        self._raw_affiliation = raw_affiliation

    @property
    def extra(self):
        """Gets the extra of this ReleaseContrib.  # noqa: E501

        Additional free-form JSON metadata about this contributor/contribution. See guide for normative schema.   # noqa: E501

        :return: The extra of this ReleaseContrib.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this ReleaseContrib.

        Additional free-form JSON metadata about this contributor/contribution. See guide for normative schema.   # noqa: E501

        :param extra: The extra of this ReleaseContrib.  # noqa: E501
        :type: object
        """

        self._extra = extra

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReleaseContrib):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other