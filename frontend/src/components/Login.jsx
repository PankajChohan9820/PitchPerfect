import React, {useState} from 'react';
import './Login.css';
import { useAuth } from '../contexts/AuthContext';

const Login = () => {

  const { loginAsync, isLoading, error } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    await loginAsync(username, password);
  };


  return (
    <div className="login-container">
      <div className="login-form">
        <div style={{ textAlign: 'center', marginBottom: '20px' }}>
          <h1 style={{ color: '#32cdb2' }}>Login</h1>
        </div>
        <div className="form-group">
          <label style={{ color: '#b4b7be' }}>Email ID</label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)}/>
        </div>
        <div className="form-group">
          <label style={{ color: '#b4b7be' }}>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        </div>
        <div className="remember-me">
          <input type="checkbox" />
          <label style={{ color: '#b4b7be' }}>Remember Me</label>
        </div>
        <button onClick={handleLogin} style={{ background: '#32cdb2', color: 'white', marginBottom: '15px' }}>Login</button>
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
