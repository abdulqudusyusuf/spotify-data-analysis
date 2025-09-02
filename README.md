# 🎧 Spotify Data Analysis Dashboard

![excel_salary_dashboard.gif](/Images/excel_salary_dashboard.gif)

## Introduction

**Spotify Wrapped** is something I always look forward to at the end of the year. Seeing which artists topped my charts and which songs I had on repeat is always exciting. But this time, I decided I wasn’t going to wait until December to get the answers. So, I pulled my own data and analyzed my listening history from **January – August 2025**. In this project, I’ll walk you through my data cleaning and collection process and of course, the detailed analysis of my listening habits.

## Data Collection Process

To kick off this project, I requested my complete Spotify listening history for 2025 directly from Spotify.  
They sent me a `.json` file containing detailed logs of every track I played. Since JSON isn’t the most convenient format for analysis, I used **Pandas** in Python to convert it into an Excel (`.xlsx`) file. This gave me a structured dataset that I could easily work with and later import into Power BI for visualization.

## 🛠️ Tools Used

- **Microsoft Excel** – for initial data cleaning and preparation.
- **Microsoft Power BI** – for data modeling, DAX calculations, and interactive dashboard creation.

## 🔄 Data Transformation Process

### Data Cleaning

- Removed tracks with playtime less than **30 seconds** (to avoid counting skipped songs)
- Dropped unnecessary columns that did not contribute to the analysis
- Verified column data types (Date, Time, Text, Numeric)

### 🔹 Load

Once the dataset was ready, I imported it into **Power BI** for modeling and visualization.

Inside Power BI, I:

- Created **calculated columns and measures** (e.g., _Average Plays per Day_)
- Applied **time intelligence functions** to capture monthly listening trends
- Designed KPI cards, bar charts, and a line chart to visualize my listening habits
- Styled the dashboard with a **Spotify-inspired theme** (green + black) for a clean, branded look

### 🔢 Creating Calculated Columns and Measures

To better understand my listening habits, I created custom DAX measures in Power BI:

**Total Minutes Listened** – The overall time spent listening.

```DAX
Total Minutes Listened = SUM('Spotify History'[Minutes Played])
```

**Unique Artists** – Distinct count of artists listened to

```DAX
Unique Artists = DISTINCTCOUNT('Spotify History'[Artist])
```

**Unique Songs** – Distinct count of songs played

```DAX
Unique Songs = DISTINCTCOUNT('Spotify History'[Song Title])
```

**Average Plays Per Day** – Daily average of songs played

```DAX
Average Plays Per Day =
DIVIDE(
    COUNTROWS('Spotify History'),
    DISTINCTCOUNT('Spotify History'[Date])
)

```

**Monthly Plays Trend** – Plays grouped by month

```DAX
Monthly Minutes =
CALCULATE(
    SUM('Spotify History'[Minutes Played]),
    VALUES('Spotify History'[Month])
)

```

## 📂 Dashboard File

🔗 [Download Power BI File (.pbix)](./StreamingHistory2025.pbix)

---

## Dashboard Overview

![excel_salary_dashboard.png](/Images/excel_salary_dashboard.png)

The dashboard contains:

- 🎵 **Top 5 Most Played Songs**
- 🎤 **Top 5 Artists**
- 📆 **Monthly Listening Trend (Line Chart)**
- ⏱️ **Average Plays per Day**
- 🎶 **Song Variety / Genre Spread**

---

## 🔍 Insights & Discoveries

### ⏱️ Total Minutes Listened

I’ve streamed music for over **22,000 minutes** so far this year — that’s around 376 hours, or almost 47 hours each month. Music clearly plays a steady role in my lifestyle.

---

### 👥 Unique Artists

I listened to **500 unique artists**. This reflects a balance of loyalty and exploration — while I have clear favorites, I still branch out to discover plenty of new voices.

---

### 🎵 Unique Songs

I played around **2,500 different songs**. This shows I don’t stick to a narrow playlist but rotate regularly between new discoveries and repeat favorites.

