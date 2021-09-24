import pyupbit

# get_ohlcv 함수는 고가/시가/저가/종가/거래량을 DataFrame으로 반환
df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1")
print(df.tail())