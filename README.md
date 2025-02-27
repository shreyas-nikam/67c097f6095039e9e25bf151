```
# QuLab: Historical Scenario Stress Test Visualizer

## Description

The **QuLab: Historical Scenario Stress Test Visualizer** is a Streamlit application designed to illustrate the potential impact of historical market events on investment portfolios. By simulating portfolio performance during significant crises such as the 1987 Crash, the 2008 Financial Crisis, and the COVID-19 Pandemic, this tool provides an educational platform for understanding portfolio behavior under stress.

**Key Features:**

*   **Historical Scenario Analysis:** Explore pre-defined historical market events and their impact on asset classes.
*   **Interactive Portfolio Allocation:**  Define your portfolio's asset allocation using intuitive sliders and observe real-time changes in portfolio performance visualizations and key metrics.
*   **Visualizations:**  Interactive charts display portfolio value trends over time and asset class contributions during selected events, enhancing understanding through visual representation.
*   **Summary Statistics:**  Key performance indicators such as Maximum Drawdown and Annualized Volatility are calculated and displayed to quantify portfolio risk and potential losses during stress scenarios.
*   **Educational Tool:**  Utilizes synthetic data to mimic real-world market behavior, focusing on demonstrating stress testing concepts for educational purposes in risk management and financial analysis.

**Disclaimer:**  The data used in this application is synthetic and for illustrative purposes only. It is not intended for investment advice or real-world financial analysis. This application is designed solely for educational purposes to demonstrate the principles of historical scenario stress testing.

## Installation

To run this Streamlit application, you need to have Python installed on your system, along with the required Python packages. Follow these steps to set up your environment:

1.  **Python Installation:** Ensure you have Python 3.8 or later installed. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **pip Installation:** Python usually comes with `pip`, the package installer for Python. If you don't have it, follow the instructions here: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

3.  **Install Required Libraries:** Open your terminal or command prompt and install the necessary Python libraries by running the following command:

    ```bash
    pip install streamlit pandas numpy plotly
    ```
    This command will install:
    *   `streamlit`: For creating the interactive web application.
    *   `pandas`: For data manipulation and analysis.
    *   `numpy`: For numerical computations.
    *   `plotly`: For creating interactive plots and visualizations.

## Usage

Once you have installed the necessary libraries, you can run the Streamlit application.

1.  **Save the Python Script:** Save the provided Python code (the code you included in your prompt) as a Python file, for example, `stress_test_app.py`.

2.  **Navigate to the Directory:** Open your terminal or command prompt and navigate to the directory where you saved the `stress_test_app.py` file using the `cd` command (change directory). For example, if you saved the file in your "Documents" folder, you might use:

    ```bash
    cd Documents
    ```

3.  **Run the Streamlit Application:**  Execute the following command in your terminal to start the Streamlit application:

    ```bash
    streamlit run stress_test_app.py
    ```

    Streamlit will launch the application in your default web browser.

4.  **Using the Application Interface:**
    *   **Sidebar Controls:** On the left sidebar, you will find the application controls:
        *   **Select Historical Event:** Use the dropdown menu labeled "Select Historical Event" to choose a historical market event you want to analyze (e.g., "2008 Financial Crisis").
        *   **Portfolio Allocation:**  In the "Portfolio Allocation" section, use the sliders to adjust the percentage allocation for each asset class in your portfolio (Stocks, Bonds, Gold, and potentially other assets depending on the selected event). The sliders range from 0% to 100%.

    *   **Main Panel - Visualizations and Statistics:** The main panel of the application displays:
        *   **Portfolio Performance During: [Selected Event]:**  The title indicates the currently selected historical event.
        *   **Portfolio Value Over Time:** An interactive line chart showing how your portfolio value changes over time, starting from an initial value of 100. The chart highlights the period of the selected historical event in red.
        *   **Asset Class Performance Contribution during Event:** A bar chart illustrating the contribution of each asset class to the overall portfolio return during the selected historical event.
        *   **Portfolio Summary Statistics:** Key metrics summarizing portfolio performance during the event, including:
            *   **Maximum Drawdown:** The largest percentage decline in portfolio value during the event period.
            *   **Annualized Volatility (during event):** The annualized standard deviation of portfolio returns during the event period, indicating the level of risk.

    *   **Experiment and Learn:**  Change the selected historical event and adjust the portfolio allocations using the sidebar controls to observe how these changes impact the visualizations and summary statistics in real-time. This interactive exploration will help you understand the potential effects of different market stresses on portfolio performance.

## Credits

Developed by: **QuantUniversity**

© 2025 QuantUniversity. All Rights Reserved.

This application was created for educational purposes as part of the QuCreate Streamlit Lab initiative at QuantUniversity.

For more information about QuantUniversity and our educational programs, please visit: [https://www.quantuniversity.com](https://www.quantuniversity.com)

## License

**Copyright © 2025 QuantUniversity. All Rights Reserved.**

This Streamlit application, including the code, design, and content, is proprietary and protected by copyright law. It is provided for educational and demonstration purposes only.

**Permitted Use:**

*   This application is intended for personal, non-commercial, educational use.
*   You may run and interact with the application as described in the "Usage" section for educational exploration and learning.

**Prohibited Use:**

*   Reproduction, distribution, modification, or commercial use of this application, or any part thereof, is strictly prohibited without prior written consent from QuantUniversity.
*   You may not use this application for investment advice, financial analysis, or any commercial or professional purposes without explicit authorization from QuantUniversity.

For inquiries regarding licensing, commercial use, or further information, please contact QuantUniversity through their website: [https://www.quantuniversity.com](https://www.quantuniversity.com)

For full legal documentation, please refer to the terms of service and copyright policy available on the QuantUniversity website.

---
```