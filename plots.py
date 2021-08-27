import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
def app(car_df):
  st.header('Visualize data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('Scatter Plot')
  features_list=st.multiselect('Select the X-axis values',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
  for feature in features_list:
    st.subheader(f'scatter_plot between {feature} and Price')
    plt.figure(figsize=(10,5))
    sns.scatterplot(X=feature,y='price',data=car_df)
    st.pyplot()
  st.subheader('Visualisation Selecter')
  chart_list=st.multiselect('Select charts or plots',('Histogram','Boxplot','Correlation Heatmap'))
  if 'Histogram' in chart_list:
    st.subheader('Histogram')
    columns=st.selectbox('Select the column to create its histogram',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
    plt.figure(figsize=(10,5))
    plt.title(f'histogram for {columns}')
    plt.hist(car_df[columns],bins='sturges',edgecolor=black)
    st.pyplot()
  if 'Boxplot' in chart_list:
    st.subheader('Boxplot')
    columns=st.selectbox('Select the column to create its boxplot',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
    plt.figure(figsize=(10,5))
    plt.title(f'Boxplot for {columns}')
    sns.boxplot(car_df[columns])
    st.pyplot()
  if 'Correlation Heatmap' in chart_list:
    st.subheader('Correlation Heatmap')
    columns=st.selectbox('Select the column to create its Correlation Heatmap',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
    plt.figure(figsize=(10,5))
    ax=sns.heatmap(car_df.corr(),annot=True)
    bottom,top=ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pyplot()