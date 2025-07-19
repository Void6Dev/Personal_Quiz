let answerCount = 1;
  function addAnswer() {
    const container = document.getElementById('answers');

    const answerDiv = document.createElement('div');
    answerDiv.classList.add('answer');

    const input = document.createElement('input');
    input.type = 'text';
    input.name = 'answer_text';
    input.placeholder = 'Ответ';
    input.required = true;

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.name = 'is_correct';
    checkbox.value = answerCount;

    const label = document.createElement('label');
    label.innerText = ' Правильный';

    answerDiv.appendChild(input);
    answerDiv.appendChild(checkbox);
    answerDiv.appendChild(label);

    container.appendChild(answerDiv);
    answerCount++;
  }

  function removeLastAnswer() {
    const container = document.getElementById('answers');
    if (container.children.length > 1) {
      container.removeChild(container.lastElementChild);
      answerCount--;
    }
  }