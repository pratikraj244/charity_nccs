
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import streamlit.components.v1 as components
st.set_page_config(
    page_title="NCCS charity data",
    layout = "wide",
    
)
d = pd.read_csv("data/core_2024_990combined.csv")
d1 = d.dropna()
data2 = d1[["is_501c3","total_assets_eoy","prohibited_tax_shelter_cd","investment_income","gross_sales_inventory","total_liabilities_eoy","total_net_assets_eoy","total_revenue","total_contributions","program_service_revenue","total_expenses","gross_income_fundraising_events","gross_income_gaming_activities","excess_benefit_transaction_cd","disqualified_persons_amts_sec509","loan_to_interested_person_cd",'excess_over_1pct_sec509',
    'excess_over_2pct_sec170',
    'public_support_subtotal_sec170',
    'public_support_sec170',
    'public_support_sec509',
    'public_support_subtotal_line6_sec509',
    'public_support_subtotal_line4_ref_sec170','public_support_subtotal_line6_ref_sec509',

            ]]
import streamlit as st
import pandas as pd

# Column descriptions dictionary
column_descriptions = {
    # Organization Status & Compliance
    "is_501c3": "Indicates if the organization is a 501(c)(3) public charity. 501(c)(3) status means donations are tax-deductible.",
        
    "prohibited_tax_shelter_cd":"Boolean flag indicating if the organization was involved in a prohibited tax shelter transaction as defined by IRS regulations.",
        
    "excess_benefit_transaction_cd":"Boolean flag indicating if the organization participated in an excess benefit transaction with a disqualified person (e.g., paying excessive compensation to a board member).",
        
    "loan_to_interested_person_cd":"Boolean flag indicating if the organization made a loan to an interested person (board member, executive, etc.).",
        
    "complaince_issue": "A count or indicator of compliance issues identified in the filing. Sums up multiple compliance flags into a single numeric score.",
        
   

    # Financial Summary
    "total_assets_eoy": "Total assets the organization owns at the end of the tax year. Includes cash, investments, property, equipment, etc.",
        
   
    "total_liabilities_eoy": "Total debts and obligations the organization owes at the end of the tax year. Includes loans, accounts payable, mortgages, etc.",
        
    
    "total_net_assets_eoy": "Total assets minus total liabilities. Represents the organization's net worth or fund balance.",
       
    
    "total_revenue":"Total revenue from all sources combined. The organization's total income for the year.",
        
    
    "total_contributions": "Total contributions, gifts, grants, and similar amounts received from donors and grantmakers.",
        
    
    "program_service_revenue":"Revenue earned from the organization's primary mission-related activities (e.g., tuition for a school, fees for healthcare services).",
        
   
    "total_expenses": "Total expenses for the year. Includes all program services, fundraising, and administrative costs.",
        
   
    "profit_loss": "Net income or loss for the year. Positive = surplus, Negative = deficit.",
        
   

    # Revenue Breakdown
    "investment_income":"Income generated from investments (dividends, interest, capital gains, etc.).",
       
   
    "gross_sales_inventory":"Gross sales of inventory, less returns and allowances. Relevant for organizations that sell goods (e.g., thrift stores, bookstores).",
        
   
    "gross_income_fundraising_events": "Gross income from fundraising events before deducting event expenses (e.g., gala ticket sales, auctions).",
        
   
    "gross_income_gaming_activities":"Gross income from gaming activities like bingo, raffles, casino nights.",
        
  

    # Public Support Tests
    "public_support_sec170":"Public support as defined under IRC Section 170(b)(1)(A)(vi). Used to determine if an organization is a publicly supported charity.",
        
   
    "public_support_subtotal_sec170": "Subtotal of public support (sec 170) before other adjustments.",
        
  
    "public_support_subtotal_line4_ref_sec170":"Specific subtotal for the public support test (line 4 reference). Used in calculating total support.",

    "public_support_sec509": "Public support as defined under IRC Section 509(a)(1). Another test to determine public charity status.",
        
  
    "public_support_subtotal_sec509":"Subtotal of public support (sec 509) before other adjustments.",
        
 
    "public_support_subtotal_line6_sec509": "Subtotal of public support (line 6 reference) in the 509(a)(1) support test.",
        
    
    "public_support_subtotal_line6_ref_sec509": "Reference subtotal for public support line 6.",
   

    # Compliance & Support Test Values
    "disqualified_persons_amts_sec509": "Amount of funds involved with disqualified persons as reported for the 509(a)(1) test.",
  
    "excess_over_1pct_sec509":"Amount of excess contributions over 1% for the 509(a)(1) support test.",

    "excess_over_2pct_sec170":"Amount of excess contributions over 2% for the 170 support test.",


    # Derived Financial Metrics
    "debt_to_assets":"A leverage ratio showing what proportion of assets are financed by debt. Higher values indicate more financial risk.",
 
    "revenue_to_expense":"A ratio showing how much revenue the organization generates for every dollar of expense.",
   
    "operating_margin":"A profitability ratio that shows what percentage of revenue remains after covering expenses.",
  
    "donation_dependency": "Measures how dependent the organization is on donations and contributions rather than earned revenue.",
        
    "liquidity_proxy": "An indicator of the organization's ability to cover short-term obligations.",
        

    # Geographic & Categorical
    "state": "The state of an organization",
        
    "assets_metrics": "A derived metric or category label related to assets. May classify organizations by size (e.g., 'Large', 'Medium', 'Small') or provide an asset ratio.",
    "profit_metrics": "A derived metric or category label related to profitability. May classify organizations as 'Surplus', 'Break-even', or 'Deficit'.",
    
    }


