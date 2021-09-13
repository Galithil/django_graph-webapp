import os
import csv
from statistics import mean
from django.conf import settings




def parse_ophtalmo():
    my_colors = ['#DA4DFE', '#2F8CFC', '#51FE48', '#E8FE48', '#FED14D', '#C14242']
    legend_sorted = ["> 180 jours", "< 180 jours", "< 60 jours", "< 30 jours", "< 14 jours", "< 7 jours"]
    colors = {}
    context = {}
    cities_times = {}
    key_tag = "Ville"
    value_tag = "Delai rendez-vous"
    with open(os.path.join(settings.DATA_DIRS['DATAVIEW'], "Delai_rdv_ophtalmos_2012.csv")) as csvfile :
        reader = csv.DictReader(csvfile, delimiter=',')
        for line in reader:
            reworked_key = "{}{}".format(line[key_tag][0],line[key_tag][1:].lower())
            try:
                cities_times[reworked_key].append(int(line[value_tag]))

            except KeyError:
                cities_times[reworked_key] = [int(line[value_tag])]

    for key in cities_times:
        values = cities_times[key]
        mean_v = mean(values)
        cities_times[key] = "{:.2f}".format(mean_v)
        if mean_v < 7:
            colors[key] = my_colors[0]
        elif mean_v < 14:
            colors[key] = my_colors[1]
        elif mean_v < 30:
            colors[key] = my_colors[2]
        elif mean_v < 60:
            colors[key] = my_colors[3]
        elif mean_v < 180:
            colors[key] = my_colors[4]
        else:
            colors[key] = my_colors[5]

    context["city_times"] = cities_times
    context["cities"] = sorted(cities_times.keys())
    context["cities_str"] = "[{}]".format(",".join(sorted(["'{}'".format(x) for x in cities_times.keys()])))
    context["times_sorted_str"] = "[{}]".format(",".join([cities_times[val] for val in context["cities"]]))
    context["colors_sorted"] = ["'{}'".format(colors[val]) for val in context["cities"]]
    context["colors_sorted_str"] = "[{}]".format(",".join(["'{}'".format(colors[val]) for val in context["cities"]]))
    context["legend_colors"] = my_colors
    context["legend_reversed"] = legend_sorted


    return context







