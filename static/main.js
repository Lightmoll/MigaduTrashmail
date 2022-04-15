var button = document.getElementById("create_button");


document.getElementById("create_form").onsubmit = function() {
    button.ariaBusy = true;
    button.setAttribute("aria-busy", "true");
}


window.onload = function() {
    var status = location.hash.substring(1)
    button.ariaBusy = false;
    button.setAttribute("aria-busy", "false");
    switch (status) {
        case "created":
            button.classList.add("good");
            button.textContent = "Created!";
            break;
        case "error":
            button.classList.add("bad");
            button.textContent = "Error!";
            break;
    }
    setTimeout(button_to_normal, 3000);
}

function button_to_normal() {
    button.classList.remove("good");
    button.classList.remove("bad");
    button.textContent = "Create";
}