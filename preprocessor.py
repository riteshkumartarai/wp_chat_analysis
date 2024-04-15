import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s*(?:AM|PM)\s-\s'

    message=re.split(pattern,data)[1:]
    dates=re.findall(pattern, data)
    Dates=[]
    for message in dates:
     cleaned_message = message.replace("\u202f", " ")
     Dates.append(cleaned_message)
    
     

    df=pd.DataFrame({'user_message':message,'message_date':Dates})
    df['message_date']=pd.to_datetime(df['message_date'],format='%m/%d/%y, %I:%M %p - ')
    df.rename(columns={'message_date':'date'},inplace=True)
    df.head()

    users = []
    messages = []
    users=[]
    messages=[]
    for message in df['user_message']:
        entry=re.split('([\w\W]+?):\s',message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
    
            users.append('group_notification')
            messages.append(entry[0])
    df['users']=users 
    df['message']=message
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df