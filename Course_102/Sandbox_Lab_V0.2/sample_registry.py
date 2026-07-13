#--------------------
#\\//\\//\\//\\//\\//
#|||| Importing |||||
#\\//\\//\\//\\//\\//
#--------------------
import random
import datetime
#---------------
#\\//\\//\\//\\
#|||| Date |||||
#\\//\\//\\//\\
#---------------



#--------------------------------------
#\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
#|||| Dectionaries, lists, tuples |||||
#\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
#--------------------------------------

samples = [ ]


#--------------------
#\\//\\//\\//\\//\\//
#|||| Functions |||||
#\\//\\//\\//\\//\\//
#--------------------

#---------------
# 1- Generatign Hash
#---------------
def generate_fake_hash():
    hex_chars = "0123456789abcdef"
    fake_hash = ""

    for i in range(64):
        random_index = random.randint(0, len(hex_chars) - 1)
        fake_hash += hex_chars[random_index]

    
    return fake_hash


#--------------
# 2-Validate Date
#--------------
def validate_date(date):
    try:
        datetime.datetime.strptime(date, "%d-%m-%Y")
        return True
    
    except ValueError:
        return False

 
 
#-------------------
# 3- Validate Status
#-------------------

def validate_status(status):
    allowed_status = ("Scanned", "Pending")

    if status in allowed_status:
        return True
    
    
    return False


#-------------------
# 4- Validate threat type
#-------------------
def validate_threat(threat):
    allowed_threats = ("Unknown", "Clean", "Trojan", "Ransomware", "Worm", "Spyware", "Adware")

    if threat in allowed_threats:
        return True
    
    
    return False


def add_sample():
    
    #check file name
    while True:
        file_name = input("Enter the file name: ").strip()

        if file_name.strip() != "":
            break

        print("Invalid file name. ")

    #check upload date 
    while True:
        upload_date = input("Enter the upload date (dd-mm-yyyy): ")
        if validate_date(upload_date):
            break

        print("Invalid date format. ")
    

    #Check scan date
    while True: 
        scan_date = input("Enter scan date (dd-mm-yyyy): ")
        if validate_date(scan_date):
            break

        print("Invalid date format. ")
    

    #Check threat type
    while True:
        threat = input("Enter Threat (Unknown / Clean / Trojan / Ransomware / Worm / Spyware / Adware): ").strip().title()
        if validate_threat(threat):
            break

        print("Invalid threat type. ")

    
    #check status
    while True:
        status = input("Enter the status (Scanned / Pending): ").strip().title()
        if validate_status(status):
            break
        
        print("Invalid status. ")
     

    sample = {
        "File Name": file_name,
        "SHA-256": generate_fake_hash(),
        "Upload Date": upload_date,
        "Scan Date": scan_date,
        "Status": status,
        "Threat": threat
    }

    samples.append(sample)

    print("Sample added successfully!")






#-------------------
# 5- Display Samples
#-------------------

def display_samples():
    if len(samples) == 0:
        print("No samples found.")
        return
    
    sample_number = 1
    for sample in samples:
        print("=" * 40)
        print(f"sample #{sample_number}")
        print("=" * 40)
        print(f"File Name   : {sample['File Name']}")
        print(f"SHA-256     : {sample['SHA-256']}")
        print(f"Upload Date : {sample['Upload Date']}")
        print(f"Scan Date   : {sample['Scan Date']}")
        print(f"Status      : {sample['Status']}")
        print(f"Threat      : {sample['Threat']}")
        print("=" * 40)
        sample_number += 1





#-------------------
# 6- Search by Name
#-------------------
def search_by_name():
    file_name = input("Enter file name: " ).strip()

    for sample in samples:
        if sample["File Name"] == file_name:
            print("=" * 40)
            print(f"File Name   : {sample['File Name']}")
            print(f"SHA-256     : {sample['SHA-256']}")
            print(f"Upload Date : {sample['Upload Date']}")
            print(f"Scan Date   : {sample['Scan Date']}")
            print(f"Status      : {sample['Status']}")
            print(f"Threat      : {sample['Threat']}")
            print("=" * 40)

            return
    
    print("Sample not found.")
    
   


#-------------------
# 7- Search by Hash
#-------------------
def search_by_hash():
    sha256_hash = input("Enter SHA-256 hash: ").strip()

    for sample in samples:
        if sample["SHA-256"] == sha256_hash:
            print("=" * 40)
            print(f"File Name   : {sample['File Name']}")
            print(f"SHA-256     : {sample['SHA-256']}")
            print(f"Upload Date : {sample['Upload Date']}")
            print(f"Scan Date   : {sample['Scan Date']}")
            print(f"Status      : {sample['Status']}")
            print(f"Threat      : {sample['Threat']}")
            print("=" * 40)

            return
    
    print("Sample not found.")