---

### 📅 Average Plays Per Day

On average, I hit **19 plays per day**. This consistency reflects how music is **integrated into my everyday activities** — whether studying, working, or relaxing.

---

### 🎤 Top 5 Artists

1. **Drake**
2. **J. Cole**
3. **PARTYNEXTDOOR (PND)**
4. **The Weeknd**
5. **Kanye West**

**Insight**: Drake completely dominates my listening, but I still keep space for other Hip-Hop and R&B heavyweights.

---

### 🎶 Top 5 Songs

1. **Crying in Chanel** – Drake
2. **Raining in Houston** – Drake
3. **Spider-Man, Superman** – Drake & PARTYNEXTDOOR
4. **On My Way** – Drake & PARTYNEXTDOOR
5. **3001** – J. Cole

**Insight**: Even my most played songs don’t run into hundreds of repeats, showing I prefer variety over looping one track endlessly.

---

### 💿 Top 5 Albums

1. **Some Sexy Songs For You** – Drake & PARTYNEXTDOOR
2. **Scorpion** – Drake
3. **For All The Dogs** – Drake
4. **Might Delete Later** – J. Cole
5. **Honestly, Nevermind** – Drake

**Insight**: One album (Some Sexy Songs For You) heavily outperformed the rest, but Drake’s influence is present throughout, with J. Cole breaking through as the only other major presence.

---

### ▶️ Total Plays

Beyond minutes, I tracked **total streams**, giving a clearer picture of my listening intensity and repeat plays.

---

### 📈 Listening Patterns

- Peaked in May **(1,151 plays)** → my busiest listening month.
- Lowest in March **(46 plays)** → almost a complete break from Spotify.
- Recovery in July–August **(832 → 922 plays)** → showing how my listening adjusts with my personal schedule.
---

### 🌍 Key Discoveries

1.  My charts are heavily Hip-Hop/R&B driven, with Drake as the backbone of my library.
2.  Even with Drake’s dominance, I still explored 544 unique artists and 2,448 songs, proving I’m not locked into just one lane.
3.  My listening habits are seasonal and lifestyle-driven — sharp drops (like March) reflect busy life periods, but I always bounce back.

## What Did I Learn?

Looking back at the analysis, a few clear patterns stand out:

- **Music as a Daily Companion**: With an average of **19 plays per day**, music isn’t just background noise — it’s a steady part of my daily rhythm.
- **Genre Loyalty**: Even though Afrobeats dominates the Nigerian scene, my data shows a clear preference for **Rap and R&B**, proving that my taste leans more international.
- **Explorer vs. Loyalist**: I listened to **500 unique artists** and **2,500 unique songs**, yet Drake has been my **Top Artist for 3+ years** — showing I balance **exploration** with **loyal loyalty**.
- **Seasonal Listening**: My listening dipped drastically in **March (46 plays)** but peaked in **May (1,151 plays)**, reflecting how life events directly influence my habits.
- **Artist Loyalty Runs Deep**: Drake consistently tops not just my artist list, but also dominates my **songs and albums** — proving he’s the backbone of my library.
- **The Power of Data Cleaning**: I learned how important it is to properly clean and structure raw data. Spotify history isn’t analysis-ready out of the box, so I had to carefully transform it to make meaningful insights possible.
- **DAX & Measures in Power BI**: I improved my ability to create calculated columns and DAX measures. Metrics like Total Minutes Listened, Unique Artists, and Average Plays Per Day helped me see how to turn raw numbers into useful insights.

## Future Work

For future analysis:

- Extend to **full-year data (Spotify Wrapped 2025)**
- Compare **listening patterns across years**
- Analyze **mood/genre transitions over time**

---

This project gave me an early preview of my **Spotify Wrapped**, showing how much music has shaped my 2025 so far.

---

```
✨ Built with **Excel | Python (Pandas) | Power BI (DAX & Visualization)**
```
