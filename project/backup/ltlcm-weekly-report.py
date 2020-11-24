import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sprints = pd.read_csv('ncis/src/ltlcm-sprints.csv')

sp_added = sprints[["backlog-sprint", "story-points-real"]]
sp_added = sp_added.fillna(value = {"story-points-real": 0})
sp_added = sp_added.rename(columns={"backlog-sprint":"sprint", "story-points-real":"sp-added"})
sp_added = sp_added.set_index("sprint")
sp_added = sp_added.groupby(by = 'sprint')
sp_added = sp_added.sum()

sp_commited_dev = sprints[["dev-begin-sprint", "story-points-real"]]
sp_commited_dev = sp_commited_dev.fillna(value = {"story-points-real": 0})
sp_commited_dev = sp_commited_dev.rename(columns={"dev-begin-sprint":"sprint", "story-points-real":"sp-commited-dev"})
sp_commited_dev = sp_commited_dev.set_index("sprint")
sp_commited_dev = sp_commited_dev.groupby(by = 'sprint')
sp_commited_dev = sp_commited_dev.sum()
sp_commited_qa = sprints[["qa-begin-sprint", "story-points-real"]]
sp_commited_qa = sp_commited_qa.fillna(value = {"story-points-real": 0})
sp_commited_qa = sp_commited_qa.rename(columns={"qa-begin-sprint":"sprint", "story-points-real":"sp-commited-qa"})
sp_commited_qa = sp_commited_qa.set_index("sprint")
sp_commited_qa = sp_commited_qa.groupby(by = 'sprint')
sp_commited_qa = sp_commited_qa.sum()

sp_done_dev = sprints[["dev-end-sprint", "story-points-real"]]
sp_done_dev = sp_done_dev.fillna(value = {"story-points-real": 0})
sp_done_dev = sp_done_dev.rename(columns={"dev-end-sprint":"sprint", "story-points-real":"sp-done-dev"})
sp_done_dev = sp_done_dev.set_index("sprint")
sp_done_dev = sp_done_dev.groupby(by = 'sprint')
sp_done_dev = sp_done_dev.sum()
sp_done_qa = sprints[["qa-end-sprint", "story-points-real"]]
sp_done_qa = sp_done_qa.fillna(value = {"story-points-real": 0})
sp_done_qa = sp_done_qa.rename(columns={"qa-end-sprint":"sprint", "story-points-real":"sp-done-qa"})
sp_done_qa = sp_done_qa.set_index("sprint")
sp_done_qa = sp_done_qa.groupby(by = 'sprint')
sp_done_qa = sp_done_qa.sum()

us_burnt_carries_dev = sprints[["dev-end-sprint", "dev-carry"]]
us_burnt_carries_dev = us_burnt_carries_dev.fillna(value = {"dev-carry": 0})
us_burnt_carries_dev = us_burnt_carries_dev.rename(columns={"dev-end-sprint":"sprint", "dev-carry":"us-burnt-carries-dev"})
us_burnt_carries_dev = us_burnt_carries_dev.set_index("sprint")
us_burnt_carries_dev = us_burnt_carries_dev.groupby(by = 'sprint')
us_burnt_carries_dev = us_burnt_carries_dev.count()
us_burnt_carries_qa = sprints[["qa-end-sprint", "qa-carry"]]
us_burnt_carries_qa = us_burnt_carries_qa.fillna(value = {"qa-carry": 0})
us_burnt_carries_qa = us_burnt_carries_qa.rename(columns={"qa-end-sprint":"sprint", "qa-carry":"us-burnt-carries-qa"})
us_burnt_carries_qa = us_burnt_carries_qa.set_index("sprint")
us_burnt_carries_qa = us_burnt_carries_qa.groupby(by = 'sprint')
us_burnt_carries_qa = us_burnt_carries_qa.count()

status = pd.merge(sp_done_dev, us_burnt_carries_dev, how='outer', on='sprint')
status = pd.merge(status, sp_commited_dev, how='outer', on='sprint')
status = pd.merge(status, sp_added, how='outer', on='sprint')
status = pd.merge(status, sp_commited_qa, how='outer', on='sprint')
status = pd.merge(status, sp_done_qa, how='outer', on='sprint')
status = pd.merge(status, us_burnt_carries_qa, how='outer', on='sprint')
status = status.fillna(value=0)
status = status.sort_values(by=['sprint'])

status['sp-total'] =  status['sp-added'].cumsum()
status['sp-burnt-dev'] =  status['sp-done-dev'].cumsum()
status['sp-remain-to-burn-dev'] =  status['sp-total'] - status['sp-burnt-dev']
status['sp-burnt-qa'] =  status['sp-done-qa'].cumsum()
status['sp-remain-to-burn-qa'] =  status['sp-total'] - status['sp-burnt-qa']

dev_status = status[['sp-added','sp-commited-dev','sp-done-dev','us-burnt-carries-dev','sp-burnt-dev','sp-total','sp-remain-to-burn-dev']]
qa_status = status[['sp-added','sp-commited-qa','sp-done-qa','us-burnt-carries-qa','sp-burnt-qa','sp-total','sp-remain-to-burn-qa']]

dev_status.to_csv('ncis/src/ltlcm-dev-status.csv',index=True)
qa_status.to_csv('ncis/src/ltlcm-qa-status.csv',index=True)

print(dev_status)

print(qa_status)