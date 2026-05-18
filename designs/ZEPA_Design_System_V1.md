# 🎨 ZEPA 디자인 시스템 스펙 (Dashboard Edition)

## 1. 브랜드 핵심 요소 (Core Branding)

*   **브랜드 이름:** ZEPA
*   **한 줄 소개:** 1인 AI 마스터
*   **타겟 감성:** 신뢰성, 첨단 기술, 간결함, 자신감 (Trustworthy, High-Tech, Minimal)

### 1.1. 컬러 팔레트 (Color Palette)
| 역할 | 이름 | Hex Code | 사용처 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | ZEPA Blue | `#007BFF` | CTA 버튼, 핵심 강조 지표, 활성 상태 | 신뢰성 부여 |
| **Secondary** | Success Green | `#28A745` | 수익 발생, 긍정적 변화, '매수' 신호 | 성공적 결과 강조 |
| **Danger** | Loss Red | `#DC3545` | 손실 발생, 위험 경고, '매도' 신호 | 경고 및 손실 표시 |
| **Background** | Dark Gray | `#1F2937` | 전체 배경 (모던한 느낌) |
| **Surface** | Light Gray | `#374151` | 카드, 위젯 배경 (대비) |
| **Text** | White | `#FFFFFF` | 텍스트 기본 색상 |

### 1.2. 타이포그래피 (Typography)
*   **폰트:** Pretendard (가독성이 높고 모던함)
*   **H1 (제목):** 32px, Bold, ZEPA Blue (섹션 제목)
*   **H2 (소제목):** 20px, SemiBold, White (위젯 제목)
*   **Body:** 14px, Regular, White (본문 텍스트)
*   **Data Label:** 16px, SemiBold, White (수치 데이터)

## 2. 핵심 컴포넌트 (Core Components)

### 2.1. KPI 카드 (Key Performance Indicator Card)
*   **용도:** 현재 포트폴리오 가치, 총 수익률 등 핵심 수치 요약.
*   **레이아웃:** 1x4 그리드 (반응형).
*   **구조:**
    *   제목 (H2): `총 수익률`
    *   메인 값 (Data Label): `+15.2%` (폰트: 36px, Bold)
    *   변동 화살표: (Success Green) $\uparrow$ `vs. -0.5% (전일)` (작은 폰트)
*   **배경:** Surface (`#374151`)

### 2.2. 차트 영역 (Chart Area)
*   **용도:** 시간 흐름에 따른 가격 변화, 지표 추이 시각화.
*   **레이아웃:** 100% 너비, 400px 높이.
*   **요구사항:**
    *   **캔들스틱 차트:** 메인 차트.
    *   **보조 지표:** RSI, MACD 등의 오버레이 차트를 하단에 배치.
    *   **인터랙션:** 마우스 오버 시 정확한 시점의 가격 정보를 툴팁으로 표시해야 함.

### 2.3. 입력 폼 (Input Form)
*   **용도:** 사용자가 수동으로 파라미터를 입력하거나 전략을 선택하는 영역.
*   **요소:**
    *   라벨 (Label): `손절 라인 설정` (Body 폰트)
    *   인풋 필드 (Input Field): `[-----]` (가로 100% 너비, 높이 40px, 배경: Dark Gray)
    *   슬라이더 (Slider): (범위 값 표시)

## 3. 대시보드 레이아웃 구조 (Dashboard Layout)

*   **전체 구조:** 사이드바 (네비게이션) + 메인 콘텐츠 영역.
*   **섹션 1: 최상단 요약 (KPI Bar)**
    *   [KPI 카드 1] [KPI 카드 2] [KPI 카드 3] [KPI 카드 4]
*   **섹션 2: 메인 차트 및 분석 (Primary Chart)**
    *   (캔들스틱 차트) $\rightarrow$ (보조 지표)
*   **섹션 3: 전략 파라미터 및 실행 (Control Panel)**
    *   (입력 폼 1: 전략 선택) $\rightarrow$ (입력 폼 2: 기간 설정) $\rightarrow$ **[실행 버튼]** (Primary Button)