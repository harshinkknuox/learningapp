from django.utils.translation import gettext_lazy as _

PAGINATION_PERPAGE=10
UAE_TIMEZONE = 'Asia/Dubai'

CARD_CHOICES = [
	    ('2', _('2 cards per row'),),
        ('3', _('3 cards per row'),),
        ('4', _('4 cards per row'),),
    ]

# PAGE_TARGETS = [
#                     'course.CoursePage',
#                 ]

NEARBY_LOCATIONS = [
    ('Dubai', 'Dubai'),
    ('Abu Dhabi', 'Abu Dhabi'),
    ('Sharjah', 'Sharjah'),
]

COMMUNITIES = [
    ('Dubaic', 'Dubaic'),
    ('Abu Dhabic', 'Abu Dhabic'),
]

DEVELOPERS = [
    ('DubaiDev', 'DubaiDev'),
    ('Abu Dhabidev', 'Abu Dhabidev'),
]