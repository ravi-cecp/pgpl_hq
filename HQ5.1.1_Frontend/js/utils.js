// UTC Timestamp: <insert UTC timestamp here>
// File: js/utils.js

function loadComponent(id, url) {
    fetch(url)
        .then((response) => response.text())
        .then((html) => {
            document.getElementById(id).innerHTML = html;
        })
        .catch((err) => console.error('Error loading component:', err));
}
