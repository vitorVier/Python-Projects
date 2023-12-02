message = input("> ")
words = message.split( " ")
emojis = {
    ":)" : "🙂",
    ":(" : "🙁"
}

outcome = " "

for word in words:
   outcome += emojis.get(word, word) + " "

print(outcome)