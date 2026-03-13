
import re

def clean_html(content):
    # 1. Remove CSS language blocks
    # Remove .lang-en, .lang-mn, .lang-fa block
    content = re.sub(r'\.lang-en,\s*\.lang-mn,\s*\.lang-fa\s*\{[^}]*\}', '', content)
    
    # Remove language mode blocks (body.en-mode, etc.)
    content = re.sub(r'body\.en-mode[^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'body\.mn-mode[^}]*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'body\.fa-mode[^}]*\}', '', content, flags=re.DOTALL)
    
    # Remove Korean mode visibility overrides that are complex
    content = re.sub(r'body:not\(\.en-mode\):not\(\.mn-mode\):not\(\.fa-mode\)\s+\.lang-ko\s*\{[^}]*\}', '', content)
    content = re.sub(r'body:not\(\.en-mode\):not\(\.mn-mode\):not\(\.fa-mode\)\s+\.[^}]*\}', '', content, flags=re.DOTALL)

    # 2. Remove language elements from HTML body
    # This is trickier with regex, but since it's well-structured...
    # We want to remove tags that have class="..." including lang-en, lang-mn, or lang-fa
    # Matches: <tag ... class="... lang-en ..." ...>...</tag>
    # Note: This might not catch everything if it spans multiple lines, but let's try.
    
    # Remove elements with lang-en, lang-mn, or lang-fa classes
    # We'll do it by finding tags with these classes.
    # We'll use a pattern that matches the whole element if it's on one or few lines.
    # Actually, a better way is to use a simple approach for the specific file structure.
    
    # Remove <li class="lang-en">...</li>, <span class="lang-en">...</span>, etc.
    content = re.sub(r'<[^>]*class="[^"]*(lang-en|lang-mn|lang-fa)[^"]*"[^>]*>.*?</[^>]+>', '', content, flags=re.DOTALL)
    # Also handle self-closing or empty ones if any
    content = re.sub(r'<[^>]*class="[^"]*(lang-en|lang-mn|lang-fa)[^"]*"[^>]*/?>', '', content)

    # 3. Clean up lang-ko classes (remove the class but keep the tag content)
    # <span class="lang-ko">Text</span> -> Text
    # We'll just remove the class attribute or the whole span if it only has this class.
    # Keep it simple: <span class="lang-ko">...</span> -> <span>...</span> or just remove the class.
    content = re.sub(r'class="lang-ko"', '', content)
    content = re.sub(r'class="\s*lang-ko\s*"', '', content) # with whitespace
    
    # Remove language toggle logic in JS
    content = re.sub(r'// 글로벌 다국어 전환 기능.*?function setLanguage.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'setLanguage\(savedLang\);', '', content)
    content = re.sub(r'const savedLang = localStorage.getItem\(\'pref-lang\'\) \|\| \'ko\';', '', content)

    # Final cleanup: Remove empty styles or double spaces
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content

with open('hansoo.html', 'r', encoding='utf-8') as f:
    text = f.read()

cleaned = clean_html(text)

with open('hansoo_cleaned.html', 'w', encoding='utf-8') as f:
    f.write(cleaned)
