function showRegisterForm() {
    document.getElementById('show-register-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
}

document.addEventListener("DOMContentLoaded", function () {
    var formFields = document.querySelectorAll('.form-field');

    formFields.forEach(function (field) {
        field.addEventListener('mouseover', function () {
            this.querySelector('.field-instruction').style.display = 'block';
        });

        field.addEventListener('mouseout', function () {
            this.querySelector('.field-instruction').style.display = 'none';
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var registrationForm = document.getElementById('registration-form');

    registrationForm.addEventListener('submit', function () {
        // Hide help text on form submission
        var helpTextElements = registrationForm.getElementsByClassName('help-text');
        for (var i = 0; i < helpTextElements.length; i++) {
            helpTextElements[i].style.display = 'none';
        }
    });
});