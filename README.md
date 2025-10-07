# Washigton State Electric Vehicle Analysis

Date: 06.10.2025

This project looks at electric vehicle data from the state of Washington with the goal of practicing reproducible coding etiquette and git version control.

## Data

Washington Technology Solutions (WaTech) provides data on Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electriv Vehicles (PHEVs) that are registered with the Washington State Department of Licensing (DOL). The dataset is stored in the data directory of this project and can be found online at [data.gov](https://catalog.data.gov/dataset/electric-vehicle-population-data) (downloaded: 06.10.2025).

Data file provided: Electric_Vehicle_Population_Data.csv

## Folder Structure
```
.
├── code
│   └── analysis.py
├── data
│   └── Electric_Vehicle_Population_Data.csv
├── result
│   └── top_wa_vehicle_makes.png
├── environment.yml
├── LICENSE
└── README.md
```

## Getting Started


### Requirements
How to get the development/analysis environment running with conda:

```
conda env create -f environment.yml
conda activate myenv_wav
```

### Main Dependencies
* **Python** 3.13
* **pandas** - data manipulation and analysis
* **matplotlib** - plotting and visualization

The analysis can be run with `python code/analysis.py` in the root directory, which produces a bar chart of the most popular electric vehicle makes in Washington and saves the chart to the result folder upon its closing.


