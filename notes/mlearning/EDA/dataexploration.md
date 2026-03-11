┌─────────────────────────────────────────────────────────────┐
│                    EXPLORATORY DATA ANALYSIS                 │
│                       "Get to know your data"                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🔍 1. LOOK AT DATA                                         │
│      df.head() / df.tail() / df.sample()                    │
│      df.shape / df.columns / df.info()                      │
│                                                              │
│  📊 2. SUMMARY STATISTICS                                    │
│      df.describe()            # Numerical stats             │
│      df.describe(include='object') # Categorical stats      │
│      df['col'].value_counts() # Category frequencies        │
│                                                              │
│  🧹 3. DATA QUALITY                                          │
│      df.isnull().sum()        # Missing values              │
│      df.duplicated().sum()    # Duplicates                  │
│      df.dtypes                # Data types                  │
│                                                              │
│  📈 4. DISTRIBUTIONS                                         │
│      df['num'].hist(bins=30)  # Histogram                   │
│      df.boxplot()             # Box plots (outliers)        │
│      sns.kdeplot(df['num'])   # Density plot                │
│                                                              │
│  🔗 5. RELATIONSHIPS                                          │
│      df.corr()                 # Correlation matrix         │
│      sns.heatmap(df.corr())    # Visual correlation         │
│      sns.pairplot(df)          # All pairs scatter          │
│      sns.scatterplot(x='col1', y='col2', data=df)           │
│                                                              │
│  📊 6. CATEGORICAL VS NUMERICAL                              │
│      df.groupby('cat')['num'].mean()  # Average by category │
│      sns.barplot(x='cat', y='num', data=df)                 │
│      sns.boxplot(x='cat', y='num', data=df)                 │
│                                                              │
│  💡 7. INSIGHTS                                              │
│      What did you find?                                      │
│      What needs cleaning?                                    │

☐ Load data
☐ Check shape & columns
☐ View sample rows
☐ Check data types
☐ Summary statistics
☐ Missing values (count & visualize)
☐ Duplicates
☐ Numerical distributions (histograms)
☐ Outliers (box plots)
☐ Categorical frequencies (bar plots)
☐ Correlations (heatmap)
☐ Relationships (pairplot, scatter)
☐ Group by analysis
☐ Document insights
☐ List cleaning steps
☐ Note feature ideas
│      What features look promising?       