This repository contains a deep learning project for classifying plant diseases using the InceptionV3 architecture pre-trained on ImageNet. The model is fine-tuned on a custom dataset of augmented plant disease images.

Key Features:
Dataset: Augmented plant disease dataset with 10 classes of tomato plant diseases.

Preprocessing: Utilized ImageDataGenerator for data augmentation (rescaling, shear, zoom, horizontal flip).

Model Architecture:
InceptionV3 base model with pre-trained ImageNet weights.
Custom dense layers added for classification.
Output layer with softmax activation for multi-class classification.

Training:
Data split into training and validation sets.
Used categorical_crossentropy as the loss function and adam optimizer.

Trained for 10 epochs with validation steps.
