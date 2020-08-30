function add_col() {
    fetch("/add_column", {
        method: "POST"
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