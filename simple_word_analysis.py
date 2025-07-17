#!/usr/bin/env python3
"""
Simple Word Frequency Analysis for Missionary Song Lyrics
This script analyzes song lyrics without requiring matplotlib/numpy
"""

import re
from collections import Counter

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
    
    # Common English stop words to filter out
    stop_words = {
        'the', 'and', 'to', 'of', 'a', 'an', 'in', 'on', 'at', 'by', 'for', 
        'with', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 
        'should', 'may', 'might', 'can', 'shall', 'must', 'ought', 'i', 'you', 
        'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
        'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that',
        'these', 'those', 'so', 'up', 'out', 'if', 'about', 'who', 'what',
        'where', 'when', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
        'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
        'own', 'same', 'than', 'too', 'very', 'just', 'now', 'oh', 'yeah',
        'cause', 'lets', 'get', 'go', 'come', 'know', 'take', 'make',
        'see', 'look', 'back', 'even', 'much', 'every', 'always', 'never',
        'there', 'here', 'again', 'away', 'around', 'through', 'without'
    }
    
    # Filter out stop words and very short words
    meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    return meaningful_words

def analyze_spiritual_themes(words):
    """Analyze spiritual and religious themes in the lyrics"""
    
    # Define theme categories
    themes = {
        'Faith & Trust': ['trust', 'faith', 'believe', 'hope', 'confident'],
        'Jesus & God': ['jesus', 'god', 'lord', 'father', 'christ', 'savior'],
        'Power & Strength': ['power', 'powerful', 'strength', 'strong', 'overcome', 'invincible'],
        'Love & Care': ['love', 'loving', 'care', 'heart', 'mercy', 'grace'],
        'Praise & Worship': ['praise', 'worship', 'thank', 'grateful', 'honor', 'glory'],
        'Life & Journey': ['life', 'journey', 'way', 'path', 'guide', 'lead'],
        'Emotions & Actions': ['smile', 'joy', 'happy', 'shout', 'sing', 'dance']
    }
    
    word_freq = Counter(words)
    theme_analysis = {}
    
    for theme, keywords in themes.items():
        theme_count = sum(word_freq[word] for word in keywords if word in word_freq)
        theme_words = {word: word_freq[word] for word in keywords if word in word_freq and word_freq[word] > 0}
        theme_analysis[theme] = {
            'total_count': theme_count,
            'words': theme_words
        }
    
    return theme_analysis

def create_simple_word_cloud_text(words, width=60):
    """Create a simple text-based word cloud representation"""
    word_freq = Counter(words)
    top_words = word_freq.most_common(20)
    
    # Create visual representation using text
    cloud_lines = []
    current_line = ""
    
    for word, count in top_words:
        # Make word size proportional to frequency
        if count >= 10:
            display_word = word.upper()
        elif count >= 5:
            display_word = word.capitalize()
        else:
            display_word = word.lower()
        
        # Add frequency indicator
        word_with_freq = f"{display_word}({count})"
        
        if len(current_line) + len(word_with_freq) + 3 <= width:
            current_line += word_with_freq + " • "
        else:
            cloud_lines.append(current_line.rstrip(" • "))
            current_line = word_with_freq + " • "
    
    if current_line:
        cloud_lines.append(current_line.rstrip(" • "))
    
    return cloud_lines

def main():
    """Main analysis function"""
    print("🎵 Missionary Song Lyrics Analysis 🎵")
    print("=" * 50)
    
    # Read and process lyrics
    lyrics = read_lyrics_file('messy_lyrics.txt')
    words = clean_and_tokenize(lyrics)
    
    print(f"Total words processed: {len(words)}")
    print(f"Unique words: {len(set(words))}")
    print()
    
    # Word frequency analysis
    print("📊 Top 25 Most Frequent Words:")
    print("-" * 30)
    word_freq = Counter(words)
    for i, (word, count) in enumerate(word_freq.most_common(25), 1):
        print(f"{i:2d}. {word:<15} {count:>3} times")
    print()
    
    # Spiritual theme analysis
    print("🙏 Spiritual Theme Analysis:")
    print("-" * 30)
    theme_analysis = analyze_spiritual_themes(words)
    for theme, data in theme_analysis.items():
        if data['total_count'] > 0:
            print(f"{theme}: {data['total_count']} total occurrences")
            for word, count in sorted(data['words'].items(), key=lambda x: x[1], reverse=True):
                print(f"  • {word}: {count} times")
            print()
    
    # Simple text-based word cloud
    print("☁️ Text-Based Word Cloud:")
    print("-" * 30)
    cloud_lines = create_simple_word_cloud_text(words)
    for line in cloud_lines:
        print(f"  {line}")
    print()
    
    # Key insights for teaching
    print("🎯 Key Insights for Teaching Japanese Kids:")
    print("-" * 45)
    
    # Find most important teaching words
    teaching_words = []
    for word, count in word_freq.most_common(50):
        if word in ['jesus', 'god', 'trust', 'love', 'power', 'hope', 'life', 'way', 'heart', 'smile', 'help', 'fear', 'overcome', 'powerful', 'forever', 'journey']:
            teaching_words.append((word, count))
    
    print("Top priority words for teaching:")
    for word, count in teaching_words[:10]:
        print(f"  • {word.upper()}: appears {count} times - high impact!")
    
    print()
    print("💡 Teaching Recommendations:")
    print("   1. Focus on high-frequency words (trust, jesus, god)")
    print("   2. Use action words (smile, help, overcome)")
    print("   3. Connect emotions to faith (love, hope, fear)")
    print("   4. Make it interactive with songs and games")
    print("   5. Use visual aids and gestures")

if __name__ == "__main__":
    main()