# --- Streamlit App ---
#st.set_page_config(page_title="Data Dictionary", layout="wide")
st.title("🔢 DATASET AND EXPLANATIONS")
st.markdown("Search and explore column definitions")

# Search bar
search_term = st.text_input("🔍 Search for a column name or description:", placeholder="e.g., revenue, support, assets")

# Filter columns based on search
if search_term:
    filtered_cols = {
        col: desc for col, desc in column_descriptions.items()
        if search_term.lower() in col.lower() or search_term.lower() in desc.lower()
    }
else:
    filtered_cols = column_descriptions

# Display results
st.write(f"Showing **{len(filtered_cols)}** of **{len(column_descriptions)}** columns")

# Create a clean table-like display
for col, desc in filtered_cols.items():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.code(col, language="python")
    with col2:
        st.markdown(desc)
    st.divider()
from logging import logProcesses
def func(x):
  if x < 0:
    return "negative assets"
  elif x > 0:
    return "positive assets"
  else:
    return "zero assets"
data2["assets_metrics"] = data2["total_net_assets_eoy"].apply(func)
data2["profit_loss"] = data2["total_revenue"] - data2["total_expenses"]
def func2(x,y):
  if x > 0 and y > 0:
    return "accumulating"
  elif x > 0 and y < 0:
    return "spending"
  elif x < 0 and y > 0:
    return "recovering"
  elif x < 0 and y < 0:
    return "detoriate"
  elif x == 0 and y > 0:
    return "breaking even"
  elif x == 0 and y < 0:
    return "no improvement"
  elif x > 0 and y == 0:
    return "building from zero"
  elif x < 0 and y == 0:
    return "falling from zero"
  else:
    return "zero balance"
data2["state"] = data2.apply(lambda x: func2(x["profit_loss"], x["total_net_assets_eoy"]), axis=1)
data2['debt_to_assets'] = data2['total_liabilities_eoy'] / data2['total_assets_eoy']
data2["revenue_to_expense"] = data2["total_revenue"] / data2["total_expenses"]
data2['operating_margin'] = (data2['total_revenue'] - data2['total_expenses']) / data2['total_revenue']
data2["donation_dependency"] = data2["total_contributions"] / data2["total_revenue"]
data2['liquidity_proxy'] = data2['investment_income'] / data2['total_expenses']
data2 = data2.fillna(0)
data2["complaince issue"] = ((data2["prohibited_tax_shelter_cd"] == 1) | (data2["loan_to_interested_person_cd"] == 1) | (data2["excess_benefit_transaction_cd"] == 1)).astype(int)
data2["public_support_pct"] = data2["public_support_sec170"] / data2["public_support_subtotal_sec170"]
data2["public_support_pct"] = data2["public_support_pct"].replace([float('inf'), -float('inf')], 0).fillna(0)
data2
data3 = data2.copy()
import numpy as np
x = data3
st.markdown("""
        <style>
        /* Style the selectbox label */
        .stSelectbox label {
            font-size: 30px !important;
            font-weight: bold !important;
        }
        
                    
        /* Target the select widget container */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #000000 !important;
            border-radius: 10px !important;
            border: 2px solid #FFFFFF !important;
        }            
        
        /* Style the selected value */
        .stSelectbox div[data-baseweb="select"] div {
            font-weight: bold !important;
            font-size: 16px !important;
        }
        
        /* Style dropdown menu items */
        div[role="listbox"] div {
            background-color: #e8f5e9 !important;
            color: black !important;
            font-size: 14px !important;
        }
        
        /* The actual list item Streamlit renders */
    li[role="option"]:hover {
        background-color: #FFFFFF !important;
        color: black !important;
    }
        

        </style>
    """, unsafe_allow_html=True)
