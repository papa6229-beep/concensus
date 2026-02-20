
import os
import sys
import time
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

    # 1. 기존 노트북 삭제 (이전 스크립트로 생성된 제목들)
    old_titles_keywords = [
        "AI 콘텐츠 에이전시", "No-Code 자동화 컨설턴트", "AI 커스텀 아트", 
        "AI 숏폼 비디오", "AI 챗봇 구축", "AI 프롬프트", "AI SEO", 
        "AI 번역", "AI 전자책", "AI 음악"
    ]
    
    print("Listing existing notebooks...")
    notebooks = client.list_notebooks()
    
    print("Deleting old notebooks...")
    deleted_count = 0
    for nb in notebooks:
        # Check if title matches any of the old keywords
        if any(keyword in nb.title for keyword in old_titles_keywords):
            print(f"Deleting: {nb.title} ({nb.id})...", end="", flush=True)
            try:
                client.delete_notebook(nb.id)
                print(" DONE!")
                deleted_count += 1
                time.sleep(0.5) # Prevent rate limiting
            except Exception as e:
                print(f" FAILED! ({e})")
    
    print(f"Deleted {deleted_count} old notebooks.")

    # 2. 신규 노트북 생성
    new_ideas = [
        "1. 🛒 쇼핑몰 데이터 분석 & 마케팅 인사이트 (AI Analytics)",
        "2. 🛍️ AI 오토 큐레이션 커머스 (Auto-Curation Commerce)",
        "3. 📰 초개인화 뉴스레터 구독 서비스 (Personalized Newsletter)",
        "4. 🎓 AI 튜터링 & 코칭 플랫폼 (SaaS LMS)",
        "5. 📢 로컬 비즈니스 리드 생성 (Lead Gen Agency)",
        "6. 📱 SNS 바이럴 콘텐츠 공장 (Viral Content Factory)",
        "7. 🛠️ 마이크로 SaaS 웹 툴 (Micro-SaaS Tools)",
        "8. 🎨 디지털 에셋 자동 판매 (Digital Asset Store)",
        "9. 📞 AI CS & 예약 관리 에이전트 (Auto-Receptionist)",
        "10. 🌐 글로벌 니치 블로그 제휴 마케팅 (Global Affiliate)"
    ]

    print(f"\nCreating {len(new_ideas)} NEW notebooks...")
    created_count = 0
    for title in new_ideas:
        print(f"Creating: {title}...", end="", flush=True)
        try:
            nb = client.create_notebook(title=title)
            print(f" DONE! (ID: {nb.id})")
            created_count += 1
            time.sleep(1) # Prevent rate limiting
        except Exception as e:
            print(f" FAILED! ({e})")

    print(f"\nFinished! Created {created_count}/{len(new_ideas)} new notebooks.")

if __name__ == "__main__":
    main()
