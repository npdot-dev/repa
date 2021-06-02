import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8') 
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

CREDENTIALS_FILE = 'credentials.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1Ycg7zTxds9DZnDvTrFcyNNKuTUxg6Yy6WF0a8Wc02WQ'

range_n = 'transactions!A:D'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_n).execute()

transaction_id = []
created_at = []
m_real_amount= []
l_client_id=[]

for i in table['values'][1:]:
    
    try:
        transaction_id.append(i[0])
    except:
        transaction_id.append(0)
    try:
        created_at.append(i[1])
    except:
        created_at.append(0)
    try:
        m_real_amount.append(i[2])
    except:
        m_real_amount.append(0)
    try:
        l_client_id.append(i[3])
    except:
        l_client_id.append(0)
    

trans = pd.DataFrame( list(zip(transaction_id, created_at, m_real_amount,l_client_id) ),columns=[ 
                                                table['values'][0][0],
                                                table['values'][0][1],
                                                table['values'][0][2],
                                                table['values'][0][3]])

range_name = 'clients!A:C'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
clients_id = []
created_at = []
i_manager_id= []

for i in table['values'][1:]:
    try:
        clients_id.append(i[0])
    except:
        clients_id.append(0)
    try:
        created_at.append(i[1])
    except:
        created_at.append(0)
    try:
        i_manager_id.append(i[2])
    except:
        i_manager_id.append(0)
    
client = pd.DataFrame( list(zip(clients_id, created_at, i_manager_id) ),columns=[ 
                                                table['values'][0][0],
                                                table['values'][0][1],
                                                table['values'][0][2]])

range_na = 'managers!A:C'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_na).execute()
manger_id = []
d_manager = []
d_club= []

for i in table['values'][1:]:
    try:
        manger_id.append(i[0])
    except:
        manger_id.append(0)
    try:
        d_manager.append(i[1])
    except:
        d_manager.append(0)
    try:
        d_club.append(i[2])
    except:
        d_club.append(0)
    
manage = pd.DataFrame( list(zip(manger_id, d_manager, d_club) ),columns=[ 
                                                table['values'][0][0],
                                                table['values'][0][1],
                                                table['values'][0][2]])

range_nam = 'leads!A:F'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_nam).execute()
lead_id = []
created_at = []
d_utm_mediur=[]
d_utm_source=[]
l_manager_id=[]
l_client_id=[]
key=[]


for i in table['values'][1:]:
    try:
        l_client_id.append(i[5])
    except:
        l_client_id.append(0)
    if i[2]+i[4] in key:
        continue        
    else:
        d_utm_source.append(i[2])
        l_manager_id.append(i[4])
        key.append(i[2]+i[4])        
            
##lead = pd.DataFrame( list(zip(lead_id, created_at, d_utm_mediur,d_utm_source,l_manager_id,l_client_id) ),columns=[ 
##                                                table['values'][0][0],
##                                                table['values'][0][1],
##                                                table['values'][0][2],
##                                                table['values'][0][3],
##                                                table['values'][0][4],
##                                                table['values'][0][5]])

##print("transactions:",trans,'',"clients:",client,'',"managers:",manage,'',"leads:",lead,sep='\n')