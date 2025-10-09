import streamlit as st
import pandas as pd
from src.finite_group import FiniteGroup, create_Cn, create_Dn

st.title("Finite Group Visualiser")

family = st.selectbox("Select a family of finite groups:", ["Cyclic Group (Cn)", "Dihedral Group (Dn)"])

if family == "Cyclic Groups (Cn)":
    order = st.number_input("Enter order of cyclic group:", min_value=1, value=4, step=1, key="n_cyclic")
else:
    order = st.number_input("Enter order of dihedral group:", min_value=2, value=4, step=2, key="n_dihedral")

if st.button("Generate Group"):
    if family == "Cyclic Groups (Cn)":
        elements, table = create_Cn(order)
        if order == 1:
            labels = ['e']
        elif order == 2:
            labels = ['e', 'g']
        else:
            labels = ['e', 'g'] + [f'g{i}' for i in range(2, order)]
        group = FiniteGroup(elements, table, labels=labels)
    else:
        elements, table, labels = create_Dn(order)
        group = FiniteGroup(elements, table, labels=labels)

    st.session_state['group'] = group
    st.session_state['family'] = family
    st.session_state['order'] = order

st.divider()

if 'group' in st.session_state:
    group = st.session_state['group']
    family = st.session_state['family']
    order = st.session_state['order']

    st.header(f"Group: {family} of order {order}")

    st.markdown("## Operation Table")
    df = pd.DataFrame(index=group.labels, columns=group.labels)
    for i, g in enumerate(group.elements):
        for j, h in enumerate(group.elements):
            df.iat[i, j] = group.labels[group.table[(g, h)]]
    st.dataframe(df)

    st.markdown("## Group Properties")

    col1, col2, col3 = st.columns(3)
    col1.metric("Order of Group", len(group.elements), border=True)
    col2.metric("Identity Element", group.labels[group.identity] if group.identity is not None else "None", border=True)
    col3.metric("Is Abelian", "Yes" if group.is_abelian() else "No", border=True)

    element_orders = group.element_orders()
    orders_str = ", ".join([f"{group.labels[k]}: {v}" for k, v in element_orders.items()])
    st.markdown(f"### Orders of Elements:\n{orders_str}")
    