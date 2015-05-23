from nose.tools import *
from ex48.parser import *
from ex48.lexicon import *

def test_corret_sentences():
    # test a simple sentence 1
    sentence = "go north"
    scanned = scan(sentence)
    parse_sentence([('verb', 'go'), ('direction', 'north')])
    sentence1 = parse_sentence(scan("go north"))
    
    sentence2 = Sentence((0,'a'), (1,'a'), (2,'a'))
    sentence2.object = 'north'
    sentence2.verb = 'go'
    sentence2.subject = 'player'

    assert_equal(sentence1.object, sentence2.object)
    

    # test a simple sentence 2
    sentence = "player eat bear"
    sentence1 = parse_sentence(scan(sentence))
    
    sentence2 = Sentence((0,'a'), (1,'a'), (2,'a'))
    sentence2.object = 'bear'
    sentence2.verb = 'eat'
    sentence2.subject = 'player'

    assert_equal(sentence1.object, sentence2.object)
