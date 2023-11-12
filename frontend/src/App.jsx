// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Upload from './components/Upload';
import { useAuth } from './contexts/AuthContext';
import GenerateButton from './components/GenerateButton'

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <Router>
      <Routes>
        <Route path="/login" element={!isAuthenticated ? <Login /> : <Navigate to="/coverletter" />} />
        <Route path="/upload" element={isAuthenticated ? <Upload /> : <Navigate to="/login" />} />
        <Route path="/coverletter" element={isAuthenticated ? <GenerateButton /> : <Navigate to="/login" />} />
        {/* Add additional routes as needed */}
        <Route path="/" element={isAuthenticated ? <Upload /> : <Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;
