import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Swarnavo Majumder"
token = enc.encode(text)

# [25216, 3274, 0, 3673, 1308, 382, 6529, 1978, 9528, 18968, 394, 761]
print("Tokens: ", token)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 6529, 1978, 9528, 18968, 394, 761])
print("Decoded: ", decoded)