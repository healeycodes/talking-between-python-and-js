const { spawn } = require('child_process');
const temperatures = []; // Store readings

const sensor = spawn('python', ['sensor.py']);
sensor.stdout.on('data', function(data) {
    
    // Coerce Buffer object to Float
    temperatures.push(parseFloat(data));

    // Log to debug
    console.log(temperatures);
});
