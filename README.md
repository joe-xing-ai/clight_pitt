

### Setup

    - Windows 10 OS
        - conda v 4.10.1, download conda from: https://www.anaconda.com/products/individual#windows
        - conda env create --file environment_windows10.yml
        - conda activate clightpitt
        - put the credential file "clight_pitt.csv" under the repo "clight_pitt" folder
        - python upload_data.py --data_path "C:\Users\joexi\Downloads\test"
                
            (clightpitt) C:\Users\joexi\work\opensource\clight_pitt>python upload_data.py --data_path "C:\Users\joexi\Downloads\test"
            2021-09-23 13:34:40,600 [INFO] upload_data: found 3 videos files, getting ready to upload now...
            2021-09-23 13:34:40,601 [INFO] upload video 0 out of total 3 videos: C:\Users\joexi\Downloads\test\video_1.mp4 to video_1.mp4 ...
            2021-09-23 13:35:18,022 [INFO] upload video 1 out of total 3 videos: C:\Users\joexi\Downloads\test\video_2.mp4 to video_2.mp4 ...
            2021-09-23 13:35:54,586 [INFO] upload video 2 out of total 3 videos: C:\Users\joexi\Downloads\test\video_3.mp4 to video_3.mp4 ...
            2021-09-23 13:36:32,692 [INFO] upload to aws s3 bucket is done!
