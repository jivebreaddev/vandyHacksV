import requests


def merchant_data():
    merchant_url = 'http://api.reimaginebanking.com/merchants?key=f6b2994f930f3175da90249976afd314'
    merchant = {
        'name': "email",
    }
    r2 = requests.get(url=merchant_url, params=None)
    data2 = r2.json()
    for elem in data2:
        name = elem['name']
        email_id = elem['_id']
        mer_email = email_id + '@gmail.com'
        merchant.update({
            name: mer_email
        })
    return merchant


def main():
    merchant_data()


if __name__ == '__main__':
    main()