import preprocess
import stopword
import time
from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()

def read_file(file_address):
    with open(file_address, 'r', encoding = 'utf-8') as f:
        file_content = f.readlines()

    return file_content

def stemming(tokens):
    result = []
    for token in tokens:
        result.append(lancaster.stem(token))
    return result

def normalize(text):
    preprocessed = preprocess.PreProcess(text)
    preprocessed.remove_punctuation()
    return preprocessed

def not_null(obj):
    return obj != None

def tokenize(normalized):
    if not_null(normalized):
        tokens = normalized.split()
        return tokens
    else: return normalized

def remove_stopwords(tokens):
    sword = stopword.StopWord()
    return sword.remove_stopwords(tokens)

def write_lists_to_file(positive_vector, negative_vector, file_name):
    f = open("result/" + file_name + "_p.txt", "w")
    f.write(str(positive_vector))
    f.close()

    f = open("result/" + file_name + "_n.txt", "w")
    f.write(str(negative_vector))
    f.close()

def get_time():
    return time.time()

def print_status(document, start_time):
    if document.getDocId() % 1500 == 0:
        print(document.getDocId(), time.time() - start_time)


   
if __name__ == '__main__':
    all_tokens = []
    tokens_list = []
    file_address = "/home/arash/learning/data_mining/assignment/dm/persianPreProcess/data/yelp_labelled.txt"
    lines = read_file(file_address)
    counter = 0
    for sentence in lines:
        sentence = sentence.lower()
        normalized_sentence = normalize(sentence)
        tokens = tokenize(normalized_sentence.get_text())
        tokens = remove_stopwords(tokens)
        tokens = stemming(tokens)
        tokens_list.append(tokens)
        for token in tokens[:-1]:
            if token not in all_tokens:
                all_tokens.append(token)
    
    positive_vector = [all_tokens]
    negative_vector = [all_tokens]
    for i in range(len(tokens_list)):
        raw_vector = []
        for token in all_tokens:
            if token in tokens_list[i][:-1]:
                raw_vector.append(1)
            else:
                raw_vector.append(0)

        if tokens_list[i][-1] == "1":
            positive_vector.append(raw_vector)
        else:
            negative_vector.append(raw_vector)
    
    write_lists_to_file(positive_vector, negative_vector, "yelp")