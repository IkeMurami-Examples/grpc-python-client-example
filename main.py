from base64 import b64encode, b64decode

import schema_pb2
import schema_pb2_grpc

import grpc
import requests

HOST = 'https://functions.yandexcloud.net/d4e***qhd'
TOKEN = 't1.9e***MBQ'

request = schema_pb2.NewProgramRequest(
    program_name='test_program'
)
print(request)
request_bytes = request.SerializeToString()
print(request_bytes)

response = requests.post(
    f'{HOST}',
    headers={
        'Authorization': f'Bearer {TOKEN}'
    },
    data=request_bytes
)

print(response)
print(response.content)