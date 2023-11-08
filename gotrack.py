import sys
import os
from datetime import datetime
import time
import segment.analytics as analytics
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def mon():
    analytics.write_key = 'YOUR WHITE KEY'
    analytics.oauth_client_id = 'YOUR ANALYTICS CLIENT ID'
    analytics.identify('j5ca137295', {
        'name': 'Jean Tinoco',
        'email': 'ticaps@ticapsoriginal.com',
        'created_at': datetime.now()
    })
    analytics.track('j5ca137295', 'Signed Up', {
      'plan': 'Free Plan'
    })
    analytics.track('j5ca137295', 'Ticapsoriginal Page', {
        'title': 'Ticapsoriginal page',
        'subtitle': 'only one from 24k',
        'author': 'Jean Tinoco'
    })
    time.sleep(1.8)
