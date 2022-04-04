# -*- coding: utf-8 -*-

"""
rootcollection

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ResetPasswordLocataireRequest(object):

    """Implementation of the 'reset_password_locataire_request' model.

    TODO: type model description here.

    Attributes:
        password (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "password": 'password'
    }

    def __init__(self,
                 password=None):
        """Constructor for the ResetPasswordLocataireRequest class"""

        # Initialize members of the class
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
        password = dictionary.get('password')

        # Return an object of this model
        return cls(password)
