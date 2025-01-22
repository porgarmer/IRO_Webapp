const hamburger = document.querySelector("#toggle-btn");

hamburger.addEventListener("click", function() {
    document.querySelector("#sidebar").classList.toggle("expand");
})

const popup = document.getElementById('right-popup');
const popupMessage = document.getElementById('popup-message');

// Display popup messages if hidden success messages are present
const hiddenMessages = document.querySelectorAll('div[style="display:none;"] p');
hiddenMessages.forEach(message => {
    const trimmedMessage = message.textContent.trim();
    console.log("Message Found:", trimmedMessage); // Debug: Check if message is retrieved
    if (trimmedMessage) {
        popupMessage.textContent = trimmedMessage;
        popup.classList.add('show');

        setTimeout(() => {
            popup.classList.remove('show');
        }, 3000); // Hide popup after 3 seconds
    }
});



document.querySelectorAll('#sidebar:not(.expand) .sidebar-item').forEach(item => {
    item.addEventListener('mouseenter', function () {
        const dropdown = this.querySelector('.sidebar-dropdown');
        if (dropdown) {
            const sidebar = document.querySelector('#sidebar');
            const rect = this.getBoundingClientRect(); // Get the link's position relative to the viewport
            const sidebarScrollTop = sidebar.scrollTop; // Get the scroll position of the sidebar

            // Adjust the dropdown position
            dropdown.style.top = `${rect.top + sidebarScrollTop - sidebar.getBoundingClientRect().top}px`;
        }
    });

    item.addEventListener('mouseleave', function () {
        const dropdown = this.querySelector('.sidebar-dropdown');
        if (dropdown) {
            dropdown.style.top = '0'; // Reset position when not hovered
        }
    });
});
