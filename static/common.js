var curr_board;

function change_board(board_name) {

    fetch("/change_board", {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: board_name
        })
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}

function add_board() {
    // get string that is in the text form for setting col name
    var name_inp = document.querySelector("#new_board_name");
    var board_name = name_inp.value;
    
    fetch("/add_board", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: board_name
        })
    })
        .then(() => {
            window.location.reload()
        }) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}

function login() {
    var username_inp = document.querySelector("#username");
    var username = username_inp.value;
    var password_inp = document.querySelector("#password");
    var user_password = password_inp.value;

    fetch("/login", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: username,
            password: user_password
        })
    })
    .then(() => {
        window.location.assign("/home")
    }) 
    .catch((error) => console.log("Something went wrong: " + error));
}

function signup() {
    var username_inp = document.querySelector("#signup_username");
    var username = username_inp.value;
    var password1_inp = document.querySelector("#new_password1");
    var password1 = password1_inp.value;
    var password2_inp = document.querySelector("#new_password2");
    var password2 = password2_inp.value;

    var signup_msg = document.querySelector("#signup_message");
    alert("G");

    // check both passwords are equal otherwise indicate passwords must be the same
    if (password1 != password2) {
        signup_msg.innerHTML = "Passwords are not the same";
        return;
    } else {
        signup_msg.innerHTML = "";
    }
    alert("F");
    fetch("/signup", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: username,
            password: password1
        })
    })
    .then(() => {
        window.location.assign("/home")
    }) 
    .catch((error) => console.log("Something went wrong: " + error));
}

function logout(){
    fetch("/logout", {
        method: "GET"
    })
    .then(() => {
        window.location.assign("/")
    })
    .catch((error) => console.log("Something went wrong: " + error));
}

