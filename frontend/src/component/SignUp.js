import React, { Component } from 'react';
import NavBar from './NavBar';
import './SignUp.css';
import Footer from './Footer';
// import { Link } from 'react-router-dom';

class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      error: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.validateInputs = this.validateInputs.bind(this);
  }

  validateInputs() {
    console.log('getting here');
    //no input
    if (this.state.email === '' || this.state.password === '') {
      this.setState({ error: 'Please provide a valid email and password' });
      // return false;
    }
    // return true;
  }

  /** handlers *********************************/

  handleChange(evt) {
    this.setState({
      [evt.target.name]: this.state.value
    });
  }

  handleSubmit(evt) {
    evt.preventDefault();
    console.log('submitting');
    // validateInputs();
    console.log('submitting SignUp credentials');
  }

  render() {
    return (
      <div>
        <div className="SignUp">
          <NavBar />
          <div className="SignUp-form-cont">
            <div className="SignUp-header">SignUp</div>
            <form onSubmit={this.validateInputs}>
              <label htmlFor="first_name">First Name:</label>
              <input
                className="SignUp-input"
                type="text"
                name="first_name"
                value={this.state.first_name}
                onChange={this.handleChange}
              />
              <label htmlFor="last_name">Last Name:</label>
              <input
                className="SignUp-input"
                type="text"
                name="last_name"
                value={this.state.last_name}
                onChange={this.handleChange}
              />
              <label htmlFor="email">Email:</label>
              <input
                className="SignUp-input"
                type="text"
                name="email"
                value={this.state.email}
                onChange={this.handleChange}
              />
              <label htmlFor="password">Password:</label>
              <input
                className="SignUp-input"
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.handleChange}
              />
              <div className="SignUp-center">
                <div className="SignUp-error">{this.state.error}</div>
                <button className="SignUp-button">SignUp</button>
                <div className="SignUp-createAccount">
                  {/* Don't have an account? <Link to="/signup">Create one.</Link> */}
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

export default SignUp;
