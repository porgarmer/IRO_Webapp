function updateUrlParam(param, value) {
    const url = new URL(window.location);
    url.searchParams.set(param, value); // Set the specified parameter
    // url.searchParams.set('page', 1); // Reset to the first page
    window.history.pushState({}, '', url); // Update the browser URL
    location.reload(); // Reload the page
}

$("#category").change(function (e) { 
    const selectedOption = this.value;
    updateUrlParam('category', selectedOption)
});

