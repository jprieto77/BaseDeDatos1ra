// Ejemplo de validación en register.js
document.querySelector('form').addEventListener('submit', function (e) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        e.preventDefault();
        alert('Las contraseñas no coinciden');
    }
});
