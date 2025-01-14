# MH Crafting Planner Backend

モンハンの調合をモチーフにした工業化された調合計画の作成アプリ


## 調合リスト

| Input1 |  Input2 | Output | Yield |
|:------:|:-------:|:------:|:-----:|
| 薬草 | アオキノコ | 回復薬 | 90  |
| 回復薬 | ハチミツ | 回復薬G | 95  |
| 不死虫 | アオキノコ | 栄養剤 | 90  |
| 不死虫 | ハチミツ | 栄養剤G | 75  |
| 栄養剤G | マンドラゴラ | 秘薬 | 65  |
| にが虫 | ハチミツ | 増強剤 | 75  |
| 増強剤 | マンドラゴラ | 活力剤 | 75  |
| 活力剤 | ケルビの角 | 古の秘薬 | 55  |
| アオキノコ | げどく草 | 解毒薬 | 95  |


## 原料リスト
※上記表を元に作成して下さい。
| ItemCode |  ItemName | Leadtime(h) |
|:------:|:-------:|:------:|
| 1 | 薬草 | 48  |
| 2 | アオキノコ | 48  |
| 3 | 回復薬 | 72  |
| 4 | ハチミツ | 54  |
| 5 | 不死虫 | 108  |
| 6 | げどく草 | 48  |
| 7 | 栄養剤 | 72  |
| 8 | 栄養剤G | 128  |
| 9 | マンドラゴラ | 108  |
| 10 | にが虫 | 72  |
| 11 | 増強剤 | 108  |
| 12 | 活力剤 | 9999   |
| 13 | ケルビの角 | 72  |
| 14 | 解毒薬 | 54  |
| 15 | 秘薬  | 9999  |
| 16 | 古の秘薬 | 9999 |


## ミキサーリスト

| ミキサー |  最大容量(kg) | 生産速度(kg/h) |  段替え(h)  |
|:------:|:-------:|:------:|:------:|
| A | 1000 | 100 |  2  |
| B | 1000 | 120 |  2  |
| C | 3000 | 200 |  1  |
| D | 5000 | 180 |  3  |


## 原料調達計画

| 調達日 |   時刻    |  ItemCode  | Weight(kg)  | 原料調達先  |
|:------:|:-------:|:------:|:------:|:------:|
| 2025-01-01 | 08:00 |  薬草  | 1000 | 仕入先A |
| 2025-01-01 | 10:00 |  アオキノコ  | 500 | 仕入先A |
| 2025-01-01 | 12:00 |  回復薬  | 500 | 仕入先A |
| 2025-01-01 | 14:00 |  ハチミツ  | 500 | 仕入先A |
| 2025-01-01 | 16:00 |  不死虫  | 500 | 仕入先A |
| 2025-01-02 | 08:00 |  げどく草  | 500 | 仕入先A |
| 2025-01-02 | 10:00 |  栄養剤  | 500 | 仕入先A |
| 2025-01-02 | 12:00 |  栄養剤G  | 500 | 仕入先A |
| 2025-01-02 | 14:00 |  マンドラゴラ  | 500 | 仕入先A |
| 2025-01-02 | 16:00 |  にが虫  | 500 | 仕入先A |
| 2025-01-03 | 08:00 |  増強剤  | 500 | 仕入先A |
| 2025-01-03 | 10:00 |  活力剤  | 500 | 仕入先A |
| 2025-01-03 | 12:00 |  ケルビの角  | 500 | 仕入先A |
| 2025-01-03 | 14:00 |  解毒薬  | 500 | 仕入先



## 出荷計画

| 出荷日 |   時刻    |  ItemCode  | Weight(kg)  | 出荷先  |
|:------:|:-------:|:------:|:------:|:------:|
| 2025-02-01 | 10:00 |  回復薬  | 500 | 顧客A |
| 2025-02-01 | 12:00 |  回復薬G  | 500 | 顧客A |
| 2025-02-01 | 14:00 |  栄養剤  | 500 | 顧客A |
| 2025-02-01 | 16:00 |  栄養剤G  | 500 | 顧客A |
| 2025-02-02 | 08:00 |  秘薬  | 500 | 顧客A |
| 2025-02-02 | 10:00 |  増強剤  | 500 | 顧客A |
| 2025-02-02 | 12:00 |  活力剤  | 500 | 顧客A |
| 2025-02-02 | 14:00 |  古の秘薬  | 500 | 顧客A |
| 2025-02-02 | 16:00 |  解毒薬  | 500 | 顧客A |
| 2025-02-03 | 08:00 |  回復薬  | 500 | 顧客A |
| 2025-02-03 | 10:00 |  回復薬G  | 500 | 顧客A |
| 2025-02-03 | 12:00 |  栄養剤  | 500 | 顧客A |
| 2025-02-03 | 14:00 |  栄養剤G  | 500 | 顧客A |