import json
import csv
import re

pattern = r"(.*?)\n"

i = 0
# 读取 JSON 文件
with open('lens.json', 'r') as file:
    data = json.load(file)

# 创建 CSV 文件并获取写入器
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pillar Name', 'Question Title', 'Choice Title', 'Trusted Advisor Checks', 'Question ID', 'Choice ID'])

    for pillar in data['pillars']:
        pillar_name = pillar['name']
        for question in pillar['questions']:
            question_title = question['title']
            question_ID = question['id']
            for choice in question['choices']:
                choice_title = choice['title']
                choice_ID = choice['id']
                helpful_resource = choice['helpfulResource']['displayText']
                if 'Trusted Advisor Checks:' in helpful_resource:
                    matches = re.findall(pattern, helpful_resource)
                    for match in matches:
                        if match.startswith("Trusted Advisor Checks:"):
                            continue
                        if match.startswith("Details:"):
                            break
                        if match.strip() != '':
                            writer.writerow([pillar_name, question_title, choice_title, match.strip(), question_ID, choice_ID])
