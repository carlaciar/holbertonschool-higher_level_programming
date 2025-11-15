document.addEventListener("DOMContentLoaded", () => {
    const helloTag = document.querySelector('#hello');
  
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
      .then(response => response.json())
      .then(data => {
        helloTag.textContent = data.hello;
      });
  });