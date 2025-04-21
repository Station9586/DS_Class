# 學生課程、成績管理系統 (Student Course and Grade Management System)

## 專案簡介

這是一個使用 Python 實現的命令列介面（CLI）學生課程與成績管理系統。系統允許使用者新增學生、為學生加選課程、登錄成績，並提供多種查詢功能，例如查詢學生成績、及格科目、推薦選課順序、熱門課程等。

## 主要功能

系統提供以下功能選項：

1.  **新增學生 (Add student):** 加入新的學生資料（姓名、學號）。
2.  **學生加選課程 (Add course to student):** 為指定學生加入課程，會檢查先修課程要求。
3.  **登錄學生成績 (Add score to student):** 為指定學生的特定課程登錄分數（0-100），會檢查學生是否已選該課程且尚未有成績。
4.  **顯示學生所選課程 (Show student course):** 列出指定學生已選修的所有課程。
5.  **顯示學生成績 (Show student grade):** 列出指定學生的所有課程及其成績。
6.  **查詢學生及格科目 (Is pass student?):** 列出指定學生所有成績及格（>=60）的科目。
7.  **獲取推薦選課順序 (Get recommended order of Choosing courses):** 根據課程的先修關係，使用拓撲排序（Topological Sort）產生建議的修課順序。
8.  **查詢課程及格學生 (Get pass student of the course):** 列出指定課程中所有成績及格的學生。
9.  **查詢最熱門的 K 門課程 (Get k popular courses):** 列出選修人數最多的前 K 門課程。
10. **顯示課程先修科目 (Show prerequisite of course):** 顯示指定課程的先修課程要求。
11. **顯示選修該課程的學生 (Show Student who Choose this course):** 列出所有選修了指定課程的學生。
12. **顯示所有學生與學號 (Show all students and id):** 列出系統中所有學生的姓名與學號。
-1. **退出系統 (Exit):** 結束程式。

## 使用的資料結構

本專案為了高效地實現各項功能，運用了多種資料結構：

* **學生資料存儲:** 使用 Python List 存儲 `Student` 物件，並搭配 Dictionary (`idx`) 快速透過姓名或學號查找學生在 List 中的索引。
* **學生已選課程:** 每個 `Student` 物件內部使用 **雙向鏈結串列 (Doubly Linked List)** 存儲該學生選修的課程名稱。
* **學生成績:** 每個 `Student` 物件內部使用 **AVL 樹 (AVL Tree)** 存儲課程名稱與對應的分數，確保成績查詢與插入的效率，並能按課程名稱排序輸出。
* **課程選修學生:** 每個 `Course` 物件內部使用 **佇列 (Queue)** 記錄選修該課程的學生順序。
* **課程熱門度:** 使用 **最大堆積 (Max Heap)** (`popularity`) 存儲課程的選修人數，方便快速查詢最熱門的 K 門課程。
* **查詢課程及格學生:** 使用 **Treap** (`subject_score`) 存儲某課程所有學生的成績，利用其分割（Split）操作快速找出成績 >= 60 的學生。
* **推薦選課順序:** 使用 **拓撲排序 (Topological Sort)** 演算法，內部透過圖（Graph，可能使用相鄰串列表示）和佇列（Queue）來處理課程間的先修依賴關係。

## 設定與使用

### 相依套件

* 標準 Python 函式庫。
* 可能需要 `pandas` 函式庫來讀取 `course.csv`（用於初始化課程資料）。如果需要，請先安裝：
    ```bash
    pip install pandas
    ```

### 輸入資料

* 程式預期在同目錄下有一個 `course.csv` 檔案，包含課程資訊，至少應有 `Subject`, `Prerequisite`, `Recommended_Grade` 這幾個欄位，用於初始化系統中的課程與先修關係。

### 執行程式

在終端機中，切換到專案目錄下，執行以下指令：

```bash
python final.py
```

程式啟動後，會顯示主選單，依照提示輸入數字選擇功能即可。
