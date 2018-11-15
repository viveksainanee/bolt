import React, { Component } from 'react';
import Routes from './Routes';
import Colors from './Colors';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Routes />
        {/* <Colors /> */}
      </div>
    );
  }
}

export default App;
