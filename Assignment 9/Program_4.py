import re

def average_score_read(file):
    sco_list = []
    with open(file, 'r') as contents:
        for line in contents:
            score = re.findall(r',(\d*)', line)
            sco_list.append(int(score[0]))
    return sum(sco_list) / len(sco_list)
    
print(average_score_read('Score.txt'))