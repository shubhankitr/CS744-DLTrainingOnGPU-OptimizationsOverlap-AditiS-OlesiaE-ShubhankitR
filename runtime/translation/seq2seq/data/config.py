# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

PAD_TOKEN = '<pad>'
UNK_TOKEN = '<unk>'
BOS_TOKEN = '<s>'
EOS_TOKEN = '<\s>'

# special PAD, UNKNOWN, BEGIN-OF-STRING, END-OF-STRING tokens
PAD, UNK, BOS, EOS = [0, 1, 2, 3]

# path to the BPE vocabulary file, relative to the data directory, it should
# point to file generated by subword-nmt/get_vocab.py
VOCAB_FNAME = 'vocab.bpe.32000'

# paths to source and target training files, relative to the data directory, it
# should point to BPE-encoded files, generated by subword-nmt/apply_bpe.py
SRC_TRAIN_FNAME = 'train.tok.clean.bpe.32000.en'
TGT_TRAIN_FNAME = 'train.tok.clean.bpe.32000.de'

# paths to source and target validation files, relative to the data directory,
# it should point to BPE-encoded files, generated by subword-nmt/apply_bpe.py
SRC_VAL_FNAME = 'newstest_dev.tok.clean.bpe.32000.en'
TGT_VAL_FNAME = 'newstest_dev.tok.clean.bpe.32000.de'

# path to the test source file, relative to the data directory, it should point
# to BPE-encoded file, generated by subword-nmt/apply_bpe.py
SRC_TEST_FNAME = 'newstest2014.tok.bpe.32000.en'

# path to the test target file, relative to the data directory, it should point
# to plaintext file, tokenization is performed by the sacrebleu package
TGT_TEST_TARGET_FNAME = 'newstest2014.de'

# path to the moses detokenizer, relative to the data directory
DETOKENIZER = 'mosesdecoder/scripts/tokenizer/detokenizer.perl'
