import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june"]
days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs    
    while True:
        city=input("Enter the name for city(Chicago, New York City, \n"\
                   "Washington) to filter with: \n").lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)  
    while True:
        month=input("Enter the name for Month(January, February, \n"\
                    "March, April, May, June) or All for no filter: \n").lower()     
        if month in months or month=="all":
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter the name for Month(Saturday, Sunday, Monday, Tuesday, \n"\
        "Wednesday, Thursday, Friday) or All for no filter: \n").lower()
        if day in days or day=="all":
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    
    # make month and day and hour columns from Start Time column
    df["month"]=df["Start Time"].dt.month
    df["day"]=df["Start Time"].dt.day_name
    df["hour"]=df["Start Time"].dt.hour
    
    # filter by month
    if month != "all":
        month =  months.index(month) + 1
        df = df[ df["month"] == month ]

    # filter by day

    if day != "all":
    # filter by day of week to create the new dataframe
        df = df[ df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day
    most_common_day = df["day"].mode()[0]
    print("The most common day is :", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df["hour"].mode()[0]
    print("The most common start hour is :", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["most_common_trip"] = df["Start Station"]+" to "+df["End Station"]
    most_common_trip = df["most_common_trip"].mode()[0]
    print("The most commonly used start station and end station :", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

# TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types: \n",user_counts)

    # TO DO: Display counts of gender
    if city != "washington":
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender: \n",gender_counts)      
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("Most Common Year: ",earliest_year)
        most_recent = df['Birth Year'].max()
        print("Most Common Year: ",most_recent)
        most_common_year = df['Birth Year'].mode()[0]
        print("Most Common Year: ",most_common_year)  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def slice_data(df):
    """ display a slice ( 5 rows ) of data."""
    for n in range(0,df.shape[0],5):
        
        answer = input("\nWould you like to display a slice more of data? Enter yes or no.\n")
        if answer.lower() != 'yes':
            break
        print(df.iloc[n: n + 5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        slice_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
