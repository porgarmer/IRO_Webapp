    // Display popup messages if hidden success messages are present
    const hiddenMessages = document.querySelectorAll('div[style="display:none;"] p');
    hiddenMessages.forEach(message => {
        const trimmedMessage = message.textContent.trim();
        if (trimmedMessage) {
            popupMessage.textContent = trimmedMessage;
            popup.classList.add('show');

            setTimeout(() => {
                popup.classList.remove('show');
            }, 3000); // Hide popup after 3 seconds
        }
    });



// $(document).ready(function () {
//     $('#addBlogForm').on('submit', function (e) {
//         e.preventDefault();
//         const formData = new FormData(this);
//         $.ajax({
//             type: 'POST',
//             url: "{% url 'management:news&articles' %}",
//             data: formData,
//             processData: false,
//             contentType: false,
//             headers: { 'X-CSRFToken': '{{ csrf_token }}' },
//             success: function (response) {
//                     alert(response.message);
//                     location.reload();  // Reload the page to update the newsarticle list
//             },
//             error: function (response) {
//                     alert('Error: ' + response.responseJSON.error);
//             }
//         });
//     });
//      $('form[id^="editBlogForm"]').on('submit', function (e) {
//                 e.preventDefault();
//                 const formData = new FormData(this);
//                 const newsarticleId = $(this).find('input[name="newsarticle_id"]').val();
//                 $.ajax({
//                     type: 'POST',
//                     url: `/edit-news&article/${newsarticleId}/`,
//                     data: formData,
//                     processData: false,
//                     contentType: false,
//                     headers: { 'X-CSRFToken': '{{ csrf_token }}' },
//                     success: function (response) {
//                         alert(response.message);
//                         location.reload();
//                     },
//                     error: function (response) {
//                         alert('Error: ' + response.responseJSON.error);
//                     }
//                 });
//             });
// });

    // Reinitialize CKEditor when a modal is opened
$(document).on('shown.bs.modal', function () {
    $('.ckeditor').each(function () {
        if (!CKEDITOR.instances[this.id]) {
            CKEDITOR.replace(this.id, {
                toolbar: 'full',
                height: 300,
                width: 'auto',
            });
        }
    });
});