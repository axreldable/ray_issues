from ray import serve

@serve.deployment
class HelloWorld:
    def __call__(self, request):
        return "Hello, world from Ray Serve!"

app = HelloWorld.bind()
