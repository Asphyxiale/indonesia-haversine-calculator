## Indonesia Distance Calculator
An interactive **Python GUI application** that allows users to calculate the **distance between two cities in Indonesia** by clicking directly on a map. The distance is computed using the **Haversine formula**, providing realistic great-circle distances.

---

## Features
* Interactive map of Indonesia
* Click to select **two cities**
* Automatically calculates distance (in km)
* Displays a dashed flight path between cities

---
## How It Works
1. The application displays a map of Indonesia.
2. Each city is plotted using latitude & longitude data.
3. When two cities are selected:
   * The **Haversine formula** calculates the distance.
   * A line is drawn between the two points.
   * The distance is displayed in kilometers.
---

## Tech Stack
* **Python 3**
* **Tkinter** – GUI framework
* **Pillow (PIL)** – Image processing
* **Math** – Distance calculations

---
## Installation
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/indonesia-distance-calculator.git
cd indonesia-distance-calculator
```
### 2. Install dependencies
```bash
pip install pillow
```
*(Tkinter is included by default in most Python installations)*
---
## Running the Application
```bash
python program.py
```
Make sure the following file structure exists:
```
project-folder/
│
├── program.py
├── assets/
│   └── indonesia.png
└── README.md
```
---

## Distance Formula Used
The app uses the **Haversine Formula**:
> Calculates the great-circle distance between two points on a sphere given their latitude and longitude.
Earth radius assumed: **6371 km**
---

