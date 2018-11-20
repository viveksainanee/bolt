import React, { Component } from 'react';
import NavBar from './NavBar';
import './Login.css';
import Footer from './Footer';
import { Link } from 'react-router-dom';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = { email: '', password: '', error: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  validateInputs() {
    console.log('getting here');
    //no input
    if (this.state.email === '' || this.state.password === '') {
      this.setState({ error: 'Please provide a valid email and password' });
      // return false;
    } else {
      this.setState({ error: '' });
    }
    // return true;
  }

  /** handlers *********************************/

  handleChange(evt) {
    this.setState({
      [evt.target.name]: evt.target.value
    });
  }

  handleSubmit(evt) {
    evt.preventDefault();
    this.validateInputs();
    console.log('submitting login credentials');
  }

  render() {
    return (
      <div>
        <div className="Login">
          <NavBar />
          <div className="Login-form-cont">
            <div className="Login-header">login</div>
            <form onSubmit={this.handleSubmit}>
              <label htmlFor="email">Email:</label>
              <input
                className="Login-input"
                type="text"
                name="email"
                value={this.state.email}
                onChange={this.handleChange}
              />
              <label htmlFor="password">Password:</label>
              <input
                className="Login-input"
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.handleChange}
              />
              <div className="Login-center">
                <div className="Login-error">{this.state.error}</div>
                <button className="Login-button">login</button>
                <div className="Login-createAccount">
                  Don't have an account? <Link to="/signup">Create one.</Link>
                </div>
              </div>
            </form>
          </div>
        </div>
        <Footer />
      </div>
    );
  }
}

export default Login;
