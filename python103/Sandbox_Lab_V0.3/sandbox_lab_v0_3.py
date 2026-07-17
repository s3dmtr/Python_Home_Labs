#--------------------
#\\//\\//\\//\\//\\//
#|||| Importing |||||
#\\//\\//\\//\\//\\//
#--------------------
import random
import datetime


#--------------------
#\\//\\//\\//\\//\\//
#||| Sample Class |||
#\\//\\//\\//\\//\\//
#--------------------

#print("\n" + "=" * 40)


class Sample:

    #|=|=|=|=|=|=|
    # Constructor
    #|=|=|=|=|=|=|

    def __init__(self):
        self.__file_name = ""
        self.__sha256 = ""
        self.__upload_date = ""
        self.__scan_date = ""
        self.__status = ""
        self.__threat = ""

        self.__generate_sha256()

    


    #|=|=|=|=|=|=|
    # Setters
    #|=|=|=|=|=|=|

    def __set_file_name(self, file_name):
        if isinstance(file_name, str) and file_name.strip():
            self.__file_name = file_name
            return True
        return False
    
    def __set_upload_date(self, upload_date):
        if isinstance(upload_date, str) and upload_date.strip():
            try:
                datetime.datetime.strptime(upload_date, "%d-%m-%Y")
                self.__upload_date = upload_date
                return True
            except ValueError:
                return False
        
        return False
            
           
        
       
    
    def __set_scan_date(self, scan_date):
        if isinstance(scan_date, str) and scan_date.strip():
            try:
                datetime.datetime.strptime(scan_date, "%d-%m-%Y")
                self.__scan_date = scan_date
                return True
            except ValueError:
                return False
            
        
        return False
    
            
    
    def __set_status(self, status):
        if isinstance(status, str) and status.strip():
            allowed_statuses = ("Scanned", "Pending")

            if status in allowed_statuses:
                self.__status = status
                return True
            
        return False
        

    
    def __set_threat(self, threat):
        if isinstance(threat, str) and threat.strip():
            allowed_threats = ("Unknown", "Clean", "Trojan", "Ransomware", "Worm", "Spyware", "Adware") # I make it as tuple for immutability
            if threat in allowed_threats:
                self.__threat = threat
                return True
        return False
    
    #|=|=|=|=|=|=|
    # Getters
    #|=|=|=|=|=|=|

    def get_file_name(self):
        return self.__file_name
    
    def get_sha256(self):
        return self.__sha256
    
    def get_upload_date(self):
        return self.__upload_date
    
    def get_scan_date(self):
        return self.__scan_date
    
    def get_status(self):
        return self.__status
    
    def get_threat(self):
        return self.__threat
    

    #|=|=|=|=|=|=|=|=|=|=|=|
    # Generate SHA256 Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def __generate_sha256(self):
        # Generate a random SHA256 hash
        hex_chars = '0123456789abcdef'
        fake_hash = ""

        for i in range(64):
            random_index = random.randint(0, len(hex_chars) - 1)
            fake_hash += hex_chars[random_index]
        
        self.__sha256 = fake_hash
    

    #|=|=|=|=|=|=|
    # Input Method
    #|=|=|=|=|=|=|
    
    def input_info(self):
        while True:
            file_name = input("Enter the file name: ").strip()

            if self.__set_file_name(file_name):
                break

            print("Invalid file name. ")
        


        while True:
            upload_date = input("Enter the upload date (dd-mm-yyyy):")

            if self.__set_upload_date(upload_date):
                break

            print("Invalid date.")

        
        while True:
            scan_date = input("Enter the scan date (dd-mm-yyyy):")

            if self.__set_scan_date(scan_date):
                break

            print("Invalid date.")
        
        while True:
            status = input("Enter the status (Scanned/Pending): ").strip()

            if self.__set_status(status):
                break

            print("Invalid status. Please enter 'Scanned' or 'Pending'.")
        
        while True:
            threat = input("Enter the threat type (Unknown/Clean/Trojan/Ransomware/Worm/Spyware/Adware): ").strip()

            if self.__set_threat(threat):
                break

            print("Invalid threat type. Please enter one of the allowed types.")
    

    #|=|=|=|=|=|=|=|=|
    # Display Method
    #|=|=|=|=|=|=|=|=|
    def display_info(self):
        print(f"File Name   : {self.__file_name}")
        print(f"SHA256 Hash : {self.__sha256}")
        print(f"Upload Date : {self.__upload_date}")
        print(f"Scan Date   : {self.__scan_date}")
        print(f"Status      : {self.__status}")
        print(f"Threat Type : {self.__threat}")
       


#--------------------
#\\//\\//\\//\\//\\//
#|| Registry Class ||
#\\//\\//\\//\\//\\//
#--------------------


