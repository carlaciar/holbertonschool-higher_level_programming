const actorName = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    actorName.textContent = data.name;
  })
  .catch((error) => {
    console.log('Error:', error);
  });