import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import NavBar from './NavBar';
// import Companies from './Companies';
// import Company from './Company';
// import Jobs from './Jobs';
// import Login from './Login';
// import Profile from './Profile';
// import JoblyApi from './JoblyApi';
// import ErrorHandler from './ErrorHandler';
// import jwt from 'jsonwebtoken';

class Routes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: [],
      currUser: null
    };
  }

  render() {
    return (
      <div>
        <Switch>
          <Route exact path="/" render={() => <Home />} />
          {/* <Route exact path="/companies" render={() => <Companies />} />
          <Route
            exact
            path="/companies/:handle"
            render={props => <Company {...props} />}
          />
          <Route exact path="/jobs" render={() => <Jobs />} />
          <Route
            exact
            path="/login"
            render={props => (
              <Login setCurrUser={this.setCurrUser} {...props} />
            )}
          />
          <Route
            exact
            path="/profile"
            render={() => <Profile currUser={this.state.currUser} />}
          />
          <Route
            render={() => (
              <ErrorHandler
                error={
                  this.state.error.length
                    ? this.state.error
                    : ['Error 404 Page Not Found!']
                }
              />
            )}
          /> */}
        </Switch>
      </div>
    );
  }
}

export default Routes;
