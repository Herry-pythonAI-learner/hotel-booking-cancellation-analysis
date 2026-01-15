def categorize_lead_time(lead_time):
     if lead_time <= 7: return '1.Last Minute(1-7 days)'
     elif lead_time <=30: return '2.Short Term(8-30 days)'
     elif lead_time <=90: return '3.Mid Term(31-90 days)'
     else: return '4.Long Term(91+ days)'
     print('Lead time categorization completed')

    
    



   