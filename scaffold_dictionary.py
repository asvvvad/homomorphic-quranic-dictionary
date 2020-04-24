#!/usr/bin/env python3
#Copyright 2020 Faissal Bensefia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import re
import json

remove_comments = lambda string: re.sub(r'\#.*', '', string)

process_line = lambda surah=None, ayah=None, text=None: {
		'surah': int(surah),
		'ayah': int(ayah),
		'text': text.replace("\n", '').split()
	} if all([surah, ayah, text]) else None

with open('quran-uthmani.txt', 'r') as f:
	all_lines = filter(None, [process_line(*(remove_comments(i)).split('|')) for i in f])

	dictionary_scaffold = {}
	for line in all_lines:
		for word in line['text']:
			if word not in dictionary_scaffold.keys():
				dictionary_scaffold[word] = { 'used_in': [], 'ipa_prounciations': [], 'definitions': [], 'see_also': [] }
			
			dictionary_scaffold[word]['used_in'].append(
				{'surah': line['surah'], 'ayah': line['ayah']}
			)
	with open('quranic-dictionary.json', 'w') as ff:
		json.dump(dictionary_scaffold, ff, sort_keys=True, indent=4)
