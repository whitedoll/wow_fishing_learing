# Wow fishing float detect

![0001](https://user-images.githubusercontent.com/60419530/122636445-431e0200-d124-11eb-957e-4c808863351f.jpg)
This project use [YOLOv5 object detection.](https://github.com/ultralytics/yolov5) You can find floats in various environments in the game.

# Inference with detect.py
You can use the pre-trained model best.pt to find a float. The requirements for [YOLOv5 object detection.](https://github.com/ultralytics/yolov5) can be installed by following the guide of the official site.:
```bash
python3 detect.py --source test/ --weights best.pt
```
    
The result save on "run/dectact"

# Training
The prepared datasets are wow_fish.zip, z01, and z02. you can check the following structure after unzipping the compressed file. 
    wow_fish
    ├── Annotations
    │   └── *.xml
    ├── images
    │   └── *.jpg
    ├── labels
    │   └── *.txt
