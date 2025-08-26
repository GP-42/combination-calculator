from FindSets import find_sets as fs

import copy
import pandas as pd
import streamlit as st

st.title("Combination calculator")
numbers_per_set = st.number_input("Amount of numbers per set",1,100)
total_per_set = st.number_input("Expected sum of the numbers in the set",0,5050,45)
min_number = st.number_input("Minimum number in range",1,100)
max_number = st.number_input("Maximum number in range",9,100)
overview_separator_char = st.text_input("Overview separator char","/",1)

if 'calculate_clicked' not in st.session_state:
    st.session_state.calculate_clicked = False

def click_calculate():
    st.session_state.calculate_clicked = True

st.button("Calculate", on_click=click_calculate)

if st.session_state.calculate_clicked:
    TOTAL_COLUMN_NAME = "Total"
    COMBINATION_COLUMN_NAME = "Combination"
    
    result = []
    
    row_template = {
        TOTAL_COLUMN_NAME : 0,
    }
    for col in range(max_number):
        row_template[f"{col+1}"] = False

    sets = fs(numbers_per_set, total_per_set, min_number, max_number)
    distinct_totals = []
    for set, total in sets:
        if total not in distinct_totals:
            distinct_totals.append(total)
    
    for total in distinct_totals:
        current = copy.deepcopy(row_template)
        current[TOTAL_COLUMN_NAME] = total
        result.append(
            current
            )
    
    data = pd.DataFrame(result)
    
    for set, total in sets:
        for item in set:
            filtered = data[data[TOTAL_COLUMN_NAME] == total].copy()
            filtered.loc[:, f"{item}"] = True
            data.loc[filtered.index] = filtered
    
    st.header("Numbers occuring in the set(s)")
    st.dataframe(data, hide_index=True)
    
    overview = []

    for set, total in sets:
        overview_elements = ""
        
        for item in set:
            if len(overview_elements) > 0:
                overview_elements = overview_elements + f" {overview_separator_char} "
            
            overview_elements = overview_elements + str(item)
        
        overview.append((total, overview_elements))

    overview_data = pd.DataFrame(overview)
    
    overview_column_config = {
        "0" : TOTAL_COLUMN_NAME,
        "1" : COMBINATION_COLUMN_NAME
    }
    
    st.header("Overview of the set(s)")
    st.dataframe(overview_data, hide_index=True, column_config=overview_column_config)