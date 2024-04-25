import time

def create_txt_files(start, end, step):
    confirmation = input("Are you sure you want to generate the files? This process will take time and occupy significant storage space. (yes/no): ")
    
    if confirmation.lower() != 'yes':
        print("Files generation cancelled.")
        return
    
    print("Generating files... Please wait.")
    
    # Moving ascii art
    animation = "|/-\\"
    idx = 0
    
    for i in range(start, end, step):
        with open(f"file{i//1000000}.txt", "w") as file:#1change 1M to 10M if you want to make each dictionary 10M.
            for j in range(i, i + step):
                file.write(str(j) + "\n")
                
        # Print animation
        print(f"\r{animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)  # Adjust sleep time for animation speed
        
    print("\nFiles generation completed.")

create_txt_files(0, 100000000, 1000000)#2change 1M to 10M for changing the range in file. 

