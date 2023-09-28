# -*- coding: utf-8 -*-
"""text_summarization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLj6fDynHxQ1U9MEMiadt0Ev9VuZP1mH
"""

!pip3 install transformers torch sentencepiece

from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")
original_text = """
// enter the text you want summarized here
"""
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)