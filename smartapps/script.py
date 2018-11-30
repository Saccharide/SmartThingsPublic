import glob

files = glob.glob("./"+ '/**/*.groovy', recursive=True)
with open ("public_description.csv" , 'w') as csv_file:

    for file in files:
        with open (file, "r") as f:
            name = ""
            description = ""
            done_parsing = False
            for line in f:
                if not done_parsing:
                    if "definition(" in line:
                        in_def_block = True
                        continue
                    elif "name:" in line: 
                        name = line.split("\"")[1]
    
                    elif "description: " in line:
                        if in_def_block:
                            description = line.split("\"")[1]
                            done_parsing = True
            combined = name + "," + '\"' + description + '\"\n'
            csv_file.write(combined)
