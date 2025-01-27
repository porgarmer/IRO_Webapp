function updateUrlParam(param, value) {
    const url = new URL(window.location);
    url.searchParams.set(param, value); // Set the specified parameter
    // url.searchParams.set('page', 1); // Reset to the first page
    window.history.pushState({}, '', url); // Update the browser URL
    location.reload(); // Reload the page
}


$("#date-sort").change(function (e) { 
    const selectedOption = this.value;
    updateUrlParam('date-sort', selectedOption)
});

function toggleBulkDeleteButton() {
    const anyChecked = $('.blogCheckbox:checked').length > 0;
    $('#bulkDeleteButton').prop('disabled', !anyChecked);
}

$('.blogCheckbox').on('change', function () {
    toggleBulkDeleteButton();
});

 // Select/Deselect All Checkboxes
 $('#selectAll').on('change', function () {
    $('.blogCheckbox').prop('checked', this.checked);
    toggleBulkDeleteButton();
});

       // Enable Bulk Delete Button For News&Articles
$('.blogCheckbox').on('change', function () {
        toggleBulkDeleteButton();
    });


function toggleBulkDeleteButton() {
        const anyChecked = $('.blogCheckbox:checked').length > 0;
        $('#bulkDeleteButton').prop('disabled', !anyChecked);
    }

$('#bulkDeleteButton').click(function (e) { 
    const selectedIds = $('.blogCheckbox:checked').map(function () {
        return $(this).val();
    }).get();


    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    $("#delete-count").text(selectedIds.length)
    deleteModal.show()

    deleteForm = $("#delete-form")
    $("#delete-form").on('submit', function (e) { 
        e.preventDefault();
        $("#ids").val(selectedIds);
        this.submit()
    })  
});