st.markdown("""
<style>
/* This will highlight dropdown options in red - helps identify the right selector */
div[role="option"] {
    background-color: red !important;
}
</style>
""", unsafe_allow_html=True)
st.title("ORGANIZATION STATES")
st.write("So the organizations is divided into 9 states, by taking profit_loss metrics and net_assets metrics into consideration.")

state_meanings = {
    "accumulating": "Making profit AND have saving. Risk is low",
    "spending": "Making profit but have debt. Risk is medium",
    "recovering": "Lost money but have savings. Risk is medium",
    "deteriorate": "Losing money AND in debt. Risk is high",
    "breaking even": "No profit, but have savings. Risk is low.",
    "no improvement": "No profit and in debt. Risk is high",
    "building from zero": "Just starting, making money. Risk is medium",
    "falling from zero": "Just starting, losing money. Risk is high",
    "zero balance": "No activity. Neutral risk."
}


state_df = pd.DataFrame([
    {"State": state, "Meaning": meaning} 
    for state, meaning in state_meanings.items()
])

# Display it
st.dataframe(state_df, use_container_width=True)


st.title("📊 INSIGHTS AND DETAILED ANALYTICS")
col1, col2, col3, col4,col5 = st.columns(5)
with col1:
  drop1 = st.selectbox(label="Organizations",options=["Complaint charity","non complaint non profit"])
if drop1 == "Complaint charity":
  li2 = len(data2[data2["is_501c3"] == True])
  col2.metric("tax exempt organization",value=li2)
  style_metric_cards(background_color="green",         # Entire card background
            border_left_color="green",border_color="green")

  li3 = len(data2[data2["prohibited_tax_shelter_cd"] == False])
  col3.metric("non tax shelter flag organization",value=li3)
  style_metric_cards(background_color="green",         # Entire card background
            border_left_color="green",border_color="green")

  li4 = len(data2[data2["excess_benefit_transaction_cd"] == False])
  col4.metric("non excess benefit organizations",value=li4)
  style_metric_cards(background_color="green",         # Entire card background
            border_left_color="green",border_color="green")

  li5= len(data2[data2["loan_to_interested_person_cd"] == False])
  col5.metric("Organizations having insider loans",value=li5)
  style_metric_cards(background_color="green",         # Entire card background
            border_left_color="green",border_color="green")

if drop1 == "non complaint non profit":
  li2 = len(data2[data2["is_501c3"] == False])
  col2.metric("tax exempt organization",value=li2)
  style_metric_cards(background_color="red",         # Entire card background
            border_left_color="red",border_color="red")

  li3 = len(data2[data2["prohibited_tax_shelter_cd"] == True])
  col3.metric("non tax shelter flag organization",value=li3)
  style_metric_cards(background_color="red",         # Entire card background
            border_left_color="red",border_color="red")

  li4 = len(data2[data2["excess_benefit_transaction_cd"] == True])
  col4.metric("non excess benefit organizations",value=li4)
  style_metric_cards(background_color="red",         # Entire card background
            border_left_color="red",border_color="red")

  li5 = len(data2[data2["loan_to_interested_person_cd"] == True])
  col5.metric("Organizations having insider loans",value=li5)
  style_metric_cards(background_color="red",         # Entire card background
            border_left_color="red",border_color="red")


