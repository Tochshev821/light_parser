import requests

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")
    with open("info.txt","w") as file:
        file.write(response.text)
    return response.text
def get_ticker(coin1="btc",coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")# разделяем дефисам если хотим получить несколько пар

    with open("ticker.txt","w") as file:
        file.write(response.text)
        return response.text

def get_depth(coin1="btc",coin2="usd",limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}?ignore_invalid=1")# разделяем дефисам если хотим получить несколько пар
    with open("depth.txt","w") as file:
        file.write(response.text)
    bids = response.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0
    for i in bids:
        price = i[0]
        coin_amount = i[1]
        total_bids_amount += price*coin_amount

    return f"total bids: {total_bids_amount} $"# last 150 orders

def get_trades(coin1="btc",coin2="usd",limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}?ignore_invalid=1")# разделяем дефисам если хотим получить несколько пар
    with open("trades.txt","w") as file:
        file.write(response.text)
    total_trade_ask = 0
    total_trade_bid = 0
    for i in response.json()[f"{coin1}_{coin2}"]:
        if i["type"] == "ask":
            total_trade_ask += i["price"]* i["amount"]
        else:
            total_trade_bid += i["price"]* i["amount"]
        info = f"[-] TOTAL {coin1} sell: {total_trade_ask} $\n TOTAL {coin1} buy: {total_trade_bid} $"

    return info

def main():
    #print(get_info())
    #print(get_ticker())
    #print(get_ticker(coin1="eth",coin2="btc"))
    print(get_depth(coin1="doge"))# ордера на продажу\покупку
    print(get_trades())

if __name__ == '__main__':
    main()







