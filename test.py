text=["Jul 2022 - Present · 1 yr 6 mos","Jul 2022 - Present · 1 yr 6 mos","Jul 2022 - Present · 1 yr 6 mos","Jul 2022 - Present · 1 yr 6 mos"]
year=0
for i in text:
    time=i.split(" · ")[1]

    if len(time)>7:
        yr=time[0]
    year=year+int(yr)

if year>3:
    print("flase")


