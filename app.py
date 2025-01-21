import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Load the dataset
df = pd.read_csv('C:/Users/sabar/OneDrive/Desktop/Dhatchan_Hackathon/olympic_medals.csv')

# Set Streamlit page configuration
st.set_page_config(page_title="Olympic Medal Analysis", page_icon="🏅", layout="wide")

# Set Plotly theme
pio.templates.default = "plotly_dark"

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#FF5733,#C70039);
        color: white;
    }
    .css-1v3fvcr {
        background: linear-gradient(#DAF7A6,#FFC300);
    }
    .stButton>button {
        color: white;
        background-color: #C70039;
        border-radius: 10px;
    }
    .st-radio>label {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app title
st.title("🏅WELCOME TO OLYMPIC MEDAL ANALYSIS")

# Sidebar for navigation
st.sidebar.title("🌍DASHBOARD")
options = st.sidebar.radio("    DATA ANALYSIS FOR OLYMPICS",
                           ['Medal Distribution by Country',
                            'Medal Distribution by Year',
                            'Medal Distribution by Sport',
                            'Medal Distribution by Medal Type',
                            'Medal Comparison Between Countries',
                            'Medal Distribution by Gender'])

# Function to plot medal distribution by country
def plot_medal_distribution_by_country():
    if 'Country' in df.columns and 'Medal' in df.columns:
        medal_count_by_country = df.groupby('Country')['Medal'].count().reset_index().sort_values(by='Medal', ascending=False)
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Country', y='Medal', data=medal_count_by_country.head(10), palette="viridis")
        plt.title('Top 10 Countries by Medal Count')
        plt.xlabel('Country')
        plt.ylabel('Medal Count')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.error("Required columns 'Country' or 'Medal' not found in dataset.")

# Function to plot medal distribution by year
def plot_medal_distribution_by_year():
    if 'Year' in df.columns and 'Medal' in df.columns:
        medal_count_by_year = df.groupby('Year')['Medal'].count().reset_index()
        plt.figure(figsize=(15, 10))
        sns.lineplot(x='Year', y='Medal', data=medal_count_by_year, marker='o', color='crimson')
        plt.title('Medal Distribution Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Medal Count')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.error("Required columns 'Year' or 'Medal' not found in dataset.")

# Function to plot medal distribution by sport
def plot_medal_distribution_by_sport():
    if 'Sport' in df.columns and 'Medal' in df.columns:
        medal_count_by_sport = df.groupby('Sport')['Medal'].count().reset_index().sort_values(by='Medal', ascending=False)
        plt.figure(figsize=(15, 10))
        sns.catplot(x='Sport', y='Medal', data=medal_count_by_sport.head(10), palette="magma")
        plt.title('Top 10 Sports by Medal Count')
        plt.xlabel('Sport')
        plt.ylabel('Medal Count')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.error("Required columns 'Sport' or 'Medal' not found in dataset.")

# Function to plot medal distribution by medal type (Pie chart)
def plot_medal_distribution_by_medal_type():
    if 'Medal' in df.columns:
        medal_count_by_type = df['Medal'].value_counts().reset_index()
        medal_count_by_type.columns = ['Medal', 'Count']
        fig = px.pie(medal_count_by_type, names='Medal', values='Count', title='Medal Distribution by Type', color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)
    else:
        st.error("Column 'Medal' not found in dataset.")

# Function to compare medal counts between selected countries
def plot_medal_comparison_between_countries():
    if 'Country' in df.columns and 'Medal' in df.columns:
        selected_countries = st.multiselect('Select Countries for Comparison', df['Country'].unique())
        if selected_countries:
            comparison_data = df[df['Country'].isin(selected_countries)]
            medal_count_comparison = comparison_data.groupby(['Country', 'Medal']).size().reset_index(name='Count')
            fig = px.bar(medal_count_comparison, x='Country', y='Count', color='Medal', barmode='group', title='Medal Comparison Between Selected Countries', color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig)
    else:
        st.error("Required columns 'Country' or 'Medal' not found in dataset.")

#  Function to plot medal distribution by Gender
def plot_medal_distribution_by_Gender():
    if 'Gender' in df.columns and 'Medal' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='Gender', hue='Medal', multiple='stack', palette='Set2')
        plt.title('Medal Distribution by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Medal Count')
        st.pyplot(plt)
    else:
        st.error("Required columns 'Gender' or 'Medal' not found in dataset.")


# Display visualizations based on user selection
if options == 'Medal Distribution by Country':
    plot_medal_distribution_by_country()
elif options == 'Medal Distribution by Year':
    plot_medal_distribution_by_year()
elif options == 'Medal Distribution by Sport':
    plot_medal_distribution_by_sport()
elif options == 'Medal Distribution by Medal Type':
    plot_medal_distribution_by_medal_type()
elif options == 'Medal Comparison Between Countries':
    plot_medal_comparison_between_countries()
elif options == 'Medal Distribution by Gender':
    plot_medal_distribution_by_Gender()