# -*- coding: utf-8 -*-

"""
rootcollection

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from rootcollection.api_helper import APIHelper
from rootcollection.configuration import Server
from rootcollection.controllers.base_controller import BaseController


class SettingsController(BaseController):

    """A Controller to access Endpoints in the rootcollection API."""
    def __init__(self, config, auth_managers):
        super(SettingsController, self).__init__(config, auth_managers)

    def update_locataire_password(self,
                                  body):
        """Does a PUT request to /mobile_settings/locataire/password/1.

        TODO: type endpoint description here.

        Args:
            body (ResetPasswordLocataireRequest): TODO: type description
                here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/mobile_settings/locataire/password/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_agent_password(self,
                              body):
        """Does a PUT request to /mobile_settings/locataire/password/1.

        TODO: type endpoint description here.

        Args:
            body (ResetPasswordLocataireRequest): TODO: type description
                here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/mobile_settings/locataire/password/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_decideur_password(self,
                                 body):
        """Does a PUT request to /web_settings/decideur/password/1.

        TODO: type endpoint description here.

        Args:
            body (ResetPasswordLocataireRequest): TODO: type description
                here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/web_settings/decideur/password/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_locataire_email(self,
                               body):
        """Does a PUT request to /mobile_settings/locataire/password/1.

        TODO: type endpoint description here.

        Args:
            body (ResetPasswordLocataireRequest): TODO: type description
                here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/mobile_settings/locataire/password/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_decideur_email(self,
                              body):
        """Does a PUT request to /web_settings/decideur/email/1.

        TODO: type endpoint description here.

        Args:
            body (DeleteLocataireRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/web_settings/decideur/email/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_agent_email(self,
                           body):
        """Does a PUT request to /mobile_settings/agent/email/1.

        TODO: type endpoint description here.

        Args:
            body (DeleteLocataireRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/mobile_settings/agent/email/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)
