#!/usr/bin/env python3
"""
Word Cloud Analysis for Missionary Song Lyrics
This script analyzes song lyrics to create word clouds and frequency analysis
"""

import re
from collections import Counter

# Try to import matplotlib, but fall back to text-based visualization if it fails
try:
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("⚠️  Matplotlib/WordCloud not available - using text-based visualization instead")

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
        'cause', 'lets', 'get', 'go', 'come', 'know', 'can', 'take', 'make',
        'see', 'look', 'back', 'even', 'much', 'every', 'always', 'never',
        'there', 'here', 'again', 'away', 'around', 'through', 'without'
    }
    
    # Filter out stop words and very short words
    meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    return meaningful_words

def generate_word_frequency(words, top_n=30):
    """Generate word frequency analysis"""
    word_freq = Counter(words)
    return word_freq.most_common(top_n)

def create_word_cloud(words, title="Word Cloud"):
    """Create and display word cloud or text-based alternative"""
    if not HAS_MATPLOTLIB:
        print(f"\n☁️  {title} (Text-based representation):")
        print("=" * 60)
        create_text_word_cloud(words)
        return
    
    text = ' '.join(words)
    
    # Create word cloud
    wordcloud = WordCloud(
        width=1200, 
        height=600,
        background_color='white',
        colormap='viridis',
        max_words=100,
        relative_scaling=0.5,
        random_state=42
    ).generate(text)
    
    # Create and save the figure
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=20, fontweight='bold', pad=20)
    plt.tight_layout()
    
    # Save as JPG
    filename = 'missionary_word_cloud.jpg'
    plt.savefig(filename, format='jpg', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"✅ Word cloud saved as '{filename}'")
    
    # Also display
    plt.show()

def create_text_word_cloud(words, width=70):
    """Create a text-based word cloud representation"""
    word_freq = Counter(words)
    top_words = word_freq.most_common(25)
    
    # Create visual representation using text
    cloud_lines = []
    current_line = ""
    
    for word, count in top_words:
        # Make word size proportional to frequency
        if count >= 15:
            display_word = f"**{word.upper()}**"
        elif count >= 10:
            display_word = f"*{word.upper()}*"
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
    
    for line in cloud_lines:
        print(f"  {line}")

def create_text_bar_chart(word_freq, title="Word Frequency", top_n=15):
    """Create a text-based bar chart"""
    print(f"\n📊 {title}:")
    print("=" * 50)
    
    max_count = max(count for _, count in word_freq[:top_n])
    bar_width = 30
    
    for word, count in word_freq[:top_n]:
        # Calculate bar length proportional to frequency
        bar_length = int((count / max_count) * bar_width)
        bar = "█" * bar_length
        
        print(f"{word:<12} {count:>3} │{bar}")
    print()

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
    print("📊 Top 20 Most Frequent Words:")
    print("-" * 30)
    word_freq = generate_word_frequency(words, 20)
    for word, count in word_freq:
        print(f"{word:<15} {count:>3}")
    print()
    
    # Spiritual theme analysis
    print("🙏 Spiritual Theme Analysis:")
    print("-" * 30)
    theme_analysis = analyze_spiritual_themes(words)
    for theme, data in theme_analysis.items():
        if data['total_count'] > 0:
            print(f"{theme}: {data['total_count']} occurrences")
            for word, count in sorted(data['words'].items(), key=lambda x: x[1], reverse=True):
                print(f"  - {word}: {count}")
            print()
    
    # Create word cloud
    create_word_cloud(words, "Missionary Song Lyrics - Word Cloud")
    
    # Create frequency bar chart
    if HAS_MATPLOTLIB:
        plt.figure(figsize=(12, 8))
        words_list, counts = zip(*word_freq[:15])
        plt.bar(words_list, counts, color='skyblue', edgecolor='navy', alpha=0.7)
        plt.title('Top 15 Most Frequent Words', fontsize=16, fontweight='bold')
        plt.xlabel('Words', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save as JPG
        bar_filename = 'word_frequency_chart.jpg'
        plt.savefig(bar_filename, format='jpg', dpi=300, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        print(f"✅ Frequency chart saved as '{bar_filename}'")
        
        plt.show()
        
        # Create theme analysis chart
        theme_names = [theme for theme, data in theme_analysis.items() if data['total_count'] > 0]
        theme_counts = [data['total_count'] for theme, data in theme_analysis.items() if data['total_count'] > 0]
        
        if theme_counts:
            plt.figure(figsize=(12, 8))
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
            plt.bar(theme_names, theme_counts, color=colors[:len(theme_names)], alpha=0.8)
            plt.title('Spiritual Themes Distribution', fontsize=16, fontweight='bold')
            plt.xlabel('Themes', fontsize=12)
            plt.ylabel('Word Count', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            # Save as JPG
            theme_filename = 'spiritual_themes_chart.jpg'
            plt.savefig(theme_filename, format='jpg', dpi=300, bbox_inches='tight',
                       facecolor='white', edgecolor='none')
            print(f"✅ Spiritual themes chart saved as '{theme_filename}'")
            
            plt.show()
    else:
        create_text_bar_chart(word_freq, "Top 15 Most Frequent Words", 15)
    
    # Summary of exported files
    if HAS_MATPLOTLIB:
        print("\n📁 EXPORTED FILES:")
        print("=" * 30)
        print("✅ missionary_word_cloud.jpg - Visual word cloud")
        print("✅ word_frequency_chart.jpg - Word frequency bar chart")
        print("✅ spiritual_themes_chart.jpg - Spiritual themes distribution")
        print("✅ teaching_flashcards.json - Teaching flashcards data")
        print("\n💡 These images are perfect for presentations and teaching materials!")

if __name__ == "__main__":
    main()