class SampleRegistry:

    #|=|=|=|=|=|=|
    # Constructor
    #|=|=|=|=|=|=|

    def __init__(self):
        self.__samples = []


    #|=|=|=|=|=|=|=|=|=|=|=|
    # adding Sample Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def add_sample(self):
        sample = Sample()
        sample.input_info()
        self.__samples.append(sample)
        print("Sample added successfully!")


    #|=|=|=|=|=|=|=|=|=|=|=|
    # Display Sample Method
    #|=|=|=|=|=|=|=|=|=|=|=|
    
    def display_samples(self):
        if not self.__samples:
            print("No sample found.")
            return


        sample_number = 1
    
        for sample in self.__samples:
          print("\n" + "=" * 40)
          print(f"Sample #{sample_number}:")
          print( "=" * 40)

          sample.display_info()
          sample_number += 1
    


    #|=|=|=|=|=|=|=|=|=|=|=|
    # Search by Name Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def search_by_name(self):
        file_name = input("Enter file name: ").strip()

        found = False

        for sample in self.__samples:
            if sample.get_file_name() == file_name:
                print("\n"+"=" * 40)
                sample.display_info()
                print("=" * 40)
                
                found = True
                

        if not found:
                print("Sample not found.")
    

    #|=|=|=|=|=|=|=|=|=|=|=|
    # Search by SHA256 Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def search_by_sha256(self):
        sha256_hash = input ("Enter SHA-256 hash: ").strip()

        found = False

        for sample in self.__samples:
            if sample.get_sha256() == sha256_hash:
                print("\n" + "=" * 40)
                sample.display_info()
                print("=" * 40)

                found = True
                break
            
        if not found:
               print("Sample not found.")
               
    
    #|=|=|=|=|=|=|=|=|=|=|=|=|
    # Search by Threat Method
    #|=|=|=|=|=|=|=|=|=|=|=|=|

    def search_by_threat(self):
        threat_type = input("Enter threat type (Unknown/Clean/Trojan/Ransomware/Worm/Spyware/Adware): ").strip()

        found = False

        for sample in self.__samples:
            if sample.get_threat() == threat_type:
                print("\n" + "=" * 40)
                sample.display_info()
                print("=" * 40)

                found = True
            
        if not found:
                print("Sample not found.")
    

    #|=|=|=|=|=|=|=|=|=|=|
    # Show Statics Method
    #|=|=|=|=|=|=|=|=|=|=|

    def show_statistics(self):
        total_samples = len(self.__samples)

        pending_samples = 0 
        scanned_samples = 0
        malware_samples = 0
        clean_samples = 0
        total_samples = len(self.__samples)

        for sample in self.__samples:
            if sample.get_status() == "Scanned":
                scanned_samples += 1
            
            elif sample.get_status() == "Pending":
                pending_samples += 1
            

            if sample.get_threat() == "Clean":
                clean_samples += 1

            else:
                malware_samples += 1
        

        print(f"Total Samples:  {total_samples}")
        print(f"Pending Samples:  {pending_samples}")
        print(f"Scanned Samples:  {scanned_samples}")
        print(f"Clean Samples:  {clean_samples}")
        print(f"Malware Samples:  {malware_samples}")
    


    #|=|=|=|=|=|=|=|=|=|=|=|
    # Oldest Samples Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def oldest_sample(self):
        if len(self.__samples) == 0:
            print("No sample found.")
            return

        oldest_sample = self.__samples[0]

        oldest_date = datetime.datetime.strptime(oldest_sample.get_upload_date(), "%d-%m-%Y")
        

        for sample in self.__samples:
            

            current_date = datetime.datetime.strptime(sample.get_upload_date(), "%d-%m-%Y")

            if current_date < oldest_date:
                
                oldest_sample = sample
                oldest_date = current_date
        
        print("\n" + "=" * 40)
        oldest_sample.display_info()
        print("=" * 40)


    #|=|=|=|=|=|=|=|=|=|=|=|
    # Newest Samples Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def newest_sample(self):
        if len(self.__samples) == 0:
            print("No sample found.")
            return

        newest_sample = self.__samples[0]

        newest_date = datetime.datetime.strptime(newest_sample.get_upload_date(), "%d-%m-%Y")

        for sample in self.__samples:
            current_date = datetime.datetime.strptime(sample.get_upload_date(), "%d-%m-%Y")

            if current_date > newest_date:
                newest_sample = sample
                newest_date = current_date
        
        print("\n" + "=" * 40)
        newest_sample.display_info()
        print("=" * 40)


    #|=|=|=|=|=|=|=|=|=|=|
    # Sort Samples Method
    #|=|=|=|=|=|=|=|=|=|=|

    def sort_samples(self):
        if len(self.__samples) == 0:
            print("No sample found.")
            return
        
        for i in range(len(self.__samples)):
            for j in range(i + 1, len(self.__samples)):
                date_i = datetime.datetime.strptime(self.__samples[i].get_upload_date(), "%d-%m-%Y")
                date_j = datetime.datetime.strptime(self.__samples[j].get_upload_date(), "%d-%m-%Y")

                if date_i > date_j:
                    self.__samples[i], self.__samples[j] = self.__samples[j], self.__samples[i]
        
        print("Samples sorted by upload date successfully!")



    #|=|=|=|=|=|=|=|=|=|=|=|
    # Reverse Samples Method
    #|=|=|=|=|=|=|=|=|=|=|=|

    def reverse_samples(self):
        if len(self.__samples) == 0:
            print("No sample found.")
            return
        
        self.__samples.reverse()
        print("Samples reversed successfully!")

    
    #|=|=|=|=|=|=|=|=|=|=|=|=|
    # Days since Upload Method
    #|=|=|=|=|=|=|=|=|=|=|=|=|

    def days_since_upload(self):
        if len(self.__samples) == 0:
            print("No sample found.")
            return
        
        for sample in self.__samples:
            upload_date = datetime.datetime.strptime(sample.get_upload_date(), "%d-%m-%Y")
            current_date = datetime.datetime.now()
            days= (current_date - upload_date).days

            print(f"File Name: {sample.get_file_name()}")
            print(f"Uploaded {days} days ago.")
            print("=" * 40)
