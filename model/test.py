import pandas as pd

# pointdf = pd.read_csv('gps_points_master.csv')
# tmp = (pointdf['latitude'] > 90.0 )| (pointdf['latitude'] < -90.0 )
# pointdf = pointdf[~tmp]
# pointdf.to_csv('gps_points_master.csv', index=False)

segmentdf = pd.read_csv('segment_master.csv')
print(segmentdf.loc[564545])
print(len(segmentdf))
segmentdf= segmentdf.drop([564545])
print(len(segmentdf))
# tmp = (segmentdf['latitude'] > 90.0 )| (segmentdf['latitude'] < -90.0 )
# segmentdf = segmentdf[~tmp]
segmentdf.to_csv('segment_master.csv', index=False)