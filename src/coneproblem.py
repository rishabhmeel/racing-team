#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("cones.csv")

centerx=df["x"].mean()
centery=df["y"].mean()
blue_df= df[df["color"]=='blue'].copy()   
yellow_df= df[df["color"]=='yellow'].copy() 

blue_df["angle"] = np.arctan2(blue_df['y'],blue_df['x'])
yellow_df["angle"] = np.arctan2(yellow_df['y'],yellow_df['x'])

blue_df=blue_df.sort_values(by='angle').reset_index(drop=True).drop(columns='color')
yellow_df=yellow_df.sort_values(by='angle').reset_index(drop=True).drop(columns='color')

red_df = (blue_df+ yellow_df)/2

plt.scatter(centerx,centery,color='red')
plt.scatter(red_df['x'],red_df['y'],color='red')
plt.show()
 
#%%
