import React, { Component } from 'react';
import NavBar from './NavBar';
import { NavLink } from 'react-router-dom';
// import { Button } from 'reactstrap';
import './Home.css';
import Footer from './Footer';

class Home extends Component {
  render() {
    return (
      <div className="Home-cont">
        <NavBar />
        <div className="Home-brand-cont">
          <div className="Home-brand">
            <div className="Home-logo">bolt</div>
            <div className="Home-slogan">Software planning for today</div>

            <NavLink to="/signup">
              <button className="Home-signUp-button">sign up</button>
            </NavLink>
          </div>
        </div>
        <Footer />
      </div>
    );
  }
}

export default Home;

/**
 * first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
 */
