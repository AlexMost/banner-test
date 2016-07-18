const canvas = new fabric.Canvas('c', {width: 600, height: 300});
const fileInput = document.getElementById('input');
const uploadLink = document.getElementById('upload');
const result = document.getElementById('result');

fileInput.addEventListener('change', (e) => {
    const url = URL.createObjectURL(e.target.files[0]);
    fabric.Image.fromURL(url, (img) => {
        canvas.add(img);
        fileInput.value = ""
    });
});


uploadLink.addEventListener('click', function() {
    const data = {file: canvas.toDataURL()};
    fetch(
        '/upload_banner',
        {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => res.json())
        .then(({ src }) => result.src = src)
});

