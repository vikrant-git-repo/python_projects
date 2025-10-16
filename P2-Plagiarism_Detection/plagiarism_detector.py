from difflib import SequenceMatcher

with open(r'C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\Plagiarism_Detection\demo1.txt') as one_file, open(r'C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\Plagiarism_Detection\demo2.txt') as two_file:
    data_file1 = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f"The plagiarized content is {matches}%")

