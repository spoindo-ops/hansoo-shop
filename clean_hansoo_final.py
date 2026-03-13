
import re

def clean_html(content):
    # 1. Remove style blocks related to languages if any left
    content = re.sub(r'/\* 글로벌 다국어 전환 스타일 \*/.*?\.lang-toggle span\.active \{[^}]*\}', '', content, flags=re.DOTALL)
    
    # 2. Cleanup JS
    content = re.sub(r'// 글로벌 다국어 전환 기능.*?function setLanguage.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'const savedLang = localStorage.getItem\(\'pref-lang\'\) \|\| \'ko\';', '', content)
    content = re.sub(r'setLanguage\(savedLang\);', '', content)

    # 3. Remove all elements with lang-en, lang-mn, lang-fa
    # This pattern matches tags that have one of these classes.
    # We use a non-greedy match for the content.
    # Note: This works for simple tags like <span class="lang-en">Text</span> or <div class="... lang-en ...">...</div>
    # But it can be tricky with nested tags.
    # Since the file mostly has simple language spans, this should work.
    
    # Remove elements with specified language classes
    content = re.sub(r'<([a-zA-Z0-9]+)[^>]*class="[^"]*(lang-en|lang-mn|lang-fa)[^"]*"[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
    
    # 4. Clean up lang-ko classes
    # Change <span class="lang-ko">Text</span> to just Text
    # Change <p class="tags lang-ko">#Tag</p> to <p class="tags">#Tag</p>
    
    # Case: <span class="lang-ko">...</span> -> ...
    content = re.sub(r'<span[^>]*class="lang-ko"[^>]*>(.*?)</span>', r'\1', content, flags=re.DOTALL)
    
    # Case: class="lang-ko" or class="... lang-ko ..."
    content = re.sub(r'class="lang-ko"', '', content)
    content = re.sub(r'class="([^"]*)\s+lang-ko\s+([^"]*)"', r'class="\1 \2"', content)
    content = re.sub(r'class="lang-ko\s+([^"]*)"', r'class="\1"', content)
    content = re.sub(r'class="([^"]*)\s+lang-ko"', r'class="\1"', content)

    # 5. Remove the lang-toggle div
    content = re.sub(r'<div class="lang-toggle".*?</div>', '', content, flags=re.DOTALL)

    # 6. Final cleanup (empty lines)
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content

with open('hansoo.html', 'r', encoding='utf-8') as f:
    text = f.read()

cleaned = clean_html(text)

with open('hansoo.html', 'w', encoding='utf-8') as f:
    f.write(cleaned)
