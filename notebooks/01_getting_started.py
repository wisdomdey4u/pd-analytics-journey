import marimo

__version__ = "0.1.0"
app = marimo.App()


@app.cell
def __():
    import pandas as pd
    import numpy as np
    print(f"pandas version: {pd.__version__}")
    print(f"numpy version: {np.__version__}")
    return pd, np


@app.cell
def __(md):
    md("""
    # 01. Getting Started with Pandas

    **Module Overview**: In this notebook, we'll explore the fundamentals of pandas - what it is, why it matters, and how to create and inspect basic data structures.

    ## Learning Outcomes
    - Understand what pandas is and why it's essential for data analysis
    - Create Series and DataFrame objects
    - Inspect data structure properties and contents
    - Understand basic data alignment concepts
    """)


@app.cell
def __(md):
    md("""
    ## What is Pandas?

    Pandas is a Python library for data manipulation and analysis. It provides:
    - **Series**: 1D labeled array (like a column in a spreadsheet)
    - **DataFrame**: 2D labeled table (like a spreadsheet)
    - **Tools**: Merging, reshaping, selection, aggregation, and alignment

    ### Core Insight: Labels & Alignment
    Unlike NumPy arrays (which use positional indexing), pandas automatically aligns data by labels.
    This is the superpower that makes pandas intuitive for data analysis.
    """)


@app.cell
def __(md):
    md("## Creating Series")


@app.cell
def __(pd, np):
    # Series from a list
    s1 = pd.Series([1, 2, 3, 4, 5])
    print("Series from list:")
    print(s1)
    print(f"\nType: {type(s1)}")
    print(f"dtype: {s1.dtype}")
    return s1


@app.cell
def __(pd):
    # Series with custom index
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print("Series with custom index:")
    print(s2)
    print(f"\nAccess by label: s2['b'] = {s2['b']}")
    return s2


@app.cell
def __(pd):
    # Series from a dictionary
    s3 = pd.Series({'name': 'Alice', 'age': 25, 'city': 'NYC'})
    print("Series from dictionary:")
    print(s3)
    print(f"\nKeys become index, values become data")
    return s3


@app.cell
def __(md):
    md("## Creating DataFrames")


@app.cell
def __(pd, np):
    # DataFrame from dict of Series
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 75000]
    }
    df1 = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df1)
    print(f"\nShape: {df1.shape}")
    print(f"Columns: {df1.columns.tolist()}")
    print(f"Index: {df1.index.tolist()}")
    return df1


@app.cell
def __(pd):
    # DataFrame with custom index
    df2 = pd.DataFrame(
        {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        },
        index=['row1', 'row2', 'row3']
    )
    print("DataFrame with custom index:")
    print(df2)
    return df2


@app.cell
def __(md):
    md("## Inspecting DataFrames")


@app.cell
def __(df1):
    print("head() - first 5 rows:")
    print(df1.head())
    print("\n" + "="*50)
    print("\ninfo() - structure and dtypes:")
    df1.info()
    print("\n" + "="*50)
    print("\ndescribe() - statistical summary:")
    print(df1.describe())


@app.cell
def __(md):
    md("""
    ## The Alignment Concept (Core Pandas Superpower)

    This is what makes pandas different from NumPy. Let's see it in action:
    """)


@app.cell
def __(pd):
    # Create two Series with the same index but different order
    s_A = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
    s_B = pd.Series([100, 200, 300], index=['z', 'x', 'y'])
    
    print("Series A:")
    print(s_A)
    print("\nSeries B:")
    print(s_B)
    print("\nWhen we add them, pandas aligns by index labels:")
    print(s_A + s_B)
    print("\n💡 Notice: Even though B's order is different, pandas aligned by label!")
    return s_A, s_B


@app.cell
def __(md):
    md("""
    ## Common Pitfall: Position vs. Label

    This is the #1 confusion for pandas beginners. Let's clarify:
    """)


@app.cell
def __(pd):
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print("Series:")
    print(s)
    print("\n--- Accessing by Position (0-based) ---")
    print(f"s.iloc[0] = {s.iloc[0]}")  # First element by position
    print(f"s.iloc[2] = {s.iloc[2]}")  # Third element by position
    print("\n--- Accessing by Label ---")
    print(f"s.loc['a'] = {s.loc['a']}")  # Element with label 'a'
    print(f"s.loc['c'] = {s.loc['c']}")  # Element with label 'c'
    print("\n💡 Rule: iloc = integer location, loc = label-based")


@app.cell
def __(md):
    md("""
    ## Exercise: Create Your Own DataFrame

    Try creating a DataFrame with information about 3 products:
    - product_name
    - price
    - stock_quantity
    - category

    Then:
    1. Check the shape
    2. Display the info
    3. Get basic statistics
    """)


@app.cell
def __(md):
    md("""
    ## Key Takeaways

    ✅ **Series** = 1D labeled array  
    ✅ **DataFrame** = 2D labeled table  
    ✅ **Index** = Labels for rows and columns  
    ✅ **Alignment** = Pandas matches by labels, not position  
    ✅ **iloc** = Position-based access  
    ✅ **loc** = Label-based access  

    ## Resource References

    - 📖 **McKinney, Ch. 5**: "Creating DataFrame and Series Objects"
    - 📄 **10 Minutes to Pandas**: "Object Creation" section
    - 🎯 **Kaggle Lesson 1**: Creating, Reading & Writing

    ## Next Steps

    - [ ] Run this notebook and modify the examples
    - [ ] Create a DataFrame with your own data
    - [ ] Move to Module 02: Data Structures (deeper dive)
    - [ ] Update LEARNING_LOG.md with your insights
    """)


if __name__ == "__main__":
    app.run()
