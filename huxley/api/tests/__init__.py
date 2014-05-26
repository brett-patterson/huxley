# Copyright (c) 2011-2014 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).

import json

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class RetrieveAPITestCase(APITestCase):
    '''Provides a base implementation to test Retrieve APIs.

    Classes that extend this must define a url_name class member, and can
    then use the get_response method to make a GET request.'''

    url_name = None

    def get_url(self, object_id):
        if not self.url_name:
            raise NotImplementedError('url_name not defined.')
        return reverse(self.url_name, args=(object_id,))

    def get_response(self, object_id):
        url = self.get_url(object_id)
        return self.client.get(url)


class CreateAPITestCase(APITestCase):
    '''Provides a base implementation to test Create APIs.

    Classes that extend this must define a url_name class member, and can
    then use the get_response method to make a POST request.

    They can optionally specify a params class member to define default
    params and then use get_params to override certain properties.'''

    url_name = None
    params = {}

    def get_url(self):
        if not self.url_name:
            raise NotImplementedError('url_name not defined.')
        return reverse(self.url_name)

    def get_params(self, **kwargs):
        params = self.params.copy()
        for param, value in kwargs.items():
            params[param] = value
        return params

    def get_response(self, params):
        return self.client.post(self.get_url(), json.dumps(params),
                                content_type='application/json')


class ListAPITestCase(APITestCase):
    '''Provides a base implementation to test List APIs.

    Classes that extend this must define a url_name class member, and can
    then use the get_response method to make a GET request.'''

    url_name = None

    def get_url(self):
        if not self.url_name:
            raise NotImplementedError('url_name not defined.')
        return reverse(self.url_name)

    def get_response(self):
        url = self.get_url()
        return self.client.get(url)
