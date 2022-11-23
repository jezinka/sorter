import requests

URL = "http://10.42.0.1:8000/predict"


def get_color_prediction(image_name):
    data = {"image_path": open(image_name, 'rb')}
    response = requests.post(url=URL, files=data)
    return response.json()["label_predictions"]


if __name__ == '__main__':
    print(get_color_prediction("sample/shot.jpg"))
