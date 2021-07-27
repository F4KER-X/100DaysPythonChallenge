PLACEHOLDER = "[name]"

with open(r"Day 024 - Mail Merge\Input\Names\invited_names.txt") as invited:
    names = invited.readlines()

with open(r"Day 024 - Mail Merge\Input\Letters\starting_letter.docx") \
        as letter:
    message = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = message.replace(PLACEHOLDER, stripped_name)
        with open(f"Day 024 - Mail Merge/Output/ReadyToSend/letterTo{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
