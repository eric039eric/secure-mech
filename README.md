# 🔒 Secure-MECH 控制模擬器

這是一個結合 **AES 加密通訊、遠端控制指令解析**、與模擬機械平台互動的 Python 專案，目標是實作一個終端機聊天介面的控制系統，可透過安全通訊來控制機械裝置（如旋轉平台）。

---

## 📁 專案結構

```
secure-mech/
├── client/                     # 使用者端程式
│   └── chat_client.py          # 發送加密指令
├── server/                     # 伺服器端程式
│   ├── chat_server.py          # 接收解密後訊息並執行動作
│   ├── control_logic.py        # 對應控制邏輯
│   └── command_mapping.json    # 指令對應資料表
├── crypto/                     # 加密模組
│   └── crypto_helper.py        # AES CBC 模式加解密工具
├── docs/                       # 文件與說明
│   └── secure-mech_summary.md  # 專案總結記錄
├── .gitignore                  # 忽略檔案設定
└── README.md                   # 你正在看的這個說明檔
```

---

## ⚙️ 功能說明

- ✅ AES 加密雙向通訊（使用者端 ↔ 伺服器）
- ✅ 模擬機構控制動作（如旋轉、停止、逆轉等）
- ✅ 指令錯誤處理與提示
- ✅ 可拓展控制指令（使用 `command_mapping.json` 設定）
- ✅ 與 Termux 和 GitHub 整合，支援跨裝置部署

---

## 🚀 執行方式

### ✅ 安裝必要套件

```bash
pip install pycryptodome
```

### ✅ 啟動伺服器端（電腦端）

```bash
cd server
python chat_server.py
```

### ✅ 啟動用戶端（可在 Termux 執行）

```bash
cd client
python chat_client.py
```

---

## 🧪 測試指令範例

| 指令              | 效果                           |
|-------------------|--------------------------------|
| `start_rotation`  | 開始旋轉（順時針 30 rpm）      |
| `stop_rotation`   | 停止旋轉                       |
| `reverse_rotation`| 反轉方向（逆時針 30 rpm）      |
| `exit`            | 離開聊天室                     |
| 其他指令          | 回傳 `未知指令`                |

---

## 🔮 未來拓展建議

- 整合 Webots 或 Arduino 進行實體或視覺模擬
- 加入登入驗證、訊息簽章、金鑰交換等安全層
- 建立 GUI 或 Web 前端介面

---

##  Youtube 影片

-[![觀看作品展示:初步階段](https://youtu.be/X-v8Dgv6xu8?si=GNeCzECrX_zgcUre)

## 👨‍💻 作者資訊

- 📛 作者：士弘 @eric039eric
- 📆 建立時間：2025-06-12
- 🧠 協助構思：ChatGPT-4o
- 🔗 專案網址：[GitHub Repository](https://github.com/eric039eric/secure-mech)

---

> 本專案由一位機械設計背景的大學生，融合電腦通訊、安全加密與遠端模擬控制製作而成。
