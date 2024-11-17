from thefuzz import fuzz
import re

def areAddressSimilar3(address1, address2):
    # make all text lower-case
    address1 = address1.lower()
    address2 =address2.lower()
    
    # replace commas with space
    address1 = address1.replace(","," ")
    address2 =address2.replace(","," ")

    # replace commas with space
    address1 = address1.replace("."," ")
    address2 =address2.replace("."," ")
    
    # remove all leading and preceding spaces
    address1 =address1.strip() 
    address2 =address2.strip()
    
    # Replacing double spaces with single space
    address1= re.sub(' +', ' ', address1) 
    address2= re.sub(' +', ' ', address2)

    # split address into a list of words for both addresses
    a1=address1.split(" ")
    a2=address2.split(" ")
    
    # checking for the list with the highest number of words then reassign them for a1 to be the smaller list
    if len(a2)<len(a1):
        a1,a2 = a2, a1

    match_type =''
    
    # number of loops completed from the left
    l1 = 0
    
    while l1< len(a1) and fuzz.ratio(a1[l1],a2[l1])>65:
        l1 += 1
    s1=0    
    r1,r2 =len(a1)-1, len(a2)-1 # word position in the list
    while r1>= l1 and r2 >=0 and fuzz.ratio(a1[r1] , a2[r2])>65:
        s1=r1
        r1, r2 = r1 - 1, r2 - 1
    similarity= (l1/len(a1)+(len(a1)-s1)/len(a1))/2
    if similarity==1.0:
        match_type='100% match'
    elif len(a1)-s1==len(a1):
        match_type = 'Matched by logic'
    elif l1>=2 and len(a1)-s1>=2:
        match_type = 'Matched by logic'
    else:
        match_type = 'No match'
    
    
    return match_type, ' Matches from the left: ',l1, 'matches from the right: ',len(a1)-s1,'No. of words in the shorter address ', len(a1), similarity