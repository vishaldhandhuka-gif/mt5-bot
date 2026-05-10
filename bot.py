LOGIN = 433568113
PASSWORD = "vi895656@UM"
SERVER = "Exness-MT5Trial7"

SYMBOLS = {
    "BTCUSD": 0.50,
    "ETHUSD": 10.00
}

BUFFER_POINTS = 50
MAX_OPEN_TRADES = 1
DEVIATION = 20
MAGIC = 123456
COMMENT = "LiquiditySweepBot"

print("Multi-symbol bot configured successfully!")
print("BTCUSD Lot:", SYMBOLS["BTCUSD"])
print("ETHUSD Lot:", SYMBOLS["ETHUSD"])
print("Login:", LOGIN)
print("Server:", SERVER)
