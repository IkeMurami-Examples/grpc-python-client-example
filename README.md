# CF Python Client

CF Endpoint: https://github.com/asman-go/cf-protobuf-api

Start:

```
$ python -m venv .venv
$ .\.venv\Scripts\activate
$ python -m pip install -r requirements.txt
```

Generate proto scheme:

on *nix:

```
$ python -m grpc_tools.protoc -I ../cf-protobuf-api/proto --python_out=. --grpc_python_out=. ../cf-protobuf-api/proto/*.proto
```

on Windows:

```
$ python -m grpc_tools.protoc -I ..\cf-protobuf-api\proto --python_out=. --grpc_python_out=. ..\cf-protobuf-api\proto\*.proto
```
