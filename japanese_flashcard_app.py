#!/usr/bin/env python3
"""
Interactive Flashcard Web App Generator
Creates a complete web application for Japanese learners to study English vocabulary
from missionary songs using interactive flashcards.
"""

import json
import re
from collections import Counter

def read_lyrics_and_generate_flashcards():
    """Read lyrics and generate flashcard data"""
    
    # Read the existing flashcard data
    try:
        with open('teaching_flashcards.json', 'r', encoding='utf-8') as f:
            flashcards = json.load(f)
    except FileNotFoundError:
        # If flashcards don't exist, create them from lyrics
        flashcards = create_flashcards_from_lyrics()
    
    # Add additional data for Japanese learners
    enhanced_flashcards = enhance_for_japanese_learners(flashcards)
    
    return enhanced_flashcards

def create_flashcards_from_lyrics():
    """Create flashcards from lyrics if they don't exist"""
    
    # Read lyrics file
    with open('messy_lyrics.txt', 'r', encoding='utf-8') as f:
        lyrics = f.read()
    
    # Clean and tokenize
    text = re.sub(r'^\d+\.\s*', '', lyrics, flags=re.MULTILINE)
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    # Filter stop words
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
    
    meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
    word_freq = Counter(meaningful_words)
    
    # Create basic flashcards
    flashcards = []
    for word, count in word_freq.most_common(50):
        flashcards.append({
            'english': word,
            'frequency_in_songs': count,
            'importance_score': min(count * 2, 10)
        })
    
    return flashcards

