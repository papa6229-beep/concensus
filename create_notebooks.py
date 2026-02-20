
import os
import sys
from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

def main():
    print("Loading auth tokens...")
    try:
        cached = load_cached_tokens()
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    if not cached:
        print("Error: No cached tokens found. Run 'notebooklm-mcp-auth' first.")
        return

    print("Initializing NotebookLM client...")
    client = NotebookLMClient(
        cookies=cached.cookies,
        csrf_token=cached.csrf_token,
        session_id=cached.session_id,
    )
    
    ideas = [
        "1. AI 콘텐츠 에이전시 (Content Agency)",
        "2. No-Code 자동화 컨설턴트 (Automation Expert)",
        "3. AI 커스텀 아트 및 POD (Custom Art & POD)",
        "4. AI 숏폼 비디오 제작소 (Short-form Video Factory)",
        "5. AI 챗봇 구축 대행 (Chatbot Service)",
        "6. AI 프롬프트 엔지니어링 (Prompt Engineering)",
        "7. AI SEO 전문가 (SEO Specialist)",
        "8. AI 번역 및 로컬라이징 (Translation & Localization)",
        "9. AI 전자책 및 강의 저작 (E-book & Course Creator)",
        "10. AI 음악 및 오디오 서비스 (Music & Audio Service)"
    ]

    print(f"Starting creation of {len(ideas)} notebooks...")
    
    created_count = 0
    for title in ideas:
        print(f"Creating notebook: {title}...", end="", flush=True)
        try:
            nb = client.create_notebook(title=title)
            print(f" DONE! (ID: {nb.id})")
            created_count += 1
        except Exception as e:
            print(f" FAILED! ({e})")

    print(f"\nFinished! Created {created_count}/{len(ideas)} notebooks.")

if __name__ == "__main__":
    main()
