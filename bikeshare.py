import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        try:
            city= input('Which city would you like to explore(chicago, new york city, or washington)?: ').lower()
            if city == 'chicago' or city == 'new york city' or city =='washington':
                print('You selected: ',city)
                break
            else:
                print('City should be "chicago","new york city", or "washington" only. Please re-enter.')
        except:
                continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month= input('Would you like to filter for a specific month? If no enter "all": ').lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                print('You selected: ',month)
                break
            else:
                print('Month should be "january", "february", "march", "april", "may", "june", or "all". Please re-enter.')
        except:
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day= input('Would you like to filter for a day of the week? If no enter "all": ').lower()
            if day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'all':
                print('You selected: ',day)
                break
            else:
                print('Day should be "sunday","monday","tuesday","wednesday","thursday","friday","saturday" or "all". Please re-enter.')
        except:
            continue


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
    df = pd.read_csv(CITY_DATA[city])
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour,month, trip combination, and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    df['trip_combo'] = df['Start Station']+' to '+df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month= df['month'].mode()[0]
    print('Most popular month for traveling: ', months[common_month - 1].title())
    # TO DO: display the most common day of week
    common_day= df['day_of_week'].mode()[0]
    print('Most popular day of the week for traveling: ', common_day)
    # TO DO: display the most common start hour
    common_hour= df['start_hour'].mode()[0]
    print('Most common start hour: ',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('Most common start station: ',common_start)
    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('Most common end station: ',common_end)
    # TO DO: display most frequent combination of start station and end station trip
    common_trip= df['trip_combo'].mode()[0]
    print('Most common comination of start and end station: ',common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration_hours=(df['Trip Duration'].sum())/120
    print('The total trip duration for the selected period was: ',total_trip_duration_hours,' hours.')

    # TO DO: display mean travel time
    avg_trip_duration_minutes= (df['Trip Duration'].mean())/60
    print('The average trip duration for the selected period was: ',avg_trip_duration_minutes,' minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print('Count of user types:\n',user_types)

    #TO DO: Display counts of gender
    try:
        gender_types=df['Gender'].value_counts()
        print('Count of genders:\n', gender_types)
    except:
        print('\nNo gender data for washington')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year=df['Birth Year'].min()
        most_recent_birth_year=df['Birth Year'].max()
        most_common_birth_year=df['Birth Year'].mode()[0]
        print('\nEarliest birth year: ',earliest_birth_year)
        print('\nMost recent birth year: ',most_recent_birth_year)
        print('\nMost common birth year: ',most_common_birth_year)
    except KeyError:
        print('No birth year data for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

#ask the user to see 5 lines of raw data
        x=0
        y=5
        while True:
            raw_data=input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
            if raw_data.lower() == 'no':
                break
            if raw_data.lower() != 'no' and raw_data.lower() != 'yes':
                print('/nInput not recognized. Please enter "yes" or "no".')
            else:
                print(df.iloc[x:y])
                x+=5
                y+=5



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
