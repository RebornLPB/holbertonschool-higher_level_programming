document.addEventListener('DOMContentLoaded', function () {
  const btn_translate = document.querySelector('#btn_translate');
  const language_code = document.querySelector('#language_code');
  const hello_div = document.querySelector('#hello');
  btn_translate.addEventListener('click', function () {
    const lang_value = language_code.value;
    fetch('https://hellosalut.stefanbohacek.com/?lang=' + lang_value)
      .then(response => response.json())
      .then(data => {
        hello_div.textContent = data.hello
      });
  });
});
