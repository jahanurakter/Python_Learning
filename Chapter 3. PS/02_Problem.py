#Write a program to fill in a letter template given below with data

letter = """Dear <|Name|>,
            You are Selected.
            <|Date|>
            \"For my career\""""


print(letter.replace("<|Name|>","Python").replace("<|Date|>",
                                                  "01 June 2026"))

#replace is a string function by replace name and date changed
