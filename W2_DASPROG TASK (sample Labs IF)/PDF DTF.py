#PERHITUNGAN PERBEDAAN JAM LIVE

live_time_gmt2 = input('Enter the event time (HH:MM:SS) in GMT+2 = ')
current_time_gmt7 = input('Enter current time (HH:MM:SS) in GMT+7 = ')

#Mengubah inputan menjadi jam, menit, dan detik
hh,mm,ss = map(int,live_time_gmt2.split(":"))
ch,cm,cs = map(int,current_time_gmt7.split(":"))

#Mengubah live time GMT+2 menjadi GMT+7
live_time_gmt2 = hh + 5

#Keterangan batasan waktu event
if ch >= hh:
    print('See you on the next Pear Event!')

#Supaya mudah untuk dibandingkan, kita ubah ke detik
live_time_seconds = (hh + 5) * 3600 + mm * 60 + ss
current_time_seconds =  ch * 3600 + cm * 60 + cs

#Perhitungan lama perbedaan waktu
if live_time_seconds >= current_time_seconds:
    difference_seconds = live_time_seconds - current_time_seconds
else:
    difference_seconds = (24 * 3600) - current_time_seconds + live_time_seconds

#Mengbubah lama perbedaan waktu menjadi jam, menit, dan detik
difference_hours = difference_seconds // 3600
difference_seconds %= 3600
difference_minutes = difference_seconds // 60
difference_seconds %= 60

print('Ali harus menunggu selama', difference_hours,'jam', difference_minutes,'menit', difference_seconds,'detik')