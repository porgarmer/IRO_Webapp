const hamburger = document.querySelector("#toggle-btn");

hamburger.addEventListener("click", function() {
    document.querySelector("#sidebar").classList.toggle("expand");
})

const popup = document.getElementById('right-popup');
const popupMessage = document.getElementById('popup-message');

// Display popup messages dynamically using Django messages
const hiddenMessages = document.querySelectorAll('#hidden-messages p');

hiddenMessages.forEach(messageElement => {
    const messageText = messageElement.textContent.trim();
    const messageTag = messageElement.dataset.tag || 'info'; // Default to 'info' if no tag provided

    if (messageText) {
        // Set the message text
        popupMessage.textContent = messageText;

        // Remove existing tag classes (e.g., 'success', 'error') before applying the new one
        popup.className = 'right-popup'; // Reset classes
        popup.classList.add(messageTag); // Add the tag class (e.g., 'success')

        // Show the popup
        popup.classList.add('show');

        // Hide the popup after 4 seconds
        setTimeout(() => {
            popup.classList.remove('show');
        }, 4000);
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
