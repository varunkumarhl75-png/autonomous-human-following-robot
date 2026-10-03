# Autonomous Computer-Vision-Based Human-Following Robot

## 1. Project Overview

This project is a computer-vision prototype for a human-following robot. It detects a person in images or video, estimates the person's horizontal position and approximate distance from the camera, analyzes basic lighting and image structure, and produces a rule-based robot command. Commands are displayed as a simulation; the project does not drive a physical robot.

## 2. Problem Statement

A mobile robot following a person needs to identify the person, determine whether they are left, centered, or right in the camera view, estimate whether they are relatively near or far, and select an appropriate response. Poor visibility also calls for a conservative response. This project explores these steps using image and sampled-video inputs.

## 3. Objectives

- Detect people with YOLO11n.
- Estimate left, center, or right position from a detected bounding box.
- Estimate near, medium, or far distance from bounding-box height relative to image height.
- Apply K-Means to a detected-person crop as an auxiliary image-processing demonstration.
- Analyze brightness and edge structure for environment-aware safety decisions.
- Produce interpretable, rule-based simulated robot commands.
- Evaluate detection on the project's 18-image set and sampled frames from three videos.

## 4. System Architecture

```text
Image or video frame
        |
        v
YOLO11n person detection
        |
        +--> Person bounding box --> Horizontal position and approximate distance
        |
        +--> Detected-person crop --> K-Means image segmentation (auxiliary)
        |
        +--> Image brightness and edge analysis --> Environment condition
                                             |
                                             v
                             Rule-based safety and command logic
                                             |
                                             v
                                Simulated robot command
```

## 5. Dataset

The project uses 18 JPG images for the reported image evaluation and three video sequences named Crosswalk, Fourway, and Night for sampled-frame testing. The notebook also prepares a small fine-tuning dataset with 12 training images, 3 validation images, and 3 test images. The fine-tuning labels were generated as pseudo-labels using pretrained YOLO detections; they are not presented as independently verified ground-truth annotations.

The original project data is stored outside the `submission/` folder. The notebook refers to those project data paths.

## 6. Methodology

- **YOLO11n human detection:** Run the pretrained YOLO11n model and select person detections (COCO class 0) for downstream processing.
- **Bounding-box-based position estimation:** Compare the horizontal center of the person's bounding box with the image's left, center, and right regions.
- **Bounding-box-height-based distance estimation:** Compare the person's bounding-box height with the image height to assign a relative near, medium, or far category. This is a visual heuristic, not a metric distance measurement.
- **K-Means image segmentation:** Apply K-Means with five clusters to a detected-person image crop for visualization and auxiliary image processing. No claim is made that K-Means improves YOLO detection accuracy.
- **Environment-aware safety analysis:** Use grayscale image brightness and edge information to classify the scene as normal, low light, or dark/unclear. This is a simple safety-oriented analysis, not a full terrain or scene classifier.
- **Rule-based simulated robot commands:** Combine position, relative distance, and environment condition. The rules can request turns, following, forward movement, or a stop; low-light conditions make movement commands cautious, and a dark/unclear condition requests a stop.

## 7. Implementation

The implementation is in a Jupyter notebook and uses Python, Ultralytics YOLO, OpenCV, NumPy, Matplotlib, and scikit-image. The notebook includes image-processing experiments, person detection, position and distance heuristics, K-Means visualization, environment analysis, command logic, and image/video evaluation code.

The project files supplied for this submission include the notebook and pretrained model. The dataset remains in the original project folders rather than being copied into `submission/`.

## 8. Experimental Results

### 18-image evaluation

| Measure | Result |
| --- | ---: |
| Images tested | 18 |
| Person detections | 18/18 |
| Detection rate | 100% |
| Average YOLO confidence | 0.890 |

The 100% figure is the **detection rate on these 18 images**, not model accuracy.

Reported simulated command counts:

