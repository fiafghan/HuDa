import streamlit as st
import polars as pl
import pandas as pd # Import pandas for type hinting and internal use with plot libs
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union
import io # To handle file uploads as a buffer

# Your original monthly_yearly_growth function definition
# ----------------------------------------------------------------------------------
def monthly_yearly_growth(
    data: Union[str, pd.DataFrame, pl.DataFrame],
    value_column: str = "beneficiaries",
    date_column: str = "date",
    period: str = "monthly"
) -> pl.DataFrame:
    """
    📊 Calculate Growth Rates (Month-over-Month, Year-over-Year)
    ============================================================
    What it does:
    -------------
    - Calculates growth of a numeric column over time
    - Supports monthly (MoM) or yearly (YoY) growth
    - Automatically converts CSV or Pandas DF to Polars DF
    
    Parameters:
    -----------
    data : str | pd.DataFrame | pl.DataFrame
        CSV path, Pandas DataFrame, or Polars DataFrame
    value_column : str
        Numeric column to calculate growth on (e.g., beneficiaries)
    date_column : str
        Column containing dates
    period : str, default="monthly"
        "monthly" → Month-over-Month
        "yearly"  → Year-over-Year

    Returns:
    --------
    pl.DataFrame
        Original data with new column "growth_rate_pct"
    
    Example Usage (Afghan survey):
    -------------------------------
    import polars as pl
    
    df = pl.DataFrame({
        "province": ["Kabul", "Kabul", "Herat", "Herat", "Kandahar", "Kandahar"],
        "date": ["2024-01-01","2024-02-01","2024-01-01","2024-02-01","2024-01-01","2024-02-01"],
        "beneficiaries": [100, 150, 200, 250, 120, 180]
    })
    
    df_growth = monthly_yearly_growth(df, value_column="beneficiaries", date_column="date", period="monthly")
    print(df_growth)

    Output Table:
    -------------
    ┌────────────┬───────────────┬────────┬───────┬────────────────┐
    │ date       ┆ beneficiaries ┆ year   ┆ month ┆ growth_rate_pct│
    ├────────────┼───────────────┼────────┼───────┼────────────────┤
    │ 2024-01-01 ┆ 100           ┆ 2024   ┆ 1     ┆ NaN            │
    │ 2024-02-01 ┆ 150           ┆ 2024   ┆ 2     ┆ 50.0           │
    │ 2024-01-01 ┆ 200           ┆ 2024   ┆ 1     ┆ NaN            │
    │ 2024-02-01 ┆ 250           ┆ 2024   ┆ 2     ┆ 25.0           │
    │ 2024-01-01 ┆ 120           ┆ 2024   ┆ 1     ┆ NaN            │
    │ 2024-02-01 ┆ 180           ┆ 2024   ┆ 2     ┆ 50.0           │
    └────────────┴───────────────┴────────┴───────┴────────────────┘

    When to Use:
    ------------
    - You have time-series survey data (monthly or yearly)
    - Want to see how numbers change over time
    - Track trends for beneficiaries, cases, or aid delivery

    Why It Is Useful:
    -----------------
    - Quickly identifies growth or decline
    - Helps plan interventions in Afghan provinces
    - Makes dashboards and reports clearer

    Where to Use:
    -------------
    - Humanitarian surveys in Afghanistan
    - Provincial health or aid statistics
    - Any dataset with numeric measures over time
    """

    # ---- Step 1: Convert input to Polars DF ----
    # Streamlit passes uploaded file content as bytes, so use io.BytesIO
    if isinstance(data, io.BytesIO): # Handle Streamlit's uploaded file object
        df = pl.read_csv(data)
    elif isinstance(data, str):
        df = pl.read_csv(data)
    elif "pandas" in str(type(data)): # This will match pd.DataFrame
        df = pl.from_pandas(data)
    elif isinstance(data, pl.DataFrame):
        df = data
    else:
        # For debugging, you might want to print type(data)
        # st.error(f"DEBUG: Unexpected data type: {type(data)}")
        raise TypeError("Input must be CSV path, Pandas DF, Polars DF, or Streamlit UploadedFile.")

    # ---- Step 2: Convert date column if needed ----
    # Attempt to infer date format if string and strptime fails
    if date_column not in df.columns:
        st.error(f"Date column '{date_column}' not found in your data.")
        st.stop() # Stop the script execution

    if df.schema[date_column] == pl.Utf8:
        try:
            # Try common YYYY-MM-DD
            df = df.with_columns(
                pl.col(date_column).str.strptime(pl.Date, "%Y-%m-%d", strict=True) # strict=True to fail fast on mismatch
            )
        except Exception:
            try: # Try MM/DD/YYYY
                df = df.with_columns(
                    pl.col(date_column).str.strptime(pl.Date, "%m/%d/%Y", strict=True)
                )
            except Exception:
                st.error(f"Could not parse date column '{date_column}'. Please ensure it's in YYYY-MM-DD or MM/DD/YYYY format. Column type is: {df.schema[date_column]}")
                st.stop()
    elif df.schema[date_column] == pl.Date:
        pass # Already a date
    else:
        st.error(f"Date column '{date_column}' is not in a recognized date or string format. Found: {df.schema[date_column]}")
        st.stop()
    
    # Ensure value column is numeric
    if df.schema[value_column] not in [pl.Int64, pl.Float64]:
        st.error(f"Value column '{value_column}' must be a numeric type. Found: {df.schema[value_column]}")
        st.stop()

    # ---- Step 3: Extract year/month for grouping and sorting ----
    df = df.with_columns([
        pl.col(date_column).dt.year().alias("year"),
        pl.col(date_column).dt.month().alias("month")
    ])
    df = df.sort(date_column)

    # ---- Step 4: Calculate growth rate ----
    if period.lower() == "monthly":
        df = df.with_columns([
            ((pl.col(value_column) - pl.col(value_column).shift(1)) / pl.col(value_column).shift(1) * 100).alias("growth_rate_pct")
        ])
    elif period.lower() == "yearly":
        df = df.with_columns([
            ((pl.col(value_column) - pl.col(value_column).shift(12)) / pl.col(value_column).shift(12) * 100).alias("growth_rate_pct")
        ])
    else:
        st.error("Period must be 'monthly' or 'yearly'.")
        st.stop()

    return df
