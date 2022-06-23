var button = document.getElementById("create_button");
var text_field = document.getElementById("create_form_text");


document.getElementById("create_form").onsubmit = function() {
    button.ariaBusy = true;
    button.setAttribute("aria-busy", "true");
}


text_field.onkeyup = function() {
    if (text_field.value == ""){
        text_field.removeAttribute("aria-invalid");
        return;
    }

    var re = /^[_A-Za-z0-9\.]{2,30}$/;
    if (re.exec(text_field.value)) {
        text_field.setAttribute("aria-invalid", "false");
    } else {
        text_field.setAttribute("aria-invalid", "true");
    }
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

function text_to_clipboard(text) {
    navigator.clipboard.writeText(text);
}