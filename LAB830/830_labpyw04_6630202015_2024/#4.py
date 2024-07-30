
#? 4. Create Dict 1key- M values

shopping = {'produce': ['apples', 'orange', 'spinach', 'carrots'], 'meat': ['ground beef', 'chicken breast']}
shopping['meat']
shopping['produce'] 

print("Produce items on your list:")
for item in shopping['produce']:
    print("* " + item, end=' ')