import React, { useState } from 'react';
import axios from 'axios';

const Upload = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    console.log("selectedFile handleFile",e.target.files[0]);
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('resume', selectedFile);
      console.log("selectedFile",selectedFile);
      try {
        // Replace 'YOUR_API_ENDPOINT' with the actual API endpoint to upload the PDF file
        const response = await axios.post('http://127.0.0.1:5000/upload-pdf', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        // Handle the response as needed
        console.log('File uploaded successfully:', response.data);

        // Clear the selected file
        setSelectedFile(null);
      } catch (error) {
        console.error('Error uploading the file:', error);
      }
    } else {
      alert('Please select a file to upload.');
    }
  };

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
      }}
    >
      <input type="file" accept=".pdf" onChange={handleFileChange} style={{ display: 'none' }} id="fileInput" />
      <label htmlFor="fileInput" style={{ backgroundColor: '#32cdb2', color: 'white', padding: '10px', cursor: 'pointer', marginBottom: '10px' }}>
        Upload Resume
      </label>
      {selectedFile && <p>Selected file: {selectedFile.name}</p>}
      <button onClick={handleUpload} style={{ backgroundColor: '#32cdb2', color: 'white', padding: '10px', cursor: 'pointer', border:'None' }}>
        Send
      </button>
    </div>
  );
};

export default Upload;
