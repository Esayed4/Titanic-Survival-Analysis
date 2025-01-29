# Titanic Survival Analysis 🚢

![Titanic](https://img.shields.io/badge/Project-Titanic_Survival_Analysis-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![SQL Server](https://img.shields.io/badge/SQL_Server-2019%2B-orange)  
![Power BI](https://img.shields.io/badge/Power_BI-Desktop-yellow)  

This project analyzes the Titanic dataset to uncover insights into survival rates based on passenger class and age. The goal is to improve ship designs by ensuring equal access to emergency exits and equipment for all passengers. The project provides **two approaches** to achieve the results:  

1. **Python, Pandas, and Power BI**: A streamlined approach using Python for data manipulation and Power BI for visualization.  
2. **Python, Pandas, Microsoft SQL Server, and Power BI**: A more robust approach that includes SQL Server for data storage and transformation.  

---

## Table of Contents 📚
- [Objective](#objective)  
- [Approaches](#approaches)  
- [Technologies Used](#technologies-used)  
- [Data Sources](#data-sources)  
- [Setup Instructions](#setup-instructions)  
- [Data Manipulation](#data-manipulation)  
- [Visualization](#visualization)  
- [Contributions](#contributions)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)  

---

## Objective 🎯
<a id="objective"></a>
- Analyze the relationship between passenger class, age, and survival rates.  
- Build a comprehensive dataset for analysis and visualization.  
- Create an interactive Power BI dashboard to present findings.  

---

## Approaches 🛤️
<a id="approaches"></a>
This project provides **two ways** to achieve the results:  

### 1. **Python, Pandas, and Power BI**  
- **Python** and **Pandas** are used for data cleaning, manipulation, and analysis.  
- The cleaned data is directly loaded into **Power BI** for visualization.  
- Ideal for quick analysis without the need for a database.  

### 2. **Python, Pandas, Microsoft SQL Server, and Power BI**  
- **Python** and **Pandas** are used for initial data preparation.  
- Data is stored and transformed in **Microsoft SQL Server**.  
- **Power BI** connects to SQL Server for visualization.  
- Ideal for larger datasets or when data transformation requires SQL.  

---

## Technologies Used 💻
<a id="technologies-used"></a>
- **Python** (with Pandas for data manipulation)  
- **Microsoft SQL Server** (for data storage and transformation in the second approach)  
- **Power BI** (for data visualization and dashboard creation)  
- **gdown** (for downloading datasets from Google Drive)  

---

## Data Sources 📂
<a id="data-sources"></a>
The dataset is sourced from the [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic). It includes:  
- Passenger class  
- Age  
- Gender  
- Ticket fare  
- Survival status  

---

## Setup Instructions 🛠️
<a id="setup-instructions"></a>

### For **Python, Pandas, and Power BI** Approach:
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/titanic-survival-analysis.git
   cd titanic-survival-analysis
   ```
2. Install Python Libraries:
   ```bash
   pip install pandas gdown
   ```
3. Run the Python Script:
   - Execute `titanic_project.py` to download and prepare the data.  
4. Open Power BI:
   - Load the cleaned dataset (`titanic_cleaned.csv`) into Power BI for visualization.  

### For **Python, Pandas, SQL Server, and Power BI** Approach:
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/titanic-survival-analysis.git
   cd titanic-survival-analysis
   ```
2. Install Python Libraries:
   ```bash
   pip install pandas pypyodbc gdown
   ```
3. Set Up SQL Server:
   - Install and configure **Microsoft SQL Server**.  
   - Create a database named `Titanic`.  
   - Create the required tables: `Train`, `Test`, `Gender_submission`, and `Final`.  
4. Run Python Scripts:
   - Execute `titanic_project.py` to download and prepare the data.  
   - Execute `titanic_project_with_sql_server2.py` to insert data into SQL Server.  
5. Execute SQL Script:
   - Run `Transformation.sql` in SQL Server Management Studio to clean and transform the data.  
6. Power BI Setup:
   - Open Power BI and connect to the SQL Server database.  
   - Load the `Final` table to create visualizations.  

---

## Data Manipulation 🔧
<a id="data-manipulation"></a>
The data is cleaned and transformed using:  
- **Python and Pandas**: For initial cleaning and preparation.  
- **SQL Server**: For advanced transformations, including handling null values, creating views, and converting categorical data to numeric formats.  

---

## Visualization 📊
<a id="visualization"></a>
The **Power BI dashboard** includes:  
- Total passengers and survivors.  
- Filters for age and class.  
- Visualizations of survival rates and classifications.  

---

## Contributions 🤝
<a id="contributions"></a>
Contributions are welcome! If you'd like to contribute:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/YourFeatureName`).  
3. Commit your changes (`git commit -m 'Add some feature'`).  
4. Push to the branch (`git push origin feature/YourFeatureName`).  
5. Open a pull request.  

---

## License 📜
<a id="license"></a>
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## Acknowledgments 🙏
<a id="acknowledgments"></a>
- Inspired by the Titanic tragedy and its impact on maritime safety.  
- Dataset sourced from the [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic).  

---

Feel free to reach out if you have any questions or suggestions! 🚀  
