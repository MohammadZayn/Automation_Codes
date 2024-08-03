import nltk
from transformers import pipeline

# Make sure to download the required nltk data
nltk.download('punkt')

# Initialize the paraphrase pipeline
paraphrase = pipeline("paraphrase-MRPC")

def rephrase_sentence(sentence):
    # Generate paraphrases for the given sentence
    paraphrases = paraphrase(sentence)
    # Extract and return the rephrased sentences
    rephrased_sentences = [para['generated_text'] for para in paraphrases]
    return rephrased_sentences

def rephrase_paragraph(paragraph, num_rephrases=5):
    # Tokenize the paragraph into sentences
    sentences = nltk.sent_tokenize(paragraph)
    rephrased_paragraphs = []

    # Rephrase each sentence and generate paragraphs
    for _ in range(num_rephrases):
        rephrased_sentences = [rephrase_sentence(sentence)[0] for sentence in sentences]
        rephrased_paragraphs.append(' '.join(rephrased_sentences))

    return rephrased_paragraphs

# Example usage
paragraph = "Machine learning is a field of artificial intelligence. It uses statistical techniques to give computer systems the ability to learn from data. These systems can improve their performance on tasks over time without being explicitly programmed."

rephrased_versions = rephrase_paragraph(paragraph)

# Print the rephrased versions
for i, version in enumerate(rephrased_versions, 1):
    print(f"Rephrased Version {i}:\n{version}\n")
