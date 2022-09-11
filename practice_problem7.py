
from asyncio.windows_events import NULL


def search_engine(sentence1,sentence2):
    word1 = sentence1.split(" ")
    word2 = sentence2.split(" ")
    score = 0
    for words in word1:
        for words1 in word2:
            if words.lower() == words1.lower():
                score+=1
            
    return score

if __name__ =='__main__':
    mystr =['python is best','ashutosh is the best','python is also a snake']
    search = input('Search here :- ')
    scores = [search_engine(search,sentence)for sentence in mystr]
    sent_score=[sent_scores for sent_scores in sorted(zip(scores,mystr))]
    for score,item in sent_score:
        if score > 0 :
            print(item)
        elif score == 0:
            NULL
        
