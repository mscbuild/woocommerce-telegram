from woocommerce import API
from .config import WC_URL, WC_KEY, WC_SECRET

wcapi = API(
    url=WC_URL,
    consumer_key=WC_KEY,
    consumer_secret=WC_SECRET,
    version="wc/v3"
)

def get_latest_order():
    orders = wcapi.get("orders").json()
    return orders[0] if orders else None
