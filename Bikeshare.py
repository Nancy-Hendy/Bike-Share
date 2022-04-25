import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = [ 'chicago', 'new york city', 'washington']
months = ['january','february','march','april','may','june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']


def get_filters():
    
    
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Which city would you like to explore? chicago, new york city , washington ? \n').lower()
    while city not in cities:
        print('Invalid Input! \n')
        city = input('Which city would you like to explore? chicago, new york city , washington ? \n').lower()



    month = input('Please type a month from January to June to filter by month,or type All if no filter needed. \n').lower()
    while month not in months:
        print ('Invalid Input!\n')
        month = input('Please type a month from January to June to filter by month,or type All if no filter needed. \n').lower()



    day = input('Please type a day of the week to filter by day,or type All if no filter needed. \n').lower()
    while day not in days:
        print ('Invalid Input!\n')
        day = input('Please type a day of the week to filter by day,or type All if no filter needed. \n').lower()


    print('-'*40)
    return city, month, day
    print (city,month,day)

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()

    if month != 'all':
        month = months.index(month) + 1
        df=df[df['month'] == month]

    if day != 'all':
        df=df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    pop_month = df['month'].mode()[0]
    print('Most popular month is: ', pop_month)

    
    pop_day = df['day'].mode()[0]
    print('Most popular day of the week is: ', pop_day)

    
    df['hour']=df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most popular start hour is: ', pop_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    pop_start = df['Start Station'].mode()[0]
    print('Most popular START station is: ',pop_start)

    
    pop_end = df['End Station'].mode()[0]
    print('Most popular END station is: ',pop_end)

   
    df['trip'] = 'from '+ df['Start Station'] + " to " + df['End Station']
    pop_trip = df['trip'].mode()[0]
    print('Most popular TRIP is: ',pop_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: ',total_time)


    
    mean_time = df['Trip Duration'].mode()[0]
    print('Mean travel time is: ',mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    user_count= df['User Type'].value_counts().to_frame()
    print('Counts of User Types: ',user_count)
    
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year= df['Birth Year'].max()
        most_common_year= df['Birth Year'].mode()[0]
        gender_count= df['Gender'].value_counts().to_frame()

        print('User gender counts: ',gender_count)
        print('Earliest Birth Year: ',int(earliest_year))
        print('Most Recent Birth Year: ',int(most_recent_year))
        print('Most Common Birth Year: ',int(most_common_year))

    except:
        print('There is no Birth Year or Gender info in selected city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    """this function take ask user if want to see
    the first 5 row of the data and output
    will be in the dataframe (df)
    and ask him if he want to see another 5 row
    """
    print('Raw data available....')

    df = pd.read_csv(CITY_DATA[city])
    more = 0
    rows = df.head()

    user_input = input('Would you like to view 5 rows of raw data? Yes or No ?:\n').lower()

    while user_input == 'yes' :
        print('Displaying the first 5 rows',rows)
        break
    while user_input == 'yes':
        print('Want to view 5 more rows of data? Yes or No?:\n ')
        more += 5
        second_input = input().lower()
        if second_input =='yes':
            print(df[more:more+5])
        else:
            break


    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
