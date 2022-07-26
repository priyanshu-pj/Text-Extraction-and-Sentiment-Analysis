from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
from nltk.corpus import stopwords


vowels = ['a', 'e', 'i', 'o', 'u']
personal_pronouns = ['I', 'me', 'you', 'he', 'she', 'it', 'him', 'her', 'we', 'us', 'they', 'them']


def sentiment_analyzer(file_name):
    """This function performs sentimental analysis on the text"""
    variables = list()

    with open(file_name, 'r', encoding='utf-16') as file:
        data = file.read()
        words = word_tokenize(data)
        sentences = sent_tokenize(data)


    """Cleaning using Stop Words List"""
    with open('files/StopWords_Generic.txt', 'r') as file:
        stop_words = file.read()

    # cleaned data removes all of the stop words present in the text
    cleaned_data = [word for word in words if word not in stop_words]


    """Creating Dictionary of Positive and Negative words"""
    # The master dictionary
    master_dic = pd.read_excel('files/LoughranMcDonald_MasterDictionary_2020.xlsx')
    pos_dict = [x for x in master_dic.loc[master_dic['Positive'] != 0]['Word']]
    neg_dict = [x for x in master_dic.loc[master_dic['Negative'] != 0]['Word']]


    """Extracting Derived Variables"""
    pos_score = 0
    neg_score = 0
    for word in cleaned_data:
        if word in pos_dict:
            pos_score += 1
        elif word in neg_dict:
            neg_score += 1
    polarity_score              =       (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)
    subjectivity_score          =       (pos_score + neg_score)/ ((len(cleaned_data)) + 0.000001)


    """Complex Word Count"""
    complex_word_count = 0
    for word in words:
        count = 0
        for w in word:
            if(w in vowels and count<2):
                count += 1
            elif count==2:
                complex_word_count += 1
                break


    """Analysis of Readablity"""
    average_sentence_length     =       (len(words) / len(sentences))
    percent_complex_words       =       (complex_word_count / len(words))
    fog_index                   =       (0.4 * (average_sentence_length + percent_complex_words))


    """Average Number of Words Per Sentence"""
    avg_num_words_sent = (len(words) / len(sentences))


    """Word Count"""
    # removing stopwords using nltk stopwords
    stop_words_nltk = stopwords.words('english')
    cleaned_data_nltk = [word for word in words if word not in stop_words_nltk]
    # removing punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_data_nltk = [word for word in cleaned_data_nltk if word not in punctuations]


    """Syllable Count Per Word"""
    syl_count = 0
    for word in words:
        # count the number of vowels in each word
        for w in word:
            if w.lower() in vowels:
                syl_count += 1
        if (len(word) > 2 and (word[-2:] == "es" or word[-2:] == "ed")):
            syl_count -= 1

    syl_count = syl_count / len(words)


    """Personal Pronouns"""
    per_pro_count = 0
    for word in words:
        if((word in personal_pronouns) or (word.capitalize() in personal_pronouns)):
            per_pro_count += 1


    """Average Word Length"""
    total_characters = 0
    for word in words:
        for w in word:
            total_characters += 1

    average_word_length = total_characters / len(words)


    # append the variables to the list
    variables.append(pos_score)
    variables.append(neg_score)
    variables.append(polarity_score)
    variables.append(subjectivity_score)
    variables.append(average_sentence_length)
    variables.append(percent_complex_words)
    variables.append(fog_index)
    variables.append(avg_num_words_sent)
    variables.append(complex_word_count)
    variables.append(len(cleaned_data_nltk))
    variables.append(syl_count)
    variables.append(per_pro_count)
    variables.append(average_word_length)


    print("Done! "+file_name)
    return variables
