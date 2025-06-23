import json

import requests
from tabulate import tabulate


def test_predict_endpoint():
    """시계열 예측 엔드포인트를 테스트하는 함수"""

    # FastAPI 서버 URL (기본 포트 8000)
    base_url = (
        "https://time-series-autoai.1wpveihz0wfq.us-south.codeengine.appdomain.cloud"
    )
    endpoint = f"{base_url}/predict"

    print("🚀 FastAPI 시계열 예측 엔드포인트 테스트 시작")
    print(f"📍 테스트 URL: {endpoint}")
    print("-" * 50)

    # 테스트 케이스들
    test_cases = [
        {"forecast_window": 1, "description": "1일 예측"},
        {"forecast_window": 3, "description": "3일 예측 (기본값)"},
        {"forecast_window": 7, "description": "7일 예측"},
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 테스트 케이스 {i}: {test_case['description']}")

        # 요청 데이터
        payload = {"forecast_window": test_case["forecast_window"]}

        try:
            # POST 요청 보내기
            response = requests.post(
                endpoint,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30,
            )

            print(f"📡 요청 데이터: {json.dumps(payload, indent=2)}")
            print(f"🔄 응답 상태코드: {response.status_code}")

            if response.status_code == 200:
                # 성공 응답 처리
                result = response.json()
                predictions = result.get("predictions", [])

                print("✅ 요청 성공!")
                print(f"📈 예측 결과 ({len(predictions)}개 레코드):")

                if predictions:
                    # 테이블 형태로 예쁘게 출력
                    print(predictions)
                else:
                    print("⚠️  예측 데이터가 비어있습니다.")

            else:
                # 에러 응답 처리
                print(f"❌ 요청 실패: {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"🔍 에러 상세: {json.dumps(error_detail, indent=2)}")
                except:
                    print(f"🔍 에러 메시지: {response.text}")

        except requests.exceptions.ConnectionError:
            print("❌ 연결 실패: FastAPI 서버가 실행 중인지 확인하세요.")
            print("💡 서버 실행 명령: fastapi run time_series_forecast.py")
            break

        except requests.exceptions.Timeout:
            print("⏰ 요청 타임아웃: 서버 응답이 너무 오래 걸립니다.")

        except Exception as e:
            print(f"💥 예상치 못한 오류: {str(e)}")

        print("-" * 50)


if __name__ == "__main__":
    print("🧪 FastAPI 시계열 예측 API 테스트 도구")
    print("=" * 60)

    # if server_ok:
    # 2. 엔드포인트 테스트
    print("\n2️⃣ 엔드포인트 테스트")
    test_predict_endpoint()

    print("\n🏁 테스트 완료!")
