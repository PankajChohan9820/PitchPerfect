import React from 'react';
import './Login.css'

const Login = () => {
  return (
    <div className="login-container">
      <div className="login-form">
        <div style={{ textAlign: 'center', marginBottom: '20px' }}>
          <h1 style={{ color: '#32cdb2' }}>Login</h1>
        </div>
        <div className="form-group">
          <label style={{ color: '#b4b7be' }}>Email ID</label>
          <input type="text" />
        </div>
        <div className="form-group">
          <label style={{ color: '#b4b7be' }}>Password</label>
          <input type="password" />
        </div>
        <div className="remember-me">
          <input type="checkbox" />
          <label style={{ color: '#b4b7be' }}>Remember Me</label>
        </div>
        <button style={{ background: '#32cdb2', color: 'white', marginBottom: '15px' }}>Login</button>
        <div style={{ textAlign: 'center', marginBottom: '10px' }}>
          <button style={{ background: 'transparent', border: 'none', color: '#b4b7be', cursor: 'pointer' }}>Forgot Password</button>
        </div>
        <div style={{ textAlign: 'center' }}>
          <button style={{ background: 'transparent', border: 'none', color: '#32cdb2', cursor: 'pointer', paddingBottom: '0px' }}>Don't have an account?</button>
        </div>
      </div>
    </div>
  );
};

export default Login;
