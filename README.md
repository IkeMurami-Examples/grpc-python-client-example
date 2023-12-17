# CF Python Client

Start:

```
$ python -m venv .venv
$ .\.venv\Scripts\activate
$ python -m pip install -r requirements.txt
```

Generate proto scheme:

on *nix:

```
$ python -m grpc_tools.protoc -I ../cf-bbprogram/proto --python_out=. --grpc_python_out=. ../cf-bbprogram/proto/*.proto
```

on Windows:

```
$ python -m grpc_tools.protoc -I ..\cf-bbprogram\proto --python_out=. --grpc_python_out=. ..\cf-bbprogram\proto\*.proto
```
