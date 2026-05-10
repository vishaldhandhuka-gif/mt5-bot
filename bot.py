# Stage 1: Real MT5 Connection + Test Order Bot
# This code actually connects to MT5 and can place a test BUY order.

import MetaTrader5 as mt5

# =========================
# ACCOUNT SETTINGS
# =========================
LOGIN = 433568113
PASSWORD = "vi895656@UM"
SERVER = "Exness-MT5Trial7"

# Symbols and Lot Sizes
SYMBOLS = {
    "BTCUSD": 0.50,
    "ETHUSD": 10.00
}

DEVIATION = 20
MAGIC = 123456
COMMENT = "Stage1TestBot"

# =========================
# CONNECT TO MT5
# =========================
print("Initializing MT5...")

if not mt5.initialize():
    print("MT5 initialize failed")
    print(mt5.last_error())
    quit()

if not mt5.login(LOGIN, password=PASSWORD, server=SERVER):
    print("Login failed")
    print(mt5.last_error())
    mt5.shutdown()
    quit()

print("Connected successfully!")
print("Account:", LOGIN)
print("Server:", SERVER)

# =========================
# SHOW SYMBOL STATUS
# =========================
for symbol, lot in SYMBOLS.items():
    info = mt5.symbol_info(symbol)
    if info is None:
        print(f"{symbol}: Symbol not found")
        continue

    if not info.visible:
        mt5.symbol_select(symbol, True)

    tick = mt5.symbol_info_tick(symbol)
    if tick:
        print(f"{symbol}: Bid={tick.bid}, Ask={tick.ask}, Lot={lot}")
    else:
        print(f"{symbol}: No market data")

# =========================
# OPTIONAL TEST ORDER
# Set to True only if you want to open a real demo trade.
# =========================
PLACE_TEST_ORDER = False

if PLACE_TEST_ORDER:
    symbol = "BTCUSD"
    lot = SYMBOLS[symbol]

    tick = mt5.symbol_info_tick(symbol)
    if tick:
        price = tick.ask
        sl = price - 1000
        tp = price + 3000

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": DEVIATION,
            "magic": MAGIC,
            "comment": COMMENT,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)

        if result and result.retcode == mt5.TRADE_RETCODE_DONE:
            print("Test BUY order opened successfully!")
            print("Ticket:", result.order)
        else:
            print("Order failed")
            print("Result:", result)

# =========================
# CLEANUP
# =========================
mt5.shutdown()
print("Stage 1 completed successfully.")
