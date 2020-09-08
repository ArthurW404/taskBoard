function add_col() {

    // get string that is in the text form for setting col name
    var new_name = document.querySelector("#new_col_name");
    var col_name = new_name.value;
    
    

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
            new_name.value = ""; 
            window.location.reload()
        }) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
        
}

function add_issue() {
    fetch("/add_item", {
        method: "POST"
    })
        .then(() => window.location.reload()) // reloads page
        .catch((error) => console.log("Something went wrong: " + error));
}