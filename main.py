# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from imageai.Detection import ObjectDetection


def detect_from_image(probability=30):
    object_detector = ObjectDetection()
    object_detector.setModelTypeAsYOLOv3()
    print('got here')
    # Load the trained model.
    object_detector.setModelPath('models/yolo.h5')
    object_detector.loadModel()
    directory = 'input'
    detections = []
    for file in os.listdir(directory):
        print(file)
        if os.path.isfile(os.path.join(directory, file)):
            detections.append(object_detector.detectObjectsFromImage(input_image=os.path.join(directory, file),
                                                                     output_image_path=os.path.join('output', file),
                                                                     minimum_percentage_probability=probability))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    detect_from_image()
