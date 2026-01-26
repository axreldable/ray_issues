# Response to GitHub Issue: Ray Serve gRPC with Nested Proto Structures

> "I could not get a service working with any arrangement other than having all the _pb2.py files in exactly the same level of the file hierarchy."

Ray Serve doesn't require all `_pb2.py` to be on the same level. 
What needs to be verified is that generated files are importable by Serve deployment.

---

## Proof: Working Example

### Structure Tested

```
2_minimal_example/
├── proto_1/
│   ├── greet.proto          → imports "proto_2/dependency.proto"
│   ├── greet_pb2.py         → contains: from proto_2 import dependency_pb2
│   └── greet_pb2_grpc.py
├── proto_2/
│   ├── dependency.proto
│   ├── dependency_pb2.py
│   └── dependency_pb2_grpc.py
├── ray_app.py               → Ray Serve deployment
├── root_client.py
```

**Result:** ✅ WORKS

### Test Output

```
bash$ python root_client.py
Response: Hello from Ray, Alice! Your email is alice@example.com
```
