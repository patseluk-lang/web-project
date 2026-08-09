let count = 0;

const button = document.getElementById("btn");
const counter = document.getElementById("counter");

button.addEventListener("click", () => {
    count += 1;
    counter.textContent = `Кліків: ${count}`;
});