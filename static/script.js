document.addEventListener("DOMContentLoaded", () => {
    const startBtn = document.getElementById("start");
    const stopBtn = document.getElementById("stop");
    const statusEl = document.getElementById("status");
    const translatedTextEl = document.getElementById("translated-text");
    const sentimentTextEl = document.getElementById("sentiment-text");

    let isListening = false;

    // Reset UI and variables
    const reset = () => {
        isListening = false;
        statusEl.textContent = "Click 'Start Listening' to begin!";
        translatedTextEl.textContent = "Awaiting input...";
        sentimentTextEl.textContent = "N/A";
        startBtn.disabled = false;
        stopBtn.disabled = true;
    };

    startBtn.addEventListener("click", () => {
        if (isListening) return; // Prevent double triggers

        isListening = true;
        statusEl.textContent = "Listening...";
        startBtn.disabled = true;
        stopBtn.disabled = false;

        // Simulate backend response
        setTimeout(() => {
            const simulatedTranslation = "Bonjour, comment ça va ?";
            const simulatedSentiment = "Positive";

            translatedTextEl.textContent = simulatedTranslation;
            sentimentTextEl.textContent = simulatedSentiment;

            statusEl.textContent = "Listening complete. Ready for the next input!";
            startBtn.disabled = false;
            stopBtn.disabled = true;

            // Allow new input after 1 second
            setTimeout(reset, 1000);
        }, 3000);
    });

    stopBtn.addEventListener("click", () => {
        if (!isListening) return; // Prevent stopping if not listening

        isListening = false;
        statusEl.textContent = "Stopped.";
        startBtn.disabled = false;
        stopBtn.disabled = true;

        reset();
    });
});
