import React, { Component } from 'react';
import './NavBar.css';
class NavBar extends Component {
  render() {
    return (
      <div className="NavBar">
        <div className="NavBar-logo-cont">
          <div className="NavBar-logo">bolt</div>
        </div>
        <div className="NavBar-links">
          <span className="NavBar-login">login</span>
          <span className="NavBar-getStarted">get started</span>
        </div>
      </div>
    );
  }
}

export default NavBar;
