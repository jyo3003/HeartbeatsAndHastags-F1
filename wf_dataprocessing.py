import pandas as pd

def process_data():

    df = pd.read_csv('data_original/f1_tweets.csv', low_memory=False)

    # Dropping irrelevant columns
    df.drop(['user_description', 'user_created', 'user_verified', 'source', 'is_retweet'], axis=1, inplace=True)

    # Converting the 'date, time' column to date format
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

    # Dropping rows with missing dates
    df.dropna(subset=['date'], inplace=True)

    # Handling missing values for specific numerical columns
    numerical_columns = ['user_followers', 'user_friends', 'user_favourites']
    for col in numerical_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, handling errors

    # Handling missing values with the mean of each column
    for col in numerical_columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Dropping duplicate rows
    df.drop_duplicates(inplace=True)

    # Use map to handle non-ASCII characters
    df = df.apply(lambda x: x.map(lambda y: ''.join([i if ord(i) < 128 else ' ' for i in str(y)])))

    # Save processed data to a new CSV file
    df.to_csv('data_processed/processed_f1_tweets.csv', index=False)
