# 🎧 Spotify Data Analysis Dashboard

## 🖼️ Preview

_(Optional: Add another dashboard screenshot or a GIF preview of the Power BI interactions)_

## 📌 Introduction

**Spotify Wrapped** is something I always look forward to at the end of the year. Seeing which artists topped my charts and which songs I had on repeat is always exciting. But this time, I decided I wasn’t going to wait until December to get the answers. So, I pulled my own data and analyzed my listening history from **January – August 2025**. In this project, I’ll walk you through my data cleaning and collection process and of course, the detailed analysis of my listening habits.

## 📊 Data Collection Process

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

**Total Plays** – Total number of songs played

```DAX
Total Plays = COUNTROWS('Spotify History')
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
Average Plays Per Day = DIVIDE([Total Plays], DISTINCTCOUNT('Spotify History'[Date]))
```

**Monthly Plays Trend** – Plays grouped by month

```DAX
Monthly Plays = CALCULATE([Total Plays], DATESMTD('Spotify History'[Date]))
```

## 📂 Dashboard File

🔗 [Download Power BI File (.pbix)](./Spotify_Analysis.pbix)

---

## 📈 Dashboard Overview

Here’s the final **Spotify Analysis Dashboard** in Power BI 🎨:

_(Insert screenshot of your dashboard here)_

The dashboard contains:

- 🎵 **Top 5 Most Played Songs**
- 🎤 **Top 5 Artists**
- 📆 **Monthly Listening Trend (Line Chart)**
- ⏱️ **Average Plays per Day**
- 🎶 **Song Variety / Genre Spread**

---

## 🔍 Insights & Discoveries

### ⏱️ Total Minutes Listened

So far in this year I have listened to music for over **22,000 minutes**. That’s over **360 hours** of streaming — showingt that i'm quite an avid music listener.

---

### 👥 Unique Artists

I listened to **500 unique artists** throughout the year. This highlights my **diverse taste in music**, as I actively explore different sounds instead of sticking to the same few artists.

---

### 🎵 Unique Songs

I played around **2,500 different songs**. This shows I don’t just replay the same tracks on loop — I enjoy rotating between **variety and new discoveries**.

---

### 📅 Average Plays Per Day

On average, I hit **19 plays per day**. This consistency reflects how music is **integrated into my everyday activities** — whether studying, working, or relaxing.

---

### 🏆 Top 5 Artists

1. **Drake**
2. **J. Cole**
3. **PARTYNEXTDOOR (PND)**
4. **The Weeknd**
5. **Kanye West**

🔑 **Insight**: My listening skews heavily toward **rap and R&B**, showing strong loyalty to my long-time favorites.

---

### 🎶 Top 5 Songs

1. **Crying in Chanel** – Drake
2. **Raining in Houston** – Drake
3. **Spider-Man, Superman** – Drake & PARTYNEXTDOOR
4. **On My Way** – Drake & PARTYNEXTDOOR
5. **3001** – J. Cole

---

### 💿 Top 5 Albums

1. **Some Sexy Songs For You** – Drake & PARTYNEXTDOOR
2. **Scorpion** – Drake
3. **For All The Dogs** – Drake
4. **Might Delete Later** – J. Cole
5. **Honestly, Nevermind** – Drake

---

### ▶️ Total Plays

Beyond minutes, I tracked **total streams**, giving a clearer picture of my listening intensity and repeat plays.

---

### 📈 Listening Patterns

My listening peaked in **May (1,151 plays)** and dipped drastically in **March (46 plays)**, possibly reflecting changes in my routine, or personal schedule.

---

### 🌍 Key Discoveries

1.  **Rap and R&B dominated my charts**, showing my international music preference over local trends.
2.  Drake has consistently been my **Top Artist for 4+ years**. This highlights strong **listening loyalty**, even as I continue to discover new music.

## 🤔 What Did I Learn?

Looking back at the analysis, a few clear patterns stand out:

- **Music as a Daily Companion**: With an average of **19 plays per day**, music isn’t just background noise — it’s a steady part of my daily rhythm.
- **Genre Loyalty**: Even though Afrobeats dominates the Nigerian scene, my data shows a clear preference for **Rap and R&B**, proving that my taste leans more international.
- **Explorer vs. Loyalist**: I listened to **500 unique artists** and **2,500 unique songs**, yet Drake has been my **Top Artist for 3+ years** — showing I balance **exploration** with **loyal loyalty**.
- **Seasonal Listening**: My listening dipped drastically in **March (46 plays)** but peaked in **May (1,151 plays)**, reflecting how life events directly influence my habits.
- **Artist Loyalty Runs Deep**: Drake consistently tops not just my artist list, but also dominates my **songs and albums** — proving he’s the backbone of my library.

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
