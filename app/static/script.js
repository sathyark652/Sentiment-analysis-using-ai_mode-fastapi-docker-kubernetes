async function predict() {
    const textInput = document.getElementById('textInput').value;

    const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + btoa('sathya123:123456')  // Replace with your actual credentials
        },
        body: JSON.stringify({ text: textInput })
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Prediction: ${data.prediction}`;

    // Update the prediction image based on the result
    const predictionImageDiv = document.getElementById('predictionImage');
    predictionImageDiv.innerHTML = "";  // Clear previous content

    
    if (data.prediction === "positive") {
        const positiveImageUrl = "/static/positive-image.jpg";
        predictionImageDiv.innerHTML = `<img src='${positiveImageUrl}' alt='Positive Image'>`;
    } else if (data.prediction === "negative") {
        const negativeImageUrl = "/static/negative-image.jpg";
        predictionImageDiv.innerHTML = `<img src='${negativeImageUrl}' alt='Negative Image'>`;
    } else {
        predictionImageDiv.innerHTML = "<p>Unknown Prediction</p>";
    }
    
}