def enhance_for_japanese_learners(flashcards):
    """Add Japanese-specific learning data"""
    
    # Enhanced vocabulary with comprehensive Japanese data including hiragana/katakana pronunciations
    japanese_vocabulary = {
        'trust': {
            'japanese': 'しんらい',
            'romaji': 'shinrai',
            'hiragana': 'しんらい',
            'pronunciation': 'SHEEN-rah-ee',
            'meaning': '信頼',
            'example': 'I trust in God - 私は神を信頼します',
            'difficulty': 'intermediate',
            'category': 'faith'
        },
        'jesus': {
            'japanese': 'イエス',
            'romaji': 'iesu',
            'katakana': 'イエス',
            'pronunciation': 'EE-eh-soo',
            'meaning': 'イエス',
            'example': 'Jesus loves you - イエスはあなたを愛しています',
            'difficulty': 'beginner',
            'category': 'faith'
        },
        'god': {
            'japanese': 'かみ',
            'romaji': 'kami',
            'hiragana': 'かみ',
            'pronunciation': 'KAH-mee',
            'meaning': '神',
            'example': 'God is powerful - 神は力強いです',
            'difficulty': 'beginner',
            'category': 'faith'
        },
        'power': {
            'japanese': 'ちから',
            'romaji': 'chikara',
            'hiragana': 'ちから',
            'pronunciation': 'CHEE-kah-rah',
            'meaning': '力',
            'example': 'God has power - 神には力があります',
            'difficulty': 'intermediate',
            'category': 'attributes'
        },
        'love': {
            'japanese': 'あい',
            'romaji': 'ai',
            'hiragana': 'あい',
            'pronunciation': 'AH-ee',
            'meaning': '愛',
            'example': 'Love is important - 愛は大切です',
            'difficulty': 'beginner',
            'category': 'emotions'
        },
        'hope': {
            'japanese': 'きぼう',
            'romaji': 'kibou',
            'hiragana': 'きぼう',
            'pronunciation': 'KEE-boh',
            'meaning': '希望',
            'example': 'I have hope - 私には希望があります',
            'difficulty': 'intermediate',
            'category': 'emotions'
        },
        'fear': {
            'japanese': 'こわい',
            'romaji': 'kowai',
            'hiragana': 'こわい',
            'pronunciation': 'KOH-wah-ee',
            'meaning': '怖い',
            'example': 'Do not fear - 恐れてはいけません',
            'difficulty': 'beginner',
            'category': 'emotions'
        },
        'life': {
            'japanese': 'いのち',
            'romaji': 'inochi',
            'hiragana': 'いのち',
            'pronunciation': 'EE-noh-chee',
            'meaning': '命',
            'example': 'Life is precious - 命は貴重です',
            'difficulty': 'intermediate',
            'category': 'concepts'
        },
        'way': {
            'japanese': 'みち',
            'romaji': 'michi',
            'hiragana': 'みち',
            'pronunciation': 'MEE-chee',
            'meaning': '道',
            'example': 'Jesus is the way - イエスは道です',
            'difficulty': 'beginner',
            'category': 'concepts'
        },
        'smile': {
            'japanese': 'ほほえみ',
            'romaji': 'hohoemi',
            'hiragana': 'ほほえみ',
            'pronunciation': 'HOH-hoh-eh-mee',
            'meaning': '微笑み',
            'example': 'Please smile - 笑顔をください',
            'difficulty': 'intermediate',
            'category': 'actions'
        },
        'powerful': {
            'japanese': 'つよい',
            'romaji': 'tsuyoi',
            'hiragana': 'つよい',
            'pronunciation': 'TSOO-yoh-ee',
            'meaning': '強い',
            'example': 'God is powerful - 神は強いです',
            'difficulty': 'intermediate',
            'category': 'attributes'
        },
        'heart': {
            'japanese': 'こころ',
            'romaji': 'kokoro',
            'hiragana': 'こころ',
            'pronunciation': 'KOH-koh-roh',
            'meaning': '心',
            'example': 'Open your heart - 心を開いてください',
            'difficulty': 'beginner',
            'category': 'concepts'
        },
        'peace': {
            'japanese': 'へいわ',
            'romaji': 'heiwa',
            'hiragana': 'へいわ',
            'pronunciation': 'HEH-ee-wah',
            'meaning': '平和',
            'example': 'Peace be with you - 平和があなたとともに',
            'difficulty': 'intermediate',
            'category': 'concepts'
        },
        'joy': {
            'japanese': 'よろこび',
            'romaji': 'yorokobi',
            'hiragana': 'よろこび',
            'pronunciation': 'YOH-roh-koh-bee',
            'meaning': '喜び',
            'example': 'Joy comes from God - 喜びは神から来ます',
            'difficulty': 'intermediate',
            'category': 'emotions'
        },
        'light': {
            'japanese': 'ひかり',
            'romaji': 'hikari',
            'hiragana': 'ひかり',
            'pronunciation': 'HEE-kah-ree',
            'meaning': '光',
            'example': 'Jesus is the light - イエスは光です',
            'difficulty': 'beginner',
            'category': 'concepts'
        }
    }
    
    # Enhance flashcards with Japanese data
    enhanced_flashcards = []
    for card in flashcards:
        english_word = card['english'].lower()
        
        if english_word in japanese_vocabulary:
            jp_data = japanese_vocabulary[english_word]
            enhanced_card = {
                **card,
                'japanese': jp_data['japanese'],
                'romaji': jp_data['romaji'],
                'hiragana': jp_data.get('hiragana', ''),
                'katakana': jp_data.get('katakana', ''),
                'pronunciation': jp_data['pronunciation'],
                'meaning': jp_data['meaning'],
                'example': jp_data['example'],
                'difficulty': jp_data['difficulty'],
                'category': jp_data['category']
            }
        else:
            # Provide basic data for words not in our enhanced list
            enhanced_card = {
                **card,
                'japanese': f'[{english_word}]',
                'romaji': english_word,
                'hiragana': '',
                'katakana': '',
                'pronunciation': f'[{english_word.upper()}]',
                'meaning': f'[{english_word}]',
                'example': f'Example with {english_word}',
                'difficulty': 'beginner',
                'category': 'general'
            }
        
        enhanced_flashcards.append(enhanced_card)
    
    return enhanced_flashcards

