
import psutil
import time
import pyodbc


import pyodbc

con = pyodbc.connect('DRIVER={SQL Server};'
                     'Server=DESKTOP-BUN7963\SQL2019;'
                     'Database=System_Information;'
                     'Trusted_Connection=yes;')


cursor = con.cursor()

while 1==1:

    cpu_percent_usage = psutil.cpu_percent()
    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_total = psutil.virtual_memory()[0]
    memory_percent_usage = psutil.virtual_memory()[2]
    memory_available= psutil.virtual_memory()[1]
    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_send = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_total = psutil.disk_usage('/')[0]
    disk_used = psutil.disk_usage('/')[1]
    disk_free = psutil.disk_usage('/')[2]
    disk_percent_usage = psutil.disk_usage('/')[3]
    """
    cursor.execute('insert into Performance values(getdate(),'
                   + str(cpu_percent_usage)+ ','
                   + str(memory_percent_usage)+ ',' 
                   + str(cpu_interrupts)+ ','
                   + str(cpu_calls)+ ','
                   + str(memory_used)+ ','
                   + str(memory_free)+ ','
                   + str(bytes_send)+ ','
                   + str(bytes_received)+ ','
                   + str(disk_percent_usage)+ ','
                   + str(memory_total)+ ','
                   + str(memory_available)+ ','
                   + str(disk_total)+ ','
                   + str(disk_used)+ ','
                   + str(disk_free))"""
    query = 'INSERT INTO Performance VALUES (GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(query, (cpu_percent_usage, memory_percent_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_send, bytes_received, disk_percent_usage, memory_total, memory_available, disk_total, disk_used, disk_free))

    
    con.commit()

    time.sleep(1)