# ----------------------------------------------------------------------------------


# --- Streamlit UI Code ---
st.set_page_config(layout="wide", page_title="Growth Rate Calculator")

st.title("📊 Growth Rate Calculator")
st.markdown("""
Upload your CSV data to calculate Month-over-Month (MoM) or Year-over-Year (YoY) growth rates.
""")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Streamlit uploaded files are bytes. We need to convert to an IO object
        # for polars to read directly.
        bytes_data = uploaded_file.getvalue()
        df = pl.read_csv(io.BytesIO(bytes_data))
        
        st.write("### Original Data Preview")
        st.dataframe(df.head(5).to_pandas()) # Convert to pandas for Streamlit's display

        all_columns = df.columns
        
        st.sidebar.header("Calculation Settings")
        
        # Selectbox for value column
        value_column = st.sidebar.selectbox(
            "Select Value Column (e.g., beneficiaries):",
            options=all_columns,
            index=all_columns.index("beneficiaries") if "beneficiaries" in all_columns else 0
        )
        
        # Selectbox for date column
        date_column = st.sidebar.selectbox(
            "Select Date Column (e.g., date):",
            options=all_columns,
            index=all_columns.index("date") if "date" in all_columns else 0
        )
        
        # Radio buttons for period type
        period_type = st.sidebar.radio(
            "Select Growth Period:",
            options=["monthly", "yearly"],
            index=0, # Default to monthly
            format_func=lambda x: f"{x.capitalize()} Growth"
        )
        
        # Optional group by column
        group_by_column = st.sidebar.selectbox(
            "Optional: Group growth by (e.g., province) for separate trends:",
            options=["None"] + all_columns,
            index=0
        )
        
        # Button to trigger calculation
        if st.sidebar.button("Calculate Growth Rates"):
            with st.spinner("Calculating growth rates..."):
                try:
                    growth_df = monthly_yearly_growth(
                        data=df, # Pass the Polars DataFrame
                        value_column=value_column,
                        date_column=date_column,
                        period=period_type
                    )

                    st.write(f"### Results: {period_type.capitalize()} Growth Rates")
                    st.dataframe(growth_df.to_pandas()) # Display results

                    # --- Plotting ---
                    st.write("### Growth Rate Trend")
                    
                    # Convert to pandas for plotting with seaborn/matplotlib
                    plot_df = growth_df.to_pandas()
                    # Ensure date column is datetime for plotting
                    plot_df[date_column] = pd.to_datetime(plot_df[date_column])
                    
                    fig, ax = plt.subplots(figsize=(12, 6))
                    
                    group_col_for_plot = group_by_column if group_by_column != "None" else None
                    
                    sns.lineplot(
                        data=plot_df,
                        x=date_column,
                        y="growth_rate_pct",
                        hue=group_col_for_plot,
                        marker='o',
                        ax=ax
                    )
                    ax.set_title(f"{period_type.capitalize()} Growth Rate Over Time" + (f" by {group_col_for_plot.capitalize()}" if group_col_for_plot else ""), fontsize=16)
                    ax.set_xlabel("Date", fontsize=12)
                    ax.set_ylabel("Growth Rate (%)", fontsize=12)
                    ax.grid(True, linestyle='--', alpha=0.7)
                    ax.axhline(0, color='grey', linestyle='--', linewidth=0.8) # Zero line for reference
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    st.pyplot(fig) # Display the plot in Streamlit
                    
                    # Download button for results
                    st.download_button(
                        label="Download Results as CSV",
                        data=growth_df.write_csv(None), # Polars can write to a buffer
                        file_name=f"{period_type}_growth_results.csv",
                        mime="text/csv"
                    )

                except Exception as e:
                    st.error(f"An error occurred during calculation: {e}")
                    # st.exception(e) # Uncomment for detailed traceback in debug
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("Need help? Refer to the example CSV structure below.")

    except Exception as e:
        st.error(f"Error reading CSV file. Please ensure it is a valid CSV. Error: {e}")
        # st.exception(e) # Uncomment for detailed traceback in debug

else:
    st.info("Upload a CSV file to begin.")
    st.markdown("""
    **Example CSV structure:**
    ```csv
    date,province,beneficiaries
    2023-01-01,Kabul,100
    2023-02-01,Kabul,110
    2023-03-01,Kabul,120
    2023-01-01,Herat,50
    2023-02-01,Herat,55
    2023-03-01,Herat,60
    ```
    """)