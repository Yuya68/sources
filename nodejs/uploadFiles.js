// this js file works to return some files when one connect as http

const fs = require('fs');
const http = require('http');
const server = http.createServer(
    function( request, response ) {

    const filename = "./sample.txt";
    const raw = fs.createReadStream( filename );

    const resHeader = {
        'Content-Type' : 'application/txt',
        'Content-Disposition' : 'attachment; filename="sample.txt"'
    };

    response.writeHead(200, resHeader );
    raw.pipe(response);

    console.log("done");

}).listen(8000);
