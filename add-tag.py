import json
import os

DATA_FILE = 'static/data/tags.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_entry(data, name, tag):
    for group in data:
        if group['tag'] == tag:
            if name not in group['names']:
                group['names'].append(name)
                print(f'  已把 {name} 加入标签 {tag}')
            else:
                print(f'  {name} 已在标签 {tag} 里，跳过')
            return
    data.append({'tag': tag, 'names': [name]})
    print(f'  新建标签 {tag}，加入 {name}')

def main():
    data = load_data()
    print('输入角色名和标签，格式：角色名 标签1 标签2 ...')
    print('直接按回车结束。')

    while True:
        line = input('> ').strip()
        if not line:
            break

        parts = line.split()
        if len(parts) < 2:
            print('  至少要有角色名和一个标签')
            continue

        name = parts[0]
        tags = parts[1:]
        for tag in tags:
            add_entry(data, name, tag)

    save_data(data)
    print(f'已保存到 {DATA_FILE}')

if __name__ == '__main__':
    main()