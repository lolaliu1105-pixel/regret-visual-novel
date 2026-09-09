# regret-visual-novel# regret-visual-novel
# Regret - 互動式視覺小說遊戲

這是一個使用 **Python** 與 **Ren'Py 引擎** 開發的文字冒險與視覺小說遊戲，透過雨夜中的神祕郵局為背景，探討記憶、遺憾與自我和解。

## 🎮 專案特色 (Features)
- **多重選項與結局分歧：** 玩家在遊戲中的每個抉擇（如是否遞上熱茶、如何面對過去的信件）會影響好感度數值與後續走向，總計包含三種不同結局。
- **物件導向設計 (OOP)：** 在程式碼中實作 `Visitor` 與 `StoryManager` 類別，將玩家互動狀態、資料與劇情流程邏輯模組化，避免全域變數汙染。
- **邊界防護與防呆機制：** 針對好感度數值加入範圍限制（Boundary Control），確保數值在多重條件判斷時不會異常溢位。

## 🛠️ 技術與工具 (Tech Stack)
- **程式語言：** Python
- **遊戲引擎：** Ren'Py SDK
- **版本控制：** Git / GitHub

## 📂 專案結構 (Project Structure)
- `script.rpy`：核心遊戲劇情腳本、選項分歧與物件類別定義。
- `images/`：角色立繪、背景圖與道具素材。
- `audio/`：背景音樂與情境音效。

## ▶️ 如何遊玩 (How to Play)
1. 下載並安裝 [Ren'Py 視覺小說引擎](https://www.renpy.org/)。
2. 將此專案複製或下載並解壓縮至 Ren'Py 的專案資料夾中（`renpy/projects/`）。
3. 打開 Ren'Py 啟動器，重新整理後點擊 `Regret` 即可開始遊玩。