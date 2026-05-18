# 🎨 ZEPA 대시보드 컴포넌트 기술 계약서 (V2.0)

## 🎯 목적
본 계약서는 UI/UX 디자인(Blueprint)을 코딩 단계에 직접 이식하기 위한 기술 사양서이다. 모든 개발자는 이 계약서를 최종 기준으로 삼아 컴포넌트를 구현해야 한다.

## 📜 적용 범위
*   **대시보드 전체 레이아웃:** Grid System (12 Column Base)
*   **주요 컴포넌트:** `ChartCard`, `FilterPanel`, `KPIWidget`, `ActivityFeed`

## 🧱 핵심 컴포넌트 정의 (Component Specification)

### 1. ChartCard (차트 카드)
*   **Props:**
    *   `title` (string): 차트 제목 (필수)
    *   `chartType` (enum): 'Line', 'Bar', 'Candle' (필수)
    *   `dataKey` (string): 백엔드 API에서 받아올 데이터 필드 (필수)
    *   `timeframe` (string): 시간 범위 ('1D', '1W', '1M' 등)
*   **State:**
    *   `isHovered` (boolean): 마우스 오버 시 상태 변화 (Tooltip 활성화)
*   **Interaction Logic:**
    *   `onTimeChange(newTimeframe)`: 클릭 시, 해당 컴포넌트와 연동된 모든 차트가 새 시간 범위로 리렌더링되어야 함.

### 2. FilterPanel (필터 패널)
*   **Props:**
    *   `filterGroup` (Array<Object>): 필터 항목 배열 (예: '종목', '거래량', '기간')
    *   `onFilterChange(key, value)`: 필터 변경 시 호출되는 콜백 함수 (전역 상태 관리와 연동)
*   **State:**
    *   `activeFilters` (Object): 현재 활성화된 필터들의 Key-Value 쌍.
*   **Interaction Logic:**
    *   모든 필터 변경은 전역 상태(`GlobalStore.filters`)를 업데이트하며, 대시보드 전체 컴포넌트에 즉시 반영되어야 함.

### 3. KPIWidget (핵심 지표 위젯)
*   **Props:**
    *   `label` (string): 지표 이름 (예: '오늘 수익률')
    *   `value` (number): 현재 값
    *   `change` (number): 전일 대비 증감률 (퍼센트 또는 절대값)
    *   `trendColor` (string): 상승/하락에 따른 색상 (Green/Red)
*   **Interaction Logic:**
    *   클릭 시: 해당 지표에 대한 상세 추이 그래프(모달)가 팝업되어야 함.

---