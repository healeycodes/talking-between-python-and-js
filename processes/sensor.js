function reportReading() {
    const temperature = (Math.random() * 20) - 5;
    process.stdout.write(`${String(temperature)}\n`);
    setTimeout(reportReading, Math.random() * 5000);
}
reportReading();