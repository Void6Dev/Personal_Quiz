const fileInput = document.getElementById('id_image');
const fileNameDisplay = document.getElementById('file-name');

fileInput.addEventListener('change', function () {
    const fileName = this.files[0] ? this.files[0].name : 'Файл не выбран';
    fileNameDisplay.textContent = fileName;
});



