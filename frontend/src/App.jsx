
import Login from './components/Login';
import './App.css';
import GenerateButton from './components/GenerateButton';
import Upload from './components/Upload';
import { useAuth } from './contexts/AuthContext';

function App() {

  const { isAuthenticated, loginAsync, isLoading, error } = useAuth();

  return (
    <div className="App">
      {isAuthenticated ? (
        <Upload/>
      ): (<Login/> ) }
    </div>
  );
}

export default App;
