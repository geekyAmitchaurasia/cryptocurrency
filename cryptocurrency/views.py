from django.shortcuts import render
import requests


def home(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = api_request.json()
    return render(request, 'home.html', {'api': api})


def prices(request):
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,XLM,LTC,ADA,MIOTA,USDT,TRX,NEO,XMR,DASH,ETC,XEM,BNB,XTZ,OMG,VEN,ZEC,QTUM,ZRX&tsyms=USD")
    price = price_request.json()
    return render(request, 'prices.html', {'price': price})


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        search = search.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + search + "&tsyms=USD")
        crypto = crypto_request.json()

        return render(request, 'search.html', {'search': search, 'crypto': crypto})

    else:
        error = "please enter a valid Crypto Currency."
        return render(request, 'search.html', {'error': error})
