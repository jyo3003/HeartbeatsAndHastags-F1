def generate_statistics_and_visuals():
    import pandas as pd
    import matplotlib.pyplot as plt
    # Define a font that supports the required glyphs
    plt.rcParams['font.family'] = 'Arial Unicode MS'
    plt.rcParams['font.size'] = 12


    file_path = 'data_processed/processed_f1_tweets.csv'
    df = pd.read_csv(file_path)

    # Selecting the quantitative and qualitative features
    quant_features = ['user_followers', 'user_friends', 'user_favourites']
    quali_features = ['user_name', 'user_location', 'hashtags', 'date']

    # Summary statistics: quantitative features
    summary_quantitative = df[quant_features].agg(['min', 'max', 'median'])

    # Summary statistics: qualitative features
    summary_qualitative = pd.DataFrame()

    for feature in quali_features:
        if feature == 'hashtags':
            all_hashtags = []
            for tags in df['hashtags']:
                if type(tags) is str:
                    extracted_tags = tags.replace("[", "").replace("]", "").replace("'", "").split(", ")
                    all_hashtags.extend(extracted_tags)
            total_categories = len(set(all_hashtags))
            most_frequent = pd.Series(all_hashtags).value_counts().idxmax()
            least_frequent = pd.Series(all_hashtags).value_counts().idxmin()
        else:
            total_categories = df[feature].nunique()
            most_frequent = df[feature].value_counts().idxmax()
            least_frequent = df[feature].value_counts().idxmin()

        summary_qualitative = summary_qualitative._append(pd.Series({'Feature': feature, '  Number of Categories': total_categories, '   Most Frequent Category': most_frequent, '        Least Frequent Category': least_frequent}), ignore_index=True)

    # Compute pairwise correlations
    correlations = df[quant_features].corr()


    # Save the summary statistics to a text file
    summary_file_path = 'data_processed/summary.txt'
    with open(summary_file_path, 'w') as file:
        file.write("\nSummary Statistics for Quantitative Features:\n\n")
        file.write(summary_quantitative.to_string() + "\n\n")
        file.write("\nSummary Statistics for Qualitative Features:\n\n")
        file.write(summary_qualitative.to_string(index=False))

    # Save the correlations to a text file
    correlations.to_csv('data_processed/correlations.txt', index=True, sep='\t')

    import pandas as pd
    import matplotlib.pyplot as plt

    file_path = 'data_processed/processed_f1_tweets.csv'
    df = pd.read_csv(file_path)

    # Selecting the quantitative and qualitative features
    quant_features = ['user_followers', 'user_friends', 'user_favourites']
    quali_features = ['user_name', 'user_location', 'hashtags', 'date']


    # Scatter plots for quantitative features
    for i in range(len(quant_features)):
        for j in range(i+1, len(quant_features)):
            feature1 = quant_features[i]
            feature2 = quant_features[j]
            plt.figure(figsize=(12, 8))  # Adjust the figure size here
            plt.scatter(df[feature1], df[feature2], alpha=0.5)
            plt.xlabel(feature1, fontsize=12)
            plt.ylabel(feature2, fontsize=12)
            plt.title(f'Scatter Plot of {feature1} vs {feature2}')
            plt.tight_layout()
            plt.savefig(f'visuals/scatter_{feature1}_{feature2}.png')
            plt.close()

    # Histograms for qualitative features
    # Define a list of colors
    colors = ['steelblue', 'indianred', 'mediumseagreen', 'salmon', 'royalblue', 'coral', 'forestgreen', 'tomato', 'mediumaquamarine', 'lightcoral']

    for i, feature in enumerate(quali_features):
        if feature not in quant_features:
            plt.figure(figsize=(12, 8))
            if feature == 'date':
                df[feature] = pd.to_datetime(df[feature])
                df[feature] = df[feature].dt.date
            counts = df[feature].value_counts()
            if len(counts) > 20:
                # Plot with different colors for each category
                counts[:20].plot(kind='bar', color=colors[:20])
            else:
                # Plot with different colors for each category
                counts.plot(kind='bar', color=colors[:len(counts)])
            plt.xlabel(feature)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {feature}')
            plt.tight_layout()
            plt.savefig(f'visuals/histogram_{feature}.png')
            plt.close()



