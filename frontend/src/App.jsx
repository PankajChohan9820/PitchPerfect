
import Login from './components/Login';
import './App.css';
import GenerateButton from './components/GenerateButton';
import Upload from './components/Upload';
import { AuthContext } from './contexts/AuthContext';
import { useAuth } from './hooks/useAuth';

function App() {
  const { user, login, logout, setUser } = useAuth();
  return (
    <AuthContext.Provider value={{ user, setUser }}>
    <div className="App">
      <Login/>
      {/* <Upload/> */}
      {/* <GenerateButton/> */}
    </div>
    </AuthContext.Provider>
  );
}

export default App;
