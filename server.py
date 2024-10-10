import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        if request.language == "fr":
            message = f"Bonjour, {request.name}!"
        elif request.language == "ar":
            message = f"مرحبا، {request.name}!"
        else:
            message = f"Hello, {request.name}!"
        return helloworld_pb2.HelloReply(message=message)

    def StreamHello(self, request, context):
        for _ in range(5):
            if request.language == "fr":
                message = f"Bonjour, {request.name}!"
            elif request.language == "ar":
                message = f"مرحبا، {request.name}!"
            else:
                message = f"Hello, {request.name}!"
            yield helloworld_pb2.HelloReply(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
