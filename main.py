from preprocess import preprocess_text
from summarizer import generate_summary

def summarize_legal_doc(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = preprocess_text(text)
    joined_text = " ".join(sentences[:20])  # Limit for performance

    summary = generate_summary(joined_text)
    print("\nOriginal Text Preview:\n", joined_text[:500], "...\n")
    print("Generated Summary:\n", summary)

if __name__ == "__main__":
    summarize_legal_doc("sample_legal.txt")  # Add your legal file
