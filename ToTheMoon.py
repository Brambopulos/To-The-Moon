
import json
from urllib.request import urlopen

debtURL = 'http://www.treasurydirect.gov/NP_WS/debt/current?format=json' #Treasury Query URL.

curDebt = 0.0
DEBUG_DEBT = 18151049785935.02 #As of 9/15/15 in dollars.

billThickness = 0.0043  #Inches
inchesInMile = 63360
milesToMoon = 238857

bills = 0
billDistance = 0.0      #Miles
percentToMoon = 0.0


denom = 0

def main():
    getDebt()
    getDenom()


    bills = int(round((curDebt / denom), 0))
    billDistance = (bills * billThickness) / inchesInMile   #Get distance in inches and convert to miles.
    percentToMoon = billDistance / milesToMoon


    print('\nCongrats! You paid off the U.S. Debt! ($' + format(curDebt, ',.2f') + ')' +
          '\nYou paid with', format(bills, ',d'), '$' + str(denom), 'bills!' +
          '\nPercent to the moon:', format(percentToMoon, '.2%') +
          '\nDistance traveled:', format(billDistance, ',.2f'), 'Miles'
          )

    tryAgain() #Ask the user if they want to redo the program.


    

def getDebt():
    global curDebt
    
    try:
        webResp = urlopen(debtURL)             #Call the url to get data.
        htmlResp = webResp.read().decode('utf-8')  #Read the data using utf-8 as the text encoding.
        
        jsonResp = json.loads(htmlResp)            #Load json data.
        curDebt = jsonResp['totalDebt']        #Set the current debt from the json data.
    except:
        print("Can not reach treasury server...\nPerhaps they couldn't pay for hosting.\n")
        curDebt = DEBUG_DEBT


def getDenom():
    global denom

    try:
        denom = int(input('Please enter a denomination of U.S. dollar. (1,2,5,10,20,50,100) '))

        if denom not in (1,2,5,10,20,50,100):   #Check that the denomination is a standard U.S. bill.
            raise Exception()
            
    except:
        print('\nError: There is no $' + str(denom), 'bill! (Or you entered text...)')
        getDenom()                              #Call this function again to get proper data.

def tryAgain():
    try:
        resp = input('\nWould you like to try again? (y,n) ')
        resp = resp.lower()

        if resp not in ('y','n'):               #Check that the user response is either y or n.
            raise Exception()
        else:
            if(resp == 'y'):
                print('\n\n')
                main()                          #Reload the program.
    except:
        tryAgain()






if __name__ == '__main__': #If this is being run directly, run main().
    main()


        
        
    

