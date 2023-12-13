from datetime import datetime

def between_dates(date1, date2):
    date_format = "%Y-%m-%d %H:%M:%S"
    return (datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)).days

with open('forum_users.txt', 'r') as file_read, open('users_stats.txt', 'w') as file_write:
    for line in file_read:
        user, st_date, end_date = line.strip().split('\t')
        relult_1 = between_dates(st_date, end_date)
        result_2 = between_dates(end_date, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file_write.write(f"{user}\t{relult_1}\t{result_2}\n")

file_read.close()
file_write.close()