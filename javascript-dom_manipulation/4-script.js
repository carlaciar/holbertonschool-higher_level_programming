const list = document.querySelector(".my_list");
const addItem = document.querySelector("#add_item");

addItem.addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    list.appendChild(newItem);
});