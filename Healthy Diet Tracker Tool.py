import json
from datetime import datetime

DATA_FILE = "diet_tracker.json"

# 预设一些常见食物的热量（每100克）
FOOD_CALORIES = {
    "apple": 52,
    "banana": 89,
    "chicken breast": 165,
    "rice": 130,
    "egg": 155,
    "broccoli": 55,
    "carrot": 41,
    "salmon": 208,
}

def load_diet():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_diet(diet):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(diet, file, indent=4)

def add_food(diet, food, quantity):
    food = food.lower()
    if food in FOOD_CALORIES:
        calories = FOOD_CALORIES[food] * quantity / 100
        diet.append({
            "food": food,
            "quantity": quantity,
            "calories": calories,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"{quantity} 克 {food} 添加成功，摄入热量：{calories:.2f} 大卡")
    else:
        print(f"{food} 不在已知食物列表中。")

def view_diet(diet):
    if diet:
        print("\n饮食记录：")
        for entry in diet:
            print(f"日期：{entry['date']} | 食物：{entry['food']} | 数量：{entry['quantity']} 克 | 热量：{entry['calories']:.2f} 大卡")
    else:
        print("没有饮食记录。")

def view_daily_report(diet):
    today = datetime.now().strftime("%Y-%m-%d")
    daily_diet = [entry for entry in diet if entry["date"].startswith(today)]
    
    if daily_diet:
        total_calories = sum(entry["calories"] for entry in daily_diet)
        print(f"\n今天的饮食报告：")
        print(f"总热量摄入：{total_calories:.2f} 大卡")
    else:
        print("今天没有饮食记录。")

if __name__ == "__main__":
    diet = load_diet()
    print("欢迎使用健康饮食追踪器！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加食物记录")
        print("2. 查看所有饮食记录")
        print("3. 查看今天的饮食报告")
        print("4. 退出")

        choice = input("请输入选项（1/2/3/4）：")

        if choice == "1":
            food = input("请输入食物名称：")
            try:
                quantity = float(input("请输入食物的摄入量（克）："))
                add_food(diet, food, quantity)
                save_diet(diet)
            except ValueError:
                print("请输入有效的数量。")
        elif choice == "2":
            view_diet(diet)
        elif choice == "3":
            view_daily_report(diet)
        elif choice == "4":
            print("感谢使用健康饮食追踪器，再见！")
            break
        else:
            print("无效选项，请重新选择。")
