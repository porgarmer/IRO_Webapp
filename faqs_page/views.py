from django.shortcuts import render

# Create your views here.
def faqs_page(request):
    
    return render(request, 'faqs_page/faqs_homepage.html') 

def faqs_page(request):
    items = [
        {'id': 1, 'title': 'Where are Your Shelters Located ?', 'description': 'Cebu City, Mandaue, Consolacion, Barili.'},
        {'id': 2, 'title': 'What is Your Adoption Process ?', 'description': 'This is the second item description.'},
        {'id': 3, 'title': 'What In-Kind Donations are Needed ?', 'description': 'This is the third item description.'},
        {'id': 4, 'title': 'What are the Requirements to Adopt ?', 'description': 'This is the third item description.'},
        {'id': 5, 'title': 'How can I get to your Shelters via Public Transportation ?', 'description': 'This is the third item description.'},

    ]
    return render(request, 'faqs_page/faqs_homepage.html', {'items': items})