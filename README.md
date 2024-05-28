
# Convert Repository into Readable Text Format

This application enables users to convert the content of a repository stored in a ZIP file into readable text format, so you can use in your **ChatGPT** as a F2P players

## Getting Started

To run this application locally, follow these steps:

1. Clone the repository.
   ```bash
   git clone https://github.com/agung-madani/convert-repository-zip-Into-text.git
   cd convert-repository-zip-Into-text
   ```

2. Install the required dependencies.
   ```bash
   pip install flask
   ```

3. Run the application.
   ```bash
   python app.py
   ```

4. Access the application through your local web browser using the displayed address.

## Usage

1. Navigate to the home page.
2. Click on the upload button to select and upload a ZIP file.
3. The application will process the file and display the content of the repository's files.

![Uploaded Files](https://github.com/agung-madani/convert-repository-zip-Into-text/assets/121701309/f1ccb0a3-fd24-4563-80bf-e08d30dbe9bb)
![Uploaded Files](https://github.com/agung-madani/convert-repository-zip-Into-text/assets/121701309/1e3024ef-76bc-4783-a1c7-5a2b4b09d3bb)

4. Utilize ChatGPT as an assistant by following these steps:

   * Use the provided prompt:
      ```text
      you are a ... assistant, i will give you a repository with its files inside it, and i will ask you
      ```
   * Enter the repository content.
   * Ask your query or request.

## Code Overview

The application is developed using Flask and comprises the following routes:

- [`/`](../../../z:/python/convertRepoIntoText/app.py): Renders the home page.
- [`/upload`](../../../z:/python/convertRepoIntoText/app.py): Manages file upload and processing.

The [`handle_zip_file`](../../../z:/python/convertRepoIntoText/app.py) function extracts file content from the uploaded ZIP file and passes it to the [`display_files.html`](../../../z:/python/convertRepoIntoText/templates/display_files.html) template.

## Contributing

Contributions are encouraged. Feel free to open issues or submit pull requests.

## License

This project is licensed under the terms of the MIT license.
