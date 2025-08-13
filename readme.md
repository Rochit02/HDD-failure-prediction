# HDD Failure Data Analysis

## 📌 Project Overview
This project focuses on analyzing hard disk drive (HDD) failures across multiple quarters starting from 2020.  
The goal is to compile and study HDD failure data to identify patterns, trends, and potential causes.

## 📊 Current Status
- ✅ Segregated **failure rows** of HDDs from each individual quarter since 2020.
- ✅ Created a **combined failure CSV file** from all quarterly datasets.
- ✅ Generated a **count of HDD models** that experienced failures.

## 🗂 Files in Project
- `failures QX YYYY.csv` → Quarterly HDD failure datasets (original data).
- `combined_failures.csv` → Consolidated dataset of all failure records.
- `model_counts.txt` → List of HDD models and their respective failure counts.
- `p2.py` → Python script for merging and counting failures.

## 📈 HDD Failure Counts by Model
Below is the failure count per HDD model from the combined dataset:

| Model | Total Count |
|-------|------------|
| ST12000NM0008 | 2903 |
| TOSHIBA MG07ACA14TA | 2527 |
| ST8000NM0055 | 2392 |
| HGST HUH721212ALN604 | 2225 |
| ST4000DM000 | 2140 |
| HGST HUH721212ALE604 | 1666 |
| TOSHIBA MG08ACA16TA | 1661 |
| ST8000DM002 | 1223 |
| ST16000NM001G | 1031 |
| ST12000NM0007 | 965 |
| ST14000NM001G | 955 |
| ST12000NM001G | 864 |
| WDC WUH722222ALE6L4 | 534 |
| ST14000NM0138 | 515 |
| TOSHIBA MG08ACA16TE | 405 |
| TOSHIBA MG08ACA16TEY | 384 |
| WDC WUH721816ALE6L4 | 365 |
| ST10000NM0086 | 360 |
| TOSHIBA MQ01ABF050 | 319 |
| WDC WUH721414ALE6L4 | 304 |
| TOSHIBA MQ01ABF050M | 282 |
| HGST HMS5C4040BLE640 | 214 |
| ST500LM012 HN | 136 |
| WDC WUH721816ALE6L0 | 127 |
| HGST HUH721212ALE600 | 124 |
| HGST HUH728080ALE600 | 114 |
| HP SSD S700 250GB | 108 |
| TOSHIBA MG10ACA20TE | 104 |
| HGST HMS5C4040ALE640 | 98 |
| ST500LM030 | 96 |
| ST24000NM002H | 63 |
| TOSHIBA MG07ACA14TEY | 57 |
| Seagate BarraCuda SSD ZA250CM10002 | 51 |
| ST12000NM000J | 43 |
| HGST HUH728080ALE604 | 39 |
| WDC WD5000LPVX | 36 |
| Seagate BarraCuda 120 SSD ZA250CM10003 | 29 |
| WD Blue SA510 2.5 250GB | 24 |
| CT250MX500SSD1 | 24 |
| TOSHIBA HDWF180 | 23 |
| ST6000DX000 | 16 |
| ST14000NM0018 | 16 |
| WUH721816ALE6L4 | 16 |
| ST18000NM000J | 11 |
| Seagate SSD | 11 |
| MTFDDAV240TCB | 10 |
| ST500LM021 | 9 |
| DELLBOSS VD | 8 |
| ST16000NM002J | 8 |
| ST14000NM000J | 7 |
| WDC WD5000LPCX | 7 |
| ST4000DM005 | 7 |
| TOSHIBA MD04ABA400V | 7 |
| ST12000NM0117 | 6 |
| ST8000NM000A | 4 |
| ST16000NM000J | 4 |
| WDC WDS250G2B0A | 3 |
| ST8000DM004 | 3 |
| MTFDDAV240TDU | 2 |
| ST10000NM001G | 2 |
| TOSHIBA MG09ACA16TE | 2 |
| WDC | 1 |
| SSDSCKKB480G8R | 1 |
| ST4000DM004 | 1 |
| HGST HDS5C4040ALE630 | 1 |
| Seagate BarraCuda SSD ZA2000CM10002 | 1 |
| HGST HUS728T8TALE6L4 | 1 |
| Micron 5300 MTFDDAK480TDS | 1 |
| ST8000DM005 | 1 |
| Seagate FireCuda 120 SSD ZA500GM10001 | 1 |
| Hitachi HDS5C4040ALE630 | 1 |
| WDC WD5000BPKT | 1 |

Total sum of all the failures from 2020 Q1 to 2025 Q2: 25700
