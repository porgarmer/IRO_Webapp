// $(document).ready(function () {
//     $('#addBlogForm').on('submit', function (e) {
//         e.preventDefault();

//         const formData = new FormData(this); // Capture the form data, including files

//         $.ajax({
//             type: 'POST',
//             url: "news-articles",
//             data: formData,
//             processData: false, // Prevent jQuery from automatically processing the data
//             contentType: false, // Let the browser set the Content-Type, including the multipart boundary
//             headers: {
//                 'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(), // Include the CSRF token
//             },
//             success: function (response) {

//                 location.reload()

//            },
//             error: function (response) {
//                 toastr.error('An error occurred while adding the post.', 'Error');
//             }
//         });
//     });

//     // Edit Blog Form Submission
//     $('#editBlogForm').on('submit', function (e) {
//         e.preventDefault();
//         const formData = new FormData(this);
//         const newsarticleId = $(this).find('input[name="newsarticle_id"]').val();
//         $.ajax({
//             type: 'POST',
//             url: `edit-news&articles/${newsarticleId}/`,
//             data: formData,
//             processData: false,
//             contentType: false,
//             headers: {
//                 'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(), // Include the CSRF token
//             },
//             success: function (response) {
//                 location.reload();
//             },
//             error: function (response) {
//                 toastr.error('An error occurred while editing the post.', 'Error');
//             }
//         });
//     });
// });
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


    const deleteModal = new bootstrap.Modal(document.getElementById('deleteNewsArticleModal'));
    $("#delete-count").text(selectedIds.length)
    deleteModal.show()

    deleteForm = $("#delete-form")
    $("#delete-form").on('submit', function (e) { 
        e.preventDefault();
        $("#ids").val(selectedIds);
        this.submit()
    })  
});


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

$("#category-news_article").change(function (e) { 
    const selectedOption = this.value;
    updateUrlParam('category', selectedOption)
});

$("#name-sort").change(function (e) { 
    const selectedOption = this.value;
    updateUrlParam('name-sort', selectedOption)
});