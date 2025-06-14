import csv
import ast
from openai import OpenAI
import re

client = OpenAI(
    api_key="sk-zZN8G1vgTHXTjpXKPskN9l6FgzReYqhFxCMZsLNEynx6vHV4",
    base_url="https://api.chatanywhere.tech/v1"
)

# 读取测试集
# test_file = 'test_sample.csv'
test_file = 'test.csv'
output_file = 'my_submission.csv'

results = []

# 先统计总行数
total = 0
with open(test_file, newline='', encoding='utf-8') as csvfile:
    total = sum(1 for _ in csvfile) - 1  # 去掉表头

with open(test_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader, 1):
        print(f"正在处理第{idx}/{total}题……")
        qid = row['Id']
        question = row['Question']
        choices = ast.literal_eval(row['Choices'])
        
        # 构造 prompt，包含多个示例
        prompt = f"""请仔细阅读以下数学问题，并从选项中选出正确答案。请严格按照格式输出答案。

示例1：
问题：Martin spends 2 hours waiting in traffic, then four times that long trying to get off the freeway. How much time does he waste total?
选项：[620, 10, 536, 379]
答案是：1

示例2：
问题：Brenda bakes 20 cakes a day. She does this for 9 days and then sells half of the cakes. How many cakes are left with Brenda?
选项：[667, 840, 90, 562]
答案是：2

示例3：
问题：Jorge is 24 years younger than Simon. In 2005, Jorge is 16 years old. In 2010, how old would Simon be?
选项：[289, 45, 236, 336]
答案是：1

示例4：
问题：Jane runs 3 kilometers in two hours. What is her speed in meters per minute?
选项：[893, 558, 834, 25]
答案是：3

示例5：
问题：Mark orders 100 chicken nuggets. A 20 box of chicken nuggets cost $4. How much did he pay for the chicken nuggets?
选项：[614, 938, 20, 997]
答案是：2

示例6：
问题：Tamika drove for 8 hours at an average speed of 45 miles per hour. Logan drove for 5 hours at 55 miles an hour. How many miles farther did Tamika drive?
选项：[519, 248, 774, 85]
答案是：3

示例7：
问题：It takes 20 minutes for John to go to the bathroom 8 times. How long would it take to go 6 times?
选项：[15, 641, 583, 802]
答案是：0

示例8：
问题：The ratio of cows to bulls in a barn is 10:27. If there are 555 cattle on the farm, how many bulls are on the farm?
选项：[453, 405, 846, 613]
答案是：1

示例9：
问题：There are 3 consecutive odd integers that have a sum of -147. What is the largest number?
选项：[11, 837, -47, 609]
答案是：2

示例10：
问题：Anika has 4 more than twice the number of pencils as Reeta. If Reeta has 20 pencils, how many pencils do the two have together?
选项：[64, 525, 70, 657]
答案是：0

示例11：
问题：Twenty gallons of tea were poured into 80 containers. Geraldo drank 3.5 containers. How many pints of tea did Geraldo drink?
选项：[94, 7, 782, 218]
答案是：1

示例12：
问题：A sack of rice, which is 50 kilograms, costs $50. If David sells it for $1.20 per kilogram, how much will be his profit?
选项：[317, 10, 442, 582]
答案是：1

示例13：
问题：Jack has $45 and 36 euros. If each euro is worth two dollars, how much money does he have total in dollars?
选项：[579, 837, 117, 32]
答案是：2

示例14：
问题：Marina had 4.5 pounds of fudge. Lazlo had 6 ounces less than 4 pounds of fudge. How many more ounces of fudge did Marina have than Lazlo?
选项：[535, 38, 14, 905]
答案是：2

示例15：
问题：A train takes 4 hours to reach a destination at a speed of 50 miles per hour. How long would it take if it traveled at 100 miles per hour instead?
选项：[498, 686, 813, 2]
答案是：3

示例16：
问题：On Thursday Walmart sold 210 pounds of ground beef. On Friday they sold twice that amount. On Saturday they only sold 150 pounds. What was the average amount of beef sold per day?
选项：[519, 248, 774, 85]
答案是：1

示例17：
问题：Frank invites his friends over to play video games. He bakes a pan of brownies before he arrives. He cuts 6 even columns and 3 even rows into the pan of brownies. If there are 6 people, how many brownies will each person get?
选项：[3, 18, 9, 6]
答案是：2

示例18：
问题：In Fifi's closet, she hangs all of her clothes on colored plastic hangers. She has clothes hanging on 7 pink hangers, 4 green hangers, one less blue hanger than there are green hangers, and twice as many yellow hangers as blue hangers. How many hangers does Fifi have in her closet?
选项：[25, 22, 19, 28]
答案是：1

示例19：
问题：Gina is figuring out how much she'll have to spend on college this year. She's taking 14 credits that cost $450 each, and she has to pay $120 for each of her 5 textbooks plus a $200 facility fee. How much will Gina spend on college this year?
选项：[$7,300, $7,400, $7,500, $7,600]
答案是：2

示例20：
问题：Luke started working on a 1000-piece jigsaw puzzle. The first day he worked on it, he put together 10% of the pieces. On the second day, he put together another 20% of the remaining pieces. How many pieces has Luke put together so far?
选项：[280, 300, 320, 340]
答案是：0

示例21：
问题：A store sells shirts for $25 each and pants for $45 each. If a customer buys 3 shirts and 2 pairs of pants, and gets a 20% discount on the total, how much does the customer pay?
选项：[165, 132, 198, 231]
答案是：1

示例22：
问题：A rectangular garden has a length of 12 meters and a width of 8 meters. If a path of uniform width is built around the garden, increasing the total area to 224 square meters, what is the width of the path?
选项：[2, 3, 4, 5]
答案是：1

示例23：
问题：A train travels at a constant speed of 60 km/h for the first 2 hours, then increases its speed to 80 km/h for the next 3 hours. What is the average speed for the entire journey?
选项：[72, 70, 75, 68]
答案是：0

示例24：
问题：A company's profit increased by 15% in the first year and then decreased by 10% in the second year. If the initial profit was $100,000, what is the final profit?
选项：[103,500, 104,500, 105,500, 106,500]
答案是：0

示例25：
问题：A mixture contains 40% alcohol and 60% water. If 5 liters of water is added to 20 liters of this mixture, what is the new percentage of alcohol?
选项：[32%, 35%, 38%, 40%]
答案是：0

示例26：
问题：A clock shows 3:45. What is the angle between the hour and minute hands?
选项：[157.5°, 162.5°, 167.5°, 172.5°]
答案是：0

示例27：
问题：A store offers a discount of 20% on all items. If a customer has a coupon for an additional 15% off the discounted price, what is the total discount percentage?
选项：[32%, 35%, 38%, 40%]
答案是：0

示例28：
问题：A rectangular box has dimensions 6cm × 8cm × 10cm. If the length is increased by 20%, the width is decreased by 25%, and the height is increased by 50%, what is the new volume?
选项：[864, 972, 1080, 1188]
答案是：1

示例29：
问题：A car travels 240 km in 3 hours. If it maintains the same speed, how long will it take to travel 400 km?
选项：[4, 5, 6, 7]
答案是：1

示例30：
问题：A shopkeeper marks up the cost price of an item by 40% and then offers a discount of 20% on the marked price. What is the final profit percentage?
选项：[12%, 15%, 18%, 20%]
答案是：0

示例31：
问题：A tank can be filled by pipe A in 6 hours and by pipe B in 8 hours. If both pipes are opened together, how long will it take to fill the tank?
选项：[3.4, 3.6, 3.8, 4.0]
答案是：0

示例32：
问题：A sum of money doubles itself in 8 years at simple interest. What is the rate of interest per annum?
选项：[12.5%, 15%, 17.5%, 20%]
答案是：0

示例33：
问题：A rectangular field has a perimeter of 100 meters. If the length is 10 meters more than the width, what is the area of the field?
选项：[400, 500, 600, 700]
答案是：2

示例34：
问题：A train crosses a platform in 20 seconds and a pole in 10 seconds. If the length of the train is 200 meters, what is the length of the platform?
选项：[100, 200, 300, 400]
答案是：1

示例35：
问题：A mixture of milk and water contains 30% milk. If 10 liters of water is added to 40 liters of this mixture, what is the new percentage of milk?
选项：[24%, 26%, 28%, 30%]
答案是：0

现在请回答以下问题：
问题：{question}
选项：{choices}

请只输出"答案是："后跟选项的索引（从0开始）。例如：答案是：1"""
        
        messages = [{'role': 'user', 'content': prompt}]
        # 调用 LLM API
        completion = client.chat.completions.create(model="deepseek-v3", messages=messages)
        content = completion.choices[0].message.content.strip()
        print(f"模型输出: {content}")
        
        # 使用正则表达式匹配"答案是："后面的数字
        match = re.search(r'答案是：\s*(\d+)', content)
        if match:
            label = int(match.group(1))
        else:
            # 如果没有找到"答案是："，尝试直接提取数字
            match = re.search(r'\b(\d+)\b', content)
            label = int(match.group(1)) if match else 0

        print(f"第{idx}/{total}题答案：{label}")
        results.append({'Id': qid, 'label': label})

# 写入结果文件
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Id', 'label'])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"结果已保存到 {output_file}") 