def generate_flashcard_webapp(flashcards):
    """Generate the complete web application"""
    
    # Convert flashcards to JavaScript format
    flashcard_data = json.dumps(flashcards, ensure_ascii=False, indent=2)
    
    html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 Christian English Flashcards for Japanese Learners</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
            font-size: 1.1em;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .controls {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        
        .btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }}
        
        .btn-primary {{
            background: #667eea;
            color: white;
        }}
        
        .btn-primary:hover {{
            background: #5a6fd8;
            transform: translateY(-2px);
        }}
        
        .btn-secondary {{
            background: #764ba2;
            color: white;
        }}
        
        .btn-secondary:hover {{
            background: #6a4190;
            transform: translateY(-2px);
        }}
        
        .btn-success {{
            background: #4CAF50;
            color: white;
        }}
        
        .btn-success:hover {{
            background: #45a049;
            transform: translateY(-2px);
        }}
        
        .progress-bar {{
            width: 100%;
            height: 20px;
            background: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #4CAF50, #45a049);
            transition: width 0.3s ease;
            border-radius: 10px;
        }}
        
        .flashcard-container {{
            perspective: 1000px;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .flashcard {{
            width: 100%;
            height: 400px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s;
            cursor: pointer;
        }}
        
        .flashcard.flipped {{
            transform: rotateY(180deg);
        }}
        
        .card-face {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px;
            text-align: center;
        }}
        
        .card-front {{
            background: white;
            color: #333;
        }}
        
        .card-back {{
            background: linear-gradient(135deg, #4CAF50, #45a049);
            color: white;
            transform: rotateY(180deg);
        }}
        
        .english-word {{
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        .pronunciation {{
            font-size: 1.3em;
            color: #666;
            margin-bottom: 20px;
            font-style: italic;
        }}
        
        .frequency {{
            background: #f0f0f0;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            color: #666;
        }}
        
        .japanese-word {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .romaji {{
            font-size: 1.5em;
            margin-bottom: 15px;
            opacity: 0.9;
        }}
        
        .hiragana-katakana {{
            font-size: 1.2em;
            margin-bottom: 10px;
            opacity: 0.8;
            font-style: italic;
            color: #E8F5E8;
        }}
        
        .pronunciation-guide {{
            font-size: 1.1em;
            margin-bottom: 15px;
            opacity: 0.7;
            font-family: monospace;
            background: rgba(255,255,255,0.1);
            padding: 5px 10px;
            border-radius: 10px;
        }}
        
        .meaning {{
            font-size: 1.8em;
            margin-bottom: 20px;
            font-weight: bold;
        }}
        
        .example {{
            font-size: 1.1em;
            opacity: 0.9;
            max-width: 400px;
            line-height: 1.4;
        }}
        
        .card-navigation {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 600px;
            margin: 30px auto;
        }}
        
        .card-counter {{
            background: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: bold;
            color: #667eea;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .difficulty-filter {{
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .filter-btn.active {{
            background: #667eea;
            color: white;
        }}
        
        .stats {{
            display: flex;
            justify-content: space-around;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
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
            font-size: 0.9em;
        }}
        
        .achievements {{
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }}
        
        .achievement {{
            padding: 8px 16px;
            background: #FFD700;
            color: #333;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        
        .audio-btn {{
            background: #FF6B6B;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            margin-top: 15px;
            transition: all 0.3s ease;
        }}
        
        .audio-btn:hover {{
            background: #FF5252;
            transform: translateY(-2px);
        }}
        
        .category-tag {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: #764ba2;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: bold;
        }}
        
        .flip-hint {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: #999;
            font-size: 0.9em;
            opacity: 0.7;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .controls {{
                flex-direction: column;
                align-items: center;
            }}
            
            .english-word {{
                font-size: 2.5em;
            }}
            
            .japanese-word {{
                font-size: 2em;
            }}
            
            .stats {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎵 Christian English Flashcards</h1>
            <p>日本人学習者向けの英語フラッシュカード - Learn English vocabulary from Christian songs</p>
        </div>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number" id="totalCards">0</div>
                <div class="stat-label">Total Cards / 総カード数</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="currentCard">1</div>
                <div class="stat-label">Current Card / 現在のカード</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="studiedCards">0</div>
                <div class="stat-label">Studied / 学習済み</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="masteredCards">0</div>
                <div class="stat-label">Mastered / 習得済み</div>
            </div>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" id="progressFill"></div>
        </div>
        
        <div class="difficulty-filter">
            <button class="filter-btn active" onclick="filterByDifficulty('all')">All / すべて</button>
            <button class="filter-btn" onclick="filterByDifficulty('beginner')">Beginner / 初級</button>
            <button class="filter-btn" onclick="filterByDifficulty('intermediate')">Intermediate / 中級</button>
            <button class="filter-btn" onclick="filterByDifficulty('advanced')">Advanced / 上級</button>
        </div>
        
        <div class="controls">
            <button class="btn btn-primary" onclick="previousCard()">← Previous / 前へ</button>
            <button class="btn btn-secondary" onclick="flipCard()">Flip Card / カードを回転</button>
            <button class="btn btn-primary" onclick="nextCard()">Next / 次へ →</button>
        </div>
        
        <div class="flashcard-container">
            <div class="flashcard" id="flashcard" onclick="flipCard()">
                <div class="card-face card-front">
                    <div class="category-tag" id="categoryTag">Faith</div>
                    <div class="english-word" id="englishWord">Loading...</div>
                    <div class="pronunciation" id="pronunciation">[Loading...]</div>
                    <div class="frequency" id="frequency">Appears in songs: 0 times</div>
                    <button class="audio-btn" onclick="playAudio(event)">🔊 Listen / 音声</button>
                    <div class="flip-hint">Click to flip / クリックして回転</div>
                </div>
                <div class="card-face card-back">
                    <div class="japanese-word" id="japaneseWord">読み込み中...</div>
                    <div class="romaji" id="romaji">Loading...</div>
                    <div class="hiragana-katakana" id="hiraganaKatakana">Loading...</div>
                    <div class="pronunciation-guide" id="pronunciationGuide">[Loading...]</div>
                    <div class="meaning" id="meaning">Loading...</div>
                    <div class="example" id="example">Loading example...</div>
                    <button class="audio-btn" onclick="playAudio(event)">🔊 Listen / 音声</button>
                </div>
            </div>
        </div>
        
        <div class="card-navigation">
            <button class="btn btn-success" onclick="markAsKnown()">✓ I Know This / 知っている</button>
            <div class="card-counter">
                <span id="cardPosition">1</span> / <span id="totalCount">0</span>
            </div>
            <button class="btn btn-secondary" onclick="markForReview()">📚 Review Later / 後で復習</button>
        </div>
        
        <div class="controls">
            <button class="btn btn-primary" onclick="shuffle()">🔀 Shuffle / シャッフル</button>
            <button class="btn btn-secondary" onclick="resetProgress()">🔄 Reset / リセット</button>
            <button class="btn btn-success" onclick="exportProgress()">💾 Export Progress / 進捗エクスポート</button>
        </div>
        
        <div class="achievements" id="achievements">
            <!-- Achievements will be added here -->
        </div>
    </div>
    
    <script>
        // Flashcard data
        const flashcards = {flashcard_data};
        
        // App state
        let currentIndex = 0;
        let filteredCards = flashcards;
        let isFlipped = false;
        let studiedCards = new Set();
        let masteredCards = new Set();
        let reviewCards = new Set();
        
        // Initialize app
        document.addEventListener('DOMContentLoaded', function() {{
            loadProgress();
            updateStats();
            displayCard();
        }});
        
        // Display current card
        function displayCard() {{
            if (filteredCards.length === 0) return;
            
            const card = filteredCards[currentIndex];
            const flashcardElement = document.getElementById('flashcard');
            
            // Update front of card
            document.getElementById('englishWord').textContent = card.english.toUpperCase();
            document.getElementById('pronunciation').textContent = '[' + card.pronunciation + ']';
            document.getElementById('frequency').textContent = `Appears in songs: ${{card.frequency_in_songs}} times`;
            document.getElementById('categoryTag').textContent = card.category || 'General';
            
            // Update back of card
            document.getElementById('japaneseWord').textContent = card.japanese;
            document.getElementById('romaji').textContent = card.romaji;
            
            // Update hiragana/katakana pronunciation
            const hiraganaKatakana = card.hiragana || card.katakana || '';
            const pronunciationText = hiraganaKatakana ? 
                `${{hiraganaKatakana}} (pronunciation: ${{card.pronunciation}})` : 
                `Pronunciation: ${{card.pronunciation}}`;
            document.getElementById('hiraganaKatakana').textContent = hiraganaKatakana;
            document.getElementById('pronunciationGuide').textContent = pronunciationText;
            
            document.getElementById('meaning').textContent = card.meaning;
            document.getElementById('example').textContent = card.example;
            
            // Update card counter
            document.getElementById('cardPosition').textContent = currentIndex + 1;
            document.getElementById('totalCount').textContent = filteredCards.length;
            
            // Reset flip state
            flashcardElement.classList.remove('flipped');
            isFlipped = false;
            
            updateStats();
        }}
        
        // Flip card
        function flipCard() {{
            const flashcardElement = document.getElementById('flashcard');
            flashcardElement.classList.toggle('flipped');
            isFlipped = !isFlipped;
            
            // Mark as studied when flipped
            if (isFlipped) {{
                studiedCards.add(filteredCards[currentIndex].english);
                saveProgress();
                updateStats();
            }}
        }}
        
        // Navigation functions
        function nextCard() {{
            currentIndex = (currentIndex + 1) % filteredCards.length;
            displayCard();
        }}
        
        function previousCard() {{
            currentIndex = (currentIndex - 1 + filteredCards.length) % filteredCards.length;
            displayCard();
        }}
        
        // Filter by difficulty
        function filterByDifficulty(difficulty) {{
            // Update active filter button
            document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Filter cards
            if (difficulty === 'all') {{
                filteredCards = flashcards;
            }} else {{
                filteredCards = flashcards.filter(card => card.difficulty === difficulty);
            }}
            
            currentIndex = 0;
            displayCard();
        }}
        
        // Mark card as known
        function markAsKnown() {{
            masteredCards.add(filteredCards[currentIndex].english);
            studiedCards.add(filteredCards[currentIndex].english);
            saveProgress();
            updateStats();
            nextCard();
            checkAchievements();
        }}
        
        // Mark card for review
        function markForReview() {{
            reviewCards.add(filteredCards[currentIndex].english);
            saveProgress();
            nextCard();
        }}
        
        // Shuffle cards
        function shuffle() {{
            for (let i = filteredCards.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [filteredCards[i], filteredCards[j]] = [filteredCards[j], filteredCards[i]];
            }}
            currentIndex = 0;
            displayCard();
        }}
        
        // Update statistics
        function updateStats() {{
            document.getElementById('totalCards').textContent = filteredCards.length;
            document.getElementById('currentCard').textContent = currentIndex + 1;
            document.getElementById('studiedCards').textContent = studiedCards.size;
            document.getElementById('masteredCards').textContent = masteredCards.size;
            
            // Update progress bar
            const progress = (studiedCards.size / flashcards.length) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }}
        
        // Play audio (Text-to-Speech)
        function playAudio(event) {{
            event.stopPropagation();
            const card = filteredCards[currentIndex];
            const text = isFlipped ? card.japanese : card.english;
            const lang = isFlipped ? 'ja-JP' : 'en-US';
            
            if ('speechSynthesis' in window) {{
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = lang;
                utterance.rate = 0.8;
                speechSynthesis.speak(utterance);
            }} else {{
                alert('Speech synthesis not supported in this browser');
            }}
        }}
        
        // Save progress to localStorage
        function saveProgress() {{
            const progress = {{
                studiedCards: Array.from(studiedCards),
                masteredCards: Array.from(masteredCards),
                reviewCards: Array.from(reviewCards)
            }};
            localStorage.setItem('flashcardProgress', JSON.stringify(progress));
        }}
        
        // Load progress from localStorage
        function loadProgress() {{
            const saved = localStorage.getItem('flashcardProgress');
            if (saved) {{
                const progress = JSON.parse(saved);
                studiedCards = new Set(progress.studiedCards || []);
                masteredCards = new Set(progress.masteredCards || []);
                reviewCards = new Set(progress.reviewCards || []);
            }}
        }}
        
        // Reset progress
        function resetProgress() {{
            if (confirm('Are you sure you want to reset all progress? / 本当に進捗をリセットしますか？')) {{
                studiedCards.clear();
                masteredCards.clear();
                reviewCards.clear();
                localStorage.removeItem('flashcardProgress');
                updateStats();
                document.getElementById('achievements').innerHTML = '';
            }}
        }}
        
        // Export progress
        function exportProgress() {{
            const progress = {{
                studiedCards: Array.from(studiedCards),
                masteredCards: Array.from(masteredCards),
                reviewCards: Array.from(reviewCards),
                totalCards: flashcards.length,
                date: new Date().toISOString()
            }};
            
            const blob = new Blob([JSON.stringify(progress, null, 2)], {{type: 'application/json'}});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'flashcard_progress.json';
            a.click();
            URL.revokeObjectURL(url);
        }}
        
        // Check achievements
        function checkAchievements() {{
            const achievements = [];
            
            if (studiedCards.size >= 5) {{
                achievements.push('🌟 First Steps / 第一歩');
            }}
            if (studiedCards.size >= 10) {{
                achievements.push('📚 Dedicated Learner / 熱心な学習者');
            }}
            if (masteredCards.size >= 5) {{
                achievements.push('💎 Master Beginner / 初級マスター');
            }}
            if (masteredCards.size >= 10) {{
                achievements.push('🏆 Vocabulary Champion / 語彙チャンピオン');
            }}
            
            const achievementsDiv = document.getElementById('achievements');
            achievementsDiv.innerHTML = achievements.map(achievement => 
                `<div class="achievement">${{achievement}}</div>`
            ).join('');
        }}
        
        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {{
            switch(e.key) {{
                case 'ArrowRight':
                case ' ':
                    nextCard();
                    break;
                case 'ArrowLeft':
                    previousCard();
                    break;
                case 'Enter':
                    flipCard();
                    break;
                case 'k':
                    markAsKnown();
                    break;
                case 'r':
                    markForReview();
                    break;
            }}
        }});
        
        // Initialize
        filteredCards = flashcards;
        updateStats();
        displayCard();
    </script>
</body>
</html>
"""
    
    return html_content

def main():
    """Main function to generate the flashcard web app"""
    print("🎌 Generating Interactive Flashcard Web App for Japanese Learners 🎌")
    print("=" * 70)
    
    # Generate enhanced flashcards
    print("📚 Reading and enhancing flashcard data...")
    flashcards = read_lyrics_and_generate_flashcards()
    
    # Generate web app
    print("🎨 Creating interactive web application...")
    html_content = generate_flashcard_webapp(flashcards)
    
    # Save to file
    filename = 'japanese_english_flashcards.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Flashcard web app created: {filename}")
    print(f"📊 Total flashcards: {len(flashcards)}")
    print(f"🎯 Features included:")
    print(f"   • Interactive flip cards with animations")
    print(f"   • Japanese translations with romaji")
    print(f"   • Audio pronunciation (Text-to-Speech)")
    print(f"   • Progress tracking and achievements")
    print(f"   • Difficulty filtering")
    print(f"   • Keyboard shortcuts")
    print(f"   • Mobile responsive design")
    print(f"   • Local storage for progress")
    print(f"")
    print(f"🌐 To use the app:")
    print(f"   1. Open '{filename}' in your web browser")
    print(f"   2. Click cards to flip them")
    print(f"   3. Use navigation buttons or keyboard shortcuts")
    print(f"   4. Track your progress and earn achievements!")
    print(f"")
    print(f"⌨️  Keyboard shortcuts:")
    print(f"   • Space/Right Arrow: Next card")
    print(f"   • Left Arrow: Previous card")
    print(f"   • Enter: Flip card")
    print(f"   • K: Mark as known")
    print(f"   • R: Mark for review")

if __name__ == "__main__":
    main()
