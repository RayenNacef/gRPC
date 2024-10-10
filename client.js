const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync('helloworld.proto', {});
const hello_proto = grpc.loadPackageDefinition(packageDefinition).helloworld;

function main() {
  const client = new hello_proto.Greeter('localhost:50051', grpc.credentials.createInsecure());
  const user = 'world';
  const language = 'en';

  client.SayHello({name: user, language: language}, function(err, response) {
    if (err) console.error(err);
    console.log('Greeting:', response.message);
  });

  const call = client.StreamHello({name: user, language: language});
  call.on('data', function(response) {
    console.log('Streaming Greeting:', response.message);
  });
  call.on('end', function() {
    console.log('Stream ended.');
  });
}

main();
