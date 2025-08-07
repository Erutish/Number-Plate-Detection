# Number Plate Detection and Recognition

A comprehensive system for detecting and recognizing number plates from images and videos using YOLOv8 and EasyOCR.

## 🚀 Features

- **Number Plate Detection**: Uses YOLOv8 model to detect number plates in images and videos
- **OCR Recognition**: Implements EasyOCR for text extraction from detected plates
- **Web Application**: Streamlit-based web interface for easy interaction
- **Video Processing**: Real-time processing of video files
- **CSV Export**: Saves detection results to CSV files
- **Confidence Filtering**: Configurable confidence threshold for detections

## 📁 Project Structure

```
yolo/
├── detect_and_recognize.py    # Main detection and recognition script
├── preprocessing.py           # Data preprocessing utilities
├── training.ipynb            # YOLO model training notebook
├── number_plate.yaml         # YOLO dataset configuration
├── web_app/
│   ├── app.py               # Streamlit web application
│   └── uploads/             # Upload directory for web app
├── dataset/                 # Dataset directory (not included in repo)
├── runs/                    # Training outputs (not included in repo)
└── README.md               # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (optional, for faster processing)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd yolo
   ```

2. **Create and activate conda environment**
   ```bash
   conda create -n yolov8-py312 python=3.12
   conda activate yolov8-py312
   ```

3. **Install dependencies**
   ```bash
   pip install ultralytics
   pip install easyocr
   pip install opencv-python
   pip install torch torchvision
   pip install streamlit
   pip install pandas
   ```

## 🎯 Usage

### Command Line Interface

#### Image Processing
```bash
python detect_and_recognize.py
```

#### Video Processing
Change the `file_path` in the script to point to your video file:
```python
file_path = "path/to/your/video.mp4"
```

### Web Application

1. **Start the Streamlit app**
   ```bash
   cd web_app
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload an image** and get instant results

## 🔧 Configuration

### Model Settings

- **Confidence Threshold**: Adjust `CONFIDENCE_THRESHOLD` in `detect_and_recognize.py`
- **GPU Usage**: Set `gpu=True/False` in the Reader initialization
- **Model Path**: Update the model path in the script

### File Paths

Update these paths in the scripts:
- Model weights: `"runs/detect/train2/weights/best.pt"`
- Input files: `"dataset/images/test/your_image.jpg"`

## 📊 Model Training

The project includes a Jupyter notebook (`training.ipynb`) for training custom YOLOv8 models:

1. **Prepare your dataset** in YOLO format
2. **Update the configuration** in `number_plate.yaml`
3. **Run the training notebook**
4. **Use the trained weights** in the detection script

## 📈 Performance

- **Detection Speed**: ~200ms per image (CPU)
- **OCR Speed**: ~500ms per plate (CPU)
- **Accuracy**: Depends on image quality and model training

## 🎨 Customization

### Adding New Classes

1. Update the YAML configuration file
2. Retrain the model with new data
3. Update the detection script accordingly

### Modifying Detection Parameters

- Adjust confidence thresholds
- Change bounding box colors
- Modify text display settings

## 📝 Output Format

The system generates:
- **Visual Output**: Images/videos with bounding boxes and recognized text
- **CSV Files**: Structured data with coordinates and text
- **Console Logs**: Processing time and detection statistics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [OpenCV](https://opencv.org/)
- [Streamlit](https://streamlit.io/)

## 📞 Support

For questions and support, please open an issue on GitHub or contact the maintainers.

---

**Note**: This repository excludes large files (models, datasets, videos) for size considerations. You'll need to add your own trained models and datasets. 