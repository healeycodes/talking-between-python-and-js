// sensor.js

function reportReading() {
    const temperature = (Math.random() * 20) - 5; // Range of -5 to 15
    process.stdout.write(temperature + '\n'); // Write with newline char
    setTimeout(reportReading, Math.random() * 5000); // Wait 0 to 5 seconds
}
reportReading();
