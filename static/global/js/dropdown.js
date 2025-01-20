document.addEventListener('DOMContentLoaded', function () {
    // Select all dropdown links
    const dropdownLinks = document.querySelectorAll('.nav-item.dropdown > a.nav-link');

    dropdownLinks.forEach(link => {
        // Add click event to allow navigation
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href && href !== '#') {
                // Navigate to the link's href
                window.location.href = href;
            }
        });
    });
});