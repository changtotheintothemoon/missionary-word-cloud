#!/usr/bin/env python3
"""
HTML Word Cloud Generator for Missionary Song Lyrics
This script generates an HTML file with JavaScript-based word cloud visualization
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

def generate_html_word_cloud(words, output_file='missionary_word_cloud.html'):
    """Generate HTML file with JavaScript word cloud"""
    
    word_freq = Counter(words)
    top_words = word_freq.most_common(50)
    
    # Convert to format needed for JavaScript
    word_data = []
    for word, count in top_words:
        word_data.append({
            'text': word,
            'size': count * 5,  # Scale up for better visualization
            'count': count
        })
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Missionary Song Lyrics - Word Cloud</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/holtzy/D3-graph-gallery@master/LIB/d3.layout.cloud.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }}
        #word-cloud {{
            width: 100%;
            height: 500px;
            border: 2px solid #ddd;
            border-radius: 8px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .stats {{
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }}
        .stat {{
            text-align: center;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
        }}
        .word-list {{
            margin-top: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }}
        .word-item {{
            display: inline-block;
            margin: 5px;
            padding: 8px 12px;
            background: #667eea;
            color: white;
            border-radius: 20px;
            font-size: 14px;
        }}
        .teaching-focus {{
            margin-top: 20px;
            padding: 20px;
            background: #fff3cd;
            border-radius: 8px;
            border-left: 4px solid #ffc107;
        }}
        .japanese-word {{
            color: #dc3545;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎵 Missionary Song Lyrics - Word Cloud Analysis 🎵</h1>
        
        <div id="word-cloud"></div>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number">{len(words)}</div>
                <div class="stat-label">Total Words</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(set(words))}</div>
                <div class="stat-label">Unique Words</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(top_words)}</div>
                <div class="stat-label">Top Words Shown</div>
            </div>
        </div>
        
        <div class="teaching-focus">
            <h3>🎯 Priority Words for Teaching Japanese Kids:</h3>
            <div class="word-list">
                <div class="word-item">TRUST <span class="japanese-word">しんらい</span> - {word_freq.get('trust', 0)} times</div>
                <div class="word-item">JESUS <span class="japanese-word">イエス</span> - {word_freq.get('jesus', 0)} times</div>
                <div class="word-item">GOD <span class="japanese-word">かみ</span> - {word_freq.get('god', 0)} times</div>
                <div class="word-item">POWER <span class="japanese-word">ちから</span> - {word_freq.get('power', 0)} times</div>
                <div class="word-item">LOVE <span class="japanese-word">あい</span> - {word_freq.get('love', 0)} times</div>
                <div class="word-item">HOPE <span class="japanese-word">きぼう</span> - {word_freq.get('hope', 0)} times</div>
                <div class="word-item">FEAR <span class="japanese-word">こわい</span> - {word_freq.get('fear', 0)} times</div>
                <div class="word-item">SMILE <span class="japanese-word">ほほえみ</span> - {word_freq.get('smile', 0)} times</div>
            </div>
        </div>
        
        <div class="word-list">
            <h3>📊 All Key Words (Top 25):</h3>
            {''.join([f'<div class="word-item">{word.upper()} ({count})</div>' for word, count in top_words[:25]])}
        </div>
    </div>
    
    <script>
        const words = {json.dumps(word_data)};
        
        // Set up dimensions
        const width = 1000;
        const height = 500;
        
        // Create SVG
        const svg = d3.select("#word-cloud")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
        
        // Create color scale
        const color = d3.scaleOrdinal(d3.schemeCategory10);
        
        // Create word cloud layout
        const layout = d3.layout.cloud()
            .size([width, height])
            .words(words)
            .padding(5)
            .rotate(() => (Math.random() - 0.5) * 60)
            .font("Impact")
            .fontSize(d => Math.max(10, Math.min(60, d.size)))
            .on("end", draw);
        
        layout.start();
        
        function draw(words) {{
            svg.append("g")
                .attr("transform", "translate(" + width/2 + "," + height/2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", d => d.size + "px")
                .style("font-family", "Impact")
                .style("fill", (d, i) => color(i))
                .attr("text-anchor", "middle")
                .attr("transform", d => "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")")
                .text(d => d.text)
                .append("title")
                .text(d => d.text + " (appears " + d.count + " times)");
        }}
    </script>
</body>
</html>
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML Word Cloud saved as '{output_file}'")
    print(f"🌐 Open this file in your web browser to see the interactive word cloud!")
    return output_file

def main():
    """Main function to generate HTML word cloud"""
    print("🎨 Generating HTML Word Cloud for Missionary Songs 🎨")
    print("=" * 60)
    
    # Read and process lyrics
    lyrics = read_lyrics_file('messy_lyrics.txt')
    words = clean_and_tokenize(lyrics)
    
    print(f"📝 Processed {len(words)} words ({len(set(words))} unique)")
    
    # Generate HTML word cloud
    html_file = generate_html_word_cloud(words)
    
    # Show top words
    word_freq = Counter(words)
    print(f"\n🔝 Top 10 Words:")
    for i, (word, count) in enumerate(word_freq.most_common(10), 1):
        print(f"  {i:2d}. {word.upper():<12} - {count} times")
    
    print(f"\n📂 Files created:")
    print(f"  • {html_file} - Interactive word cloud (open in browser)")
    print(f"  • teaching_flashcards.json - Teaching flashcards")
    
    print(f"\n💡 To view the word cloud:")
    print(f"  1. Open '{html_file}' in your web browser")
    print(f"  2. The word cloud will be interactive and colorful")
    print(f"  3. Hover over words to see their frequency")
    print(f"  4. Perfect for presentations and teaching materials!")

if __name__ == "__main__":
    main()
