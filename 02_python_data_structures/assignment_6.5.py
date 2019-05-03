
text = "X-DSPAM-Confidence:    0.8475"

index = text.find('0')

string_value = text[index:]

float_value = float(string_value)

print(float_value)