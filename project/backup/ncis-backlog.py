import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

backlog = pd.read_csv('ncis/src/ncis-backlog.csv')

epics = backlog.groupby(by='epic').epic.count()
epic_qty = epics.count()

grouped = backlog.groupby(by=['epic','issue-type']).status.count()
print(grouped.sort_values(['epic','issue-type']))

print(epic_qty)