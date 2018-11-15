import React, { Component } from 'react';
import NavBar from './NavBar';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = { email: '', password: '' };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(evt) {
    this.setState({
      [evt.target.name]: this.state.value
    });
  }

  handleSubmit(evt) {
    evt.preventDefault();
    console.log('submitting login credentials');
  }

  render() {
    return (
      <div className="Login">
        <NavBar />
        <div className="Login-form-cont">
          <h1>login</h1>
          <form onSubmit={this.handleSubmit}>
            <label htmlFor="email">Email:</label>
            <input
              type="text"
              name="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
            <label htmlFor="password">password:</label>
            <input
              type="password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
            <button>login</button>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
