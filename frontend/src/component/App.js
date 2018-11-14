import React, { Component } from 'react';
import './App.css';
import Home from './Home';
import Colors from './Colors';
import Footer from './Footer';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Home />
        <Colors />
        <Footer />
      </div>
    );
  }
}

export default App;
