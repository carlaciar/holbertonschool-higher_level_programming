const myHeader = document.querySelector("header");
const updateHeader = document.querySelector("#update_header");

updateHeader.addEventListener("click", () => {
    myHeader.textContent = "New Header!!!";
});