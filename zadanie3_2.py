shopping_dict = {
    "piekarnia," : ["Chleb", "Pączek", "Bułki"],
    "warzywniak," : ["Marchew", "Seler", "Rukola"]
}

for key, value in shopping_dict.items():
    print("Idę do", key.capitalize(),  "kupuję tu następujące rzeczy", value)


len_values = len(shopping_dict["piekarnia,"]) + len(shopping_dict["warzywniak,"])
print("W sumie kupuję", len_values , "produktów")
