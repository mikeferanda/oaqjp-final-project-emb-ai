let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.readyState == 4) {
            document.getElementById("system_response").innerHTML = "Error analyzing sentiment.";
            console.error("Sentiment analysis request failed:", this.status, this.responseText);
        }
    };
    const url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict';
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    http.setRequestHeader("grpc-metadata-mm-model-id", "emotion_aggregated-workflow_lang_en_stock");

    const inputJson = JSON.stringify({ "raw_document": { "text": textToAnalyze } });
    xhttp.send(inputJson);
}
