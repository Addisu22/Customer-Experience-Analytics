# Fintech App Review Analysis - Task 1

## Objective
Collect and preprocess 1,200+ user reviews from Google Play Store for three Ethiopian banks (CBE, BOA, Dashen) to support fintech app improvement.

## Methodology
- Used `google-play-scraper` to collect reviews.
- Targeted 400+ reviews per bank.
- Extracted: review, rating, date, bank name, and source.
- Cleaned data: removed duplicates, handled missing, normalized dates.
- Saved to CSV for further NLP and sentiment analysis.

## Result
- Reviews collected: 1,200+
- Missing data: < 5%
- File: `clean_reviews.csv`
