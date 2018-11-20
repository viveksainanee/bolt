import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css';

class NavBar extends Component {
  render() {
    return (
      <div className="NavBar">
        <div className="NavBar-logo-cont">
          <div className="NavBar-logo">
            <NavLink to="/">bolt</NavLink>
          </div>
        </div>
        <div className="NavBar-links">
          <span className="NavBar-login">
            <NavLink to="/login">login</NavLink>
          </span>
          <span className="NavBar-signUp">
            <NavLink to="/signup">sign up</NavLink>
          </span>
        </div>
      </div>
    );
  }
}

export default NavBar;
