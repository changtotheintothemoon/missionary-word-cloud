# Missionary Word Cloud Analysis

This project analyzes Christian song lyrics to create word clouds and identify key vocabulary for teaching Japanese children about faith.

## Files

1. **`word_cloud_analysis.py`** - Main word cloud and frequency analysis
2. **`japanese_teaching_tool.py`** - Specialized tool for selecting teaching vocabulary
3. **`install_requirements.py`** - Installs required Python packages
4. **`messy_lyrics.txt`** - Clean song lyrics (processed)

## Setup

1. Install required packages:
```bash
python install_requirements.py
```

2. Run the word cloud analysis:
```bash
python word_cloud_analysis.py
```

3. Run the Japanese teaching tool:
```bash
python japanese_teaching_tool.py
```

## Features

### Word Cloud Analysis (`word_cloud_analysis.py`)
- Creates visual word clouds from song lyrics
- Analyzes word frequency with bar charts
- Categorizes words by spiritual themes:
  - Faith & Trust
  - Jesus & God
  - Power & Strength
  - Love & Care
  - Praise & Worship
  - Life & Journey
  - Emotions & Actions

### Japanese Teaching Tool (`japanese_teaching_tool.py`)
- Identifies most important words for teaching Japanese kids
- Provides Japanese translations (hiragana/katakana)
- Organizes vocabulary by difficulty level:
  - **Beginner** (6-8 years): Simple, high-frequency words
  - **Intermediate** (9-11 years): More complex concepts
  - **Advanced** (12+ years): Deep faith concepts
- Creates lesson plans with target age groups
- Generates flashcard data (saved as JSON)
- Prioritizes words by frequency × importance score

## Teaching Recommendations

The tool identifies priority words like:
- **god** (かみ) - Core concept, appears frequently
- **jesus** (イエス) - Central to Christian faith
- **love** (あい) - Fundamental emotion
- **trust** (しんらい) - Key faith concept
- **power** (ちから) - Describes God's attributes

## Usage Tips for Japanese Mission

1. **Start with high-frequency words** - Kids will hear them often in songs
2. **Use hand gestures** - Visual learning helps retention
3. **Practice pronunciation** - Work with native speakers
4. **Create simple sentences** - Build on vocabulary
5. **Use songs for practice** - Kids love singing!
6. **Make it interactive** - Games and activities work best

## Output Files

- `teaching_flashcards.json` - Structured flashcard data for teaching
- Word cloud images (displayed during analysis)
- Frequency charts (displayed during analysis)

## Customization

You can modify the vocabulary lists in `japanese_teaching_tool.py` to:
- Add more Japanese translations
- Adjust difficulty levels
- Change importance scores
- Add new word categories
