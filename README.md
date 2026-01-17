# 🏨 Hotel Booking Cancellation Predictor
**Bridging 10+ Years of Front-Desk Experience with Machine Learning**

## 📌 Executive Summary
This project addresses one of the most significant challenges in the hospitality industry: **Revenue Loss due to Cancellations**. Using a dataset of over 36,000 reservations, I developed a machine learning pipeline that predicts cancellations with **80.37% accuracy**. 

As a former **Hotel Receptionist**, I designed this analysis to provide actionable insights that help hotel managers distinguish between "stable" bookings and "high-risk" reservations.

---

## 📉 Key Business Insights

### 1. The "Ghost Revenue" of Long Lead Times
Analysis confirms that bookings made **91+ days in advance** have a significantly higher cancellation rate (**~39%**) compared to last-minute arrivals (**~15%**). 
* **Business Impact:** Long-term bookings create a false sense of security in occupancy forecasts. 
* **Strategy:** Introduce stricter deposit requirements for bookings exceeding a 90-day window.



### 2. The OTA Paradox (High Volume, High Risk)
The **Online Segment** generates the hotel's highest total revenue but also carries the highest cancellation rate (**~37%**). 
* **Business Impact:** Revenue from Online Travel Agents is volatile and prone to sudden drops.
* **Strategy:** Implement non-refundable "Advanced Purchase" rates specifically for the online segment to lock in revenue.

### 3. The "Engagement Shield"
Guests who make **special requests** (e.g., high floor, extra bed) or require **parking spaces** are statistically more likely to show up. 
* **Business Impact:** High guest engagement during the booking process is a strong predictor of stay commitment.



---

## 🛠️ Technical Methodology
* **Exploratory Data Analysis (EDA):** Performed statistical **T-tests** to validate the significance of lead time on cancellation behavior.
* **Feature Engineering:** Created `total_nights` and `previous_cancelled_guests` to capture complex guest behaviors.
* **Professional Pipeline:** Developed a modular Scikit-Learn `Pipeline` utilizing `ColumnTransformer` for:
  * **Scaling:** `StandardScaler` for numeric features.
  * **Encoding:** `OneHotEncoder` for categorical categories.
* **Validation:** Verified model stability using **5-Fold Cross-Validation**.

---

## 📊 Model Performance
| Metric | Score | Professional Meaning |
| :--- | :--- | :--- |
| **Accuracy** | **80.37%** | The model is correct 8 out of 10 times across all data folds. |
| **Precision** | **74%** | Minimizes false alarms; prevents annoying loyal guests with unnecessary follow-ups. |
| **Recall** | **63%** | Successfully catches over half of all potential cancellations before they happen. |



---

## 📂 Project Structure
```text
Hotel_Cancellation_Project/
├── data/
│   └── Hotel Reservations.csv.zip   # Compressed raw dataset
├── notebooks/
│   └── Hotel_Analysis.ipynb         # Full EDA and Model Training
├── src/
│   ├── hotelpipe.py                 # Scikit-Learn Pipeline code
│   └── helper.py                    # Feature engineering functions
├── README.md                        # Project summary and insights
└── requirements.txt                 # Python dependencies

## 📊 Business Intelligence Dashboard (Power BI)
![Hotel Reservations Dashboard](reports/Final_Dashboard_Reservations_Project.jpg)

> **Key Insight:** The dashboard reveals that **60.05% of revenue loss** originates from **Long Term** bookings, providing a clear target for policy changes.