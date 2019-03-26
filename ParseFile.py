filename = 'c:/temp/pg35688.txt'

with open(filename) as file_object:
    contents = file_object.read()

worldlist = contents.split()

len_worldlist = len(worldlist)

print('Total ' + str(len_worldlist) + ' words in the book')

summary_list = []
count_summary = 0
for word in worldlist:
    if word in summary_list:
        count_summary = count_summary
    else:
        count_summary += 1
        summary_list.append(word.lower())

summaryfile = 'c:/temp/summarylist.txt'
with open(summaryfile, 'w') as summary_object:
    for aword in summary_list:
        summary_object.write(aword+'\n')
    summary_object.write('Total ' + str(count_summary) + ' words used in the book')

wordfile = 'c:/temp/wordlist.txt'
for i in range(1, len_worldlist):
    worldlist[i] = worldlist[i] + '\n'
with open(wordfile, 'w') as word_object:
    word_object.writelines(worldlist)

