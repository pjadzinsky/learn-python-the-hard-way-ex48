from nose.tools import *
from ex48.parser import *
from ex48.lexicon import *
import pdb

def test_corret_sentences():
    pdb.set_trace()
    #parse_sentence([('verb', 'go'), ('direction', 'north')])
    sentence1 = parse_sentence(scan("go north"))
    #print(sent_obj1.__dict__)
    #scanned = scan(sentence)
    #sent_obj1 = Sentence(scanned['noun'], scanned['verb'], scanned['object'])

    sentence2 = Sentence((0,'a'), (1,'a'), (2,'a'))
    sentence2.object = 'north'
    sentence2.verb = 'go'
    sentence2.subject = 'player'

    assert_equal(sentence1.object, sentence2.object)