#---------------------
# 8- Search by Threat
#---------------------
def search_by_threat():
    threat = input("Enter Threat: ").strip().title()

    found = False

    for sample in samples:
        if sample["Threat"] == threat:
            print("=" * 40)
            print(f"File Name   : {sample['File Name']}")
            print(f"SHA-256     : {sample['SHA-256']}")
            print(f"Upload Date : {sample['Upload Date']}")
            print(f"Scan Date   : {sample['Scan Date']}")
            print(f"Status      : {sample['Status']}")
            print(f"Threat      : {sample['Threat']}")
            print("=" * 40)

            found = True
        
    if not found:
        print("No samples found.")





#-------------------
# 9- Show Statistics
#-------------------
def show_statistics():
    total_samples = len(samples)
    print(f"Total Samples: {total_samples}")

    pending_samples = 0
    scanned_samples = 0
    malware_samples = 0
    clean_samples = 0

    for sample in samples: 
        if sample["Status"] == "Pending":
            pending_samples += 1
        
        elif sample["Status"] == "Scanned":
            scanned_samples += 1
        
        if sample["Threat"] == "Clean":
            clean_samples += 1
        
        elif sample["Threat"] != "Clean":
            malware_samples += 1

    print(f"Pending Samples: {pending_samples}")
    print(f"Scanned Samples: {scanned_samples}")
    print(f"Clean Samples: {clean_samples}")
    print(f"Malware Samples: {malware_samples}")






#------------------------
# 10- Show Oldest Samples 
#------------------------
def oldest_sample():
    if len(samples) == 0:
        print("No samples found.")
        return
    
    oldest = samples[0]

    for sample in samples:

        current_date = datetime.datetime.strptime(sample["Upload Date"], "%d-%m-%Y")
        oldest_date = datetime.datetime.strptime(oldest["Upload Date"], "%d-%m-%Y")
        
        if current_date < oldest_date:
            oldest = sample
    
    print("=" * 40)
    print(f"File Name   : {oldest['File Name']}")
    print(f"SHA-256     : {oldest['SHA-256']}")
    print(f"Upload Date : {oldest['Upload Date']}")
    print(f"Scan Date   : {oldest['Scan Date']}")
    print(f"Status      : {oldest['Status']}")
    print(f"Threat      : {oldest['Threat']}")
    print("=" * 40)
    



#------------------------
# 11- Show Newest Samples
#------------------------
def newest_sample():
    if len(samples) == 0:
        print("No samples found.")
        return
    
    newest = samples[0]

    for sample in samples:

        current_date = datetime.datetime.strptime(sample["Upload Date"], "%d-%m-%Y")
        newest_date = datetime.datetime.strptime(newest["Upload Date"], "%d-%m-%Y")
        
        if current_date > newest_date:
            newest = sample
    
    print("=" * 40)
    print(f"File Name   : {newest['File Name']}")
    print(f"SHA-256     : {newest['SHA-256']}")
    print(f"Upload Date : {newest['Upload Date']}")
    print(f"Scan Date   : {newest['Scan Date']}")
    print(f"Status      : {newest['Status']}")
    print(f"Threat      : {newest['Threat']}")
    print("=" * 40)





#--------------------
# 12- Soritng Samples 
#--------------------
def sort_samples():

    if len(samples) == 0:
        print("No samples found.")
        return
    
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            first_date = datetime.datetime.strptime(samples[i]["Upload Date"], "%d-%m-%Y")
            second_date = datetime.datetime.strptime(samples[j]["Upload Date"], "%d-%m-%Y")

            if first_date > second_date:
                temp = samples[i]
                samples[i] = samples[j]
                samples[j] = temp   
    
    print("Samples sorted by upload date successfully!")





#--------------------
# 13- Reverse Samples 
#--------------------
def reverse_samples():
    if len(samples) == 0:
        print("No samples found.")
        return
    
    samples.reverse()
    print("Samples reversed successfully!")




#--------------------
# 14- soritng Samples 
#--------------------

def days_since_upload():
    if len(samples) == 0:
        print("No samples found.")
        return
    
    today = datetime.datetime.now()

    for sample in samples:
        upload_date = datetime.datetime.strptime( sample["Upload Date"], "%d-%m-%Y")

        days = (today - upload_date).days

        print(f"File Name : {sample['File Name']}")
        print(f"Uploaded {days} days ago")
        print("=" * 40)




def main():
    while True:
        print("\nMalware Sample Management System")
        print("1. Add Sample")
        print("2. Display Samples")
        print("3. Search by Name")
        print("4. Search by Hash")
        print("5. Search by Threat")
        print("6. Show Statistics")
        print("7. Show Oldest Sample")
        print("8. Show Newest Sample")
        print("9. Sort Samples by Upload Date")
        print("10. Reverse Samples")
        print("11. Days Since Upload")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            add_sample()
        elif choice == "2":
            display_samples()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            search_by_hash()
        elif choice == "5":
            search_by_threat()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            oldest_sample()
        elif choice == "8":
            newest_sample()
        elif choice == "9":
            sort_samples()
        elif choice == "10":
            reverse_samples()
        elif choice == "11":
            days_since_upload()
        elif choice == "12":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
