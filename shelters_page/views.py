from django.shortcuts import render

def shelters_page(request):
    shelters = [
        {
            'name': 'Camp IRO',
            'description': 'Providing open spaces and loving care for dogs in need.',
            'logo_url': '/static/pics/camp_iro.png',
            'button_text': 'Donate to Camp IRO',
            'images': [
                {'url': '/static/pics/iro1.png'},
                {'url': '/static/pics/iro2.png'},
                {'url': '/static/pics/iro3.png'},
                {'url': '/static/pics/iro4.png'},
            ],
        },
        {
            'name': 'IRO "O" Cattery',
            'description': 'A safe haven for kittens and cats.',
            'logo_url': '/static/pics/iro_o_cattery.png',
            'button_text': 'Sponsor a Cat',
            'images': [
                {'url': '/static/pics/cat1.png'},
                {'url': '/static/pics/cat2.png'},
                {'url': '/static/pics/cat3.png'},
                {'url': '/static/pics/cat4.png'},

            ],
        },
        {
            'name': 'IRO Tuesday Foster Home',
            'description': 'A safe haven for dogs and cats.',
            'logo_url': '/static/pics/iro_foster.png',
            'button_text': 'Foster a rescue',
            'images': [
                {'url': '/static/pics/foster1.png'},
                {'url': '/static/pics/foster2.png'},
                {'url': '/static/pics/foster3.png'},
                {'url': '/static/pics/foster4.png'},

            ],
        },
        {
            'name': 'IRO Lolo Ali Center(LAC)',
            'description': 'Retirement home for dogs.',
            'logo_url': '/static/pics/lolo_ali_center.png',
            'button_text': 'Home for dogs',
            'images': [
                {'url': '/static/pics/lolo1.png'},
                {'url': '/static/pics/lolo2.png'},
                {'url': '/static/pics/lolo3.png'},
                {'url': '/static/pics/lolo4.png'},

            ],
        },
    ]
    return render(request, 'shelters_page.html', {'shelters_page': shelters})
