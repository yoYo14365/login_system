const math = document.getElementsByClassName("math");
const science = document.getElementsByClassName("science");
const games = document.getElementsByClassName("games");

math[0].addEventListener("click", () => {
    window.location.href = "/admin/math";
});

science[0].addEventListener("click", () => {
    window.location.href = "/admin/science";
});

games[0].addEventListener("click", () => {
    window.location.href = "/admin/games";
});