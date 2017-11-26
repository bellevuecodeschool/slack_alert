from price_bot import PriceBot
from slack_client import SlackClient

price_bot = PriceBot()
slacK_client = SlackClient()

price = price_bot.get_price()
print(price)

if price < 200:
    msg = 'Item is available at £{}'.format(price)
    slack_client.call_slack(msg)

#msg = input('Enter message: ')
#slack_client.call_slack(msg)
