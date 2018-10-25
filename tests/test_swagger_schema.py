from flex.core import load, validate_request, validate_response
from mock import patch


class Request(object):
    def __init__(self, path, method, query_data, headers, data, content_type):
        self.path = path
        self.method = method
        self.query_data = query_data
        self.headers = headers
        self.data = data
        self.content_type = content_type


class Response(object):
    def __init__(self, path, status_code):
        self.path = path
        self.status_code = status_code


def mock_validate_request_content_type(request, content_types, **kwargs):
    from flex.validation.common import validate_content_type
    validate_content_type(request.content_type, content_types, **kwargs)


@patch('flex.validation.operation.validate_request_content_type', mock_validate_request_content_type)
def test_post_pet():
    schema = load("swagger/swagger.yaml")
    data = {
        'name': '',
        'photoUrls': [''],
        'tags': [{
            'id': 1,
            'name': 'Tijger'
        }],
        'status': 'sold'
    }
    request = Request(path='/v2/pet', method='post', query_data={}, headers={}, data=data, content_type='application/json')
    validate_request(request, schema)

    resp = Response(path='/v2/pet', status_code='201')
    validate_response(resp, 'post', schema)