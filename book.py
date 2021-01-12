import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scrapper import book_scrape

def scrape(file_path):  # location of books_2000.csv
    # df = book_scrape(num_books=1200)
     # ========== OR ============
    df = pd.read_csv(file_path)
    return df


def data_clean(df):
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop_duplicates(inplace=True)
    
    df['num_rating'] = df['num_rating'].astype(str)
    df['num_rating'] = df['num_rating'].apply(lambda x: x.replace(' ratings', ''))
    df['num_rating'] = df['num_rating'].astype(object)

    ## sparse minirating column to get avg_rating and num_ratings
    df['avg_rating'] = df['minirating'].apply(lambda x: (x.split('— ')[0]))
    df['avg_rating'] = df['avg_rating'].apply(lambda x: x.replace(' avg rating', ''))
    df['avg_rating'] = df['avg_rating'].apply(lambda x: x.replace(' ', ''))

    df['num_ratings'] = df['minirating'].apply(lambda x: (x.split('— ')[1]))
    df['num_ratings'] = df['num_ratings'].apply(lambda x: x.replace(' ratings', ''))

    return df


def preprocessing(df):
    df.avg_rating = pd.to_numeric(df.avg_rating, errors="coerce")
    df.num_ratings = pd.to_numeric(df.num_ratings, errors="coerce")
    # df = df.fillna(0)
    # df['num_ratings'] = df['num_ratings'].astype(int)
    # df['avg_rating'] = df['avg_rating'].astype(int)

    scaler = MinMaxScaler((1, 10))
    df['minmax_norm_rating'] = scaler.fit_transform(df[['avg_rating']])
    df['mean_norm_ratings'] = 1 + (df['avg_rating'] - df['avg_rating'].mean()) / (df['avg_rating'].max() - df['avg_rating'].min()) * 9
    return df

def analyse(df):
    pass

def main():
    df = scrape('books_2000.csv')
    clean_df = data_clean(df)
    processed_df = preprocessing(clean_df)
    analyse(processed_df)


if __name__ == '__main__':
    main()

