# -*- coding: utf-8 -*-

"""
rootcollection

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SignUpAgentRequest(object):

    """Implementation of the 'sign_up_agent_request' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        family_name (string): TODO: type description here.
        email (string): TODO: type description here.
        phone_number (string): TODO: type description here.
        password (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "family_name": 'family_name',
        "email": 'email',
        "phone_number": 'phone_number',
        "password": 'password'
    }

    def __init__(self,
                 name=None,
                 family_name=None,
                 email=None,
                 phone_number=None,
                 password=None):
        """Constructor for the SignUpAgentRequest class"""

        # Initialize members of the class
        self.name = name
        self.family_name = family_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get('name')
        family_name = dictionary.get('family_name')
        email = dictionary.get('email')
        phone_number = dictionary.get('phone_number')
        password = dictionary.get('password')

        # Return an object of this model
        return cls(name,
                   family_name,
                   email,
                   phone_number,
                   password)
