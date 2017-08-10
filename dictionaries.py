apple_language = {
    "spanish" : "manzana",
    "french" : "pomme",
    "latin" : "appel"
}
banana_language = {
    "spanish" : "plátano",
    "french" : "banane",
    "dutch" : "banaan"
}
orange_language = {
    "spanish" : "naranja",
    "french" : "orange",
    "dutch" : "oranje"
}
watermelon_language = {
    "spanish" : "sandía",
    "french" : "pastèque",
    "dutch" : "oranje"
}
strawberry_language = {
    "spanish" : "fresa",
    "french" : "fraise",
    "dutch" : "aardbei"
}

fruits = {
"apple" : apple_language,
"banana" : banana_language,
"orange" : orange_language,
"watermelon" : watermelon_language,
"strawberry" : strawberry_language
}
for key in fruits:
    print(key)
word = input("choose an English word to translate")
for key in fruits[word]:
    print(key)
language = input("choose a language")
print(fruits[word][language])
