import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest



def handle(text, stop_word_vi):



        # Tokenize văn bản thành các câu và chuyển đổi sang chữ thường
        sentences = sent_tokenize(text.lower())

        # Tokenize mỗi câu thành các từ
        words = [word for sentence in sentences for word in word_tokenize(sentence)]

        # Loại bỏ stop words
        filtered_words = [word for word in words if word not in stop_word_vi]

        # Tính tần suất xuất hiện của các từ
        word_freq = FreqDist(filtered_words)

        # Xác định số lượng câu muốn giữ lại trong tóm tắt
        summary_length = 4

        # Chọn ra các câu quan trọng nhất
        important_sentences = nlargest(summary_length, sentences, key=lambda sentence: sum(word_freq[word] for word in word_tokenize(sentence) if word.lower() not in stop_word_vi))

        # In tóm tắt
        summary = ' '.join(important_sentences)
        return summary



