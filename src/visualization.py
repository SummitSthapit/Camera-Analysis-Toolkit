import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=30, color='blue', edgecolor='black')
    plt.title('Price Distribution of Cameras')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('output/price_distribution.png')
    plt.close()

def plot_resolution_vs_price(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Max resolution'], df['Price'], color='red', alpha=0.5)
    plt.title('Resolution vs Price of Cameras')
    plt.xlabel('Max Resolution (MP)')
    plt.ylabel('Price')
    plt.grid()
    plt.savefig('output/resolution_vs_price.png')
    plt.close()

def plot_release_year_distribution(df):
    plt.figure(figsize=(10, 6))
    df['Release year'] = df['Release date']
    plt.hist(df['Release year'].dropna(), bins=30, color='green', edgecolor='black')
    plt.title('Release Year Distribution of Cameras')
    plt.xlabel('Release Year')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('output/release_year_distribution.png')
    plt.close()

def plot_release_trend(df):
    plt.figure(figsize=(10, 6))
    df['Release year'] = df['Release date']
    yearly_counts = df['Release year'].value_counts().sort_index()
    plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-')
    plt.title('Number of Cameras Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Cameras')
    plt.grid()
    plt.savefig('output/release_trend.png')
    plt.close()
