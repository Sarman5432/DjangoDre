import "bootstrap/dist/css/bootstrap.min.css";

import logo from './logo.svg';
import './App.css';
import NavBar from './components/NavBar'
import FightersContainer from "./components/FightersContainer";

function App() {
  return (
    <div className="App">
      <NavBar />
      <FightersContainer />
    </div>
  );
}

export default App;
