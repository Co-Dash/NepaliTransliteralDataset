'''
Taken from https://github.com/sushil79g/Nepali_nlp/blob/master/Nepali_nlp
under MIT license
'''

import string


class Tokenizer:
    def __init__(self):
        pass

    def sentence_tokenize(self, text):
        """This function tokenize the sentences
        
        Arguments:
            text {string} -- Sentences you want to tokenize
        
        Returns:
            sentence {list} -- tokenized sentence in list
        """
        sentences = text.split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences

    def word_tokenize(self, sentence, new_punctuation=[]):
        """This function tokenize with respect to word
        
        Arguments:
            sentence {string} -- sentence you want to tokenize
            new_punctuation {list} -- more punctutaion for tokenizing  default ['।',',',';','?','!','—','-']
        
        Returns:
            list -- tokenized words
        """
        punctuations = ['।', ',', ';', '?', '!', '—', '-', '.']
        if new_punctuation:
            punctuations = set(punctuations + new_punctuation)

        for punct in punctuations:
            sentence = ' '.join(sentence.split(punct))

        return sentence.split()
