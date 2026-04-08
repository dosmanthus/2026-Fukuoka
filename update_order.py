import sys

file_path = "/Users/dd/Documents/DD/2026 福岡/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

dinner_block = """          {
            time: "17:00",
            title: "晚餐備案：天麩羅處 Hirao / 漢堡排 牛丸 / 強棒拉麵",
            desc: "人多就附近店家自由選擇，【必吃清單】福岡靈魂美食！現炸天婦羅一道道上桌，搭配無限供應的招牌「柚子花枝」小菜。翻桌率快。16席",
            icon: "fa-utensils",
            tag: "必吃",
            price: "¥800 - ¥1,200",
            menuLink: "http://www.hirao-foods.net/menu/",
            location: "福岡市中央区大名2-6-20",
            googleMap: "Tempura+Hirao+Daimyo",
            imgType: "food",
            image: "img/Tempura-Hirao27.jpg",
            // image: "img/LINE_ALBUM_福岡必吃_260210_x.jpg", // TBD
            transport: {
              text: "步行前往 (約 6 分)",
              icon: "fa-person-walking",
            },
          },
"""

motsunabe_sig = """          {
            time: "17:00",
            title: "博多牛腸鍋 前田屋 (大名店)","""

if dinner_block in content:
    idx_motsunabe = content.find(motsunabe_sig)
    if idx_motsunabe != -1:
        # Check if dinner_block is before motsunabe
        idx_dinner = content.find(dinner_block)
        if idx_dinner < idx_motsunabe:
            # Remove dinner_block from original place
            content = content.replace(dinner_block, "")
            # Reconstruct content by inserting dinner_block before motsunabe
            idx_motsunabe_new = content.find(motsunabe_sig)
            content = content[:idx_motsunabe_new] + dinner_block + content[idx_motsunabe_new:]
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully reordered")
        else:
            print("Dinner block is not before Motsunabe")
    else:
        print("Motsunabe signature not found")
else:
    print("Dinner block not found")
