// AuthContext.js
import React, { createContext, useContext, useReducer, useEffect } from 'react';

const AuthContext = createContext();

const initialState = {
  isAuthenticated: false,
  user: null,
  isLoading: false,
  error: null,
};

const authReducer = (state, action) => {
  switch (action.type) {
    case 'LOGIN_START':
      return {
        ...state,
        isLoading: true,
        error: null,
      };
    case 'LOGIN_SUCCESS':
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload,
        isLoading: false,
      };
    case 'LOGIN_FAILURE':
      return {
        ...state,
        isAuthenticated: false,
        user: null,
        isLoading: false,
        error: action.payload,
      };
    case 'LOGOUT':
      return {
        ...state,
        isAuthenticated: false,
        user: null,
        isLoading: false,
        error: null,
      };
    default:
      return state;
  }
};

const AuthProvider = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  const hashPassword = async (password) => {
    const saltRounds = 10;
    return await password;
  };

  const loginAsync = async (username, password) => {
    dispatch({ type: 'LOGIN_START' });

    try {
      // Hash the password before sending it to the server
      const hashedPassword = await hashPassword(password);

      const response = await fetch('http://127.0.0.1:5000/login-check', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password: hashedPassword }),
      });

      if (!response.ok) {
        throw new Error('Invalid credentials');
      }

      const user = await response.json();
      dispatch({ type: 'LOGIN_SUCCESS', payload: user });

      // Store hashed credentials in localStorage
      localStorage.setItem('authCredentials', JSON.stringify({ username, password: hashedPassword }));
    } catch (error) {
      dispatch({ type: 'LOGIN_FAILURE', payload: error.message });
    }
  };

  const logout = () => {
    // Remove credentials from localStorage
    localStorage.removeItem('authCredentials');
    dispatch({ type: 'LOGOUT' });
  };

  useEffect(() => {
    // Check for stored credentials on component mount
    const storedCredentials = localStorage.getItem('authCredentials');

    if (storedCredentials) {
      const { username, password } = JSON.parse(storedCredentials);
      loginAsync(username, password);
    }
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return (
    <AuthContext.Provider value={{ ...state, loginAsync, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

const useAuth = () => {
  return useContext(AuthContext);
};

export { AuthProvider, useAuth };
