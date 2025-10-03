import streamlit as st
import pandas as pd
from src.finite_group import create_Cn, operate, display_table, check_order, find_identity, is_abelian

st.title("Finite Group Visualiser")

n = st.number_input("Enter the order of the cyclic group Cn:", min_value=1, value=4, step=1, key="n")
if st.button("Generate Group") or ("elements" in st.session_state and "table" in st.session_state):
    if "elements" not in st.session_state or "table" not in st.session_state or st.session_state.n != n:
        elements, table = create_Cn(n)
        st.session_state["elements"] = elements
        st.session_state["table"] = table
    else:
        elements = st.session_state["elements"]
        table = st.session_state["table"]

    st.write("Elements of Cn:", elements)
    st.write("Order of each element:", check_order(elements, table))
    st.write("Identity Element:", find_identity(elements, table))
    st.write("Is the group abelian?", is_abelian(elements, table))
    st.write("Operation Table:")
    display_table(elements, table)
    st.dataframe(pd.DataFrame.from_dict(table, orient='index'))

    a = st.number_input("Enter first element (a):", min_value=0, max_value=n-1, value=0, step=1, key="a")
    b = st.number_input("Enter second element (b):", min_value=0, max_value=n-1, value=0, step=1, key="b")
    if st.button("Operate a and b"):
        result = operate(a, b, table)
        st.write(f"The result of operating {a} and {b} is: {result}")
