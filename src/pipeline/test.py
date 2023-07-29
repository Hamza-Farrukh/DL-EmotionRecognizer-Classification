# Custom
from src.pipeline.predict import Predict


if __name__ == "__main__":
    obj = Predict()
    result = obj.predict_with_premade('MyPic.jpg')
    print(result)
