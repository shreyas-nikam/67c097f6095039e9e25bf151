# Technical Specifications for Historical Scenario Stress Test Visualizer

## Overview

This specification outlines the requirements and functionalities for a **single-page** Streamlit application named **Historical Scenario Stress Test Visualizer**. The primary purpose of this application is to visually demonstrate the potential impacts of significant historical market events on a user-defined financial portfolio.

## Functional Requirements

### Core Features

- **Historical Event Selection**:
  - Users can choose from a predefined list of historical market events (e.g., 1987 crash, Asian crisis) by selecting from a dropdown menu. This references the concept of "Historical scenarios" as outlined on page 2 of the provided document, where historical crises are characterized and quantified.

- **Portfolio Input**:
  - An interactive form is provided for users to input their portfolio allocations. This includes specifying asset classes and respective weight percentages. 

- **Portfolio Value Visualization**:
  - Dynamic visualizations including line charts, bar graphs, and scatter plots to represent the trend of portfolio value over the chosen event duration. These are interactive and update in real-time based on user input.

- **Visual Enhancements**:
  - **Annotations & Tooltips**: Charts include detailed annotations and tooltips. This allows users to gain insights directly on the visualizations, aiding in their understanding of portfolio reactions to past market events.

- **Summary Statistics**:
  - Computation and display of key portfolio performance metrics during the historical event, such as:
    - Maximum drawdown
    - Portfolio volatility
  - These statistics are dynamically calculated based on the portfolio inputs provided by the user.

### User Interaction

- **Input Forms and Widgets**:
  - The application incorporates Streamlit widgets that enable users to experiment with various portfolio compositions. Users can adjust parameters and immediately observe the impact on the portfolio's historical performance.

- **Real-time Updates**:
  - Any changes in the input parameters instantly reflect in the visualizations and statistics, facilitating a smooth exploratory data analysis experience.

- **Inline Help and Documentation**:
  - Integrated within the application are inline help texts and tooltips. These guide users through the process of interacting with the app, making it more accessible, especially for those new to data visualization concepts.

## Data Handling

### Dataset Details

- **Type**: Synthetic
- **Source**: A synthetic dataset is used to mimic real-world financial data, ensuring the preservation of data privacy while providing realistic data patterns.
- **Attributes**:
  - Contains numerical values, categorical variables, and simulated time-series data representing various market conditions and asset classes.

- **Purpose**: The synthetic dataset serves as a controlled environment for demonstrating data handling and visualization techniques, allowing users to interpret potential real-world scenarios comprehensively.

## Visualization Details

### Interactive Charts

- The application makes extensive use of dynamic visualizations:
  - **Line Charts**: Track portfolio value fluctuations over time.
  - **Bar Graphs**: Compare portfolio performance metrics across different historical events.
  - **Scatter Plots**: Illustrate correlations between asset classes and other financial indicators.

### Annotations & Tooltips

- The added annotations and tooltips enhance user understanding by providing direct, context-sensitive explanations within the visualizations, linking the static data to quantifiable insights.

## Learning Outcomes

### Learning Objectives Supported

- **Data Transformation**: Users gain practical experience in converting raw portfolio data into meaningful and interactive visualizations using Streamlit.
  
- **Data Preprocessing and Exploration**: Users learn about data preprocessing stages and explore historical market data through engaging visual tools.

- **Application Development**: The project supports learners in developing an intuitive, user-friendly application that explains underlying data concepts related to historical financial crises and their impact on personal investments.

The application effectively utilizes the described synthetic dataset and visualization details to provide a hands-on learning experience, augmenting the theoretical insight available in the source document with practical, interactive exploration.