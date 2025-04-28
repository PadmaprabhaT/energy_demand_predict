function makePrediction() {
    const country = document.getElementById("country").value;
    const year = document.getElementById("year").value;

    // Validate if year is a number
    if (isNaN(year) || year.trim() === "") {
        document.getElementById("predictionResult").innerText = "Please enter a valid year.";
        return;
    }

    document.getElementById("predictionResult").innerText = "Sending request for prediction..."; // Intermediate step

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ country: country, year: year })
    })
    .then(response => {
        document.getElementById("predictionResult").innerText = "Request received. Predicting..."; // Intermediate step
        return response.json();
    })
    .then(data => {
        if (data.prediction) {
            document.getElementById("predictionResult").innerText = `✅ Predicted Energy Demand for ${country} in ${year}: ${data.prediction} TWh`;
        } else {
            document.getElementById("predictionResult").innerText = "❌ Sorry, no data available for the selected parameters.";
        }
    })
    .catch(error => {
        document.getElementById("predictionResult").innerText = "⚠️ An error occurred. Please try again later.";
    });
}
