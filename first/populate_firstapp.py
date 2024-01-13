import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')

import django
django.setup()

## Fake pop script
import random
from firstapp.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen = Faker()
topic = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

## add the fake data 
## using instead of shell command
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        ## get topic for entry 
        top = add_topic()
        
        ## creating fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        ## creating new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        ## create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
        
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
    

    


        