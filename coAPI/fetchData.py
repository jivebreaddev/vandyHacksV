import requests
import random

def merchant_data():
    merchant_url = 'http://api.reimaginebanking.com/merchants?key=f6b2994f930f3175da90249976afd314'
    merchant = {}
    merchant['Saurabh Bhandari'] = 'sbhandari155708@troy.edu'
    merchant['Sichang Park'] = 'spark@troy.edu'
    merchant['Bikal Lamichhane'] = 'blamichhane@troy.edu'
    emails = ['@gmail.com', '@yahoo.com', '@outlook.com']
    r2 = requests.get(url=merchant_url, params=None)
    data2 = r2.json()
    for elem in data2:
        name = elem['name']
        email_id = elem['_id']
        mer_email = email_id + emails[random.randint(0, 2)]
        merchant.update({
            name: mer_email
        })
    return merchant


def main():
    merchant_data()


if __name__ == '__main__':
    main()


