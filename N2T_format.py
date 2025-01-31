import re


def convert_markdown(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # 변환: # 하나짜리를 ## 두 개로 변환
    content = re.sub(r"^(# )", r"## ", content, flags=re.MULTILINE)

    # 변환: <aside>content</aside> 를 삭제
    content = re.sub(r"<aside>.*?</aside>", "", content, flags=re.DOTALL)

    # 변환: --- 디바이더 전후에 <br> 태그와 한 줄 패딩 추가
    content = re.sub(r"---", r"<br>\n\n---\n\n<br>", content)

    # 새로운 파일명 생성
    output_file = input_file.replace(".md", "_converted.md")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"변환 완료: {output_file}")


input_file = "./test.md"
convert_markdown(input_file)