drop = st.selectbox(label="Organization States",options=["size and scale metrics","revenue source metrics","financial health and efficiency","public support, states and complaince"])
if drop == "size and scale metrics":
  col1,col2 = st.columns(2)
  with col1:
    st.subheader("Average assets with states")
    
    assets = data2.groupby("state")["total_assets_eoy"].mean().reset_index()
    f12 = px.bar(
        assets, 
        x="state", 
        y=assets["total_assets_eoy"],  # Pass the series directly
    )
    st.plotly_chart(f12, width='stretch')
    st.write("This insights tell that which states of the organization, own more or less. It also helps to identify what states of the organization has major facilities/investments")

    st.subheader("Average liabilities with states")
    liabilities = data2.groupby("state")["total_liabilities_eoy"].mean().reset_index()
    f3 = px.area(
        data_frame=liabilities,
        x="state",
        y="total_liabilities_eoy",
    )
    st.plotly_chart(f3, use_container_width=True)
    st.write("This insights tell that which states of the organization owe more or less. It helps to asses which state of an organization, has debt burden and by how much, on calculating the average.")


    st.subheader("Average net assets with states")
    net_assets = data2.groupby("state")["total_net_assets_eoy"].mean().reset_index()
    f4 = px.line(
        data_frame=net_assets,
        x="state",
        y="total_net_assets_eoy",
    )
    st.plotly_chart(f4, use_container_width=True)
    st.write("This insights tell that which states of the organization's financial condition is good or bad. For better state of organization, assets must be greater than liabilities.")

    revenue = data2.groupby("state")["total_revenue"].mean().reset_index()
  with col2:
    st.subheader("Average revenue with states")
    f5 = px.bar(
        data_frame=revenue,
        x="state",
        y="total_revenue",
    )
    st.plotly_chart(f5, use_container_width=True)
    st.write("It tells, which state of an organizations have more or less income. Greater the income, greater is that state.")
    st.subheader("Average expenses with states")
    expenses = data2.groupby("state")["total_expenses"].mean().reset_index()
    f9 = px.area(
        data_frame=expenses,
        x = "state",
        y = "total_expenses",
    )
    st.plotly_chart(f9, use_container_width=True)
    st.write("This insight says, which state of an organization spends more or less. It helps us to understand, the cost of operations for a organization state ")
    st.subheader("Average revenue to expense ratio with states")
    revenue_to_expense = data2.groupby("state")["revenue_to_expense"].mean().reset_index()
    f12 = px.line(
        data_frame=revenue_to_expense,
        x = "state",
        y = "revenue_to_expense",
    )
    st.plotly_chart(f12, use_container_width=True)
    st.write("This insight says which state of an organization are in surplus or in deficit. For surplus, revenue should be greater than expense, and for deficit, expense is greater than revenue.")


if drop == "revenue source metrics":
  col1,col2 = st.columns(2)
  with col1:
    st.subheader("Average investment income with states")
    state_investment_income = data2.groupby("state")["investment_income"].mean().reset_index()
    f1 = px.bar(
        data_frame=state_investment_income,
        x="state",
        y="investment_income",
        color_discrete_sequence=["#0c59ff"]
    )
    
    st.plotly_chart(f1, use_container_width=True)
    st.write("This insights tells us the average income from investments for each organization states. It also identifies which organizations are wealthy.")
    st.subheader("Average contributions with states")
    contributions = data2.groupby("state")["total_contributions"].mean().reset_index()
    f6 = px.area(
        data_frame=contributions,
        x="state",
        y="total_contributions",
        color_discrete_sequence=["#0c59ff"]
    )
    st.plotly_chart(f6, use_container_width=True)
    st.write("This insight tells, average donations received from people, for each organization states. Higher contributions means, people donate generously, while lower donations means, organizations rely on other source.")
  with col2:
    st.subheader("Average program service revenue with states")
    program_serivce_revenue = data2.groupby("state")["program_service_revenue"].mean().reset_index()
    f7 = px.bar(
        data_frame=program_serivce_revenue,
        x = "state",
        y = "program_service_revenue",
        color_discrete_sequence=["#0c59ff"]
    )
    st.plotly_chart(f7, use_container_width=True)
    st.write("This insight tells us, average income earned from mission services. It identifies, the organization state with social enterprise model.")
    st.subheader("Average gross sales inventory with states")
    gross_sales = data2.groupby("state")["gross_sales_inventory"].mean().reset_index()
    f2 = px.area(
        data_frame=gross_sales,
        x="state",
        y="gross_sales_inventory",
        color_discrete_sequence=["#0c59ff"]
    )
    st.plotly_chart(f2, use_container_width=True)
    st.write("This insight tells average revenue generated, from selling goods and services, such as merchandise, thrift stores, etc, by the organization state.")



