import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from functions import tops, mean_values, max_values, min_values

# ---------------
# main tables for analyze
# ---------------
pd.set_option('display.max_columns', None)
wheat = pd.read_csv('wheat.csv')
barley = pd.read_csv('barley.csv')
leguminous_crops = pd.read_csv('leguminous_crops.csv')
rapeseed = pd.read_csv('rapeseed.csv')
ukraine = pd.read_csv('ukraine.csv')


# ------ WHEAT ------
# 1. Top 10 regions by harvested_area (wheat) and yield on 1ha
top_wheat = tops(wheat, ['harvested_area', 'volume_production', 'yield_1ha'])

biggest_area_wheat = top_wheat['harvested_area']
biggest_production_wheat = top_wheat['volume_production']
biggest_yield_wheat = top_wheat['yield_1ha']

# 2. Statystics indicators (wheat): mean, max, min
mean_wheat = mean_values(wheat)
max_wheat = max_values(wheat)
min_wheat = min_values(wheat)


# ------ Barley ------
# 1. Top 10 regions by harvested_area (barley) and yield on 1ha
top_barley = tops(barley, ['harvested_area', 'volume_production', 'yield_1ha'])

biggest_area_barley = top_barley['harvested_area']
biggest_production_barley = top_barley['volume_production']
biggest_yield_barley = top_barley['yield_1ha']

# 2. Statystics indicators (barley): mean, max, min
mean_barley = mean_values(barley)
max_barley = max_values(barley)
min_barley = min_values(barley)


# ------ Leguminous_crops ------
# 1. Top 10 regions by harvested_area (leguminous_crops) and yield on 1ha
top_leguminous_crops = tops(
    leguminous_crops, ['harvested_area', 'volume_production', 'yield_1ha'])

biggest_area_leguminous_crops = top_leguminous_crops['harvested_area']
biggest_production_leguminous_crops = top_leguminous_crops['volume_production']
biggest_yield_leguminous_crops = top_leguminous_crops['yield_1ha']

# 2. Statystics indicators (leguminous_crops): mean, max, min
mean_leguminous_crops = mean_values(leguminous_crops)
max_leguminous_crops = max_values(leguminous_crops)
min_leguminous_crops = min_values(leguminous_crops)

# ------ Rapeseed ------
# 1. Top 10 regions by harvested_area (rapeseed) and yield on 1ha
top_rapeseed = tops(
    rapeseed, ['harvested_area', 'volume_production', 'yield_1ha'])

biggest_area_rapeseed = top_rapeseed['harvested_area']
biggest_production_rapeseed = top_rapeseed['volume_production']
biggest_yield_rapeseed = top_rapeseed['yield_1ha']

# 2. Statystics indicators (rapeseed): mean, max, min
mean_rapeseed = mean_values(rapeseed)
max_rapeseed = max_values(rapeseed)
min_rapeseed = min_values(rapeseed)


# ----------------------VISUALISATION----------------------------

# Ukraine

plt.figure(figsize=(7, 6), facecolor='lightblue')
plt.pie(ukraine['volume_production'],
        labels=ukraine['culture_name'],
        explode=(0.15, 0, 0, 0, 0),
        autopct='%1.1f%%',
        textprops={'fontsize': 10, 'fontweight': 'bold', 'color': 'black'})
