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
