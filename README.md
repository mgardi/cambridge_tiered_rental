# cambridge_tiered_rental
development on Cambridge, MD tiered rental PoC 

Build violatuions data from latest City data set 

1. Run SDAT-etl on a monthly or quarterly basis to get latest sales and assetment data
    Creates lates sdat-can-ref file used in later notebooks
    be sure output_fn = '_output/SDAT-CAN-ref-072021_src_sdat_etl.csv' matches filename read into later notebooks
2. Run violations-etl to get latest code violations data 
creates 'violation_clusters.csv'

3. ?
4. Base_scoring 
Requres 'violation_clusters.csv'