plt.title('The volume of production, yield and the area of agricultural crops collected by their species as of 01 August, 2025',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.legend(ukraine['culture_name'], loc='lower left')
plt.savefig('ukraine_vol_production.png', dpi=300, bbox_inches='tight')
plt.show()


# ===== WHEAT =======


# Wheat: top 10 reg by area
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars = plt.barh(biggest_area_wheat['region'],
                biggest_area_wheat['harvested_area'], zorder=3)
plt.title('Top 10 regions by harvested area (wheat)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('area, thsd.ha')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_pos = biggest_area_wheat['harvested_area'].values.argmax()
bars[max_pos].set_color('orange')
plt.savefig('harvested_area_wheat.png', dpi=300, bbox_inches='tight')
plt.show()


# Dependence between area and production
plt.figure(figsize=(7, 6), facecolor='lightblue')
sns.scatterplot(wheat, x='volume_production',
                y='harvested_area', s=150, zorder=3)
plt.title('Dependence between harvested area and volume production',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.grid(True, 'both', alpha=0.3, zorder=0)
plt.savefig('dependence.png', dpi=300, bbox_inches='tight')
plt.show()


# Wheat: top 10 reg by production
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars_wheat = plt.barh(biggest_production_wheat['region'],
                      biggest_production_wheat['volume_production'], zorder=3)
plt.title('Top 10 regions by volume production (wheat)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('volume of production, thsd. tons')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for wheats in bars_wheat:
    width = wheats.get_width()
    plt.text(width + 0.5, wheats.get_y() + wheats.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_vol_wheat = biggest_production_wheat['volume_production'].values.argmax()
bars_wheat[max_vol_wheat].set_color('orange')
plt.savefig('vol_production_wheat.png', dpi=300, bbox_inches='tight')
plt.show()


# --------BARLEY --------


plt.figure(figsize=(7, 6), facecolor='lightblue')
plt.pie(ukraine['volume_production'],
        labels=ukraine['culture_name'],
        explode=(0.0, 0.15, 0, 0, 0),
        autopct='%1.1f%%',
        textprops={'fontsize': 10, 'fontweight': 'bold', 'color': 'black'})
plt.title('The volume of production, yield and the area of agricultural crops collected by their species as of 01 August, 2025',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.legend(ukraine['culture_name'], loc='lower left')
plt.savefig('barley.png', dpi=300, bbox_inches='tight')
plt.show()

# Barley top_harvest_area
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars = plt.barh(biggest_area_barley['region'],
                biggest_area_barley['harvested_area'], zorder=3)
plt.title('Top 10 regions by harvested area (barley)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('area, thsd.ha')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for barley in bars:
    width = barley.get_width()
    plt.text(width + 0.5, barley.get_y() + barley.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_barl_ar = biggest_area_barley['harvested_area'].values.argmax()
bars[max_barl_ar].set_color('yellow')
plt.savefig('harvested_area_barley.png', dpi=300, bbox_inches='tight')
plt.show()


# Barley top_volume_production
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars_barley = plt.barh(biggest_production_barley['region'],
                       biggest_production_barley['volume_production'], zorder=3)
plt.title('Top 10 regions by volume production (barley)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('volume of production, thsd. tons')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for barleys in bars_barley:
    width = barleys.get_width()
    plt.text(width + 0.5, barleys.get_y() + barleys.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_vol_barley = biggest_production_barley['volume_production'].values.argmax()
bars_barley[max_vol_barley].set_color('yellow')
plt.savefig('vol_production_barley.png', dpi=300, bbox_inches='tight')
plt.show()

# ======RAPESEED======

# Rapeseed Ukraine
plt.figure(figsize=(7, 6), facecolor='lightblue')
plt.pie(ukraine['volume_production'],
        labels=ukraine['culture_name'],
        explode=(0.0, 0, 0, 0.15, 0),
        autopct='%1.1f%%',
        textprops={'fontsize': 10, 'fontweight': 'bold', 'color': 'black'})
plt.title('The volume of production, yield and the area of agricultural crops collected by their species as of 01 August, 2025',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.legend(ukraine['culture_name'], loc='lower left')
plt.savefig('ukraine_rapeseed.png', dpi=300, bbox_inches='tight')
plt.show()


# RAPESEEDS top-10 area
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars = plt.barh(biggest_area_rapeseed['region'],
                biggest_area_rapeseed['harvested_area'], zorder=3)
plt.title('Top 10 regions by harvested area (rapeseed)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('area, thsd.ha')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for rapeseed in bars:
    width = rapeseed.get_width()
    plt.text(width + 0.5, rapeseed.get_y() + rapeseed.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_barl_ar = biggest_area_rapeseed['harvested_area'].values.argmax()
bars[max_barl_ar].set_color('red')
plt.savefig('harvested_area_rapeseed.png', dpi=300, bbox_inches='tight')
plt.show()


# Rapeseed top-10 volume production
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars_rapeseed = plt.barh(biggest_production_rapeseed['region'],
                         biggest_production_rapeseed['volume_production'], zorder=3)
plt.title('Top 10 regions by volume production (rapeseed)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('volume of production, thsd. tons')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for rapeseeds in bars_rapeseed:
    width = rapeseeds.get_width()
    plt.text(width + 0.5, rapeseeds.get_y() + rapeseeds.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_vol_rapeseed = biggest_production_rapeseed['volume_production'].values.argmax(
)
bars_rapeseed[max_vol_rapeseed].set_color('red')
plt.savefig('vol_production_rapeseed.png', dpi=300, bbox_inches='tight')
plt.show()


# ========= Leguminous crops =============

# Leguminous crops top-10 area
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars = plt.barh(biggest_area_leguminous_crops['region'],
                biggest_area_leguminous_crops['harvested_area'], zorder=3)
plt.title('Top 10 regions by harvested area (leguminous_crops)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('area, thsd.ha')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for leguminous_crops in bars:
    width = leguminous_crops.get_width()
    plt.text(width + 0.5, leguminous_crops.get_y() + leguminous_crops.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_barl_ar = biggest_area_leguminous_crops['harvested_area'].values.argmax()
bars[max_barl_ar].set_color('green')
plt.savefig('harvested_area_leguminous_crops.png',
            dpi=300, bbox_inches='tight')
plt.show()


# leguminous_crops top-10 volume production
plt.figure(figsize=(14, 6), facecolor='lightblue')
bars_leguminous_crops = plt.barh(biggest_production_leguminous_crops['region'],
                                 biggest_production_leguminous_crops['volume_production'], zorder=3)
plt.title('Top 10 regions by volume production (leguminous_crops)',
          fontsize=14,
          fontweight='bold',
          wrap=True)
plt.xlabel('volume of production, thsd. tons')
plt.grid(True, 'both', alpha=0.3, zorder=0)
for leguminous_cropss in bars_leguminous_crops:
    width = leguminous_cropss.get_width()
    plt.text(width + 0.5, leguminous_cropss.get_y() + leguminous_cropss.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=12, fontweight='bold')
plt.gca().invert_yaxis()
max_vol_leguminous_crops = biggest_production_leguminous_crops['volume_production'].values.argmax(
)
bars_leguminous_crops[max_vol_leguminous_crops].set_color('green')
plt.savefig('vol_production_leguminous_crops.png',
            dpi=300, bbox_inches='tight')
plt.show()
