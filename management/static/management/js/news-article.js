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

       // Enable Bulk Delete Button
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

    console.log(selectedIds)


    const deleteModal = new bootstrap.Modal(document.getElementById('deleteNewsArticleModal'));
    $("#delete-count").text(selectedIds.length)
    deleteModal.show()

    deleteForm = $("#delete-form")
    $("#delete-form").on('submit', function (e) { 
        e.preventDefault();
        $("#newsarticleIds").val(selectedIds);
        this.submit()
    })  
});