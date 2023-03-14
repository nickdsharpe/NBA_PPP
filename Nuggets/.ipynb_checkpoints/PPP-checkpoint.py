import pandas as pd
import time
import numpy as np


def PPP(data):
    
    timeStart = time.time()
    
    #Grab the column headers
    headers = data.columns
    
    # Create the Overall PNR column
    PNRData = data.iloc[:,:5]
    
    # Assign PNR variables
    PNRshoot2FGA = PNRData.loc['shoot2FGA'].sum().sum()
    PNRshoot2FGM = PNRData.loc['shoot2FGM'].sum().sum()
    PNRshoot2FTA = PNRData.loc['shoot2FTA'].sum().sum()
    PNRshoot2FTM = PNRData.loc['shoot2FTM'].sum().sum()
    PNRshoot2TO = PNRData.loc['shoot2TO'].sum().sum()
    PNRshoot3FGA = PNRData.loc['shoot3FGA'].sum().sum()
    PNRshoot3FGM = PNRData.loc['shoot3FGM'].sum().sum()
    PNRshoot3FTA = PNRData.loc['shoot3FTA'].sum().sum()
    PNRshoot3FTM = PNRData.loc['shoot3FTM'].sum().sum()
    PNRshoot3TO = PNRData.loc['shoot3TO'].sum().sum()
    
    PNRpass2FGA = PNRData.loc['pass2FGA'].sum().sum()
    PNRpass2FGM = PNRData.loc['pass2FGM'].sum().sum()
    PNRpass2FTA = PNRData.loc['pass2FTA'].sum().sum()
    PNRpass2FTM = PNRData.loc['pass2FTM'].sum().sum()
    PNRpass2TO = PNRData.loc['pass2TO'].sum().sum()
    PNRpass3FGA = PNRData.loc['pass3FGA'].sum().sum()
    PNRpass3FGM = PNRData.loc['pass3FGM'].sum().sum()
    PNRpass3FTA = PNRData.loc['pass3FTA'].sum().sum()
    PNRpass3FTM = PNRData.loc['pass3FTM'].sum().sum()
    PNRpass3TO = PNRData.loc['pass3TO'].sum().sum()
    
    PNRFGA2 = PNRpass2FGA + PNRshoot2FGA
    PNRFGM2 = PNRpass2FGM + PNRshoot2FGM
    PNRFTA2 = PNRpass2FTA + PNRshoot2FTA
    PNRFTM2 = PNRpass2FTM + PNRshoot2FTM
    PNRTO2 = PNRpass2TO + PNRshoot2TO
    PNRFGA3 = PNRpass3FGA + PNRshoot3FGA
    PNRFGM3 = PNRpass3FGM + PNRshoot3FGM
    PNRFTA3 = PNRpass3FTA + PNRshoot3FTA
    PNRFTM3 = PNRpass3FTM + PNRshoot3FTM
    PNRTO3 = PNRpass3TO + PNRshoot3TO
    
    
    
    # Assign shooting data to new variables
    shoot2FGA = data.loc['shoot2FGA'].sum().sum()
    shoot2FGM = data.loc['shoot2FGM'].sum().sum()
    shoot2FTA = data.loc['shoot2FTA'].sum().sum()
    shoot2FTM = data.loc['shoot2FTM'].sum().sum()
    shoot2TO = data.loc['shoot2TO'].sum().sum()
    shoot3FGA = data.loc['shoot3FGA'].sum().sum()
    shoot3FGM = data.loc['shoot3FGM'].sum().sum()
    shoot3FTA = data.loc['shoot3FTA'].sum().sum()
    shoot3FTM = data.loc['shoot3FTM'].sum().sum()
    shoot3TO = data.loc['shoot3TO'].sum().sum()
    
    # Assign passing data to new variables
    pass2FGA = data.loc['pass2FGA'].sum().sum()
    pass2FGM = data.loc['pass2FGM'].sum().sum()
    pass2FTA = data.loc['pass2FTA'].sum().sum()
    pass2FTM = data.loc['pass2FTM'].sum().sum()
    pass2TO = data.loc['pass2TO'].sum().sum()
    pass3FGA = data.loc['pass3FGA'].sum().sum()
    pass3FGM = data.loc['pass3FGM'].sum().sum()
    pass3FTA = data.loc['pass3FTA'].sum().sum()
    pass3FTM = data.loc['pass3FTM'].sum().sum()
    pass3TO = data.loc['pass3TO'].sum().sum()
    
    # Create Overall data variables
    FGA2 = pass2FGA + shoot2FGA
    FGM2 = pass2FGM + shoot2FGM
    FTA2 = pass2FTA + shoot2FTA
    FTM2 = pass2FTM + shoot2FTM
    TO2 = pass2TO + shoot2TO
    FGA3 = pass3FGA + shoot3FGA
    FGM3 = pass3FGM + shoot3FGM
    FTA3 = pass3FTA + shoot3FTA
    FTM3 = pass3FTM + shoot3FTM
    TO3 = pass3TO + shoot3TO
    
    # Calculate shooting, passing, and total Points per Possesion
    shootingPPP_tot = round(((shoot2FGM * 2) + (shoot3FGM * 3) + (shoot2FTM + shoot3FTM)) / ((shoot2FGA + shoot3FGA) + ((shoot2FTA + shoot3FTA) * 0.44) + (shoot2TO + shoot3TO)),2)
    shootingPPP_2pt = round(((shoot2FGM * 2) + shoot2FTM) / (shoot2FGA + (shoot2FTA * 0.44) + shoot2TO),2)
    shootingPPP_3pt = round(((shoot3FGM * 3) + shoot3FTM) / (shoot3FGA + (shoot3FTA * 0.44) + shoot3TO),2)
    passingPPP_tot = round(((pass2FGM * 2) + (pass3FGM * 3) + (pass2FTM + pass3FTM)) / ((pass2FGA + pass3FGA) + ((pass2FTA + pass3FTA) * 0.44) + (pass2TO + pass3TO)),2)
    passingPPP_2pt = round(((pass2FGM * 2) + pass2FTM) / (pass2FGA + (pass2FTA * 0.44) + pass2TO),2)
    passingPPP_3pt = round(((pass3FGM * 3) + pass3FTM) / (pass3FGA + (pass3FTA * 0.44) + pass3TO),2)
    ppp_2pt = round((((shoot2FGM + pass2FGM)* 2) + (shoot2FTM + pass2FTM)) / ((shoot2FGA + pass2FGA) + (0.44 *  (shoot2FTA + pass2FTA)) + (shoot2TO + pass2TO)),2)
    ppp_3pt = round((((shoot3FGM + pass3FGM) * 3) + (shoot3FTM + pass3FTM)) / ((shoot3FGA + pass3FGA) + (0.44 * (shoot3FTA + pass3FTA)) + (shoot3TO + pass3TO)),2)
    ppp_tot = round(((FGM2 * 2) + (FGM3 * 3) + (FTM2 + FTM3)) / ((FGA2 + FGA3) + ((FTA2 + FTA3) * 0.44) + (TO2 + TO3)),2)
    
    # Calculate Possesion totals
    shootPoss_totOVR = int((shoot2FGA + (0.44*(shoot2FTA + shoot3FTA)) + shoot2TO + shoot3FGA + shoot3TO))
    shootPoss_2pt = int((shoot2FGA + (0.44 * shoot2FTA) + shoot2TO))
    shootPoss_3pt = int((shoot3FGA + (0.44 * shoot3FTA) + shoot3TO))
    passingPoss_totOVR = int((pass2FGA + (0.44*(pass2FTA + pass3FTA)) + pass2TO + pass3FGA + pass3TO))
    passingPoss_2pt = int((pass2FGA + (.044 * pass2FTA) + pass2TO))
    passingPoss_3pt = int((pass3FGA + (0.44 * pass3FTA) + pass3TO))
    totPossOVR = (shootPoss_totOVR + passingPoss_totOVR)
    totPoss_2ptOVR = (shootPoss_2pt + passingPoss_2pt)
    totPoss_3ptOVR = (shootPoss_3pt + passingPoss_3pt)  
    
    # Sum up field foal attempts
    tot3FGA = shoot3FGA + pass3FGA
    tot2FGA = shoot2FGA + pass2FGA
    passFGA = pass2FGA + pass3FGA
    shootFGA = shoot2FGA + shoot3FGA
    totFGA = shoot2FGA + pass2FGA + shoot3FGA + pass3FGA
    
    # Calculate possesion percentage and shooting percentage for overall stats, assign 'N/A' if no data exists
    try:
        shootPoss_perOVR = str(round(((shootPoss_totOVR / totPossOVR)*100),1)) + '%'
    except(ZeroDivisionError):
        shootPoss_perOVR = 'N/A'
    
    try:
        passingPoss_perOVR = str(round(((passingPoss_totOVR / totPossOVR)*100),1)) + '%'
    except(ZeroDivisionError):
        passingPoss_perOVR = 'N/A'
        
    try:
        totFG_per = str(round(((shoot2FGM + shoot3FGM + pass2FGM + pass3FGM) / (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA)* 100),1)) + '%'
    except(ZeroDivisionError):
        totFG_per = 'N/A'
        
    try:
        shootFG_per = str(round((((shoot2FGM + shoot3FGM) / (shoot2FGA + shoot3FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        shootFG_per = 'N/A'
        
    try:
        passFG_per = str(round((((pass2FGM + pass3FGM) / (pass2FGA + pass3FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        passFG_per = 'N/A'
        
    try:
        tot2FG_per = str(round((((pass2FGM + shoot2FGM) / (pass2FGA + shoot2FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        tot2FG_per = 'N/A'
        
    try:
        tot3FG_per = str(round((((pass3FGM + shoot3FGM) / (pass3FGA + shoot3FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        tot3FG_per = 'N/A'
        
    try:
        shoot2FG_per = str(round((((shoot2FGM) / (shoot2FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        shoot2FG_per = 'N/A'
    
    
    try:
        if shoot3FGA == 0:  
            shoot3FG_per = 'N/A'
        else:
            shoot3FG_per = str(round((((shoot3FGM) / (shoot3FGA))* 100), 1)) + "%"
    except:
        shoot3FG_per = 'N/A'
        
    try:
        pass2FG_per = str(round((((pass2FGM) / (pass2FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        pass2FG_per = 'N/A'
        
    try:
        pass3FG_per = str(round((((pass3FGM) / (pass3FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        pass3FG_per = 'N/A'
        
    # Calculate PNR possession totals
    PNRshootPoss_totOVR = int((PNRshoot2FGA + (0.44 * (PNRshoot2FTA + PNRshoot3FTA)) + PNRshoot2TO + PNRshoot3FGA + PNRshoot3TO))
    PNRshootPoss_2pt = int((PNRshoot2FGA + (0.44 *PNRshoot2FTA) + PNRshoot2TO))
    PNRshootPoss_3pt = int((PNRshoot3FGA + (0.44 * PNRshoot3FTA) + PNRshoot3TO))
    PNRpassingPoss_totOVR = int((PNRpass2FGA + (0.44 * (PNRpass2FTA + PNRpass3FTA)) + PNRpass2TO + PNRpass3FGA + PNRpass3TO))
    PNRpassingPoss_2pt = (PNRpass2FGA + PNRpass2FTA + PNRpass2TO)
    PNRpassingPoss_3pt = (PNRpass3FGA + PNRpass3FTA + PNRpass3TO)
    PNRtotPossOVR = (PNRshootPoss_totOVR + PNRpassingPoss_totOVR)
    PNRtotPoss_2ptOVR = (PNRshootPoss_2pt + PNRpassingPoss_2pt)
    PNRtotPoss_3ptOVR = (PNRshootPoss_3pt + PNRpassingPoss_3pt) 
    
    # Calculate PNR shooting, passing, and total PPP
    try:
        if PNRshootPoss_totOVR == 0:
            PNRshootingPPP_tot = 'N/A'
        else:
            PNRshootingPPP_tot = round(((PNRshoot2FGM * 2) + (PNRshoot3FGM * 3) + (PNRshoot2FTM + PNRshoot3FTM)) / (PNRshootPoss_totOVR),2)
    except:
        PNRshootingPPP_tot = 'N/A'
    
    try:
        if PNRshootPoss_2pt == 0:
            PNRshootingPPP_2pt = 'N/A'
        else:
            PNRshootingPPP_2pt = round(((PNRshoot2FGM * 2) + PNRshoot2FTM) / (PNRshootPoss_2pt),2)
    except:
        PNRshootingPPP_2pt = 'N/A'
    
    try:
        if PNRshootPoss_3pt == 0:
            PNRshootingPPP_3pt = 'N/A'
        else:
            PNRshootingPPP_3pt = round(((PNRshoot3FGM * 3) + PNRshoot3FTM) / (PNRshootPoss_3pt),2)
    except:
        PNRshootingPPP_3pt = 'N/A'

    
    try:
        if PNRpassingPoss_totOVR == 0:
            PNRpassingPPP_tot = 'N/A'
        else:
            PNRpassingPPP_tot = round(((PNRpass2FGM * 2) + (PNRpass3FGM * 3) + (PNRpass2FTM + PNRpass3FTM)) / (PNRpassingPoss_totOVR))
    except:
        PNRpassingPPP_tot = 'N/A'
    
    try:
        if PNRpassingPoss_2pt == 0:
            PNRpassingPPP_2pt = 'N/A'
        else:
            PNRpassingPPP_2pt = round(((PNRpass2FGM * 2) + PNRpass2FTM) / (PNRpassingPoss_2pt),2)
    except:
            PNRpassingPPP_2pt = 'N/A'
    
    try:
        if PNRtotPoss_3ptOVR == 0:
            PNRpassingPPP_3pt = 'N/A'
        else:
            PNRpassingPPP_3pt = round(((PNRpass3FGM * 3) + PNRpass3FTM) / (PNRtotPoss_3ptOVR),2)
    except:
        PNRpassingPPP_3pt = 'N/A'
        
    try:
        if PNRtotPoss_2ptOVR == 0:
            PNRppp_2pt = 'N/A'
        else:
            PNRppp_2pt = round((((PNRshoot2FGM + PNRpass2FGM)* 2) + (PNRshoot2FTM + PNRpass2FTM)) / (PNRtotPoss_2ptOVR),2)
    except:
        PNRppp_2pt = 'N/A'
        
    try:
        if PNRtotPoss_3ptOVR == 0:
            PNRppp_3pt = 'N/A'
        else:
            PNRppp_3pt = round((((PNRshoot3FGM + PNRpass3FGM) * 3) + (PNRshoot3FTM + PNRpass3FTM)) / (PNRtotPoss_3ptOVR),2)
    except:
        PNRppp_3pt = 'N/A'
        
    try:
        if PNRtotPossOVR == 0:
            PNRppp_tot = 'N/A'
        else:
            PNRppp_tot = round(((PNRFGM2 * 2) + (PNRFGM3 * 3) + (PNRFTM2 + PNRFTM3)) / (PNRtotPossOVR),2)
    except:
        PNRppp_tot = 'N/A'
    
    # Sum up PNR field goal attempts
    PNRtot3FGA = PNRshoot3FGA + PNRpass3FGA
    PNRtot2FGA = PNRshoot2FGA + PNRpass2FGA
    PNRpassFGA = PNRpass2FGA + PNRpass3FGA
    PNRshootFGA = PNRshoot2FGA + PNRshoot3FGA
    PNRtotFGA = PNRshoot2FGA + PNRpass2FGA + PNRshoot3FGA + PNRpass3FGA
    
    # Calculate PNR possession percentages and shooting percentages. assign 'N/A' if no data exists
    try:
        PNRshootPoss_perOVR = str(round(((PNRshootPoss_totOVR / PNRtotPossOVR)*100),1)) + '%'
    except(ZeroDivisionError):
        PNRshootPoss_perOVR = 'N/A'
        
    try:
        PNRpassingPoss_perOVR = str(round(((PNRpassingPoss_totOVR / PNRtotPossOVR)*100),1)) + '%'
    except(ZeroDivisionError):
        PNRpassingPoss_perOVR = 'N/A'
        
    try:
        PNRtotFG_per = str(round(((PNRshoot2FGM + PNRshoot3FGM + PNRpass2FGM + PNRpass3FGM) / (PNRshoot2FGA + PNRpass2FGA + PNRshoot3FGA + PNRpass3FGA)* 100),1)) + '%'
    except(ZeroDivisionError):
        PNRtotFG_per = 'N/A'
        
    try:
        PNRshootFG_per = str(round((((PNRshoot2FGM + PNRshoot3FGM) / (PNRshoot2FGA + PNRshoot3FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        PNRshootFG_per = 'N/A'
        
    try:
        if PNRpassFGA == 0:
            PNRpassFG_per = 'N/A'
        else:
            PNRpassFG_per = str(round((((PNRpass2FGM + PNRpass3FGM) / (PNRpassFGA))*100),1)) + '%'
    except:
        PNRpassFG_per = 'N/A'
        
    try:
        PNRtot2FG_per = str(round((((PNRpass2FGM + PNRshoot2FGM) / (PNRpass2FGA + PNRshoot2FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        PNRtot2FG_per = 'N/A'
        
    try:
        PNRtot3FG_per = str(round((((PNRpass3FGM + PNRshoot3FGM) / (PNRpass3FGA + PNRshoot3FGA))*100),1)) + '%'
    except(ZeroDivisionError):
        PNRtot3FG_per = 'N/A'
    
    try:
        PNRshoot2FG_per = str(round((((PNRshoot2FGM) / (PNRshoot2FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        PNRshoot2FG_per = 'N/A'
        
    try:
        if PNRshoot3FGA == 0:
            PNRshoot3FG_per = 'N/A'
        else:
            PNRshoot3FG_per = str(round((((PNRshoot3FGM) / (PNRshoot3FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        PNRshoot3FG_per = 'N/A'
    
    try:
        if PNRpass2FGA == 0:
            PNRpass2FG_per = 'N/A'
        else:
            PNRpass2FG_per = str(round((((PNRpass2FGM) / (PNRpass2FGA))* 100), 1)) + '%'
    except:
        PNRpass2FG_per = 'N/A'
        
    try:
        if PNRpass3FGA == 0:
            PNRpass3FG_per = 'N/A'
        else:
            PNRpass3FG_per = str(round((((PNRpass3FGM) / (PNRpass3FGA))* 100), 1)) + '%'
    except(ZeroDivisionError):
        PNRpass3FG_per = 'N/A'
        
    try:
        PNRtotPoss = (PNRshootPoss_totOVR + PNRpassingPoss_totOVR)
    except(ZeroDivisionError):
        PNRtotPoss = 'N/A'
        
    try:
        PNRtotPoss_per = str(round(((PNRtotPoss / totPossOVR)*100),1)) + '%'
    except(ZeroDivisionError):
        PNRtotPoss_per = 'N/A'
    
    # Calculate turnovers an turnover percentage
    total_to = TO2 + TO3
    pnr_to = PNRTO2 + PNRTO3
    total_to_per = str(round((((total_to * 100) / totPossOVR)),1)) + '%'
    
    # Create the index
    index = ['Total PPP', '% of Poss.', 'Total TO', 'Total FG%', 
             'Shooting PPP', '% of Shooting Poss.', 'Shooting FG%', 'Shooting 2pt Att.', 'Shooting 2pt FG%', 'Shooting 3pt Att.', 'Shooting 3pt FG%',
             'Passing PPP', '% of Passing Poss.', 'Passing FG%', 'Passing 2pt Att.', 'Passing 2pt FG%', 'Passing 3pt Att.', 'Passing 3pt FG%']   
    
    # Create the PPP DataFrame
    data_df = pd.DataFrame(columns=headers, index=index)
    
    # Create 'PNR' column using PNR data
    data_df['PNR'] = [str(PNRppp_tot), (str(PNRtotPoss_per)), pnr_to, (str(PNRtotFG_per)), 
                        str(PNRshootingPPP_tot), str(PNRshootPoss_perOVR), str(PNRshootFG_per), str(PNRshoot2FGA), str(PNRshoot2FG_per), str(PNRshoot3FGA), str(PNRshoot3FG_per),
                        str(PNRpassingPPP_tot), str(PNRpassingPoss_perOVR), str(PNRpassFG_per), str(PNRpass2FGA), str(PNRpass2FG_per), str(PNRpass3FGA), str(PNRpass3FG_per)]
    
    #Create the 'TOTAL' column at the end of the dataframe
    data_df['TOTAL'] = [str(ppp_tot), (str(totPossOVR)), total_to_per, (str(totFG_per)), 
                        str(shootingPPP_tot), str(shootPoss_perOVR), str(shootFG_per), str(shoot2FGA), str(shoot2FG_per), str(shoot3FGA), str(shoot3FG_per),
                        str(passingPPP_tot), str(passingPoss_perOVR), str(passFG_per), str(pass2FGA), str(pass2FG_per), str(pass3FGA), str(pass3FG_per)]
    
    # Create dictionary for each column
    col_dicts = {col_name: data[col_name].to_dict() for col_name in data.columns}
    
    # Loop over each column dictionary to create new calculated column
    for i, col_dict in col_dicts.items():
        
        shoot2FGA = col_dict['shoot2FGA']
        shoot2FGM = col_dict['shoot2FGM']
        shoot2FTA = col_dict['shoot2FTA']
        shoot2FTM = col_dict['shoot2FTM']
        shoot2TO = col_dict['shoot2TO']
        shoot3FGA = col_dict['shoot3FGA']
        shoot3FGM = col_dict['shoot3FGM']
        shoot3FTA = col_dict['shoot3FTA']
        shoot3FTM = col_dict['shoot3FTM']
        shoot3TO = col_dict['shoot3TO']

        pass2FGA = col_dict['pass2FGA']
        pass2FGM = col_dict['pass2FGM']
        pass2FTA = col_dict['pass2FTA']
        pass2FTM = col_dict['pass2FTM']
        pass2TO = col_dict['pass2TO']
        pass3FGA = col_dict['pass3FGA']
        pass3FGM = col_dict['pass3FGM']
        pass3FTA = col_dict['pass3FTA']
        pass3FTM = col_dict['pass3FTM']
        pass3TO = col_dict['pass3TO']

        FGA2 = pass2FGA + shoot2FGA
        FGM2 = pass2FGM + shoot2FGM
        FTA2 = pass2FTA + shoot2FTA
        FTM2 = pass2FTM + shoot2FTM
        TO2 = pass2TO + shoot2TO
        FGA3 = pass3FGA + shoot3FGA
        FGM3 = pass3FGM + shoot3FGM
        FTA3 = pass3FTA + shoot3FTA
        FTM3 = pass3FTM + shoot3FTM
        TO3 = pass3TO + shoot3TO
        
        total_to = TO2 + TO3
        
        try:
            shootingPPP_tot = round(((shoot2FGM * 2) + (shoot3FGM * 3) + (shoot2FTM + shoot3FTM)) / ((shoot2FGA + shoot3FGA) + ((shoot2FTA + shoot3FTA) * 0.44) + (shoot2TO + shoot3TO)),2)
        except(ZeroDivisionError):
            shootingPPP_tot = 'N/A'
            
        try:
            shootingPPP_2pt = round(((shoot2FGM * 2) + shoot2FTM) / (shoot2FGA + (shoot2FTA * 0.44) + shoot2TO),2)
        except(ZeroDivisionError):
            shootingPPP_2pt = 'N/A'
            
        try:
            shootingPPP_3pt = round(((shoot3FGM * 3) + shoot3FTM) / (shoot3FGA + (shoot3FTA * 0.44) + shoot3TO),2)
        except(ZeroDivisionError):
            shootingPPP_3pt = 'N/A'
        
        
        shootPoss_tot = shoot2FGA + (0.44*(shoot2FTA + shoot3FTA)) + shoot2TO + shoot3FGA + shoot3TO
        try:
            shootPoss_per = str(round(((shootPoss_tot / shootPoss_totOVR)*100),1)) + '%'
        except(ZeroDivisionError):
            shootPoss_per = 'N/A'
            
        shootPoss_2pt = (shoot2FGA + shoot2FTA + shoot2TO)
        shootPoss_3pt = (shoot3FGA + shoot3FTA + shoot3TO)
        shootFGA = shoot2FGA + shoot3FGA
            
        try:
            shootFG_per = str(round((((shoot2FGM + shoot3FGM) / (shoot2FGA + shoot3FGA))*100),1)) + '%'
        except(ZeroDivisionError):
            shootFG_per = 'N/A'
            
        try:
            shoot2FG_per = str(round((((shoot2FGM) / (shoot2FGA))* 100), 1)) + '%'
        except(ZeroDivisionError):
            shoot2FG_per = 'N/A'
            
        try:
            shoot3FG_per = str(round((((shoot3FGM) / (shoot3FGA))* 100), 1)) + '%'
        except(ZeroDivisionError):
            shoot3FG_per = 'N/A'

        try:
            passingPPP_tot = round(((pass2FGM * 2) + (pass3FGM * 3) + (pass2FTM + pass3FTM)) / ((pass2FGA + pass3FGA) + ((pass2FTA + pass3FTA) * 0.44) + (pass2TO + pass3TO)),2)
        except(ZeroDivisionError):
            passingPPP_tot = 'N/A'
            
        try:
            passingPPP_2pt = round(((pass2FGM * 2) + pass2FTM) / (pass2FGA + (pass2FTA * 0.44) + pass2TO),2)
        except(ZeroDivisionError):
            passingPPP_2pt = 'N/A'
            
        try:
            passingPPP_3pt = round(((pass3FGM * 3) + pass3FTM) / (pass3FGA + (pass3FTA * 0.44) + pass3TO),2)
        except(ZeroDivisionError):
            passingPPP_3pt = 'N/A'
            
        passingPoss_tot =  pass2FGA + (0.44*(pass2FTA + pass3FTA)) + pass2TO + pass3FGA + pass3TO
        try:
            passingPoss_per = str(round(((passingPoss_tot / passingPoss_totOVR)*100),1)) + '%'
        except(ZeroDivisionError):
            passingPoss_per = 'N/A'
        
        passingPoss_2pt = (pass2FGA + pass2FTA + pass2TO)
        passingPoss_3pt = (pass3FGA + pass3FTA + pass3TO)
        passFGA = (pass2FGA + pass3FGA)
            
        try:
            passFG_per = str(round((((pass2FGM + pass3FGM) / (pass2FGA + pass3FGA))*100),1)) + '%'
        except(ZeroDivisionError):
            passFG_per = 'N/A'
            
        try:
            pass2FG_per = str(round((((pass2FGM) / (pass2FGA))* 100), 1)) + '%'
        except(ZeroDivisionError):
            pass2FG_per = 'N/A'
            
        try:
            pass3FG_per = str(round((((pass3FGM) / (pass3FGA))* 100), 1)) + '%'
        except(ZeroDivisionError):
            pass3FG_per = 'N/A'
        
        try:
            ppp_2pt = round((((shoot2FGM + pass2FGM)* 2) + (shoot2FTM + pass2FTM)) / ((shoot2FGA + pass2FGA) + (0.44 *  (shoot2FTA + pass2FTA)) + (shoot2TO + pass2TO)),2)
        except(ZeroDivisionError):
            ppp_2pt = 'N/A'
        
        try:
            ppp_3pt = round((((shoot3FGM + pass3FGM) * 3) + (shoot3FTM + pass3FTM)) / ((shoot3FGA + pass3FGA) + (0.44 * (shoot3FTA + pass3FTA)) + (shoot3TO + pass3TO)),2)
        except(ZeroDivisionError):
            ppp_3pt = 'N/A'
            
        try:
            ppp_tot = round(((FGM2 * 2) + (FGM3 * 3) + (FTM2 + FTM3)) / ((FGA2 + FGA3) + ((FTA2 + FTA3) * 0.44) + (TO2 + TO3)),2)
        except(ZeroDivisionError):
            ppp_tot = 'N/A'
        
        totPoss = (shootPoss_tot + passingPoss_tot)
            
        try:
            totPoss_per = str(round(((totPoss / totPossOVR)*100),1)) + '%'
        except(ZeroDivisionError):
            totPoss_per = 'N/A'
            
        totPoss_2pt = (shootPoss_2pt + passingPoss_2pt)
        totPoss_3pt = (shootPoss_3pt + passingPoss_3pt) 
        totFGA = (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA)
        
        try: 
            totFG_per = str(round((((shoot2FGM + shoot3FGM + pass2FGM + pass3FGM) / (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA))* 100),1)) + '%'
        except(ZeroDivisionError):
            totFG_per = 'N/A'
            
        tot2FGA = shoot2FGA + pass2FGA
        try:
            tot2FG_per = str(round((((pass2FGM + shoot2FGM) / (pass2FGA + shoot2FGA))*100),1)) + '%'
        except(ZeroDivisionError):
            tot2FG_per = 'N/A'
            
        tot3FGA = shoot3FGA + pass3FGA
        try:
            tot3FG_per = str(round((((pass3FGM + shoot3FGM) / (pass3FGA + shoot3FGA))*100),1)) + '%'
        except(ZeroDivisionError):
            tot3FG_per = 'N/A'
       
        data_df[i] = [str(ppp_tot), str((totPoss_per)), total_to, (str(totFG_per)),
                      str(shootingPPP_tot), str(shootPoss_per), (str(shootFG_per)), str(shoot2FGA), str(shoot2FG_per), str(shoot3FGA), str(shoot3FG_per),
                      str(passingPPP_tot), str(passingPoss_per), str(passFG_per), str(pass2FGA), str(pass2FG_per), str(pass3FGA), str(pass3FG_per)]
        
    timeEnd = time.time()
    #print(timeEnd - timeStart)
    
    # Rename column headers
    data_df = data_df.rename(columns={'TRAN' : 'Transition', 'ACO' : 'Attacking Closeouts', "C/S" : "Catch & Shoot", "OBS" : "Off Ball Screens", "CUT" : "Cutting", "OREB" : "Off. Rebounds", "PNR" :"PNR / DHO"})
    
    data_df = data_df.transpose()
    
    return(data_df)