import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifier):
        self._classifier = classifier

    def classify(self,features):
        votes=[]
        for c in self.classifiers:
            v=c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self,features):
        votes=[]
        for c in self.classifiers:
            v=c.classify(features)
            votes.append(v)
        choice_votes=votes.count(mode(votes))
        conf=choice_votes / len(votes)
        return conf
        
short_positive = open("short_reviews/positive.txt","r").read()
short_negative = open("short_reviews/negative.txt","r").read()

allowed_word_types = ["J"] #adjective allowed
all_words = []
documents = []
for p in short_positive.split('\n'):
    documents.append((p,"positive"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for p in short_negative.split('\n'):
    documents.append((p,"negative"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

save_document = open("pickled_modules/documents.pickle","wb")
pickle.dump(documents,save_document)
save_documents.close()

def find_features(document):
    words=word_tokenize(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return(features)

feature_set=[(find_features(rev),category)for (rev,category) in documents]
random.shuffle(feature_set)
print(len(feature_set))

training_set=feature_set[:10000]
testing_set=feature_set[10000:]

classifier= nltk.NaiveBayesClassifier.train(training_set)
print("Original Analysis accuracy : ", (nltk.classify.accuracy(classifier,training_set)*100))
classifier.show_most_informative_features(15)

save_classifier= open("pickled_modules/OriginalNaiveBayes.pickle","wb")
pickle.dump(classifier,save_file)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("Multinomial Analysis accuracy : ", (nltk.classify.accuracy(MNB_classifier,training_set)*100))
save_classifier= open("pickled_modules/MultiNomialNaiveBayes.pickle","wb")
pickle.dump(MNB,save_file)
save_classifier.close()

BernoulliNB = SklearnClassifier(BernoulliNB())
BernoulliNB.train(training_set)
print("Bernoulli Analysis accuracy : ", (nltk.classify.accuracy(BernoulliNB,training_set)*100))
save_classifier= open("pickled_modules/BernoulliNaiveBayes.pickle","wb")
pickle.dump(BernoulliNB,save_file)
save_classifier.close()

LogisticRegression = SklearnClassifier(LogisticRegression())
LogisticRegression.train(training_set)
print("LogisticRegression Analysis accuracy : ", (nltk.classify.accuracy(LogisticRegression,training_set)*100))
save_classifier= open("pickled_modules/LogRegressionNaiveBayes.pickle","wb")
pickle.dump(LogisticRegression,save_file)
save_classifier.close()

SGDClassifier = SklearnClassifier(SGDClassifier())
SGDClassifier.train(training_set)
print("SGDClassifier Analysis accuracy : ", (nltk.classify.accuracy(SGDClassifier,training_set)*100))
save_classifier= open("pickled_modules/SGDClassifierNaiveBayes.pickle","wb")
pickle.dump(SGDClassifier,save_file)
save_classifier.close()

SVC = SklearnClassifier(SVC())
SVC.train(training_set)
print("SVC Analysis accuracy : ", (nltk.classify.accuracy(SVC,training_set)*100))
save_classifier= open("pickled_modules/SVCNaiveBayes.pickle","wb")
pickle.dump(SVC,save_file)
save_classifier.close()

LinearSVC = SklearnClassifier(LinearSVC())
LinearSVC.train(training_set)
print("LinearSVC Analysis accuracy : ", (nltk.classify.accuracy(LinearSVC,training_set)*100))
save_classifier= open("pickled_modules/LineraSVCNaiveBayes.pickle","wb")
pickle.dump(LinearSVC,save_file)
save_classifier.close()

voted_classifier=VoteClassifier(classifier_f,MNB_classifier,
                                BernoulliNB,LogisticRegression,
                                SGDClassifier,SVC,LinearSVC)
print("voted_classifier Analysis accuracy : ", (nltk.classify.accuracy(voted_classifier,training_set)*100))

def sentiment(text):
    feats=find_features(text)

    return voted_classifier.classify(feats)
