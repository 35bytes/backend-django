# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
  {
    'title': 'Mont Blanc',
    'user': {
      'name': 'Yésica Cortés',
      'picture': 'https://picsum.photos/60/60/?image=1027'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/600?image=1036',
  },
  {
    'title': 'Via Láctea',
    'user': {
      'name': 'Christian Van der Henst',
      'picture': 'https://picsum.photos/60/60/?image=1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/800/800/?image=903',
  },
  {
    'title': 'Nuevo auditorio',
    'user': {
      'name': 'Uriel (thespianartist)',
      'picture': 'https://picsum.photos/60/60/?image=883'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://picsum.photos/500/700/?image=1076',
  }
]

@login_required
def list_posts(request):
  """List existing posts."""
  return render(request, 'posts/feed.html', {'posts': posts})