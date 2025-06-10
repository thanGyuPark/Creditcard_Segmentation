from flask import Flask, request, Response, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("api_sample.html")

@app.route('/getApiCall', methods=['GET', 'POST'])
def get_api_call():
    # 인증키 및 기본값 설정
    AUTH_KEY = "inu=0XIxbTS069ZThQY=jBaJZdYW3vhP8f66Yz90y3M="
    API_TYPE = "TO0"

    # 클라이언트에서 받은 파라미터
    localcode = request.values.get('localcode')
    bgnYmd = request.values.get('bgnYmd')
    endYmd = request.values.get('endYmd')

    # 요청 URL 구성
    base_url = f"http://www.localdata.go.kr/platform/rest/{API_TYPE}/openDataApi"
    params = {
        "authKey": AUTH_KEY,
        "resultType": "xml"
    }
    if localcode:
        params["localCode"] = localcode
    if bgnYmd and endYmd:
        params["bgnYmd"] = bgnYmd
        params["endYmd"] = endYmd

    # API 호출
    response = requests.get(base_url, params=params)

    # 결과 XML 그대로 클라이언트에 반환
    return Response(response.text, content_type="text/xml; charset=utf-8")


if __name__ == "__main__":
    app.run(debug=True)