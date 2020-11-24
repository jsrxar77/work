import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def transform(input, output, begin_sprint, end_sprint, carry):

    INPUT = input
    OUTPUT = output
    BEGIN_SPRINT = begin_sprint
    END_SPRINT = end_sprint
    CARRY = carry
   
    sprints = pd.read_csv(INPUT)

    sp_added = sprints[["backlog-sprint", "story-points-original"]]
    sp_added = sp_added.fillna(value = {"story-points-original": 0})
    sp_added = sp_added.rename(columns={"backlog-sprint":"sprint", "story-points-original":"sp-added"})
    sp_added = sp_added.set_index("sprint")
    sp_added = sp_added.groupby(by = 'sprint')
    sp_added = sp_added.sum()

    sp_commitment_planning = sprints[[BEGIN_SPRINT, "story-points-original"]]
    sp_commitment_planning = sp_commitment_planning.fillna(value = {"story-points-original": 0})
    sp_commitment_planning = sp_commitment_planning.rename(columns={BEGIN_SPRINT:"sprint", "story-points-original":"sp-commited-planning"})
    sp_commitment_planning = sp_commitment_planning.set_index("sprint")
    sp_commitment_planning = sp_commitment_planning.groupby(by = 'sprint')
    sp_commitment_planning = sp_commitment_planning.sum()

    sp_completed = sprints[[END_SPRINT, "story-points-original",CARRY]]
    sp_completed = sp_completed.where(sp_completed[CARRY] == 0)
    sp_completed = sp_completed[[END_SPRINT, "story-points-original"]]
    sp_completed = sp_completed.fillna(value = {"story-points-original": 0})
    sp_completed = sp_completed.rename(columns={END_SPRINT:"sprint", "story-points-original":"sp-completed"})
    sp_completed = sp_completed.set_index("sprint")
    sp_completed = sp_completed.groupby(by = 'sprint')
    sp_completed = sp_completed.sum()

    sp_completed_from_carries = sprints[[END_SPRINT, "story-points-original",CARRY]]
    sp_completed_from_carries = sp_completed_from_carries.where(sp_completed_from_carries[CARRY] == 1)
    sp_completed_from_carries = sp_completed_from_carries[[END_SPRINT, "story-points-original"]]
    sp_completed_from_carries = sp_completed_from_carries.fillna(value = {"story-points-original": 0})
    sp_completed_from_carries = sp_completed_from_carries.rename(columns={END_SPRINT:"sprint", "story-points-original":"sp-completed-from-carries"})
    sp_completed_from_carries = sp_completed_from_carries.set_index("sprint")
    sp_completed_from_carries = sp_completed_from_carries.groupby(by = 'sprint')
    sp_completed_from_carries = sp_completed_from_carries.sum()

    status = pd.merge(sp_added, sp_commitment_planning, how='outer', on='sprint')
    status = pd.merge(status, sp_completed, how='outer', on='sprint')
    status = pd.merge(status, sp_completed_from_carries, how='outer', on='sprint')
    status = status.fillna(value=0)
    status = status.sort_values(by=['sprint'])

    status.to_csv(OUTPUT,index=True);

# NCIS dev status
transform('ncis/weekly-report/1-10-2020/ncis-sprints-v2.csv', 'ncis/weekly-report/1-10-2020/ncis-dev-status.csv', "dev-begin-sprint", "dev-end-sprint", "dev-carry")

# NCIS qa status
transform('ncis/weekly-report/1-10-2020/ncis-sprints-v2.csv', 'ncis/weekly-report/1-10-2020/ncis-qa-status.csv', "qa-begin-sprint", "qa-end-sprint", "qa-carry")

# LTLCM dev status
# ransform('ncis/weekly-report/1-3-2020/ltlcm-sprints-v2.csv', 'ncis/weekly-report/1-3-2020/ltlcm-dev-status.csv', "dev-begin-sprint", "dev-end-sprint", "dev-carry")

# LTLCM qa status
# transform('ncis/weekly-report/1-3-2020/ltlcm-sprints-v2.csv', 'ncis/weekly-report/1-3-2020/ltlcm-qa-status.csv', "qa-begin-sprint", "qa-end-sprint", "qa-carry")