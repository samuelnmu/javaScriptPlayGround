// Set up the page and attach event listeners to buttons
document.addEventListener("DOMContentLoaded", function () {
    // Attach click event listeners to all buttons
    document.querySelectorAll("button").forEach(button => {
        button.onclick = function () {
            showPage(this.dataset.page); // Call showPage with the data-page value
        };
    });

    // Initialize by showing the first page (optional)
    // showPage("page1");
});

function showPage(page) {
    // Hide all div elements
    document.querySelectorAll("div").forEach(div => {
        div.style.display = "none";
    });

    // Display the specific div with the given id
    const targetDiv = document.querySelector(`#${page}`);
    if (targetDiv) {
        targetDiv.style.display = "block";
    } else {
        console.error(`No element found with id: ${page}`);
    }
}
