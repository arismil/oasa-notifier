import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["POST"])
def message(request):
    if request.method == "POST":
        if request.data["message"]["text"]:
            requests.post(
                url="https://chatapi.viber.com/pa/send_message",
                json={
                    "receiver": "Y/WGvosl2THqAOzX8ZSKOg==",
                    "sender": {"name": "Bus Helper"},
                    "tracking_data": "tracking data",
                    "type": "text",
                    "text": request.data["message"]["text"],
                },
                headers={
                    "X-Viber-Auth-Token": "502ffbbd70a7e53f-7c2fccec81219468-5d3130e602ebb845"
                },
                timeout=20,
            )
        return Response({})
