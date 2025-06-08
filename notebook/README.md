# Bank Reviews Analysis

## Task 1: Data Collection and Preprocessing

### Methodology

1. **Data Collection**:
   - Used `google-play-scraper` Python package
   - Targeted 3 major US banks:
     - Chase (`com.chase.sig.android`)
     - Bank of America (`com.infonow.bofa`)
     - Wells Fargo (`com.wf.wellsfargomobile`)
   - Collected 400+ English reviews per bank (NEWEST first)
   - Implemented rate limiting (2s between requests)

2. **Preprocessing**:
   - Removed duplicate reviews
   - Handled missing values:
     - Dropped reviews with empty text
     - Filled missing ratings with 0
   - Normalized dates to YYYY-MM-DD format
   - Removed very short reviews (<5 characters)

### Files

- `scraper.py`: Main scraping script
- `preprocess.py`: Data cleaning pipeline
- `bank_reviews.csv`: Raw scraped data
- `clean_reviews.csv`: Processed dataset

### How to Run

```bash
pip install -r requirements.txt
python scraper.py
python preprocess.py
```