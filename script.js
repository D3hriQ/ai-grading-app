document.getElementById('gradingForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const textInput = document.getElementById('textInput').value;
    const imageInput = document.getElementById('imageInput').files[0];
    const codeInput = document.getElementById('codeInput').value;

    const formData = new FormData();
    formData.append('textInput', textInput);
    formData.append('imageInput', imageInput);
    formData.append('codeInput', codeInput);

    const response = await fetch('/grade', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});