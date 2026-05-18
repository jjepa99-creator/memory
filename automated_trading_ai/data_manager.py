import pandas as pd
import numpy as np
import pandas_datareader as pdr
from typing import List, Dict

class DataManager:
    """
    금융 데이터를 수집, 정제, 통합하는 데이터 관리자.
    """
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data: pd.DataFrame = pd.DataFrame()

    def fetch_price_data(self, exchange: str = 'yahoo') -> pd.DataFrame:
        """
        OHLCV 데이터를 외부 소스에서 가져와서 저장합니다.
        :param exchange: 데이터 출처 (e.g., 'yahoo', 'kraken')
        :return: 가격 데이터가 담긴 DataFrame
        """
        print(f"[{self.ticker}] {exchange}에서 OHLCV 데이터를 가져오는 중...")
        try:
            # 예시: Yahoo Finance 사용
            data = pdr.get_data_yahoo(self.ticker, start=self.start_date, end=self.end_date)
            self.data = data.reset_index()
            print("✅ 가격 데이터 로드 완료.")
            return self.data
        except Exception as e:
            print(f"❌ 가격 데이터 로드 실패: {e}")
            return pd.DataFrame()

    def fetch_sentiment_data(self, source: str) -> pd.DataFrame:
        """
        외부 비정형 데이터 (뉴스 감성 점수, 경제 지표 등)를 가져와서 통합합니다.
        실제 구현 시, API 호출 로직이 필요합니다.
        :param source: 데이터 출처 (e.g., 'news', 'macro')
        :return: 감성 점수 데이터가 담긴 DataFrame
        """
        print(f"[{self.ticker}] {source}에서 비정형 데이터 로드 중...")
        # Placeholder: 실제 API 호출 및 데이터 파싱 로직이 들어갑니다.
        dummy_data = pd.DataFrame({
            'Date': pd.to_datetime(pd.date_range(start=self.start_date, end=self.end_date, freq='D')),
            'Sentiment_Score': np.random.uniform(-1.0, 1.0, size=len(pd.date_range(start=self.start_date, end=self.end_date, freq='D'))),
        })
        self.data = self.data.merge(dummy_data, on='Date', how='left')
        print("✅ 감성 데이터 로드 및 통합 완료.")
        return self.data

    def preprocess_data(self) -> pd.DataFrame:
        """
        데이터를 결측치 처리, 정규화, 특성 엔지니어링하여 모델 입력 형태로 만듭니다.
        """
        print("⚙️ 데이터 전처리 및 특성 엔지니어링 시작...")
        # TODO: 결측치 처리, 로그 변환, 이동 평균 계산 등 복잡한 로직 구현 필요
        self.data = self.data.dropna()
        print(f"✅ 데이터 전처리 완료. 최종 데이터 크기: {len(self.data)} 행.")
        return self.data

if __name__ == '__main__':
    # 테스트 실행 예시
    print("=== DataManager 테스트 실행 ===")
    manager = DataManager(ticker="AAPL", start_date="2022-01-01", end_date="2023-12-31")
    df = manager.fetch_price_data()
    if not df.empty:
        df = manager.fetch_sentiment_data(source='news')
        final_df = manager.preprocess_data()
        print("\n--- 최종 데이터 구조 (Head) ---")
        print(final_df.head())
    else:
        print("테스트 실패: 가격 데이터 로드에 실패했습니다.")