if drop == "financial health and efficiency":
  col1,col2 = st.columns(2)
  with col1:
    st.subheader("Average operating margin with states")
    operating_margin = data2.groupby("state")["operating_margin"].mean().reset_index()
    f13 = px.area(
        data_frame=operating_margin,
        x = "state",
        y = "operating_margin",
        color_discrete_sequence=["#fffb1c"]
    )
    st.plotly_chart(f13, use_container_width=True)
    
    st.write("This insight helps to identify, profit/surplus percentage for each organization states. Greater this factor, more better and stable is that state of an organization.")
  with col2:
    st.subheader("Average debt to assets with states")
    debt_to_assets = data2.groupby("state")["debt_to_assets"].mean().reset_index()
    f11 = px.line(
        data_frame=debt_to_assets,
        x = "state",
        y = "debt_to_assets",
        color_discrete_sequence=["#fffb1c"]
    )
    st.plotly_chart(f11, use_container_width=True)
    st.write("This insight tells average leverage for each organization states. Interpretation: < 25%: Low debt, financially conservative. 25-50%: Moderate debt, typical with buildings/mortgages. 50-75%: High debt, vulnerable to economic shocks. > 75%: Danger zone, risk of insolvency ")

if drop == "public support, states and complaince":
  col1,col2 = st.columns(2)
  with col1:
    st.subheader("Average public support percentage with states")
    public_support = data2.groupby("state")["public_support_pct"].mean().reset_index()
    f8 = px.bar(
        data_frame=public_support,
        x = "state",
        y = "public_support_pct",
        color_discrete_sequence=["#ce0000"]
    )
    st.plotly_chart(f8, use_container_width=True)
    st.write("This stats tell us which organization states has how much public support, in percentage. Interpretation: - > 33%: Strong public support (true public charities). 10-33%: Moderate public support. < 10%: Weak public support (possible private foundations)")
  with col2:
    st.subheader("Average complaince issues with states")
    complaince_issue = data2.groupby("state")["complaince issue"].mean().reset_index()
    f15 = px.area(
        data_frame= complaince_issue,
        x = "state",
        y = "complaince issue",
        color_discrete_sequence=["#ce0000"]
    )
    st.plotly_chart(f15, use_container_width=True)
    st.write("This insight tells which no of each organization states have complaince issues. The complaince issues includes, prohibited tax shelter, disqualified persons amounts, and loan to interested persons")
  

st.header("PREDICTIONS")
st.write("To predict the state of an organization, I used machine learning models, that gave high accuracy matching the industry standards.")
x.replace([np.inf, -np.inf], 0, inplace=True)
good_features = [
    'total_assets_eoy',      # Size (but don't use net version!)
    'total_liabilities_eoy', # Debt level
    'total_contributions',   # Donation amount
    'program_service_revenue', # Earned revenue
    'investment_income',     # Endowment income
    'donation_dependency',   # Revenue mix (calculated from contributions/revenue)
    'debt_to_assets',        # Leverage ratio
    'excess_over_1pct_sec509', # Public support concentration
    'excess_over_2pct_sec170',
    'total_net_assets_eoy',
    'total_revenue',
    'total_expenses'
]

# Select only these (or similar)
x2 = x[good_features].copy()
y2 = data3["state"]
from sklearn.model_selection import train_test_split
x_train2,x_test2,y_train2,y_test2 = train_test_split(x2,y2,test_size=0.2,random_state=42)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
rf = RandomForestClassifier(n_estimators=60,           # Moderate trees
    max_depth=15,     # Need 15 orgs to split
    min_samples_leaf=9,        # Each leaf covers 8 orgs
    random_state=40)
rf.fit(x_train2,y_train2)
y_pred2 = rf.predict(x_test2)
print(y_pred2)
print(accuracy_score(y_test2,y_pred2))
print(confusion_matrix(y_test2,y_pred2))
print(classification_report(y_test2,y_pred2))
col6,col8 = st.columns(2)
import pandas as pd
with col6:
  st.subheader("Testing dataset for predictions")
  x_test1 = x_test2.copy()
  x_test1["states"] = y_pred2
  x_test1
with col8:
  st.subheader("Number of predicted organization states")
  series = pd.Series(y_pred2).value_counts()
  states = pd.DataFrame({
      'state': ["accumulating","reocvering","detoriate","spending","building from zero","zero balance","falling from zero","breaking even"],
      'count': series.values
  })
  fig20 = px.bar(x = states["state"], y = states["count"], labels={"x": "states", "y": "count"})
  st.plotly_chart(fig20, use_container_width=True)

