import os

import numpy
import Image
from decaf.scripts.imagenet import DecafNet

def label(data_path, number_of_labels=1, equal_weights=True):
    """ 
    Create annotation files for directories of pictures. 
    Number of labels returned can be adjusted.
    Equal weighting of predictions.
    """
    net = DecafNet()

    entities = os.listdir(data_path)
    for entity in entities:
        labels = []
        pictures = os.listdir(os.path.join(data_path,entity))
        for picture in pictures:
            imarray = numpy.array(Image.open(os.path.join(data_path,entity,picture)))
            scores = net.classify(imarray)
            predictions = net.top_k_prediction(scores,number_of_labels) # Format:([confidence],[labels])
            labels.extend(predictions[1])
        
        if equal_weights:
            prediction = max(set(labels),key=labels.count)
        elif confidence_weights:
            pass

        with open("label.txt","w") as opened_file:
            opened_file.write(prediction)

if __name__ == "__main__":
    label("")
