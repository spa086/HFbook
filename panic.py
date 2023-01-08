phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(5):
    plist.pop()
plist.pop(3)
plist.remove("D")
plist.remove(" ")
plist.insert(2, " ")
plist.insert(4, "a")
on_work = []


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
