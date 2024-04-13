#!/usr/bin/env python
# coding: utf-8

संवेदनशीलता = 5
शर्त = True
if शर्त:
    print("संवेदनशीलता:", संवेदनशीलता)
    print("शर्त:", शर्त)
else:
    print("असत्य: सही")

संख्orएँ = [1, 2, 3, 4, 5]
कुल = 0
for ऐ in संख्orएँ:
    कुल += ऐ
    print("संख्याओं का योग:", कुल)

गणना = 10
for ऐ in range(गणना):
    print(ऐ)
    गणना += 1


class मेरी_कक्षा:
    संदेश = "यह एक कक्षा है"

    def print_संदेश(self):
        print(self.संदेश)


पथ = "/कक्षा/उदाहरण/पथ/फ़ाइल.टेक्स्ट"
try:
    with open(पथ) as फ़ाइल:
        pass
except:
    print("फ़ाइल नहीं मिली")
