function add_col() {
    var col_name = "Test";
    fetch("/add_column", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            name: col_name
        })
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}

function add_issue() {
    fetch("/add_item", {
        method: "POST"
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}