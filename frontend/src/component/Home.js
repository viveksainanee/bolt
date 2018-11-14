import React, { Component } from 'react';
import NavBar from './NavBar';
import './Home.css';

class Home extends Component {
  render() {
    return (
      <div className="Home-cont">
        <NavBar />
        <div className="Home-brand-cont">
          <div className="Home-logo">bolt</div>
          <div className="Home-slogan">Software planning for today</div>
        </div>
      </div>
    );
  }
}

export default Home;
