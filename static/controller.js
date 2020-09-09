var curr_button_id = -1;

function handle_issue_button(id) {
    curr_button_id = id;
    console.log(curr_button_id);
}

function add_col() {

    // get string that is in the text form for setting col name
    var name_inp = document.querySelector("#new_col_name");
    var col_name = name_inp.value;
    
    fetch("/add_column", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: col_name
        })
    })
        .then(() => {
            name_inp.value = ""; 
            window.location.reload()
        }) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}

function add_issue(col_id) {
    if (curr_button_id == -1) {
        console.log("Add issue button was not clicked!!");
        return;
    }
    var name_inp = document.querySelector("#new_issue_name");
    var description_inp = document.querySelector("#issue_descript");
    var issue_name = name_inp.value;
    var issue_descript = description_inp.value;
    fetch("/add_item", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: issue_name,
            description: issue_descript,
            col_id: curr_button_id
        })
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}