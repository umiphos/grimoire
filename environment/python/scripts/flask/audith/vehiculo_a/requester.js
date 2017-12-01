//var mysql      = require('mysql');
var request = require('request');


//Conexión a MySQL
/**var connection = mysql.createConnection({
  host     : '127.0.0.1',
  user     : 'root',
  password : 'pass',
  database : 'Qamaleontis'
});
*/



///'http://192.168.1.174:5000/GetLastRecords',

var options = {
    hostname: 'http://192.168.1.174:5000/GetLastRecords',
    method: 'GET',
    json:true
}
request(options, function(error, response, body){
    if(error) console.log(error);
    else console.log(body);
});