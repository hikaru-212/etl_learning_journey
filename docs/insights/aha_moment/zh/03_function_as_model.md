# 從單一函式到整個系統：一種分形式的哲學
> [切換至英文版 / Switch to English Version](../en/03_function_as_model.md)


## 火花：兩種「Function」的故事（「函式」vs. 「函數」）
*(2025-09-23)*

我曾在網路上看到一個有趣的討論：
*function* 到底該翻譯成 **「函式」** 還是 **「函數」**？

-   **函數 (hánshù)** 帶有數學意涵：一個純粹的映射 *Domain → f →
    Codomain*。
-   **函式 (hánshì)** 更像是程式中的功能模組或程式區塊。

這個細微的差異觸發了我的思考：
我的 **Input - Bridge - Output** 框架，究竟比較像程式中的一個小函式，
還是更接近整個腳本本身？

------------------------------------------------------------------------

### 理解的轉變

我意識到：**整個腳本本身就是一個函數**。
它也完全符合數學結構：

-   **輸入**：資源、資料、條件
-   **橋接**：腳本的處理邏輯
-   **輸出**：結果、交付物

更重要的是，這種模式是 **遞迴巢狀的** ------ 就像俄羅斯娃娃一樣：

-   **一個專案** 本身是一個巨大的函數：
    *Input (人力/時間) → Bridge (開發過程) → Output (成果)*
-   **一個系統** 也是函數：
    *Input (原始資料) → Bridge (ETL流程) → Output (乾淨資料)*
-   **模組 / 腳本 / 函式** 也都遵循同樣的模式，一層層向下。

``` mermaid
graph TD
    %% 定義樣式
    style BridgeNode fill:#E0E7FF,stroke:#364F99,stroke-width:2px
    style CoreNode fill:#FFF2CC,stroke:#CC9900,stroke-width:1.5px
    style EnablerNode fill:#E6F7FF,stroke:#1E90FF,stroke-width:1.5px

    %% 專案層級
    subgraph Project["專案層級"]
        P_Input[輸入: 資源] --> P_Bridge(橋接: 開發過程<br><b>包含 Core + Enablers</b>) --> P_Output[輸出: 服務]
    end

    %% 系統層級
    subgraph System["系統層級"]
        S_Input[輸入: 原始資料] --> S_Bridge(橋接: ETL流程<br><b>包含 Core + Enablers</b>) --> S_Output[輸出: 乾淨資料]
    end
    
    %% 模組層級
    subgraph Module["模組層級"]
        M_Input[輸入: DataFrame] --> M_Bridge(橋接: 轉換邏輯<br><b>包含 Core + Enablers</b>) --> M_Output[輸出: 整理後的表格]
    end

    %% Core + Enablers 細節 (收斂)
    subgraph Detail["橋接內部結構 (遞迴)"]
        direction LR
        Core["Core (I → B → O)"]:::CoreNode
        Enabler1["Enabler 1 (I → B → O)"]:::EnablerNode
        Enabler2["Enabler 2 (I → B → O)"]:::EnablerNode
    end

    %% 層級鏈接 (虛線表示「包含 / 展開」)
    P_Bridge -. "包含" .-> System
    S_Bridge -. "包含" .-> Module
    M_Bridge -. "展開" .-> Detail
```

------------------------------------------------------------------------

## 統一洞見：Core × Enablers 也是函數

在每一層，**Bridge** 都可以進一步拆解為 **Core** 與 **Enablers**：

-   **Core** = 直接創造價值的處理邏輯
-   **Enablers** = 守護者，確保 Core 能可靠運行（驗證、紀錄、監控...）

更深的洞見是：**Enablers 自身也遵循 Input - Bridge - Output**。
例如：

-   **Pandera 驗證**：
    *Input (dataframe) → Bridge (驗證規則) → Output (通過 / 拒絕)*
-   **單元測試**：
    *Input (測試資料) → Bridge (測試邏輯) → Output (通過 / 失敗)*

因此，Core 與 Enabler
都不是例外------它們都只是這個普遍模型中的不同角色。

``` mermaid
graph LR
    %% 定義樣式
    style Input fill:#FFD2D2,stroke:#B00,stroke-width:2px
    style Output fill:#D2FFD2,stroke:#0B0,stroke-width:2px
    style Bridge fill:#E0E7FF,stroke:#364F99,stroke-width:2px

    Input --> Bridge --> Output

    subgraph Bridge["Bridge (例如 ETL 系統)"]
        direction TB
        
        Core("Core: 轉換邏輯 <br> (I → B → O)")
        Enabler1("Enabler: 驗證 <br> (I → B → O)")
        Enabler2("Enabler: 編排 <br> (I → B → O)")
    end
```

------------------------------------------------------------------------

## 實際效益

這個洞見幫助我建立了一套統一的設計哲學：
**Function 作為思維模型**。

它帶來三個實際好處：

1.  **任何層級的清晰性**
    我可以自由縮放------從一行程式碼到整個專案架構------
    並且始終用 Input - Bridge - Output 作為描述語言。

2.  **可預測的設計**
    在設計新功能時，我會先定義 I/O (Core)，
    再考慮需要哪些 Enablers（測試、驗證、監控）。
    這使設計過程更有紀律與可重複性。

3.  **高效的除錯**
    當系統出錯時，我能快速定位問題：
    發生在 Input、Output，還是 Bridge？
    如果是 Bridge，那是 Core 邏輯出錯，還是某個 Enabler 出錯？

------------------------------------------------------------------------

## ✅ 一句話總結

這個探索始於一個語言上的細微差異------「函式」作為程式區塊
vs. 「函數」作為數學映射。
它最後帶來的深刻洞見是：函數不僅僅是語法單位，而是一種
**可遞迴應用的思維模型**。

-   **Input - Bridge - Output** 是骨架。
-   **Core vs Enablers** 是血肉。

兩者結合，構成了我統一的設計方法論。

``` mermaid
graph LR
    %% 主框架
    subgraph System [Input–Bridge–Output 框架]
        direction LR
        X["Domain (X)"] --> F["f"] --> Y["Codomain (Y)"]
        Input([輸入]) --> Bridge --> Output([輸出])
    end

    %% Bridge 內部結構
    subgraph Bridge [Bridge 內部結構]
        direction TB
        Core["Core: 轉換 - 改變意義"]

        subgraph Enablers [Enablers - 確保正確性]
            direction LR
            Validation[驗證]
            Orchestration[排程]
            Testing[測試]
        end

        Validation --> Core
        Orchestration --> Core 
        Testing --> Core
    end

    %% 樣式
    style Input fill:#FFD2D2,stroke:#B00,stroke-width:2px
    style Output fill:#D2FFD2,stroke:#0B0,stroke-width:2px
    style Core fill:#FFF2CC,stroke:#CC9900,stroke-width:2px
```