| Command                    |  Count |
| -------------------------- | -----: |
| FOLLOW                     |      5 |
| STOP                       |      6 |
| STOP - ENVIRONMENT UNCLEAR |      1 |
| TURN LEFT                  |      1 |
| TURN RIGHT                 |      3 |
| MOVE FORWARD               |      0 |
| **Total**                  | **16** |


These reported command counts sum to 16; they are reproduced as provided and are not treated as a complete 18-image breakdown.

### Sampled-video evaluation

| Video | Sampled frames detected | Detection rate |
| --- | ---: | ---: |
| Crosswalk | 76/76 | 100% |
| Fourway | 252/257 | 98.05% |
| Night | 107/113 | 94.69% |

These rates apply to the sampled AI frames reported by the project, not every frame in the original videos.

### Fine-tuning experiment

| Metric | Pretrained YOLO11n | Fine-tuned model |
| --- | ---: | ---: |
| Precision | 0.986 | 0.003 |
| Recall | 1.000 | 1.000 |
| mAP50 | 0.995 | 0.913 |
| mAP50-95 | 0.995 | 0.523 |

Fine-tuning was an experiment using a very small pseudo-labeled dataset. It did not improve the pretrained model on the reported evaluation, so the final system uses pretrained YOLO11n.

## 9. Limitations

- The image dataset is small, so the reported image results should not be treated as evidence of broad generalization.
- Pseudo-labels were used for the fine-tuning experiment and may contain labeling errors.
- Robot commands are simulated outputs; they do not control a physical robot.
- Bounding-box height provides only a rough relative distance estimate and is not a calibrated distance measurement.
- The environment module is a basic environment-aware safety module, not a full terrain classifier.
- K-Means is an auxiliary segmentation step. No improvement to YOLO accuracy is claimed.
- Video detection rates are calculated on sampled frames.

## 10. How to Run

## 10. How to Run
1. Open the complete project folder in VS Code.
2. Make sure Python and the required packages are installed:
   - `ultralytics`
   - `opencv-python`
   - `numpy`
   - `matplotlib`
   - `scikit-image`
3. Open `submission/notebooks/Untitled.ipynb`.
4. Select the Python environment containing the required packages.
5. Run the notebook cells in order.
6. The pretrained YOLO11n weights are provided at:
   `submission/models/yolo11n.pt`

The notebook uses the project's original dataset folders. If the project is moved to another computer, update the local file paths in the notebook as required.

## 11. Project Structure

```text
submission/
├── notebooks/
│   └── Untitled.ipynb
├── models/
│   └── yolo11n.pt
├── results/
└── documentation/
    └── Autonomous_Human_Following_Robot_2
```
## 12. Individual Contributions

### Varun Kumar H L — Computer Vision & Machine Learning
- Integrated the pretrained YOLO11n human detector.
- Prepared the fine-tuning dataset.
- Conducted the pretrained versus fine-tuned YOLO experiment.
- Evaluated human detection on the project's image dataset.
- Implemented K-Means image segmentation as an auxiliary image-processing component.
- Worked on computer-vision model evaluation and results.

### Tanushree — Robot Decision & System Integration
- Implemented horizontal human-position estimation (LEFT/CENTER/RIGHT).
- Implemented relative distance estimation (NEAR/MEDIUM/FAR).
- Developed the environment-aware safety analysis module.
- Implemented rule-based simulated robot commands.
- Integrated the detection, environment, and decision components.
- Worked on sampled-video evaluation and result presentation.
## 13. Conclusion

This mini-project demonstrates an end-to-end computer-vision workflow for human detection, relative position and distance estimation, basic environment-aware safety analysis, and simulated following commands. The reported tests show person detections across the project's image set and sampled video frames. The small pseudo-labeled fine-tuning experiment did not outperform pretrained YOLO11n, so the pretrained model was retained. Further work would require larger independently labeled datasets and validation on a physical robot before making real-world performance claims.
