#!/usr/bin/env python3
"""
Japanese Kids Teaching Tool - Key Word Selector
This script identifies the most important words from missionary songs 
that would be valuable for teaching Japanese children about faith.
"""

import re
from collections import Counter
import json

def read_lyrics_file(filename):
    """Read and clean the lyrics file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def clean_and_tokenize(text):
    """Clean text and extract meaningful words"""
    # Remove song numbers and extra whitespace
    text = re.sub(r'^\d+\.\s*', '', text, flags=re.MULTILINE)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and split into words
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    return words

def get_teaching_vocabulary():
    """
    Curated vocabulary for teaching Japanese kids about faith
    Organized by difficulty level and spiritual importance
    """
    
    vocabulary = {
        'essential_faith_words': {
            'description': 'Core faith concepts - highest priority',
            'words': {
                'god': {'japanese': 'かみ (kami)', 'difficulty': 1, 'importance': 10},
                'jesus': {'japanese': 'イエス (iesu)', 'difficulty': 1, 'importance': 10},
                'love': {'japanese': 'あい (ai)', 'difficulty': 1, 'importance': 9},
                'trust': {'japanese': 'しんらい (shinrai)', 'difficulty': 2, 'importance': 9},
                'pray': {'japanese': 'いのり (inori)', 'difficulty': 2, 'importance': 8},
                'hope': {'japanese': 'きぼう (kibou)', 'difficulty': 2, 'importance': 8},
                'peace': {'japanese': 'へいわ (heiwa)', 'difficulty': 2, 'importance': 8},
                'power': {'japanese': 'ちから (chikara)', 'difficulty': 2, 'importance': 7},
                'heart': {'japanese': 'こころ (kokoro)', 'difficulty': 1, 'importance': 7}
            }
        },
        
        'action_words': {
            'description': 'Words that encourage action/behavior',
            'words': {
                'smile': {'japanese': 'ほほえみ (hohoemi)', 'difficulty': 2, 'importance': 6},
                'sing': {'japanese': 'うたう (utau)', 'difficulty': 1, 'importance': 6},
                'help': {'japanese': 'たすける (tasukeru)', 'difficulty': 1, 'importance': 7},
                'share': {'japanese': 'わける (wakeru)', 'difficulty': 1, 'importance': 6},
                'listen': {'japanese': 'きく (kiku)', 'difficulty': 1, 'importance': 6},
                'follow': {'japanese': 'ついていく (tsuite iku)', 'difficulty': 3, 'importance': 6},
                'overcome': {'japanese': 'かつ (katsu)', 'difficulty': 3, 'importance': 6}
            }
        },
        
        'descriptive_words': {
            'description': 'Words that describe God/Jesus',
            'words': {
                'powerful': {'japanese': 'つよい (tsuyoi)', 'difficulty': 2, 'importance': 6},
                'forever': {'japanese': 'えいえん (eien)', 'difficulty': 3, 'importance': 6},
                'great': {'japanese': 'すばらしい (subarashii)', 'difficulty': 2, 'importance': 5},
                'wonderful': {'japanese': 'すてき (suteki)', 'difficulty': 2, 'importance': 5},
                'amazing': {'japanese': 'すごい (sugoi)', 'difficulty': 1, 'importance': 5}
            }
        },
        
        'emotional_words': {
            'description': 'Emotional/feeling words',
            'words': {
                'happy': {'japanese': 'うれしい (ureshii)', 'difficulty': 1, 'importance': 5},
                'joy': {'japanese': 'よろこび (yorokobi)', 'difficulty': 2, 'importance': 6},
                'fear': {'japanese': 'こわい (kowai)', 'difficulty': 1, 'importance': 4},
                'worry': {'japanese': 'しんぱい (shinpai)', 'difficulty': 2, 'importance': 4},
                'courage': {'japanese': 'ゆうき (yuuki)', 'difficulty': 2, 'importance': 6}
            }
        },
        
        'life_concepts': {
            'description': 'Life and journey concepts',
            'words': {
                'life': {'japanese': 'いのち (inochi)', 'difficulty': 2, 'importance': 7},
                'journey': {'japanese': 'たび (tabi)', 'difficulty': 2, 'importance': 5},
                'way': {'japanese': 'みち (michi)', 'difficulty': 1, 'importance': 6},
                'home': {'japanese': 'いえ (ie)', 'difficulty': 1, 'importance': 5},
                'family': {'japanese': 'かぞく (kazoku)', 'difficulty': 1, 'importance': 6},
                'friend': {'japanese': 'ともだち (tomodachi)', 'difficulty': 1, 'importance': 5}
            }
        }
    }
    
    return vocabulary

def analyze_lyrics_for_teaching(lyrics_text):
    """Analyze lyrics and identify key teaching words"""
    
    words = clean_and_tokenize(lyrics_text)
    word_freq = Counter(words)
    
    vocabulary = get_teaching_vocabulary()
    
    # Find which teaching words appear in the lyrics
    found_words = {}
    
    for category, data in vocabulary.items():
        found_words[category] = {
            'description': data['description'],
            'words': {}
        }
        
        for word, info in data['words'].items():
            if word in word_freq:
                found_words[category]['words'][word] = {
                    'frequency': word_freq[word],
                    'japanese': info['japanese'],
                    'difficulty': info['difficulty'],
                    'importance': info['importance'],
                    'teaching_score': word_freq[word] * info['importance']
                }
    
    return found_words, word_freq

def generate_lesson_plan(found_words):
    """Generate a structured lesson plan for teaching"""
    
    lesson_plan = {
        'beginner_lesson': {
            'title': 'First Words of Faith (初めての信仰の言葉)',
            'target_age': '6-8 years old',
            'duration': '15-20 minutes',
            'words': []
        },
        'intermediate_lesson': {
            'title': 'Growing in Faith (信仰の成長)',
            'target_age': '9-11 years old', 
            'duration': '20-25 minutes',
            'words': []
        },
        'advanced_lesson': {
            'title': 'Deep Faith Concepts (深い信仰の概念)',
            'target_age': '12+ years old',
            'duration': '25-30 minutes',
            'words': []
        }
    }
    
    # Collect all words with their scores
    all_words = []
    for category, data in found_words.items():
        for word, info in data['words'].items():
            all_words.append({
                'word': word,
                'category': category,
                'frequency': info['frequency'],
                'japanese': info['japanese'],
                'difficulty': info['difficulty'],
                'importance': info['importance'],
                'teaching_score': info['teaching_score']
            })
    
    # Sort by teaching score (frequency * importance)
    all_words.sort(key=lambda x: x['teaching_score'], reverse=True)
    
    # Distribute words by difficulty
    for word_data in all_words:
        if word_data['difficulty'] == 1:
            lesson_plan['beginner_lesson']['words'].append(word_data)
        elif word_data['difficulty'] == 2:
            lesson_plan['intermediate_lesson']['words'].append(word_data)
        else:
            lesson_plan['advanced_lesson']['words'].append(word_data)
    
    return lesson_plan

def create_flashcard_data(lesson_plan):
    """Create flashcard data for teaching"""
    
    flashcards = []
    
    for lesson_type, lesson_data in lesson_plan.items():
        for word_data in lesson_data['words'][:10]:  # Top 10 words per lesson
            flashcards.append({
                'english': word_data['word'],
                'japanese': word_data['japanese'],
                'category': word_data['category'],
                'lesson_level': lesson_type,
                'frequency_in_songs': word_data['frequency'],
                'importance_score': word_data['importance'],
                'example_usage': f"This word appears {word_data['frequency']} times in the songs"
            })
    
    return flashcards

def main():
    """Main analysis function"""
    print("🎌 Japanese Kids Teaching Tool - Key Word Selector 🎌")
    print("=" * 60)
    
    # Read and analyze lyrics
    lyrics = read_lyrics_file('messy_lyrics.txt')
    found_words, word_freq = analyze_lyrics_for_teaching(lyrics)
    
    # Generate lesson plan
    lesson_plan = generate_lesson_plan(found_words)
    
    # Display results
    print("\n📚 LESSON PLAN RECOMMENDATIONS:")
    print("-" * 40)
    
    for lesson_type, lesson_data in lesson_plan.items():
        print(f"\n{lesson_data['title']}")
        print(f"Target Age: {lesson_data['target_age']}")
        print(f"Duration: {lesson_data['duration']}")
        print("Top Words to Teach:")
        
        for i, word_data in enumerate(lesson_data['words'][:8], 1):
            print(f"  {i}. {word_data['word'].upper()} → {word_data['japanese']}")
            print(f"     Appears {word_data['frequency']} times | Importance: {word_data['importance']}/10")
    
    print("\n🎯 PRIORITY TEACHING WORDS (By Frequency × Importance):")
    print("-" * 50)
    
    # Get top priority words across all categories
    all_priority_words = []
    for category, data in found_words.items():
        for word, info in data['words'].items():
            all_priority_words.append({
                'word': word,
                'japanese': info['japanese'],
                'score': info['teaching_score'],
                'frequency': info['frequency'],
                'importance': info['importance']
            })
    
    all_priority_words.sort(key=lambda x: x['score'], reverse=True)
    
    for i, word_data in enumerate(all_priority_words[:15], 1):
        print(f"{i:2d}. {word_data['word'].upper():<12} → {word_data['japanese']:<20} "
              f"(Score: {word_data['score']:2d} = {word_data['frequency']} × {word_data['importance']})")
    
    # Create flashcards
    flashcards = create_flashcard_data(lesson_plan)
    
    # Save flashcard data to JSON
    with open('teaching_flashcards.json', 'w', encoding='utf-8') as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Flashcard data saved to 'teaching_flashcards.json'")
    print(f"📝 Total flashcards created: {len(flashcards)}")
    
    # Teaching tips
    print("\n🎓 TEACHING TIPS:")
    print("-" * 20)
    print("1. Start with high-frequency words (they'll hear them often)")
    print("2. Use hand gestures and actions for better retention")
    print("3. Practice pronunciation with native Japanese speakers")
    print("4. Create simple sentences using these words")
    print("5. Use the songs as practice - kids love singing!")
    print("6. Make it interactive with games and activities")

if __name__ == "__main__":
    main()
