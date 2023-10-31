import React, { useState } from 'react';
import axios from 'axios';

const GenerateButton = () => {
  const [pageUrl, setPageUrl] = useState('');

  // Function to make the API call
  const callAPI = async () => {
    if (!pageUrl) {
      // Ensure that you have the URL before making the API call
      console.error('No URL available.');
      return;
    }

    try {
      // Replace 'YOUR_API_ENDPOINT' with your actual API endpoint
      console.log("pageUrl",pageUrl)
      const response = await axios.post('YOUR_API_ENDPOINT', { url: pageUrl });

      // Handle the response from the API
      console.log('API response:', response.data);
    } catch (error) {
      console.error('Error making API call:', error);
    }
  };

  // Handle messages from the background script
//   chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     if (message.action === 'setPageUrl') {
//       // Receive the current page's URL from the background script
//       setPageUrl(message.url);
//     }
//   });

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <button
        onClick={callAPI}
        style={{ backgroundColor: '#32cdb2', color: 'white', padding: '10px', cursor: 'pointer' }}
      >
        Generate
      </button>
    </div>
  );
};

export default GenerateButton;
