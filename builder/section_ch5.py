# -*- coding: utf-8 -*-
import os

def get_section_ch5():
    path = os.path.join(os.path.dirname(__file__), 'ch5.html')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
