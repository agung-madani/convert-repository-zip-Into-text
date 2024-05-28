# Convert Repo Into Text

This application allows users to upload a ZIP file of a repository and displays the content of the files in the repository.

## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository.
   ```bash
   git clone https://github.com/agung-madani/convert-repository-zip-Into-text.git
   cd convert-repository-zip-Into-text
   ```
2. Install the required dependencies.
   ```bash
   pip install flask
   ```
4. Run the application.
   ```bash
   python app.py
   ```
5. There will appear the address & open on your local web page
   * Running on ...

## Usage

1. Navigate to the home page.
2. Click on the upload button to upload a ZIP file.
3. The application will display the content of the files in the repository.

![image](https://github.com/agung-madani/convert-repository-zip-Into-text/assets/121701309/f1ccb0a3-fd24-4563-80bf-e08d30dbe9bb)

![image](https://github.com/agung-madani/convert-repository-zip-Into-text/assets/121701309/1e3024ef-76bc-4783-a1c7-5a2b4b09d3bb)

## Code Overview

The application is built with Flask and uses the following routes:

- [`/`](../../../z:/python/convertRepoIntoText/app.py): Renders the home page.
- [`/upload`](../../../z:/python/convertRepoIntoText/app.py): Handles the file upload and processing.

The application uses the [`handle_zip_file`](../../../z:/python/convertRepoIntoText/app.py) function to extract the content of the files from the uploaded ZIP file and pass it to the [`display_files.html`](../../../z:/python/convertRepoIntoText/templates/display_files.html) template.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license.
