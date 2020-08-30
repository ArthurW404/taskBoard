
function add_col() {
    console.log(":F");
    fetch("/add_column", {
        method: "POST"
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}

function add_issue11() {
    console.log(":FUCK");
    fetch("/add_item", {
        method: "POST"
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}