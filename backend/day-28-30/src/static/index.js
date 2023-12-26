const updateBtns = document.querySelectorAll(".display-update");
const deleteBtns = document.querySelectorAll(".display-delete");
const updateEntryBtn = document.getElementById("updateEntryBtn");

const updateWebsite = document.getElementById("updateWebsite");
const updateEmail = document.getElementById("updateEmail");
const updatePassword = document.getElementById("updatePassword");
let id;

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", (event) => {
        const parentNode = event.target.parentNode;
        id = parentNode.dataset.id;
        updateWebsite.value = parentNode.dataset.website;
        updateEmail.value = parentNode.dataset.email;
        updatePassword.value = parentNode.dataset.password;
    });

    deleteBtns[i].addEventListener("click", (event) => {
        id = event.target.parentNode.dataset.id;
        fetch(`delete/${id}`, {
            method: "DELETE"
        }).then(data => data.json()).then(_ => window.location.href = "/")
    })
}

updateEntryBtn.addEventListener("click", () => {
    fetch(`update/${id}`, {
        body: JSON.stringify({website: updateWebsite.value, email: updateEmail.value, password: updatePassword.value}),
        headers: {
            "Content-Type": "application/json"
        },
        method: "PATCH"
    }).then(data => data.json()).then(_ => window.location.href = "/")
});
