# WA_Chimera
<img src="/Chimera.png" alt="WA Chimera" width="300">
WA_Chimera is a program designed to streamline the process of analyzing AWS Trusted Adviser (TA) reports and registering identified risks into a Well-Architected (WA) workload created through a specified Custom Lens. It addresses two key challenges:

1. For users without enterprise support, exporting TA reports from the console can be time-consuming and cumbersome due to the numerous spreadsheet pages, making it difficult to filter, search, and analyze issues. WA_Chimera analyzes the report content and consolidates P0 and P1 check items, along with detailed descriptions, into a TA-check.xlsx file.

2. Even with enterprise support, reviewing issues from TAM-exported files, finding corresponding accounts, and updating the WA workload can be tedious. WA_Chimera can update the issues from the report directly into the WA workload notes, making it easier to update the WA check items based on the notes content.

### Key features of WA_Chimera:

1. Local deployment: Runs directly on a Mac, easy and convenient
2. Not limited to whether there is enterprise support service, just use the TA report export from AWS Trusted Adviser console.
3. Automatically generates a readable Excel file.
4. Automatically updates WA workload notes (version 2).

## Usage

1. Ensure you have a Python 3 environment with a version not lower than Python 3.12.2.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Execute the program by running `python3 WA.py`.
4. Import the XLSX file exported from the AWS Trusted Adviser service.
5. Upon successful execution, the analysis results will be output to the `TA-check.xlsx` file in the current directory.
6. Refer to the `TA-check.xlsx` file and manually create/modify the workload in the WA Tool accordingly.

### New Feature in Version 2: Update to AWS WA Tool

In the V2 version, a new feature has been added to update the NOTES of questions in AWS WA Tool. Before using this feature, you need to set up your AWS Access Key and Secret Access Key. Please refer to the documentation for setting up your AK/SK (set them in your system environment variables, following the AWS CLI installation and setup documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

After setting up your AK/SK, you can click on the "Setting" option in this application to configure the Region, Workload, and Lens. Once you have successfully imported the exported XLSX files from the AWS Trusted Adviser service, you can perform the "Update Workload" operation.

**The logic for updating WA notes**: It aims to preserve as much historical log in the notes as possible, with the most recent updates placed at the top. Due to the 2048 character limit, only the latest 2000 characters of the log will be retained.

If you encounter any issues, please report them in the "Issues" section of this repository.


## Supported Custom Lens

The current supported Custom Lens is:
https://gitlab.aws.dev/aws-gcr-sa/gcr-war-key-workload-custom-lens (March 1st version)

When lens.json changes, it needs to be processed by the pjson.py program to generate a new output.csv file. Whether to automatically trigger the update of lens.json based on the updates of gcr-war-key-workload-custom-lens is still under consideration. If necessary, this feature will be supported in future versions.
