let time = window.timerValue;
const timerEl = document.getElementById('timer');
const form = document.getElementById('answerForm');
const statusMsg = document.getElementById('statusMsg');
const submitBtn = document.getElementById('submitBtn');
let answered = false;

function goNext() {
  const nextUrl = new URL(window.location.href);
  const currentQ = parseInt(nextUrl.searchParams.get("q") || "0");
  nextUrl.searchParams.set("q", currentQ + 1);
  window.location.href = nextUrl.toString();
}

function submitAnswer() {
  if (answered) return;
  answered = true;

  const formData = new FormData(form);
  fetch(window.submitUrl, {
    method: "POST",
    headers: {
      'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === 'ok') {
      statusMsg.textContent = "Ответ сохранён!";
    } else {
      statusMsg.textContent = data.message || "Ошибка";
      statusMsg.style.color = 'red';
    }
  })
  .catch(err => {
    statusMsg.textContent = "Ошибка сети";
    statusMsg.style.color = 'red';
  })
  .finally(() => {
    setTimeout(goNext, 500);
  });
}

submitBtn.addEventListener('click', () => {
  if (!form.reportValidity()) return;
  submitAnswer();
});

const countdown = setInterval(() => {
  time--;
  timerEl.textContent = `Осталось времени: ${time} сек`;
  if (time <= 0) {
    clearInterval(countdown);
    if (!answered) {
      submitAnswer();
    }
  }
}, 1000);