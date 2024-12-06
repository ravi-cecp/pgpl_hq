// js/main.js
// UTC Timestamp: 2024-12-05 12:34
// Main JavaScript logic for frontend

// Login logic
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            window.location.href = '/dashboard';
        } else {
            document.getElementById('error-message').innerText = data.message;
        }
    })
    .catch(err => console.error('Error during login:', err));
}

// Approve user logic
function approveUser(userId) {
    fetch(`/approve_user/${userId}`, { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.reload();
    })
    .catch(err => console.error('Error during approval:', err));
}

// Fetch modules for a user
function fetchModules() {
    fetch('/modules')
    .then(response => response.json())
    .then(data => {
        const modulesContainer = document.getElementById('modules-container');
        data.modules.forEach(module => {
            const moduleElement = document.createElement('div');
            moduleElement.innerText = module.name;
            modulesContainer.appendChild(moduleElement);
        });
    })
    .catch(err => console.error('Error fetching modules:', err));
}
