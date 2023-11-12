import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GenerateButton = () => {
  const [pageUrl, setPageUrl] = useState('Hi');
  const [cover, setCover] = useState('');
  const [loading, setLoading] = useState(false);

  const callAPI = async () => {
    if (!pageUrl) {
      console.error('No URL available.');
      return;
    }
    try {
      setLoading(true); // Set loading to true before making the API call

      const response = await axios.post('http://127.0.0.1:5000/scrape', { url: pageUrl });
      setCover(response.data.data);
    } catch (error) {
      console.error('Error making API call:', error);
    } finally {
      setLoading(false); // Set loading to false after API call is complete
    }
  };

  const handleChange = (event) => {
    setCover(event.target.value);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <textarea
        value={cover}
        onChange={handleChange}
        placeholder="Cover letter will be generating here"
        style={{padding:'10px'}}
      />
      {loading && <p>Generating text...</p>}
      <button
        onClick={callAPI}
        style={{ backgroundColor: '#32cdb2', color: 'white', padding: '10px', cursor: 'pointer', marginTop:'10px' }}
      >
        Generate
      </button>
    </div>
  );
};

export default GenerateButton;