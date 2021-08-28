text = "X-DSPAM-Confidence:    0.8475";
x = text.find("0")
result = text[x:]
print(float(result))
