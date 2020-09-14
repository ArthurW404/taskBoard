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
    var msg = document.querySelector("#add_board_msg");
    var board_name = name_inp.value;
    if (board_name == "") {
        msg.innerHTML = "<p>Name of board cannot be empty</p>";
        return;
    }
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

function del_board(board_name) {
    console.log(board_name);
    fetch("/delete_board", {
        method: "DELETE",
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