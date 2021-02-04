import OpenDartReader
api_key = 'd92e1e01ed0185352a4b4ca637c89b4f83acae78'

dart = OpenDartReader(api_key)

# 단일기업 전체 재무제표 (삼성전자 2018 전체 재무제표)
dart.finstate_all('005930', 2018)

print(dart.finstate_all('005930', 2018))
