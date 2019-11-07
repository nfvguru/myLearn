var http=require("http");

http.createServer(function(request,response) {
    response.writeHead(200,{'Content-Type': 'Text/Plain'});
    response.end("Lava's Server");
}).listen(6061);

console.log("Lavanz server running on port 6061");
