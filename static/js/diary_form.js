// === Form Submit ===
document.getElementById('diaryForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const resultDiv = document.getElementById('result');
    const spinner = document.getElementById('loadingSpinner');
    const messageText = document.getElementById('message');

    resultDiv.innerHTML = '';
    messageText.textContent = '';
    spinner.style.display = 'inline-block';

    try {
        const response = await fetch(form.action, {
            method: form.method,
            body: formData
        });

        if (!response.ok) throw new Error('Sunucu hatası!');

        const data = await response.json();

        resultDiv.innerHTML =
            `<div class="alert alert-success" role="alert">
                <strong>Günlüğünüz kaydedildi!</strong><br>
                🧠 <strong>Duygu:</strong> ${data.sentiment}<br>
                💡 <strong>Yorum:</strong> ${data.comment}<br>
                ${data.suggestions ? `<strong>✅ Öneriler:</strong><br>${data.suggestions}` : ''}
            </div>`;

        form.reset();
        document.getElementById("liveTranscript").innerHTML = "<em>Tanıdığınız metin burada görünecek...</em>";
    } catch (error) {
        resultDiv.innerHTML =
            `<div class="alert alert-danger" role="alert">
                ${error.message || 'Bir hata oluştu.'}
            </div>`;
    } finally {
        spinner.style.display = 'none';
    }
});

// === Sesli Günlük ===
const micButton = document.getElementById("micButton");
const contentInput = document.querySelector("textarea[name='content']");
const liveTranscriptDiv = document.getElementById("liveTranscript");

let recognition;

if ("webkitSpeechRecognition" in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.lang = "tr-TR";

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        contentInput.value += transcript + " ";
        liveTranscriptDiv.innerHTML = `<strong>${contentInput.value}</strong>`;
    };

    recognition.onerror = function (event) {
        alert("🎤 Ses algılanamadı: " + event.error);
    };

    recognition.onend = function () {
        micButton.textContent = "🎤 Sesli Günlük Başlat";
    };
} else {
    alert("Tarayıcınız sesli giriş özelliğini desteklemiyor.");
}

micButton.addEventListener("click", () => {
    if (recognition) {
        if (micButton.textContent.includes("Dinleniyor")) {
            recognition.stop();
            micButton.textContent = "🎤 Sesli Günlük Başlat";
        } else {
            recognition.start();
            micButton.textContent = "🛑 Dinleniyor...";
        }
    }
});

// === Sekme Geçişi ===
document.getElementById('textInputTab').addEventListener('click', () => {
    document.getElementById('textInputArea').style.display = 'block';
    document.getElementById('voiceInputArea').style.display = 'none';
    document.getElementById('textInputTab').classList.add('btn-primary');
    document.getElementById('textInputTab').classList.remove('btn-secondary');
    document.getElementById('voiceInputTab').classList.add('btn-secondary');
    document.getElementById('voiceInputTab').classList.remove('btn-primary');
});

document.getElementById('voiceInputTab').addEventListener('click', () => {
    document.getElementById('textInputArea').style.display = 'none';
    document.getElementById('voiceInputArea').style.display = 'block';
    document.getElementById('voiceInputTab').classList.add('btn-primary');
    document.getElementById('voiceInputTab').classList.remove('btn-secondary');
    document.getElementById('textInputTab').classList.add('btn-secondary');
    document.getElementById('textInputTab').classList.remove('btn-primary');
});

// === İpuçları Göster/Gizle Fonksiyonu ===
function toggleTips() {
    const tipsContent = document.getElementById('quickTipsContent');
    const toggleIcon = document.getElementById('tipToggleIcon');
    if (tipsContent.style.display === 'none' || tipsContent.style.display === '') {
        tipsContent.style.display = 'block';
        toggleIcon.textContent = '▲';
    } else {
        tipsContent.style.display = 'none';
        toggleIcon.textContent = '▼';
    }
}
