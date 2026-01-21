const form = document.getElementById("loginform");

form.addEventListener("submit", (event) => {

    event.preventDefault();  // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    $.ajax({
        type: "POST",
        url: "/login",
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify({ username: username, password: password, for: "confirmation" }),
    success: function(response) {
        console.log("The login was successful");
        console.log(response);
        window.location.href = response.redirect;
    },
    error: function(xhr, status, error) {
        console.error("Login failed");
        console.error(xhr.responseText);
    }
    });
});
